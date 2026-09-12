#!/usr/bin/env python3

import csv
import sys
from pathlib import Path
from collections import Counter

RUTA_PUNTUACIONES = Path(
    "06_Experimento/evaluadores/puntuaciones_reales.csv"
)

RUTA_MAPA = Path(
    "../mapa_confidencial_NO_SUBIR/mapa_origen.csv"
)

RUTA_SALIDA = Path(
    "07_Datos/datos_procesados/puntuaciones_experimento_con_origen.csv"
)


def error(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main():
    if not RUTA_PUNTUACIONES.exists():
        error(f"No existe {RUTA_PUNTUACIONES}")

    if not RUTA_MAPA.exists():
        error(f"No existe {RUTA_MAPA}")

    mapa = {}

    with RUTA_MAPA.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")

        for fila in reader:
            rid = fila["id_cegado"].strip()

            if rid in mapa:
                error(f"ID duplicado en mapa: {rid}")

            mapa[rid] = {
                "origen": fila["origen"].strip(),
                "id_original": fila["id_original"].strip(),
                "semilla_usada": fila["semilla_usada"].strip(),
            }

    if len(mapa) != 50:
        error(f"El mapa debería tener 50 requisitos y tiene {len(mapa)}")

    conteo_origen_mapa = Counter(
        x["origen"] for x in mapa.values()
    )

    if conteo_origen_mapa["Humano"] != 25:
        error(
            f"Se esperaban 25 requisitos humanos; hay "
            f"{conteo_origen_mapa['Humano']}"
        )

    if conteo_origen_mapa["LLM"] != 25:
        error(
            f"Se esperaban 25 requisitos LLM; hay "
            f"{conteo_origen_mapa['LLM']}"
        )

    filas = []

    with RUTA_PUNTUACIONES.open(
        encoding="utf-8-sig",
        newline=""
    ) as f:

        reader = csv.DictReader(f)

        for fila in reader:
            rid = fila["requisito"].strip()

            if rid not in mapa:
                error(f"{rid} no existe en mapa_origen.csv")

            try:
                puntuacion = int(fila["puntuacion"])
                orden = int(fila["orden"])
            except ValueError:
                error(f"Puntuación u orden inválido en {rid}")

            if puntuacion < 1 or puntuacion > 5:
                error(
                    f"Puntuación fuera de rango en "
                    f"{rid}: {puntuacion}"
                )

            filas.append({
                "evaluador": fila["evaluador"].strip(),
                "requisito": rid,
                "origen": mapa[rid]["origen"],
                "id_original": mapa[rid]["id_original"],
                "dimension": fila["dimension"].strip(),
                "puntuacion": puntuacion,
                "orden": orden,
            })

    if len(filas) != 750:
        error(
            f"Se esperaban 750 puntuaciones; "
            f"hay {len(filas)}"
        )

    evaluadores = sorted(
        set(f["evaluador"] for f in filas)
    )

    requisitos = sorted(
        set(f["requisito"] for f in filas)
    )

    dimensiones = sorted(
        set(f["dimension"] for f in filas)
    )

    if len(evaluadores) != 3:
        error(
            f"Se esperaban 3 evaluadores; "
            f"hay {len(evaluadores)}"
        )

    if len(requisitos) != 50:
        error(
            f"Se esperaban 50 requisitos; "
            f"hay {len(requisitos)}"
        )

    if len(dimensiones) != 5:
        error(
            f"Se esperaban 5 dimensiones; "
            f"hay {len(dimensiones)}"
        )

    por_requisito = Counter(
        f["requisito"] for f in filas
    )

    incorrectos = {
        k: v
        for k, v in por_requisito.items()
        if v != 15
    }

    if incorrectos:
        error(
            "Requisitos con cantidad incorrecta "
            f"de puntuaciones: {incorrectos}"
        )

    por_evaluador = Counter(
        f["evaluador"] for f in filas
    )

    incorrectos_eval = {
        k: v
        for k, v in por_evaluador.items()
        if v != 250
    }

    if incorrectos_eval:
        error(
            "Evaluadores con cantidad incorrecta: "
            f"{incorrectos_eval}"
        )

    RUTA_SALIDA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    campos = [
        "evaluador",
        "requisito",
        "origen",
        "id_original",
        "dimension",
        "puntuacion",
        "orden",
    ]

    with RUTA_SALIDA.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=campos
        )

        writer.writeheader()
        writer.writerows(filas)

    print("Preparación del dataset analítico")
    print("--------------------------------")
    print(f"Puntuaciones totales: {len(filas)}")
    print(
        f"Evaluadores: {len(evaluadores)} -> "
        f"{', '.join(evaluadores)}"
    )
    print(f"Requisitos: {len(requisitos)}")
    print(
        f"Dimensiones: {len(dimensiones)} -> "
        f"{', '.join(dimensiones)}"
    )
    print("Origen:")
    print("  Humano: 25 requisitos")
    print("  LLM:    25 requisitos")
    print("Puntuaciones por evaluador:")

    for ev in evaluadores:
        print(
            f"  {ev}: "
            f"{por_evaluador[ev]}"
        )

    print()
    print(f"OK: {RUTA_SALIDA}")


if __name__ == "__main__":
    main()
