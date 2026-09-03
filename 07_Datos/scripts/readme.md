# Scripts de datos y análisis

Esta carpeta contiene las copias canónicas de los scripts reproducibles
utilizados por `07_Datos/`.

## Ejecución principal

Desde la raíz del repositorio:

`python 07_Datos/scripts/run_all.py`

El orquestador ejecuta:

1. `anonimizar_encuesta.py`
2. `preparar_dataset_zenodo_agregado.py`
3. `curva_saturacion.py`

La ejecución reproduce y verifica los datasets procesados y los resultados de
saturación disponibles actualmente.

## Scripts

- `run_all.py`: punto de entrada único de la cadena reproducible.
- `anonimizar_encuesta.py`: genera `respuestas_anonimizadas.csv`.
- `preparar_dataset_zenodo_agregado.py`: genera el dataset agregado de Zenodo.
- `curva_saturacion.py`: genera la tabla y figuras de saturación.
- `generar_fichas.py`: utilidad para fichas técnicas de archivos audiovisuales.

`generar_fichas.py` no forma parte de la ejecución automática de `run_all.py`,
porque requiere como entrada una carpeta de material audiovisual y pertenece al
flujo de documentación de evidencias.

## Estado

La cadena disponible fue ejecutada y verificada localmente el 2026-09-03.

El experimento comparativo humano–LLM permanece pendiente y `run_all.py` no
genera resultados simulados para ese componente.
