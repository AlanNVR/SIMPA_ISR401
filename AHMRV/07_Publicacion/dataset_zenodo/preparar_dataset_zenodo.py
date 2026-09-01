#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prepara el conjunto de datos destinado a depósito abierto en Zenodo.

Entrada:
    AHMRV/07_Publicacion/respuestas_anonimizadas.csv

Salida:
    AHMRV/07_Publicacion/dataset_zenodo/respuestas_zenodo.csv

Transformaciones:
- elimina las marcas temporales exactas;
- elimina todas las columnas de comentarios;
- conserva ID y las respuestas cerradas;
- no modifica, recodifica ni imputa respuestas.
"""

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[3]

entrada = ROOT / "AHMRV" / "07_Publicacion" / "respuestas_anonimizadas.csv"
salida = ROOT / "AHMRV" / "07_Publicacion" / "dataset_zenodo" / "respuestas_zenodo.csv"

if not entrada.exists():
    sys.exit(f"ERROR: no existe el archivo de entrada: {entrada}")

with entrada.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    if reader.fieldnames is None:
        sys.exit("ERROR: el CSV no contiene encabezados.")

    encabezados = list(reader.fieldnames)
    filas = list(reader)

excluir_exactas = {
    "Hora de inicio",
    "Hora de finalización",
}

def es_comentario(nombre):
    return (
        nombre == "Comentarios del cuestionario"
        or nombre.startswith("Comentarios:")
    )

conservar = [
    h for h in encabezados
    if h not in excluir_exactas and not es_comentario(h)
]

# Guardas de seguridad para evitar publicar accidentalmente campos no previstos.
if "ID" not in conservar:
    sys.exit("ERROR: no se encontró la columna ID esperada.")

if len(conservar) != 16:
    sys.exit(
        f"ERROR: se esperaban 16 columnas publicables y se obtuvieron "
        f"{len(conservar)}. Revisar estructura antes de publicar."
    )

for campo in excluir_exactas:
    if campo not in encabezados:
        sys.exit(f"ERROR: falta la columna esperada: {campo}")

# Si alguna columna de comentarios adquiere contenido en una versión futura,
# se exige revisión manual antes de regenerar el paquete abierto.
comentarios = [h for h in encabezados if es_comentario(h)]

for campo in comentarios:
    if any((fila.get(campo) or "").strip() for fila in filas):
        sys.exit(
            f"ERROR: la columna de texto libre '{campo}' contiene datos. "
            f"Revisión manual requerida antes de depósito abierto."
        )

salida.parent.mkdir(parents=True, exist_ok=True)

with salida.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=conservar,
        lineterminator="\r\n",
    )
    writer.writeheader()

    for fila in filas:
        writer.writerow({h: fila.get(h, "") for h in conservar})

print("Dataset Zenodo generado.")
print("Filas:", len(filas))
print("Columnas originales:", len(encabezados))
print("Columnas publicables:", len(conservar))
print("Marcas temporales eliminadas: 2")
print("Columnas de comentarios eliminadas:", len(comentarios))
print("Salida:", salida)
