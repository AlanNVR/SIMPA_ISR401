#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Genera el resumen agregado destinado al depósito abierto en Zenodo.

Entrada:
    07_Datos/datos_procesados/respuestas_anonimizadas.csv

Salida:
    07_Datos/datos_procesados/respuestas_zenodo_agregadas.csv

Criterios:
- excluye ID, marcas temporales y columnas de comentarios;
- agrega 15 preguntas sustantivas;
- trata "¿Cuál es la mayor dificultad en su trabajo diario?" como respuesta múltiple,
  separada por punto y coma;
- no publica respuestas individuales.
"""

from pathlib import Path
from collections import Counter
import csv
import sys

ROOT = Path(__file__).resolve().parents[2]
entrada = ROOT / "07_Datos" / "datos_procesados" / "respuestas_anonimizadas.csv"
salida = ROOT / "07_Datos" / "datos_procesados" / "respuestas_zenodo_agregadas.csv"

if not entrada.exists():
    sys.exit(f"ERROR: no existe el archivo de entrada: {entrada}")

with entrada.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    if reader.fieldnames is None:
        sys.exit("ERROR: el CSV no contiene encabezados.")
    encabezados = list(reader.fieldnames)
    filas = list(reader)

def es_comentario(nombre):
    return nombre == "Comentarios del cuestionario" or nombre.startswith("Comentarios:")

excluir = {"ID", "Hora de inicio", "Hora de finalización"}
preguntas = [h for h in encabezados if h not in excluir and not es_comentario(h)]

if len(filas) != 62:
    sys.exit(f"ERROR: se esperaban 62 registros y se obtuvieron {len(filas)}.")

if len(preguntas) != 15:
    sys.exit(f"ERROR: se esperaban 15 preguntas sustantivas y se obtuvieron {len(preguntas)}.")

pregunta_multiple = "¿Cuál es la mayor dificultad en su trabajo diario?"
if pregunta_multiple not in preguntas:
    sys.exit("ERROR: no se encontró la pregunta múltiple esperada.")

salida.parent.mkdir(parents=True, exist_ok=True)

campos = [
    "pregunta_id",
    "pregunta",
    "tipo_respuesta",
    "opcion",
    "frecuencia",
    "n_validos",
    "porcentaje",
]

with salida.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=campos, lineterminator="\r\n")
    writer.writeheader()

    for i, pregunta in enumerate(preguntas, start=1):
        valores = [(fila.get(pregunta) or "").strip() for fila in filas]
        validos = [v for v in valores if v]
        n_validos = len(validos)

        if pregunta == pregunta_multiple:
            contador = Counter()
            for valor in validos:
                opciones = [x.strip() for x in valor.split(";") if x.strip()]
                contador.update(opciones)
            tipo = "multiple"
        else:
            contador = Counter(validos)
            tipo = "simple"

        for opcion in sorted(contador):
            frecuencia = contador[opcion]
            porcentaje = (frecuencia / n_validos * 100) if n_validos else 0.0
            writer.writerow({
                "pregunta_id": f"P{i:02d}",
                "pregunta": pregunta,
                "tipo_respuesta": tipo,
                "opcion": opcion,
                "frecuencia": frecuencia,
                "n_validos": n_validos,
                "porcentaje": f"{porcentaje:.1f}",
            })

print("Resumen Zenodo agregado generado.")
print("Participantes de origen:", len(filas))
print("Preguntas agregadas:", len(preguntas))
print("Pregunta multiple:", pregunta_multiple)
print("Salida:", salida)
