#!/usr/bin/env python3
"""Ejecuta la cadena reproducible disponible del paquete 07_Datos."""

from pathlib import Path
import csv
import hashlib
import importlib.util
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
DATOS = ROOT / "07_Datos"
SCRIPTS = DATOS / "scripts"
CRUDOS = DATOS / "datos_crudos"
PROCESADOS = DATOS / "datos_procesados"
RESULTADOS = DATOS / "resultados"

XLSX = CRUDOS / "Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx"
CODIFICACION_DOMINIO = CRUDOS / "codificacion.csv"
CODIFICACION_CONTRASTE = PROCESADOS / "codificacion_tercera_ronda.csv"

ANONIMIZADAS = PROCESADOS / "respuestas_anonimizadas.csv"
ZENODO = PROCESADOS / "respuestas_zenodo_agregadas.csv"

TABLA_SAT = RESULTADOS / "tabla_saturacion.csv"
FIGURAS_SAT = [
    RESULTADOS / "curva_saturacion_dominio.png",
    RESULTADOS / "curva_saturacion_dominio.pdf",
    RESULTADOS / "curva_saturacion_contraste.png",
    RESULTADOS / "curva_saturacion_contraste.pdf",
    RESULTADOS / "curva_saturacion_agregada.png",
    RESULTADOS / "curva_saturacion_agregada.pdf",
]

ZENODO_SHA256 = "b40ab460fc1d3d931beebaf5dd3037f564db8774559feee1ec1d371fa01b39b9"


def ejecutar(etiqueta, *comando):
    print(f"\n=== {etiqueta} ===", flush=True)
    subprocess.run(
        [str(x) for x in comando],
        cwd=ROOT,
        check=True,
    )


def comprobar_dependencias():
    faltan = [
        nombre
        for nombre in ("openpyxl", "matplotlib")
        if importlib.util.find_spec(nombre) is None
    ]

    if faltan:
        raise RuntimeError(
            "Faltan dependencias Python: " + ", ".join(faltan)
        )


def comprobar_entrada(path):
    if not path.is_file():
        raise FileNotFoundError(f"No existe el insumo requerido: {path}")


def dimensiones_csv(path, delimiter=","):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, delimiter=delimiter)
        cabecera = next(reader)
        filas = sum(1 for _ in reader)

    return filas, len(cabecera)


def sha256(path):
    h = hashlib.sha256()

    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloque)

    return h.hexdigest()


def comprobar_tabla_saturacion(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))

    if len(rows) != 16:
        raise RuntimeError(
            f"tabla_saturacion.csv debe contener 16 entrevistas; contiene {len(rows)}"
        )

    ids = [r["ID_entrevista"] for r in rows]
    esperados = [f"ENTR-{i:02d}" for i in range(1, 17)]
    if ids != esperados:
        raise RuntimeError(
            "Orden/IDs inesperados en tabla_saturacion.csv:\n"
            f"Esperado: {esperados}\nObtenido: {ids}"
        )

    estratos = [r["Estrato"] for r in rows]
    if estratos[:8] != ["dominio"] * 8 or estratos[8:] != ["contraste"] * 8:
        raise RuntimeError("La separación dominio/contraste de tabla_saturacion.csv es incorrecta")

    return rows


def main():
    print("SIMPA — cadena reproducible de 07_Datos")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Raíz: {ROOT}")

    comprobar_dependencias()
    comprobar_entrada(XLSX)
    comprobar_entrada(CODIFICACION_DOMINIO)
    comprobar_entrada(CODIFICACION_CONTRASTE)

    RESULTADOS.mkdir(parents=True, exist_ok=True)

    ejecutar(
        "1/3 Anonimización del cuestionario",
        sys.executable,
        SCRIPTS / "anonimizar_encuesta.py",
        XLSX,
        "--out",
        ANONIMIZADAS,
    )

    ejecutar(
        "2/3 Dataset agregado para Zenodo",
        sys.executable,
        SCRIPTS / "preparar_dataset_zenodo_agregado.py",
    )

    ejecutar(
        "3/3 Análisis de saturación estratificado",
        sys.executable,
        SCRIPTS / "curva_saturacion.py",
    )

    esperados = [
        ANONIMIZADAS,
        ZENODO,
        TABLA_SAT,
        *FIGURAS_SAT,
    ]

    for path in esperados:
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(f"Salida ausente o vacía: {path}")

    if dimensiones_csv(ANONIMIZADAS) != (62, 34):
        raise RuntimeError(
            f"Dimensiones inesperadas en {ANONIMIZADAS.name}: "
            f"{dimensiones_csv(ANONIMIZADAS)}"
        )

    if dimensiones_csv(ZENODO) != (64, 7):
        raise RuntimeError(
            f"Dimensiones inesperadas en {ZENODO.name}: "
            f"{dimensiones_csv(ZENODO)}"
        )

    if dimensiones_csv(TABLA_SAT, delimiter=";") != (16, 11):
        raise RuntimeError(
            f"Dimensiones inesperadas en {TABLA_SAT.name}: "
            f"{dimensiones_csv(TABLA_SAT, delimiter=';')}"
        )

    tabla = comprobar_tabla_saturacion(TABLA_SAT)

    hash_zenodo = sha256(ZENODO)

    if hash_zenodo != ZENODO_SHA256:
        raise RuntimeError(
            "El dataset Zenodo reproducido no coincide con el snapshot publicado.\n"
            f"Esperado: {ZENODO_SHA256}\n"
            f"Obtenido: {hash_zenodo}"
        )

    print("\n=== VERIFICACIÓN FINAL ===")
    print("respuestas_anonimizadas.csv: 62 filas × 34 columnas")
    print("respuestas_zenodo_agregadas.csv: 64 filas × 7 columnas")
    print("tabla_saturacion.csv: 16 filas × 11 columnas")
    print("estrato dominio: 8 entrevistas")
    print("estrato contraste: 8 entrevistas")
    print(f"códigos agregados al cierre: {tabla[-1]['Codigos_acumulados_agregado']}")
    print(f"SHA-256 Zenodo: {hash_zenodo}")
    print("\nOK: cadena reproducible completada correctamente.")


if __name__ == "__main__":
    main()
