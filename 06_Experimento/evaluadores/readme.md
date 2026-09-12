# Evaluadores independientes — EXP-06

Reclutamiento, consentimiento y puntuación de los tres evaluadores
independientes exigidos por el protocolo (RQ2, `06_Experimento/protocolo.tex`).
**Estado: completo.**

## Contenido

| Archivo | Qué es |
|---|---|
| `registro_evaluadores.csv` | Seguimiento de los tres evaluadores: perfil, independencia, consentimiento, fechas |
| `EV-01_hoja_puntuacion.csv` | Puntuación de los 50 requisitos cegados por el evaluador EV-01 |
| `EV-02_hoja_puntuacion.csv` | Puntuación de los 50 requisitos cegados por el evaluador EV-02 |
| `EV-03_hoja_puntuacion.csv` | Puntuación de los 50 requisitos cegados por el evaluador EV-03 |

## Criterio de independencia

Un evaluador se considera independiente cuando:

- no es integrante del equipo AHMRV;
- no participó en la elicitación de ningún requisito del conjunto humano
  (`06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv`);
- no tuvo acceso a la salida del LLM antes de esta evaluación.

El protocolo ya declara, como amenaza a la validez externa asumida de
antemano, que es esperable que los evaluadores sean estudiantes y no
profesionales en ejercicio. Eso no descalifica a un evaluador; lo que sí lo
descalifica es no cumplir los tres puntos anteriores.

## Los tres evaluadores

| Código | Perfil | Consentimiento | Evaluación completa |
|---|---|---|---|
| EV-01 | Ingeniero de Software con experiencia en R.R. | 2026-09-11 | Sí — 50/50 |
| EV-02 | Estudiante de 5to nivel de Software | 2026-09-11 | Sí — 50/50 |
| EV-03 | Profesional en TI, especialista en QA | 2026-09-11 | Sí — 50/50 |

Detalle completo en `registro_evaluadores.csv`.

## Estructura de las hojas de puntuación

Cada `EV-XX_hoja_puntuacion.csv` tiene 50 filas (`R-001` a `R-050`, mismo
identificador que `06_Experimento/cegado/requisitos_cegados.csv`) con estas
columnas:

| Columna | Contenido |
|---|---|
| `id_requisito` | `R-001`–`R-050` |
| `COM` | Completitud, escala 1–5 |
| `AMB` | Ausencia de ambigüedad, escala 1–5 |
| `VER` | Verificabilidad, escala 1–5 |
| `COR` | Corrección respecto de la fuente, escala 1–5 |
| `CON` | Consistencia interna, escala 1–5 |
| `observaciones` | Texto libre |

Escala (igual que `../instrumentos/rubrica_evaluacion.pdf`): 1 ausente · 2
marginal · 3 deficiencias apreciables · 4 deficiencias menores · 5
plenamente presente.

Las tres hojas fueron verificadas antes de incorporarse: 50 filas cada una,
sin celdas de puntuación vacías, todos los valores dentro del rango 1–5.

## Cegado

Ningún archivo de esta carpeta indica si un `R-XXX` proviene del conjunto
humano o del LLM. Esa correspondencia está en `mapa_origen.csv`, generado
por EXP-05 y custodiado fuera del repositorio (responsable: Edson Rizzo),
precisamente para que la evaluación se hiciera a ciegas.

## Siguiente paso

Con las tres hojas completas, corresponde:

1. Desvelar el cegado con `mapa_origen.csv` para poder analizar por origen.
2. Calcular el acuerdo entre evaluadoras (RQ2): $\alpha$ de Krippendorff
   ordinal (principal) y $\kappa$ ponderado cuadrático por pares
   (secundario), conforme a `../osf_deviations.md`.
3. Ejecutar el modelo mixto ordinal (RQ1) sobre las puntuaciones.

Esto todavía no se ha hecho.
