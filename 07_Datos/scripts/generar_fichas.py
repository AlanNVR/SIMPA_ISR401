#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de fichas técnicas — Proyecto SIMPA
Equipo AHMRV · ISR-401 · UTEQ

Recorre una carpeta con archivos YA DESCIFRADOS (el contenido extraído de un
contenedor .7z del repositorio complementario) y produce/actualiza
fichas_tecnicas.csv con una fila por archivo: duración, códec, tamaño y
SHA-256 calculados directamente del archivo — nunca inventados.

Principio del punto 18 del plan operativo: si un dato no se puede obtener,
el script se detiene con un error explícito. NUNCA escribe "PENDIENTE".

Uso:
    python3 generar_fichas.py <carpeta_extraida> <nombre_contenedor.7z> \
        <repositorio_url> <url_release> \
        [--csv ruta/a/fichas_tecnicas.csv] [--actualizar]

Ejemplo real:
    python3 07_Datos/scripts/generar_fichas.py ./tmp_extraido/audios \
        evidencias_entrevistas_audios.7z \
        https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias \
        https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-evidencias/evidencias_entrevistas_audios.7z \
        --csv 02_Evidencias/00_Restringido/fichas_tecnicas.csv --actualizar

Codigos de participante reconocidos: ENTR-XX (entrevistas) y WT-XX (walkthrough).

Requiere: ffprobe (parte de ffmpeg) para audio/video. No requiere nada extra
para calcular tamaño o SHA-256 (usa la librería estándar de Python).
"""

import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CABECERA = [
    "id_archivo", "tipo", "fecha", "codigo_participante",
    "duracion_segundos", "codec", "tamano_bytes", "sha256",
    "contenedor", "ruta_en_contenedor", "estado_archivo", "estado_hash",
    "ruta_detectada_relativa", "repositorio", "url_release",
]

EXT_AUDIO = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}
EXT_VIDEO = {".mp4", ".mov", ".mkv", ".avi", ".webm"}
EXT_IMAGEN = {".jpg", ".jpeg", ".png", ".heic"}
EXT_DOC = {".pdf"}

# Patrones de nomenclatura del proyecto:
#   Entrevistas: AAAA-MM-DD_Rol_ENTR-XX_Tecnica.ext
#   Walkthrough: AAAA-MM-DD_Walkthrough_Perfil_WT-XX_Tipo.ext
PATRON_NOMBRE = re.compile(
    r"(?P<fecha>\d{4}-\d{2}-\d{2}).*?(?P<entr>(?:ENTR|WT)-\d{2})", re.IGNORECASE
)

# Patron alterno para archivos ya publicados dentro de contenedores, cuyo nombre
# interno no puede cambiarse sin resubir el contenedor: P01_video_01.mp4
PATRON_ALTERNO = re.compile(r"^P(?P<num>\d{2})_", re.IGNORECASE)

# Mapa ENTR-XX -> fecha, construido en tiempo de ejecucion desde los nombres de
# los consentimientos. NUNCA se rellena a mano.
MAPA_FECHAS = {}


def cargar_mapa_fechas(carpeta):
    """Construye {ENTR-XX: fecha} leyendo los nombres de archivo de una carpeta.

    Se usa para resolver la fecha de archivos cuyo nombre interno no la lleva.
    La fecha procede de un consentimiento real, no de una suposicion.
    """
    carpeta = Path(carpeta)
    if not carpeta.is_dir():
        error(f"--fechas-desde: '{carpeta}' no es una carpeta valida.")
    encontrados = 0
    for ruta in carpeta.rglob("*"):
        if not ruta.is_file():
            continue
        m = PATRON_NOMBRE.search(ruta.name)
        if m:
            codigo = m.group("entr").upper()
            fecha = m.group("fecha")
            previa = MAPA_FECHAS.get(codigo)
            if previa and previa != fecha:
                error(f"Fecha contradictoria para {codigo}: '{previa}' y '{fecha}'. "
                      "Revisa los nombres antes de continuar.")
            MAPA_FECHAS[codigo] = fecha
            encontrados += 1
    if not encontrados:
        error(f"--fechas-desde: no se reconocio ningun nombre con patron "
              f"AAAA-MM-DD_..._ENTR-XX_... en '{carpeta}'.")
    print(f"Mapa de fechas construido desde '{carpeta}': "
          f"{len(MAPA_FECHAS)} codigos.")


def error(msg):
    sys.exit(f"ERROR: {msg}\nEl script se detiene aquí — no se escribe PENDIENTE.")


def sha256_de(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloque)
    return h.hexdigest()


def ffprobe_info(ruta):
    """Devuelve (duracion_segundos, codec) usando ffprobe. Falla si no puede."""
    try:
        salida = subprocess.run(
            [
                "ffprobe", "-v", "error", "-print_format", "json",
                "-show_format", "-show_streams", str(ruta),
            ],
            capture_output=True, text=True, check=True,
        )
    except FileNotFoundError:
        error("ffprobe no está instalado o no está en el PATH. "
              "Instálalo (ffmpeg) antes de correr este script.")
    except subprocess.CalledProcessError as e:
        error(f"ffprobe no pudo leer '{ruta}': {e.stderr.strip()}")

    datos = json.loads(salida.stdout)
    duracion = datos.get("format", {}).get("duration")
    if duracion is None:
        error(f"No se pudo obtener la duración de '{ruta}' (ffprobe no la reportó).")

    codecs = []
    for stream in datos.get("streams", []):
        c = stream.get("codec_name")
        if c and c not in codecs:
            codecs.append(c)
    if not codecs:
        error(f"No se pudo obtener el códec de '{ruta}' (ffprobe no reportó streams).")

    return round(float(duracion), 6), "+".join(codecs)


def extraer_fecha_participante(nombre_archivo):
    m = PATRON_NOMBRE.search(nombre_archivo)
    if m:
        return m.group("fecha"), m.group("entr").upper()

    # Nombre interno ya publicado, del tipo P01_video_01.mp4
    a = PATRON_ALTERNO.search(nombre_archivo)
    if a:
        codigo = "ENTR-%s" % a.group("num")
        fecha = MAPA_FECHAS.get(codigo)
        if not fecha:
            error(
                f"'{nombre_archivo}' resuelve a {codigo}, pero no hay fecha para "
                f"ese codigo. Ejecuta con --fechas-desde apuntando a la carpeta "
                "de consentimientos, para que la fecha proceda de un documento "
                "real y no de una suposicion."
            )
        return fecha, codigo

    error(
        f"'{nombre_archivo}' no sigue el patrón AAAA-MM-DD_..._ENTR-XX_... "
        "ni AAAA-MM-DD_..._WT-XX_... ni PNN_...; "
        "no se puede inferir fecha/código de participante de forma segura. "
        "Renombra el archivo antes de procesarlo."
    )


def procesar_archivo(ruta, contenedor, ruta_en_contenedor, repositorio, url_release):
    nombre = ruta.name
    ext = ruta.suffix.lower()

    if ext in EXT_AUDIO:
        tipo = "audio"
        duracion, codec = ffprobe_info(ruta)
    elif ext in EXT_VIDEO:
        tipo = "video"
        duracion, codec = ffprobe_info(ruta)
    elif ext in EXT_IMAGEN:
        tipo = "imagen"
        duracion, codec = "N/A", "N/A"
    elif ext in EXT_DOC:
        tipo = "documento"
        duracion, codec = "N/A", "N/A"
    else:
        error(f"Extensión no reconocida en '{nombre}' ({ext}). "
              "Agrega el tipo correspondiente en EXT_AUDIO/EXT_VIDEO/EXT_IMAGEN "
              "del script, o renombra el archivo.")

    fecha, codigo_participante = extraer_fecha_participante(nombre)
    tamano = ruta.stat().st_size
    if tamano == 0:
        error(f"'{nombre}' pesa 0 bytes — archivo corrupto o vacío.")
    hash_sha = sha256_de(ruta)

    return {
        "id_archivo": nombre,
        "tipo": tipo,
        "fecha": fecha,
        "codigo_participante": codigo_participante,
        "duracion_segundos": duracion,
        "codec": codec,
        "tamano_bytes": tamano,
        "sha256": hash_sha,
        "contenedor": contenedor,
        "ruta_en_contenedor": ruta_en_contenedor,
        "estado_archivo": "RUTA",
        "estado_hash": "OK",
        "ruta_detectada_relativa": ruta_en_contenedor,
        "repositorio": repositorio,
        "url_release": url_release,
    }


def main():
    args = sys.argv[1:]
    if len(args) < 4:
        sys.exit(__doc__)

    carpeta, contenedor, repositorio, url_release = args[:4]
    resto = args[4:]

    ruta_csv = "fichas_tecnicas.csv"
    actualizar = False
    i = 0
    while i < len(resto):
        if resto[i] == "--csv":
            ruta_csv = resto[i + 1]
            i += 2
        elif resto[i] == "--actualizar":
            actualizar = True
            i += 1
        elif resto[i] == "--fechas-desde":
            cargar_mapa_fechas(resto[i + 1])
            i += 2
        else:
            error(f"Argumento no reconocido: {resto[i]}")

    carpeta = Path(carpeta)
    if not carpeta.is_dir():
        error(f"'{carpeta}' no es una carpeta válida.")

    archivos = sorted(p for p in carpeta.rglob("*") if p.is_file())
    if not archivos:
        error(f"No se encontró ningún archivo dentro de '{carpeta}'.")

    filas_nuevas = {}
    for ruta in archivos:
        ruta_relativa = ruta.relative_to(carpeta).as_posix()
        fila = procesar_archivo(ruta, contenedor, ruta_relativa, repositorio, url_release)
        filas_nuevas[fila["id_archivo"]] = fila
        print(f"OK  {fila['id_archivo']}  ({fila['tipo']}, {fila['tamano_bytes']} bytes)")

    # Cargar CSV existente si se pide actualizar, preservando filas no tocadas
    filas_finales = []
    ids_ya_escritos = set()
    if actualizar and os.path.exists(ruta_csv):
        with open(ruta_csv, encoding="utf-8-sig", newline="") as f:
            lector = csv.DictReader(f, delimiter=";")
            for fila in lector:
                if fila["id_archivo"] in filas_nuevas:
                    filas_finales.append(filas_nuevas[fila["id_archivo"]])
                    ids_ya_escritos.add(fila["id_archivo"])
                else:
                    filas_finales.append(fila)

    for id_archivo, fila in filas_nuevas.items():
        if id_archivo not in ids_ya_escritos:
            filas_finales.append(fila)

    with open(ruta_csv, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=CABECERA, delimiter=";")
        escritor.writeheader()
        escritor.writerows(filas_finales)

    print(f"\n{len(filas_nuevas)} archivo(s) procesados. CSV escrito en: {ruta_csv}")
    print("Ningún dato fue inventado: todo viene de ffprobe, os.stat y sha256 real.")


if __name__ == "__main__":
    main()
