# Verificación de resultados canónicos para publicación

Fecha de verificación: 2026-09-15
Responsable: Jhostyn Macías

## Archivos verificados en 07_Datos/resultados/

- acuerdo_kappa_ponderado.csv — última regeneración: 86edce8, 2026-09-12
- acuerdo_krippendorff.csv — última regeneración: 86edce8, 2026-09-12
- curva_saturacion_agregada/contraste/dominio (.pdf/.png) + tabla_saturacion.csv
- modelo_ordinal_mixto.csv, resumen_modelos_ordinales.txt

## Observación relevante

Los valores de acuerdo interevaluador (kappa ponderado y alpha de Krippendorff)
son cercanos a cero o negativos en la mayoría de dimensiones, indicando acuerdo
nulo o pobre. Esto no es un error de cálculo: es el resultado real del análisis
y así debe quedar reportado, sin reinterpretarlo como un acuerdo aceptable.

## Cruce contra el manuscrito

manuscrito_final.tex (605b46c, 2026-09-15 17:58) y manuscrito_final.pdf
(2da6fe4, 2026-09-15 18:14) están compilados después de la última regeneración
de resultados (12/09). El texto reporta correctamente que el acuerdo fue
"muy bajo" y "próximo a cero", consistente con las cifras reales de los CSV.
Kappa ponderado se reporta como medida secundaria, Krippendorff como principal.

## Conclusión

Los cuatro elementos que exige §16 (kappa ponderado, Krippendorff, saturación,
modelo ordinal) están presentes, son reales, y el manuscrito los reporta con
fidelidad a los datos, sin distorsión.
