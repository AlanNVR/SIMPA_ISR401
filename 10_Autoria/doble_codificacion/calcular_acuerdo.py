#!/usr/bin/env python3
"""
AUT-07 — Paso final: calcular el coeficiente de acuerdo entre codificadores.

Compara codificacion_allan.csv y codificacion_josthyn.csv sobre el mismo
subconjunto congelado (subconjunto_fragmentos.csv) y calcula:

  - Porcentaje de acuerdo observado (Po) sobre el campo Codigo
  - Kappa de Cohen (corrige por acuerdo esperado al azar)
  - Intervalo de confianza 95% del Kappa, por bootstrap (2000 remuestreos)

Requiere: pip install scikit-learn numpy --break-system-packages
Ejecutar desde 10_Autoria/doble_codificacion/, o ajustar las rutas.
"""
import csv
import sys
from pathlib import Path
import numpy as np
from sklearn.metrics import cohen_kappa_score

CARPETA = Path(".")

def cargar(nombre):
    ruta = CARPETA / nombre
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f, delimiter=";")
        filas = list(lector)
    return {fila["ID_fragmento"]: fila for fila in filas}

def main():
    allan = cargar("codificacion_allan.csv")
    josthyn = cargar("codificacion_josthyn.csv")

    if set(allan.keys()) != set(josthyn.keys()):
        sys.exit("ERROR: los IDs de fragmento no coinciden entre ambas hojas. "
                 "¿Se usó el mismo subconjunto_fragmentos.csv como base?")

    ids = sorted(allan.keys())
    vacios_allan = [i for i in ids if not allan[i]["Codigo"].strip()]
    vacios_josthyn = [i for i in ids if not josthyn[i]["Codigo"].strip()]
    if vacios_allan or vacios_josthyn:
        print(f"AVISO: {len(vacios_allan)} fragmentos sin codificar por Allan, "
              f"{len(vacios_josthyn)} sin codificar por Josthyn.")
        print("El cálculo solo puede correr cuando AMBAS hojas estén completas.")
        sys.exit(1)

    codigos_allan = [allan[i]["Codigo"].strip().upper() for i in ids]
    codigos_josthyn = [josthyn[i]["Codigo"].strip().upper() for i in ids]

    n = len(ids)
    coincidencias = sum(1 for a, j in zip(codigos_allan, codigos_josthyn) if a == j)
    po = coincidencias / n

    kappa = cohen_kappa_score(codigos_allan, codigos_josthyn)

    # Bootstrap 95% CI para kappa
    rng = np.random.default_rng(seed=42)
    boot_kappas = []
    idx = np.arange(n)
    for _ in range(2000):
        muestra = rng.choice(idx, size=n, replace=True)
        a_b = [codigos_allan[k] for k in muestra]
        j_b = [codigos_josthyn[k] for k in muestra]
        try:
            boot_kappas.append(cohen_kappa_score(a_b, j_b))
        except Exception:
            continue
    ic_inf, ic_sup = np.percentile(boot_kappas, [2.5, 97.5])

    print("=" * 60)
    print("AUT-07 — Resultado del acuerdo entre codificadores")
    print("=" * 60)
    print(f"Fragmentos comparados: {n}")
    print(f"Porcentaje de acuerdo observado (Po): {po:.3f} ({po*100:.1f}%)")
    print(f"Kappa de Cohen: {kappa:.3f}")
    print(f"IC 95% (bootstrap, 2000 remuestreos): [{ic_inf:.3f}, {ic_sup:.3f}]")
    print()
    if kappa < 0.20:
        interpretacion = "acuerdo insignificante"
    elif kappa < 0.40:
        interpretacion = "acuerdo aceptable/débil"
    elif kappa < 0.60:
        interpretacion = "acuerdo moderado"
    elif kappa < 0.80:
        interpretacion = "acuerdo sustancial"
    else:
        interpretacion = "acuerdo casi perfecto"
    print(f"Interpretación (escala Landis & Koch, 1977): {interpretacion}")

    with open(CARPETA / "resultado_acuerdo.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["Metrica", "Valor"])
        w.writerow(["Fragmentos_comparados", n])
        w.writerow(["Porcentaje_acuerdo_observado", f"{po:.4f}"])
        w.writerow(["Kappa_Cohen", f"{kappa:.4f}"])
        w.writerow(["IC95_inferior", f"{ic_inf:.4f}"])
        w.writerow(["IC95_superior", f"{ic_sup:.4f}"])
        w.writerow(["Interpretacion", interpretacion])
    print(f"\nGuardado: resultado_acuerdo.csv")

if __name__ == "__main__":
    main()
