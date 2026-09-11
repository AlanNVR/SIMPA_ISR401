#!/usr/bin/env python3
"""
AUT-07 — Paso 0: congelar el subconjunto fijo antes de la doble codificación.

Extrae los fragmentos de EV-04 (ronda dominio) y ENTR-13 (ronda contraste)
directamente de los archivos fuente ya codificados por el equipo, y genera:

  1. subconjunto_fragmentos.csv — SOLO el texto del fragmento y su ID de
     evidencia, SIN el código/categoría original. Es lo único que Allan y
     Josthyn deben ver antes de codificar.
  2. codificacion_allan.csv y codificacion_josthyn.csv — plantillas vacías
     con las mismas filas, para que cada quien complete Codigo/Categoria de
     forma independiente.

Ejecutar UNA sola vez, desde la raíz del repo. No debe volver a ejecutarse
después de que alguien empiece a codificar, o el subconjunto dejaría de
estar congelado.
"""
import csv
from pathlib import Path

REPO = Path(".")
SALIDA = Path("10_Autoria/doble_codificacion")
SALIDA.mkdir(parents=True, exist_ok=True)

FUENTES = [
    ("07_Datos/datos_crudos/codificacion.csv", "EV-04"),
    ("07_Datos/datos_procesados/codificacion_tercera_ronda.csv", "ENTR-13"),
]

filas_subconjunto = []
for ruta, entrevista_objetivo in FUENTES:
    with open(REPO / ruta, encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f, delimiter=";")
        for fila in lector:
            if fila["ID_evidencia"] == entrevista_objetivo:
                filas_subconjunto.append({
                    "ID_fragmento": None,  # se asigna después, secuencial
                    "Fragmento": fila["Fragmento"],
                    "ID_evidencia": fila["ID_evidencia"],
                })

# ID secuencial estable, independiente del orden original de las fuentes
for i, fila in enumerate(filas_subconjunto, start=1):
    fila["ID_fragmento"] = f"DC-{i:03d}"

# 1. Subconjunto congelado (sin códigos, lo único visible antes de codificar)
with open(SALIDA / "subconjunto_fragmentos.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["ID_fragmento", "Fragmento", "ID_evidencia"], delimiter=";")
    w.writeheader()
    for fila in filas_subconjunto:
        w.writerow(fila)

# 2. Plantillas vacías, una por codificador
for nombre in ["allan", "josthyn"]:
    with open(SALIDA / f"codificacion_{nombre}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "ID_fragmento", "Fragmento", "ID_evidencia", "Codigo", "Categoria"
        ], delimiter=";")
        w.writeheader()
        for fila in filas_subconjunto:
            w.writerow({
                "ID_fragmento": fila["ID_fragmento"],
                "Fragmento": fila["Fragmento"],
                "ID_evidencia": fila["ID_evidencia"],
                "Codigo": "",       # a completar por el codificador
                "Categoria": "",    # a completar por el codificador
            })

print(f"Subconjunto congelado: {len(filas_subconjunto)} fragmentos "
      f"({sum(1 for f in filas_subconjunto if f['ID_evidencia']=='EV-04')} de EV-04, "
      f"{sum(1 for f in filas_subconjunto if f['ID_evidencia']=='ENTR-13')} de ENTR-13)")
print(f"Archivos generados en {SALIDA}/")
