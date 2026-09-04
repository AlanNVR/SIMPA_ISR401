#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_fichas.py — Verifica que cada fila de fichas_tecnicas.csv apunte a un
contenedor que existe realmente como asset del release, comprobando cada URL por
HTTP.

Uso, desde la raiz del repositorio:

    python 07_Datos/scripts/verificar_fichas.py

Produce:
    02_Evidencias/00_Restringido/verificacion_fichas.md

No modifica el CSV. Solo verifica y reporta.
"""

import csv
import os
import sys
import urllib.request
from collections import Counter
from datetime import date

CSV = "02_Evidencias/00_Restringido/fichas_tecnicas.csv"
SALIDA = "02_Evidencias/00_Restringido/verificacion_fichas.md"
BASE = ("https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias"
        "/releases/download/v1.0-evidencias")


def http_status(url, timeout=25):
    """Devuelve el codigo HTTP siguiendo redirecciones, o 0 si falla la red."""
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def main():
    if not os.path.exists(CSV):
        sys.exit("No encuentro %s. Ejecuta desde la raiz del repositorio." % CSV)

    with open(CSV, newline="", encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f, delimiter=";"))

    print("Filas leidas: %d" % len(filas))

    # Contenedores distintos declarados en el CSV
    contenedores = sorted({(r.get("contenedor") or "").strip() for r in filas} - {""})
    print("Contenedores distintos declarados: %d" % len(contenedores))

    # Una peticion HTTP por contenedor distinto, no por fila
    estado = {}
    for c in contenedores:
        url = "%s/%s" % (BASE, c)
        estado[c] = http_status(url)
        print("  %-3s %s" % (estado[c], c))

    # Comprobacion adicional: la url_release de cada fila debe apuntar al mismo
    # contenedor que declara la columna 'contenedor'
    incoherentes = []
    for r in filas:
        c = (r.get("contenedor") or "").strip()
        u = (r.get("url_release") or "").strip()
        if c and u and not u.endswith("/" + c):
            incoherentes.append((r.get("id_archivo", "?"), c, u))

    ok = sum(1 for r in filas if estado.get((r.get("contenedor") or "").strip()) == 200)
    roto = len(filas) - ok

    # Celdas afectadas: columna 'contenedor' + columna 'url_release' por fila rota
    celdas = roto * 2

    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write("# Verificacion de fichas_tecnicas.csv\n\n")
        f.write("**Fecha de verificacion:** %s\n\n" % date.today().isoformat())
        f.write("**Metodo:** peticion HTTP HEAD siguiendo redirecciones sobre la\n")
        f.write("URL de descarga de cada contenedor declarado.\n\n")
        f.write("**Release:** `v1.0-evidencias` de "
                "`erizzov-boop/SIMPA_ISR401_Evidencias`\n\n")

        f.write("## Resumen\n\n")
        f.write("| Concepto | Valor |\n|---|---:|\n")
        f.write("| Filas del inventario | %d |\n" % len(filas))
        f.write("| Contenedores distintos declarados | %d |\n" % len(contenedores))
        f.write("| Filas que resuelven | %d |\n" % ok)
        f.write("| Filas que NO resuelven | %d |\n" % roto)
        f.write("| Celdas afectadas | %d |\n\n" % celdas)

        f.write("## Estado por contenedor\n\n")
        f.write("| Contenedor declarado | HTTP | Filas | Veredicto |\n")
        f.write("|---|---:|---:|---|\n")
        cuenta = Counter((r.get("contenedor") or "").strip() for r in filas)
        for c in contenedores:
            v = "resuelve" if estado[c] == 200 else "**NO resuelve**"
            f.write("| `%s` | %d | %d | %s |\n" % (c, estado[c], cuenta[c], v))
        f.write("\n")

        f.write("## Detalle por fila\n\n")
        f.write("| id_archivo | ENTR | Contenedor | HTTP |\n|---|---|---|---:|\n")
        for r in filas:
            c = (r.get("contenedor") or "").strip()
            f.write("| %s | %s | `%s` | %d |\n" % (
                r.get("id_archivo", ""), r.get("codigo_participante", ""),
                c, estado.get(c, 0)))
        f.write("\n")

        if incoherentes:
            f.write("## Incoherencias entre `contenedor` y `url_release`\n\n")
            f.write("| id_archivo | contenedor | url_release |\n|---|---|---|\n")
            for i, c, u in incoherentes:
                f.write("| %s | `%s` | `%s` |\n" % (i, c, u))
            f.write("\n")

        if roto == 0:
            f.write("## Conclusion\n\n")
            f.write("Las %d filas apuntan a un contenedor que existe con ese "
                    "nombre exacto.\n" % len(filas))
        else:
            f.write("## Conclusion\n\n")
            f.write("%d de %d filas declaran un contenedor inexistente. "
                    "La evidencia correspondiente no es alcanzable "
                    "siguiendo el inventario.\n" % (roto, len(filas)))

    print("\nEscrito: %s" % SALIDA)
    print("Filas que resuelven: %d de %d" % (ok, len(filas)))
    return 0 if roto == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
