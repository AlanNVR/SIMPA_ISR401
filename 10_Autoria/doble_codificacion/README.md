# AUT-07 — Doble codificación con acuerdo reproducible

**Responsable:** Josthyn Macías · **Codificador 1:** Allan Villafuerte ·
**Codificador 2:** Josthyn Macías · **Apoyo metodológico:** Denisses Huilcapi

## Subconjunto congelado

Se seleccionaron **39 fragmentos** (~17% del corpus total de 227),
estratificados entre las dos rondas de campo:

- **EV-04** (ronda dominio) — 26 fragmentos
- **ENTR-13** (ronda contraste) — 13 fragmentos

Se eligió por estratificación deliberada (una entrevista de cada ronda), no
al azar sobre fragmentos sueltos, para que cada codificador tenga contexto
completo de la entrevista al codificar, no fragmentos descontextualizados.

**El subconjunto quedó congelado el 11 de septiembre de 2026 con el script
`00_extraer_subconjunto.py`.** No debe volver a ejecutarse: generaría un
nuevo orden de `ID_fragmento` y rompería la comparabilidad.

## Archivos de este directorio

| Archivo | Qué es | Estado |
|---|---|---|
| `subconjunto_fragmentos.csv` | Los 39 fragmentos, SOLO texto + ID de evidencia, sin código | ✅ Generado |
| `codificacion_allan.csv` | Codificación de los 39 fragmentos realizada por Allan | ✅ Completa |
| `codificacion_josthyn.csv` | Codificación de los 39 fragmentos realizada por Josthyn | ✅ Completa |
| `calcular_acuerdo.py` | Calcula Kappa de Cohen + IC 95% por bootstrap | ✅ Probado y funcional |
| `resultado_acuerdo.csv` | Resultado canónico del cálculo de acuerdo | ✅ Generado |

## Procedimiento ejecutado

1. **Congelación del subconjunto.** El 11 de septiembre de 2026 se fijaron 39
   fragmentos provenientes de `EV-04` y `ENTR-13`.
2. **Primera codificación.** Allan y Josthyn realizaron la clasificación de los
   fragmentos y conservaron sus archivos de trabajo.
3. **Normalización metodológica.** La primera comparación evidenció que se
   estaban utilizando esquemas de códigos diferentes. Para que el coeficiente
   midiera la consistencia de aplicación de un mismo esquema y no la diferencia
   entre taxonomías incompatibles, el 12 de septiembre de 2026 se realizó una
   recodificación de los 39 fragmentos utilizando un catálogo compartido.
4. **Cálculo reproducible.** El script `calcular_acuerdo.py` se ejecutó sobre
   las dos codificaciones finales y generó `resultado_acuerdo.csv`.
5. **Conservación del resultado.** El resultado canónico se mantiene en el CSV
   y se resume a continuación.

La recodificación con catálogo compartido debe tenerse en cuenta al interpretar
el coeficiente: el resultado final evalúa la consistencia con que ambos
codificadores aplicaron un esquema común.

## Resultado final

Los valores canónicos se toman de `resultado_acuerdo.csv`:

- **Fragmentos comparados:** 39
- **Porcentaje de acuerdo observado (Po):** 41,03%
- **Kappa de Cohen:** 0,3972
- **IC 95%:** [0,2358, 0,5484]
- **Interpretación registrada:** acuerdo aceptable/débil

### Trazabilidad temporal

- **Congelación del subconjunto:** 2026-09-11
- **Codificación inicial:** 2026-09-11
- **Recodificación con catálogo compartido:** 2026-09-12
- **Resultado canónico vigente:** `resultado_acuerdo.csv`

### Interpretación

El valor final no corresponde al resultado preliminar obtenido cuando los dos
codificadores aplicaban esquemas de códigos distintos.

El resultado vigente procede de la recodificación de los mismos 39 fragmentos
con un catálogo compartido. Por ello, el Kappa de Cohen de 0,3972 debe
interpretarse como una medida de consistencia en la aplicación de ese esquema
común.

El acuerdo no se presenta como alto. Se conserva el valor observado y su
intervalo de confianza sin sustituirlo por estimaciones ni resultados de prueba.
