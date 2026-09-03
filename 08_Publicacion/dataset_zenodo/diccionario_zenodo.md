# Diccionario de datos — `respuestas_zenodo_agregadas.csv`

Proyecto SIMPA · ISR-401 · UTEQ

## Identificación

- Filas agregadas: 64
- Preguntas representadas: 15
- Columnas: 7
- Participantes de origen: 62
- Codificación: UTF-8 con BOM
- Separador: coma
- Unidad de análisis: una opción de respuesta dentro de una distribución marginal por pregunta
- Fuente inmediata: `../respuestas_anonimizadas.csv`

Ninguna fila del archivo agregado corresponde a una persona.

## Columnas

| Columna | Descripción |
|---|---|
| `pregunta_id` | Identificador local P01–P15 de la pregunta sustantiva |
| `pregunta` | Texto de la pregunta |
| `tipo_respuesta` | `simple` o `multiple` |
| `opcion` | Categoría u opción observada |
| `frecuencia` | Número de respuestas que contienen la opción |
| `n_validos` | Número de participantes con respuesta válida en la pregunta |
| `porcentaje` | `frecuencia / n_validos × 100`, redondeado a una cifra decimal |

## Interpretación

Para las preguntas de respuesta simple, la suma de frecuencias por pregunta es igual a `n_validos` y los porcentajes suman aproximadamente 100 %, con diferencias posibles por redondeo.

La pregunta P04, `¿Cuál es la mayor dificultad en su trabajo diario?`, es multirrespuesta. En el archivo fuente sus opciones están separadas por `;`. Una persona puede seleccionar más de una opción; por ello, la suma de frecuencias puede superar `n_validos` y los porcentajes pueden sumar más de 100 %.

No deben interpretarse las filas de distintas preguntas como registros vinculables entre sí.

## Exclusiones deliberadas

La versión abierta no contiene:

- `ID`;
- `Nombre`;
- `Correo electrónico`;
- `Hora de inicio`;
- `Hora de finalización`;
- `Comentarios del cuestionario`;
- columnas `Comentarios: ...`;
- filas individuales;
- cruces entre preguntas o perfiles de participantes.

Esta estructura responde al criterio de publicar estadística descriptiva sin divulgar respuestas individuales identificables o vinculables.

## Reproducibilidad

El resumen se genera mediante:

    python preparar_dataset_zenodo_agregado.py

El script exige 62 registros de origen y 15 preguntas sustantivas antes de generar el archivo.
