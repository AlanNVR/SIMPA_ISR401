# Registro de reestructuración — 2026-09-03

## Propósito

Este documento deja constancia de las correcciones y tareas de reestructuración
realizadas en el repositorio SIMPA durante el 2026-09-03.

## Trabajo realizado

Durante esta jornada se trabajó, entre otros puntos, en:

- traslado de las carpetas principales desde `AHMRV/` hacia la raíz;
- renumeración de las carpetas para obtener la estructura 01–11;
- creación y consolidación de `07_Datos/`;
- centralización de datos crudos y procesados;
- centralización de scripts de transformación y análisis;
- integración del dataset agregado publicado en Zenodo;
- corrección de rutas internas después de la reestructuración;
- documentación del paquete de datos;
- creación del diccionario de datos;
- documentación de licencias, desviaciones y depósito;
- implementación de `07_Datos/scripts/run_all.py`;
- generación determinista de los resultados de saturación;
- creación y verificación de `checksums_datos.sha256`;
- comprobación de la cadena reproducible mediante una sola orden.

## Commits registrados en Git durante la jornada

- `bbc14bd` — 2026-09-03 02:01:51 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — chore: eliminar AHMRV/.gitattributes vacío
- `e11f9a2` — 2026-09-03 02:03:46 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — chore: eliminar archivo.txt de 1 byte en scripts
- `2624c0f` — 2026-09-03 02:07:16 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover 01_ERS a la raíz del repositorio
- `e7c0a23` — 2026-09-03 02:09:29 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover 02_Evidencias a la raíz del repositorio
- `fa7fbae` — 2026-09-03 02:11:10 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover 03_Modelado a la raíz del repositorio
- `b6f1389` — 2026-09-03 02:12:28 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover 04_Trazabilidad a la raíz del repositorio
- `d35118d` — 2026-09-03 02:14:18 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover 05_MVP a la raíz del repositorio
- `88b2be0` — 2026-09-03 02:15:21 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover 06_Experimento a la raíz del repositorio
- `a6720f6` — 2026-09-03 02:16:15 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: renumerar 07_Publicacion a 08_Publicacion en la raíz
- `c19c34f` — 2026-09-03 02:17:24 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: renumerar 08_Etica a 09_Etica en la raíz
- `c271a1c` — 2026-09-03 02:18:33 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: renumerar 09_Defensa a 11_Defensa en la raíz
- `0cd8643` — 2026-09-03 02:22:43 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover datos_crudos a 07_Datos
- `fefbfc3` — 2026-09-03 02:24:21 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover datos_procesados a 07_Datos
- `afb0e8a` — 2026-09-03 02:25:18 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover resultados a 07_Datos
- `510d0ed` — 2026-09-03 02:26:27 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: mover scripts_analisis a 07_Datos/scripts
- `0ec46a6` — 2026-09-03 02:30:52 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: centralizar scripts de datos en 07_Datos
- `cd11e47` — 2026-09-03 02:48:24 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: integrar dataset procesado y actualizar rutas de datos
- `4686757` — 2026-09-03 02:54:11 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: integrar dataset agregado reproducible en 07_Datos
- `1236a21` — 2026-09-03 03:43:12 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — refactor: centralizar datos crudos y análisis de saturación en 07_Datos
- `b2ccce6` — 2026-09-03 04:13:22 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — docs: completar documentación base de 07_Datos
- `4aebea3` — 2026-09-03 04:25:17 -0500 — AlanNVR <avillafuerter@uteq.edu.ec> — feat: implementar cadena reproducible de 07_Datos
