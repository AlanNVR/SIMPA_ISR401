# Cómo llenar `EV-X_hoja_puntuacion.csv`

Una copia de `PLANTILLA_hoja_puntuacion.csv` por evaluador, renombrada
`EV-1_hoja_puntuacion.csv`, `EV-2_hoja_puntuacion.csv`,
`EV-3_hoja_puntuacion.csv`.

## Columnas

| Columna | Qué va ahí |
|---|---|
| `id_requisito` | Ya viene puesto (`R-001` a `R-050`, igual que `requisitos_cegados.csv`). No editar. |
| `COM` | Completitud — 1 a 5 |
| `AMB` | Ausencia de ambigüedad — 1 a 5 |
| `VER` | Verificabilidad — 1 a 5 |
| `COR` | Corrección respecto de la fuente — 1 a 5 |
| `CON` | Consistencia interna — 1 a 5 |
| `observaciones` | Texto libre. Obligatorio si el requisito le pareció ambiguo o incompleto; opcional en el resto. |

## Escala (igual que `rubrica_evaluacion.pdf`)

1 ausente · 2 marginal · 3 deficiencias apreciables · 4 deficiencias
menores · 5 plenamente presente.

## Reglas

- Las 50 filas deben quedar puntuadas en las cinco dimensiones. Ninguna
  celda de puntuación en blanco al entregar.
- Si duda entre dos niveles, elija el menor (mismo criterio que indica la
  hoja de puntuación en PDF).
- No reordene las filas ni cambie los códigos `R-XXX`.
- No agregue columnas nuevas.
- Guarde el archivo con codificación UTF-8 y `;` como separador, para que
  sea compatible con el resto de los CSV del proyecto.

## Metadato del evaluador

La fecha, hora de inicio y hora de fin de cada evaluador no van dentro de
este archivo — ya están en
`06_Experimento/evaluadores/registro_evaluadores.csv`. Este CSV es
únicamente la puntuación de los 50 requisitos.
