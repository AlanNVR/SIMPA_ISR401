#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curva de saturación temática — Proyecto SIMPA
Equipo AHMRV · ISR-401 · UTEQ

Lee codificacion.csv y produce:
  - curva_saturacion.png / .pdf   figura para el ERS
  - tabla_saturacion.csv          tabla de aportación por entrevista

Uso:
    python3 curva_saturacion.py [codificacion.csv]

Requiere: matplotlib
"""

import csv
import sys
from collections import OrderedDict

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit("Falta matplotlib.  Instalar con:  pip install matplotlib")

ENTRADA = sys.argv[1] if len(sys.argv) > 1 else "codificacion.csv"

# Orden cronológico de las entrevistas. La curva de saturación depende del
# orden de recolección, no del alfabético: alterarlo invalida la lectura.
ORDEN = ["EV-01", "EV-02", "EV-03", "EV-04", "EV-05", "EV-06", "EV-07", "EV-08"]

ETIQUETA = {
    "EV-01": "Administrador\ngeneral",
    "EV-02": "Asesor\ntécnico",
    "EV-03": "Jefe de\npolinización",
    "EV-04": "Extractora\n(supervisor)",
    "EV-05": "Trabajador\nagrícola I",
    "EV-06": "Trabajador\nagrícola II",
    "EV-07": "Asistente de\nadministración",
    "EV-08": "Extractora\n(técnico)",
}

# ---------------------------------------------------------------- lectura
por_entrevista = OrderedDict((e, []) for e in ORDEN)
with open(ENTRADA, encoding="utf-8") as f:
    for fila in csv.DictReader(f, delimiter=";"):
        ev = fila["ID_evidencia"].strip()
        if ev in por_entrevista:
            por_entrevista[ev].append(fila["Codigo"].strip())

# ------------------------------------------------------------ acumulación
vistos = set()
nuevos, acumulado, totales = [], [], []
for ev in ORDEN:
    codigos = por_entrevista[ev]
    # Un codigo repetido dentro de la MISMA entrevista aporta una sola vez
    unicos_nuevos = {c for c in codigos if c not in vistos}
    vistos.update(codigos)
    nuevos.append(len(unicos_nuevos))
    acumulado.append(len(vistos))
    totales.append(len(codigos))

# ------------------------------------------------------------ tabla CSV
with open("tabla_saturacion.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["Orden", "ID_evidencia", "Perfil", "Codigos_totales",
                "Codigos_nuevos", "Acumulado", "Porcentaje_nuevos"])
    for i, ev in enumerate(ORDEN):
        pct = 100 * nuevos[i] / totales[i] if totales[i] else 0
        w.writerow([i + 1, ev, ETIQUETA[ev].replace("\n", " "),
                    totales[i], nuevos[i], acumulado[i], f"{pct:.1f}"])

# ------------------------------------------------------------ figura
VERDE = "#006633"
NARANJA = "#B8860B"

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 7.4),
                               sharex=True,
                               gridspec_kw={"height_ratios": [2, 1.15],
                                            "hspace": 0.14})

x = range(1, len(ORDEN) + 1)

# --- panel superior: códigos nuevos por entrevista
barras = ax1.bar(x, nuevos, color=VERDE, alpha=0.82, width=0.62,
                 edgecolor="white", linewidth=0.8)
# destacar el repunte
barras[3].set_color(NARANJA)
barras[3].set_alpha(0.95)

for i, v in enumerate(nuevos):
    ax1.text(i + 1, v + 0.55, str(v), ha="center", va="bottom",
             fontsize=9.5, fontweight="bold",
             color=NARANJA if i == 3 else "#333333")

ax1.set_ylabel("Códigos nuevos aportados", fontsize=10.5)
ax1.set_ylim(0, max(nuevos) * 1.28)
ax1.grid(axis="y", alpha=0.22, linestyle=":")
ax1.set_axisbelow(True)
ax1.spines[["top", "right"]].set_visible(False)

# anotación del repunte
ax1.annotate(
    "Repunte: la extractora abre\nun dominio no explorado",
    xy=(4, nuevos[3]), xytext=(5.15, nuevos[3] + 4.2),
    fontsize=9, color=NARANJA,
    arrowprops=dict(arrowstyle="->", color=NARANJA, lw=1.3,
                    connectionstyle="arc3,rad=-0.22"))

ax1.axvspan(0.5, 3.5, color="#006633", alpha=0.05)
ax1.axvspan(3.5, 8.5, color="#B8860B", alpha=0.05)
ax1.text(2.0, max(nuevos) * 1.17, "Primera ronda", ha="center",
         fontsize=9, style="italic", color="#555555")
ax1.text(6.0, max(nuevos) * 1.17, "Segunda ronda", ha="center",
         fontsize=9, style="italic", color="#555555")

ax1.set_title("Curva de saturación temática — 8 entrevistas, 68 códigos",
              fontsize=12.5, fontweight="bold", pad=13)

# --- panel inferior: acumulado
ax2.plot(x, acumulado, marker="o", color=VERDE, linewidth=2.1,
         markersize=6.5, markerfacecolor="white", markeredgewidth=1.9)
for i, v in enumerate(acumulado):
    ax2.text(i + 1, v + 2.3, str(v), ha="center", fontsize=8.6, color="#333333")

ax2.set_ylabel("Códigos acumulados", fontsize=10.5)
ax2.set_xlabel("Entrevista, en orden cronológico de recolección", fontsize=10.5)
ax2.set_xticks(list(x))
ax2.set_xticklabels([f"{ORDEN[i]}\n{ETIQUETA[ORDEN[i]]}" for i in range(len(ORDEN))],
                    fontsize=8.1)
ax2.set_ylim(0, max(acumulado) * 1.16)
ax2.grid(axis="y", alpha=0.22, linestyle=":")
ax2.set_axisbelow(True)
ax2.spines[["top", "right"]].set_visible(False)

# tight_layout omitido: incompatible con los axvspan del panel superior
plt.savefig("curva_saturacion.png", dpi=300, bbox_inches="tight",
            facecolor="white")
plt.savefig("curva_saturacion.pdf", bbox_inches="tight", facecolor="white")

# ------------------------------------------------------------ resumen
print(f"Entrada: {ENTRADA}")
print(f"Total de fragmentos codificados: {sum(totales)}")
print(f"Códigos únicos: {acumulado[-1]}\n")
print(f"{'#':>2}  {'EV':<7}{'total':>7}{'nuevos':>8}{'acum':>7}{'% nuevos':>10}")
print("-" * 44)
for i, ev in enumerate(ORDEN):
    pct = 100 * nuevos[i] / totales[i] if totales[i] else 0
    print(f"{i+1:>2}  {ev:<7}{totales[i]:>7}{nuevos[i]:>8}"
          f"{acumulado[i]:>7}{pct:>9.1f}%")

print("\nLectura de la curva")
print("-" * 44)
print("La aportación desciende de forma sostenida hasta EV-03, lo que sugería")
print("saturación al cierre de la primera ronda. El repunte de EV-04")
print(f"({nuevos[3]} códigos nuevos) demuestra que era una saturación APARENTE:")
print("correspondía al agotamiento de un dominio, no del problema completo.")
print(f"La caída de EV-08 ({nuevos[7]} códigos), pese a pertenecer al mismo")
print("dominio nuevo, indica que ese dominio sí saturó con dos fuentes.")
print("\nGenerados: curva_saturacion.png, curva_saturacion.pdf, tabla_saturacion.csv")
