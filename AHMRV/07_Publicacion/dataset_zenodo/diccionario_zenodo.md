# Diccionario de datos — `respuestas_zenodo.csv`

Proyecto SIMPA · ISR-401 · UTEQ

## Identificación

- Registros: 62
- Columnas: 16
- Codificación: UTF-8 con BOM
- Separador: coma
- Unidad de análisis: una respuesta al cuestionario por registro
- Fuente inmediata: `../respuestas_anonimizadas.csv`

## Variables

| # | Variable | Tipo / dominio |
|---|---|---|
| 1 | `ID` | Entero secuencial 1–62. No identifica a la persona |
| 2 | Labor principal | Nominal |
| 3 | Años de experiencia | Ordinal |
| 4 | Registro actual de la labor | Nominal |
| 5 | Mayor dificultad diaria | Nominal múltiple |
| 6 | Frecuencia de plagas o enfermedades | Ordinal |
| 7 | Usa smartphone | Dicotómica |
| 8 | Comodidad con aplicaciones | Likert 1–5 |
| 9 | Señal de internet | Ordinal |
| 10 | Utilidad de diagnóstico de plaga por foto | Likert 1–5 |
| 11 | Utilidad de diagnóstico nutricional por foto | Likert 1–5 |
| 12 | Utilidad de registro de labores en teléfono | Likert 1–5 |
| 13 | Utilidad de conteo automático por GPS | Likert 1–5 |
| 14 | Utilidad de alertas | Likert 1–5 |
| 15 | Preocupación por registro GPS | Ordinal |
| 16 | Intención de uso de la aplicación | Ordinal |

## Variables deliberadamente excluidas

Para la versión destinada a depósito abierto se eliminan:

- `Hora de inicio`;
- `Hora de finalización`;
- `Comentarios del cuestionario`;
- todas las columnas cuyo encabezado comienza con `Comentarios:`.

Las dos columnas temporales tenían 62 valores únicos y se retiraron como medida adicional de minimización de riesgo.

Las columnas de comentarios estaban vacías para los 62 registros y no aportan información analítica al depósito.

## Reproducibilidad

El dataset se genera mediante:

    python preparar_dataset_zenodo.py

El script aborta si cambia inesperadamente la estructura de entrada o si una columna de comentarios adquiere contenido, obligando a una revisión manual antes de preparar una nueva versión pública.
