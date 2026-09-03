# Datos y cadena de análisis — SIMPA

Proyecto SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
Equipo AHMRV — Universidad Técnica Estatal de Quevedo

## 1. Propósito

La carpeta `07_Datos/` concentra los datos utilizados por el proyecto, sus
transformaciones reproducibles, los scripts de análisis y los resultados
derivados.

La separación estructural del repositorio es:

- `06_Experimento/`: diseño del estudio, protocolo, registro OSF, instrumentos
  y procedimiento experimental.
- `07_Datos/`: datos crudos, datos procesados, scripts, resultados y
  documentación de reproducibilidad.
- `08_Publicacion/`: manuscrito y artefactos relacionados con publicación.

Los datos y la cadena de análisis se centralizan aquí para evitar múltiples
copias canónicas del mismo insumo.

## 2. Estructura

El primer nivel de esta carpeta está definido como:

- `datos_crudos/`
- `datos_procesados/`
- `scripts/`
- `resultados/`
- `diccionario_datos.csv`
- `README_datos.md`
- `LICENSE-DATA.txt`
- `checksums_datos.sha256`
- `desviaciones.md`
- `registro_deposito.md`

`checksums_datos.sha256` se generará cuando el contenido del paquete quede
estabilizado.

## 3. Datos crudos

### 3.1. Cuestionario

Archivo:

`datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx`

Corresponde a la exportación primaria del cuestionario aplicado a 62
participantes.

Se conserva para trazabilidad y reproducibilidad, pero está excluido del
depósito abierto. Consulte `LICENSE-DATA.txt`.

### 3.2. Codificación temática

Archivo:

`datos_crudos/codificacion.csv`

Contiene la codificación temática actualmente disponible para EV-01 a EV-08.

La ejecución vigente del análisis produce:

- 138 fragmentos codificados;
- 68 códigos únicos.

La cobertura pendiente de entrevistas posteriores se documenta en
`desviaciones.md`.

## 4. Datos procesados

### 4.1. Respuestas anonimizadas

Archivo:

`datos_procesados/respuestas_anonimizadas.csv`

Se genera desde el XLSX crudo mediante:

`07_Datos/scripts/anonimizar_encuesta.py`

El procesamiento elimina columnas identificativas y artefactos del formulario
sin imputar ni modificar las respuestas sustantivas.

### 4.2. Dataset agregado para Zenodo

Archivo:

`datos_procesados/respuestas_zenodo_agregadas.csv`

Se genera mediante:

`07_Datos/scripts/preparar_dataset_zenodo_agregado.py`

El conjunto contiene:

- 62 participantes de origen;
- 15 preguntas sustantivas;
- 64 filas agregadas;
- 7 columnas.

Ninguna fila del conjunto agregado representa a una persona individual.

El depósito se documenta en `registro_deposito.md`.

## 5. Scripts

Los scripts reproducibles se encuentran en:

`07_Datos/scripts/`

Actualmente incluyen:

- `anonimizar_encuesta.py`
- `preparar_dataset_zenodo_agregado.py`
- `curva_saturacion.py`
- `generar_fichas.py`

Estos archivos constituyen las copias canónicas de los scripts de datos y
análisis dentro del repositorio.

## 6. Resultados

Los resultados reproducibles se encuentran en:

`07_Datos/resultados/`

Actualmente están disponibles los productos del análisis de saturación:

- `tabla_saturacion.csv`
- `curva_saturacion.png`
- `curva_saturacion.pdf`

Se regeneran mediante:

`07_Datos/scripts/curva_saturacion.py`

La ejecución vigente procesa la codificación real de EV-01 a EV-08 y produce:

- 138 fragmentos codificados;
- 68 códigos únicos.

Estos resultados corresponden al análisis cualitativo de entrevistas y no al
experimento comparativo humano–LLM prerregistrado.

## 7. Experimento humano–LLM

El diseño y protocolo del experimento comparativo se encuentran en:

`06_Experimento/`

El experimento principal todavía no ha sido ejecutado completamente.

Por esta razón, no se presentan como resultados reales:

- evaluación a ciegas completa;
- comprobación de ceguera;
- kappa con intervalo de confianza;
- tamaño del efecto con IC del 95 %;
- análisis estadístico final del experimento.

No se generan cifras hipotéticas o simuladas para completar estos entregables.

El estado y las limitaciones asociadas se registran en:

`desviaciones.md`

## 8. Diccionario de datos

El archivo:

`diccionario_datos.csv`

documenta 54 columnas pertenecientes a cuatro conjuntos:

- `respuestas_anonimizadas.csv`: 34 columnas;
- `respuestas_zenodo_agregadas.csv`: 7 columnas;
- `codificacion.csv`: 6 columnas;
- `tabla_saturacion.csv`: 7 columnas.

Para cada columna se documenta:

- dataset;
- nombre de la columna;
- tipo;
- unidad;
- rango admisible;
- codificación de valores perdidos;
- procedencia;
- descripción.

## 9. Reproducibilidad

La cadena actual puede ejecutarse mediante scripts individuales versionados.

La guía de entrega exige además un único punto de entrada reproducible.

El punto de entrada previsto es:

`07_Datos/scripts/run_all.py`

**Estado actual: pendiente de implementación y verificación.**

No se declara todavía cumplimiento de ejecución mediante una sola orden.

El orquestador deberá ejecutar únicamente transformaciones y análisis
respaldados por datos reales existentes en el repositorio.

No deberá fabricar resultados para componentes experimentales que todavía no
han sido ejecutados.

## 10. Integridad

El manifiesto específico del paquete será:

`checksums_datos.sha256`

Este archivo se generará después de estabilizar el contenido definitivo de
`07_Datos/`.

No se mantiene durante cada cambio intermedio de la reestructuración para evitar
registrar hashes transitorios.

Una vez creado, deberá permitir verificar la integridad de los componentes
versionados del paquete de datos mediante SHA-256.

## 11. Licencia y privacidad

La política específica para los datos se encuentra en:

`LICENSE-DATA.txt`

En términos generales:

- los datos anonimizados y agregados destinados a reutilización abierta se
  distribuyen bajo CC BY 4.0;
- el XLSX crudo queda expresamente fuera de la publicación abierta;
- los scripts se rigen por la licencia de código declarada en el repositorio.

Las restricciones de privacidad y protección de datos prevalecen sobre una
autorización general de reutilización cuando correspondan.

## 12. Depósito

El estado vigente del depósito se documenta en:

`registro_deposito.md`

DOI de versión:

`10.5281/zenodo.22236500`

Concept DOI:

`10.5281/zenodo.22236499`

La carpeta:

`08_Publicacion/dataset_zenodo/`

se conserva como snapshot histórico congelado y no debe modificarse para adaptar
su contenido a reorganizaciones posteriores del repositorio.

## 13. Desviaciones y limitaciones

Las desviaciones, limitaciones metodológicas y pendientes conocidos se registran
en:

`desviaciones.md`

No se eliminan ni ocultan limitaciones para aparentar cumplimiento.

Una desviación solo se considera cerrada cuando existe evidencia versionada que
demuestre su resolución.
