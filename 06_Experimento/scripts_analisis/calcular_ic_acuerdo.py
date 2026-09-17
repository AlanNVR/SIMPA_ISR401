#!/usr/bin/env python3
"""
Calcula intervalos de confianza (bootstrap, 95%, percentil) para el alpha de
Krippendorff ordinal y el kappa ponderado cuadratico, por remuestreo sobre
los requisitos (unidades) dentro de cada dimension.

Metodo: bootstrap no parametrico sobre unidades, 2000 iteraciones, semilla
fija para reproducibilidad. Es el metodo estandar cuando no hay forma
cerrada de varianza (caso de Krippendorff alpha ordinal).
"""
import csv
from itertools import combinations
from pathlib import Path

import numpy as np
import krippendorff
from sklearn.metrics import cohen_kappa_score

ENTRADA = Path("06_Experimento/evaluadores/puntuaciones_reales.csv")
SALIDA_ALPHA = Path("07_Datos/resultados/acuerdo_krippendorff.csv")
SALIDA_KAPPA = Path("07_Datos/resultados/acuerdo_kappa_ponderado.csv")
SALIDA_KAPPA_PROM = Path("07_Datos/resultados/acuerdo_kappa_ponderado_promedio.csv")

DIMENSIONES = ["COM", "AMB", "VER", "COR", "CON"]
EVALUADORES_ESPERADOS = ["EV-01", "EV-02", "EV-03"]
B = 2000
SEED = 20260916


def cargar_datos():
    datos = {d: {} for d in DIMENSIONES}
    with ENTRADA.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            ev = fila["evaluador"].strip()
            req = fila["requisito"].strip()
            dim = fila["dimension"].strip()
            punt = int(fila["puntuacion"])
            datos[dim].setdefault(req, {})[ev] = punt
    return datos


def main():
    datos = cargar_datos()
    rng = np.random.default_rng(SEED)

    filas_alpha = []
    filas_kappa = []
    filas_kappa_prom = []

    for dimension in DIMENSIONES:
        requisitos = sorted(datos[dimension])
        n = len(requisitos)

        matriz = np.array(
            [[datos[dimension][r][ev] for r in requisitos] for ev in EVALUADORES_ESPERADOS],
            dtype=float,
        )

        alpha_puntual = krippendorff.alpha(reliability_data=matriz, level_of_measurement="ordinal")

        boot_alpha = np.empty(B)
        boot_kappa_pares = {p: np.empty(B) for p in combinations(EVALUADORES_ESPERADOS, 2)}
        boot_kappa_prom = np.empty(B)

        for b in range(B):
            idx = rng.integers(0, n, size=n)
            sub = matriz[:, idx]
            boot_alpha[b] = krippendorff.alpha(reliability_data=sub, level_of_measurement="ordinal")

            kappas_b = []
            for i, (ev_a, ev_b) in enumerate(combinations(EVALUADORES_ESPERADOS, 2)):
                pa = matriz[EVALUADORES_ESPERADOS.index(ev_a), idx]
                pb = matriz[EVALUADORES_ESPERADOS.index(ev_b), idx]
                k = cohen_kappa_score(pa, pb, labels=[1, 2, 3, 4, 5], weights="quadratic")
                boot_kappa_pares[(ev_a, ev_b)][b] = k
                kappas_b.append(k)
            boot_kappa_prom[b] = float(np.mean(kappas_b))

        ic_a_lo, ic_a_hi = np.nanpercentile(boot_alpha, [2.5, 97.5])
        filas_alpha.append({
            "dimension": dimension,
            "alpha_krippendorff_ordinal": f"{alpha_puntual:.6f}",
            "ic95_inferior": f"{ic_a_lo:.6f}",
            "ic95_superior": f"{ic_a_hi:.6f}",
            "n_requisitos": n,
            "n_evaluadores": len(EVALUADORES_ESPERADOS),
            "metodo_ic": f"bootstrap percentil, B={B}, semilla={SEED}",
        })

        for (ev_a, ev_b), arr in boot_kappa_pares.items():
            pa = [datos[dimension][r][ev_a] for r in requisitos]
            pb = [datos[dimension][r][ev_b] for r in requisitos]
            kappa_puntual = cohen_kappa_score(pa, pb, labels=[1, 2, 3, 4, 5], weights="quadratic")
            lo, hi = np.nanpercentile(arr, [2.5, 97.5])
            filas_kappa.append({
                "dimension": dimension,
                "evaluador_a": ev_a,
                "evaluador_b": ev_b,
                "kappa_ponderado_cuadratico": f"{kappa_puntual:.6f}",
                "ic95_inferior": f"{lo:.6f}",
                "ic95_superior": f"{hi:.6f}",
                "n_requisitos": n,
            })

        prom_puntual = float(np.mean([
            cohen_kappa_score(
                [datos[dimension][r][a] for r in requisitos],
                [datos[dimension][r][b] for r in requisitos],
                labels=[1, 2, 3, 4, 5], weights="quadratic",
            )
            for a, b in combinations(EVALUADORES_ESPERADOS, 2)
        ]))
        lo_p, hi_p = np.nanpercentile(boot_kappa_prom, [2.5, 97.5])
        filas_kappa_prom.append({
            "dimension": dimension,
            "kappa_ponderado_promedio": f"{prom_puntual:.6f}",
            "ic95_inferior": f"{lo_p:.6f}",
            "ic95_superior": f"{hi_p:.6f}",
            "metodo_ic": f"bootstrap percentil sobre el promedio de 3 pares, B={B}, semilla={SEED}",
        })

    with SALIDA_ALPHA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas_alpha[0].keys()))
        w.writeheader(); w.writerows(filas_alpha)

    with SALIDA_KAPPA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas_kappa[0].keys()))
        w.writeheader(); w.writerows(filas_kappa)

    with SALIDA_KAPPA_PROM.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas_kappa_prom[0].keys()))
        w.writeheader(); w.writerows(filas_kappa_prom)

    print("=== alpha de Krippendorff (con IC95%) ===")
    for r in filas_alpha:
        print(f"{r['dimension']}: {r['alpha_krippendorff_ordinal']} "
              f"[{r['ic95_inferior']}, {r['ic95_superior']}]")
    print()
    print("=== kappa ponderado promedio por dimension (con IC95%) ===")
    for r in filas_kappa_prom:
        print(f"{r['dimension']}: {r['kappa_ponderado_promedio']} "
              f"[{r['ic95_inferior']}, {r['ic95_superior']}]")


if __name__ == "__main__":
    main()