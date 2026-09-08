# Resultados

Esta carpeta contiene resultados generados reproduciblemente por los scripts
versionados en `../scripts/`.

## Análisis de saturación temática

La ejecución vigente utiliza dos fuentes reales de codificación:

- `../datos_crudos/codificacion.csv`: primeras ocho entrevistas, estrato de dominio;
- `../datos_procesados/codificacion_tercera_ronda.csv`: `ENTR-09` a `ENTR-16`, estrato de contraste.

Los resultados vigentes son:

- `tabla_saturacion.csv`
- `curva_saturacion_dominio.png`
- `curva_saturacion_dominio.pdf`
- `curva_saturacion_contraste.png`
- `curva_saturacion_contraste.pdf`
- `curva_saturacion_agregada.png`
- `curva_saturacion_agregada.pdf`

Estos archivos se generan mediante:

`../scripts/curva_saturacion.py`

La ejecución verificada el 2026-09-07 produce:

- 138 fragmentos en dominio;
- 89 fragmentos en contraste;
- 227 fragmentos totales;
- 68 códigos únicos en dominio;
- 31 códigos únicos en contraste;
- 20 códigos compartidos entre los dos estratos;
- 11 códigos nuevos del contraste frente al dominio;
- 79 códigos únicos en la vista agregada.

`tabla_saturacion.csv` contiene 16 filas × 11 columnas.

## Interpretación

Las curvas de dominio y contraste deben interpretarse por separado.

La curva agregada se conserva únicamente como vista descriptiva de las 16
entrevistas. No debe utilizarse como prueba de saturación homogénea entre
poblaciones distintas.

Esta separación responde a la adenda A.14 y a la medida asociada al riesgo de
mezclar poblaciones con distinta relación con el dominio.

## Resultados anteriores

Los antiguos archivos genéricos:

- `curva_saturacion.png`
- `curva_saturacion.pdf`

correspondían exclusivamente al análisis de las primeras ocho entrevistas.

Se retiran de la carpeta de resultados al incorporar las tres curvas
estratificadas, para evitar mantener dos resultados vigentes con alcances
diferentes.

## Experimento humano–LLM

Los archivos de esta carpeta corresponden al análisis cualitativo de
entrevistas.

No corresponden al experimento comparativo humano–LLM descrito en
`06_Experimento/`, cuya ejecución completa continúa pendiente.

No se incorporan resultados hipotéticos ni cifras simuladas para completar ese
experimento.
