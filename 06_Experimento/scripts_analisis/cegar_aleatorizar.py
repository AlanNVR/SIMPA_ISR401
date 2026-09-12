#!/usr/bin/env python3
"""
cegar_aleatorizar.py — TAREA EXP-05

Toma los 25 requisitos humanos (06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv)
y los 25 requisitos del LLM (06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md),
y produce:

  1) 06_Experimento/cegado/requisitos_cegados.csv
     — Los 50 requisitos normalizados al MISMO formato, SIN ninguna pista de
       procedencia, con IDs nuevos R-001..R-050, en orden ALEATORIO.
       Este es el archivo que reciben los evaluadores.

  2) ../mapa_confidencial_NO_SUBIR/mapa_origen.csv  (FUERA del repo)
     — R-ID ↔ origen (Humano/LLM) ↔ ID original ↔ semilla usada.
       Este archivo NO se entrega a los evaluadores y NO debe quedar dentro
       del repo, para que no se pueda subir por accidente. Custodio: Edson
       Rizzo, según el reparto de EXP-05.

Qué se retira para cegar:
  - id_origen, evidencia_fuente, procedencia, nota_metodologica (CSV humano)
  - códigos de evidencia embebidos en actor_origen (ej. "· EV-02, EV-04")
  - el prefijo H-/LLM- de los identificadores originales

Qué se normaliza para que ambos conjuntos luzcan iguales:
  - "Pre:/Post:" (humano) y "Precondición:/Postcondición:" (LLM) -> un único
    formato: "Precondición: ... | Postcondición: ..."
  - encabezados de campo idénticos y en el mismo orden para los dos orígenes

Uso:
    python3 cegar_aleatorizar.py [--seed 20260912]

Requiere ejecutarse desde la RAÍZ del repositorio.
"""

import argparse
import csv
import random
import re
import sys
from pathlib import Path

RUTA_HUMANO = Path("06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv")
RUTA_LLM = Path("06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md")
DIR_SALIDA = Path("06_Experimento/cegado")          # dentro del repo — solo el archivo cegado
DIR_SALIDA_CONFIDENCIAL = Path("../mapa_confidencial_NO_SUBIR")  # FUERA del repo
RUTA_CEGADOS = DIR_SALIDA / "requisitos_cegados.csv"
RUTA_MAPA = DIR_SALIDA_CONFIDENCIAL / "mapa_origen.csv"

CAMPOS_SALIDA = [
    "id_cegado",
    "nombre",
    "descripcion",
    "actor",
    "entradas_salidas",
    "precondicion_postcondicion",
    "prioridad_moscow",
    "criterio_verificacion",
]


def normalizar_pre_post(texto: str) -> str:
    """Unifica 'Pre:/Post:' y 'Precondición:/Postcondición:' a un solo formato."""
    t = texto.strip()
    t = re.sub(r"\bPre:\s*", "Precondición: ", t)
    t = re.sub(r"\bPost:\s*", "Postcondición: ", t)
    # separador uniforme entre precondición y postcondición
    t = re.sub(r"\s*Postcondición:", " | Postcondición:", t)
    t = re.sub(r"\s*\|\s*\|\s*", " | ", t)
    return t.strip()


def limpiar_actor(texto: str) -> str:
    """Quita códigos de evidencia embebidos, ej. 'Administrador · EV-02, EV-04' -> 'Administrador'."""
    return re.split(r"\s*·\s*", texto.strip())[0].strip()


def leer_humanos(ruta: Path):
    items = []
    with ruta.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for fila in reader:
            items.append({
                "origen": "Humano",
                "id_original": fila["id_conjunto"].strip(),
                "nombre": fila["nombre"].strip(),
                "descripcion": fila["descripcion"].strip(),
                "actor": limpiar_actor(fila["actor_origen"]),
                "entradas_salidas": fila["entradas_salidas"].strip(),
                "precondicion_postcondicion": normalizar_pre_post(fila["pre_postcondiciones"]),
                "prioridad_moscow": fila["prioridad"].strip(),
                "criterio_verificacion": fila["criterio_verificacion"].strip(),
            })
    return items


PATRON_BLOQUE_LLM = re.compile(
    r"###\s*(LLM-\d+)\s*\n"
    r"1\.\s*\*\*Identificador:\*\*\s*.*?\n"
    r"2\.\s*\*\*Nombre:\*\*\s*(.*?)\n"
    r"3\.\s*\*\*Descripción:\*\*\s*(.*?)\n"
    r"4\.\s*\*\*Actor/origen:\*\*\s*(.*?)\n"
    r"5\.\s*\*\*Entradas/salidas:\*\*\s*(.*?)\n"
    r"6\.\s*\*\*Precondiciones/postcondiciones:\*\*\s*(.*?)\n"
    r"7\.\s*\*\*Prioridad MoSCoW:\*\*\s*(.*?)\n"
    r"8\.\s*\*\*Criterio de verificación:\*\*\s*(.*?)(?:\n\n|\Z)",
    re.DOTALL,
)


def leer_llm(ruta: Path):
    texto = ruta.read_text(encoding="utf-8")
    items = []
    for m in PATRON_BLOQUE_LLM.finditer(texto):
        (id_original, nombre, descripcion, actor, entradas_salidas,
         pre_post, prioridad, criterio) = m.groups()
        items.append({
            "origen": "LLM",
            "id_original": id_original.strip(),
            "nombre": nombre.strip(),
            "descripcion": descripcion.strip(),
            "actor": limpiar_actor(actor),
            "entradas_salidas": entradas_salidas.strip(),
            "precondicion_postcondicion": normalizar_pre_post(pre_post),
            "prioridad_moscow": prioridad.strip(),
            "criterio_verificacion": criterio.strip(),
        })
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20260912,
                     help="Semilla de aleatorización (documentar el valor usado en el mapa)")
    args = ap.parse_args()

    if not RUTA_HUMANO.exists() or not RUTA_LLM.exists():
        print("ERROR: corre este script desde la raíz del repositorio "
              "(no encuentro los archivos de entrada).", file=sys.stderr)
        sys.exit(1)

    humanos = leer_humanos(RUTA_HUMANO)
    llm = leer_llm(RUTA_LLM)

    print(f"Requisitos humanos leídos: {len(humanos)}")
    print(f"Requisitos LLM leídos:     {len(llm)}")

    if len(humanos) != 25 or len(llm) != 25:
        print("⚠️  ADVERTENCIA: se esperaban 25 y 25. Revisar antes de continuar.",
              file=sys.stderr)

    todos = humanos + llm

    rng = random.Random(args.seed)
    rng.shuffle(todos)

    DIR_SALIDA.mkdir(parents=True, exist_ok=True)
    DIR_SALIDA_CONFIDENCIAL.mkdir(parents=True, exist_ok=True)

    with RUTA_CEGADOS.open("w", encoding="utf-8", newline="") as f_cegado, \
         RUTA_MAPA.open("w", encoding="utf-8", newline="") as f_mapa:

        w_cegado = csv.DictWriter(f_cegado, fieldnames=CAMPOS_SALIDA, delimiter=";")
        w_cegado.writeheader()

        w_mapa = csv.writer(f_mapa, delimiter=";")
        w_mapa.writerow(["id_cegado", "origen", "id_original", "semilla_usada"])

        for i, item in enumerate(todos, start=1):
            id_cegado = f"R-{i:03d}"

            w_cegado.writerow({
                "id_cegado": id_cegado,
                "nombre": item["nombre"],
                "descripcion": item["descripcion"],
                "actor": item["actor"],
                "entradas_salidas": item["entradas_salidas"],
                "precondicion_postcondicion": item["precondicion_postcondicion"],
                "prioridad_moscow": item["prioridad_moscow"],
                "criterio_verificacion": item["criterio_verificacion"],
            })

            w_mapa.writerow([id_cegado, item["origen"], item["id_original"], args.seed])

    print(f"\n✅ Escrito: {RUTA_CEGADOS}  ({len(todos)} filas, para evaluadores)")
    print(f"✅ Escrito: {RUTA_MAPA}  (CONFIDENCIAL — custodio: Edson Rizzo, no compartir)")
    print(f"   Semilla usada: {args.seed}")


if __name__ == "__main__":
    main()
