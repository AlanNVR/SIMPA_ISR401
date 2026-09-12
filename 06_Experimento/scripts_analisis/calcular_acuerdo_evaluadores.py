#!/usr/bin/env python3

import csv
import platform
from itertools import combinations
from pathlib import Path
import importlib.metadata as md

import numpy as np
import krippendorff
from sklearn.metrics import cohen_kappa_score


ENTRADA = Path(
    "06_Experimento/evaluadores/puntuaciones_reales.csv"
)

SALIDA_ALPHA = Path(
    "07_Datos/resultados/acuerdo_krippendorff.csv"
)

SALIDA_KAPPA = Path(
    "07_Datos/resultados/acuerdo_kappa_ponderado.csv"
)

SALIDA_META = Path(
    "07_Datos/resultados/metadatos_acuerdo.txt"
)

DIMENSIONES = ["COM", "AMB", "VER", "COR", "CON"]
EVALUADORES_ESPERADOS = ["EV-01", "EV-02", "EV-03"]


def main():
    if not ENTRADA.exists():
        raise SystemExit(f"ERROR: no existe {ENTRADA}")

    datos = {
        d: {}
        for d in DIMENSIONES
    }

    total = 0

    with ENTRADA.open(
        encoding="utf-8-sig",
        newline=""
    ) as f:

        reader = csv.DictReader(f)

        for fila in reader:
            evaluador = fila["evaluador"].strip()
            requisito = fila["requisito"].strip()
            dimension = fila["dimension"].strip()

            try:
                puntuacion = int(fila["puntuacion"])
            except ValueError:
                raise SystemExit(
                    f"ERROR: puntuación inválida en {requisito}"
                )

            if dimension not in DIMENSIONES:
                raise SystemExit(
                    f"ERROR: dimensión desconocida: {dimension}"
                )

            if puntuacion not in range(1, 6):
                raise SystemExit(
                    f"ERROR: puntuación fuera de rango: {puntuacion}"
                )

            datos[dimension].setdefault(
                requisito, {}
            )

            if evaluador in datos[dimension][requisito]:
                raise SystemExit(
                    "ERROR: puntuación duplicada para "
                    f"{evaluador}, {requisito}, {dimension}"
                )

            datos[dimension][requisito][evaluador] = puntuacion
            total += 1

    if total != 750:
        raise SystemExit(
            f"ERROR: se esperaban 750 puntuaciones y hay {total}"
        )

    SALIDA_ALPHA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    resultados_alpha = []
    resultados_kappa = []

    for dimension in DIMENSIONES:
        requisitos = sorted(datos[dimension])

        if len(requisitos) != 50:
            raise SystemExit(
                f"ERROR: {dimension} tiene "
                f"{len(requisitos)} requisitos"
            )

        for requisito in requisitos:
            evaluadores = sorted(
                datos[dimension][requisito]
            )

            if evaluadores != EVALUADORES_ESPERADOS:
                raise SystemExit(
                    f"ERROR: evaluadores incompletos en "
                    f"{dimension}/{requisito}: {evaluadores}"
                )

        # Matriz: evaluadores x requisitos
        matriz = np.array(
            [
                [
                    datos[dimension][req][ev]
                    for req in requisitos
                ]
                for ev in EVALUADORES_ESPERADOS
            ],
            dtype=float,
        )

        alpha = krippendorff.alpha(
            reliability_data=matriz,
            level_of_measurement="ordinal",
        )

        resultados_alpha.append({
            "dimension": dimension,
            "alpha_krippendorff_ordinal": f"{alpha:.6f}",
            "n_requisitos": len(requisitos),
            "n_evaluadores": len(EVALUADORES_ESPERADOS),
        })

        for ev_a, ev_b in combinations(
            EVALUADORES_ESPERADOS, 2
        ):
            punt_a = [
                datos[dimension][req][ev_a]
                for req in requisitos
            ]

            punt_b = [
                datos[dimension][req][ev_b]
                for req in requisitos
            ]

            kappa = cohen_kappa_score(
                punt_a,
                punt_b,
                labels=[1, 2, 3, 4, 5],
                weights="quadratic",
            )

            resultados_kappa.append({
                "dimension": dimension,
                "evaluador_a": ev_a,
                "evaluador_b": ev_b,
                "kappa_ponderado_cuadratico": f"{kappa:.6f}",
                "n_requisitos": len(requisitos),
            })

    with SALIDA_ALPHA.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as f:

        campos = [
            "dimension",
            "alpha_krippendorff_ordinal",
            "n_requisitos",
            "n_evaluadores",
        ]

        writer = csv.DictWriter(
            f,
            fieldnames=campos
        )

        writer.writeheader()
        writer.writerows(resultados_alpha)

    with SALIDA_KAPPA.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as f:

        campos = [
            "dimension",
            "evaluador_a",
            "evaluador_b",
            "kappa_ponderado_cuadratico",
            "n_requisitos",
        ]

        writer = csv.DictWriter(
            f,
            fieldnames=campos
        )

        writer.writeheader()
        writer.writerows(resultados_kappa)

    with SALIDA_META.open(
        "w",
        encoding="utf-8"
    ) as f:

        f.write("Análisis de acuerdo entre evaluadores\n")
        f.write("------------------------------------\n")
        f.write(f"Python: {platform.python_version()}\n")
        f.write(f"numpy: {md.version('numpy')}\n")
        f.write(
            f"krippendorff: "
            f"{md.version('krippendorff')}\n"
        )
        f.write(
            f"scikit-learn: "
            f"{md.version('scikit-learn')}\n"
        )
        f.write(
            "Medida principal: alpha de "
            "Krippendorff ordinal\n"
        )
        f.write(
            "Medida secundaria: kappa de Cohen "
            "ponderado cuadratico por pares\n"
        )
        f.write("Escala: 1-5 ordinal\n")
        f.write("Evaluadores: EV-01, EV-02, EV-03\n")
        f.write("Requisitos por dimension: 50\n")

    print("Acuerdo entre evaluadores")
    print("-------------------------")

    for r in resultados_alpha:
        print(
            f"{r['dimension']}: "
            f"alpha = "
            f"{r['alpha_krippendorff_ordinal']}"
        )

    print()
    print(f"OK: {SALIDA_ALPHA}")
    print(f"OK: {SALIDA_KAPPA}")
    print(f"OK: {SALIDA_META}")


if __name__ == "__main__":
    main()
