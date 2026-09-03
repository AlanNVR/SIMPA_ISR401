# Datos crudos

**Estado: pendiente para el experimento — los datos crudos ya existentes residen
en su carpeta de evidencia original y no se duplican aquí.**

Esta carpeta alojará los datos en bruto del componente experimental, tal como se
obtengan, sin transformación alguna.

## Principio de conservación

El archivo crudo es evidencia primaria y **no se modifica nunca**. Toda limpieza,
recodificación o anonimización produce un archivo distinto, que se deposita en
`../datos_procesados/` junto con el script que lo genera. Un dato crudo alterado
deja de ser verificable.

## Datos crudos que ya existen en el repositorio

| Dato | Ubicación | Naturaleza |
|---|---|---|
| Exportación del cuestionario aplicado (62 respuestas) | `07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx` | Exportación directa de Google Forms, intacta |
| Codificación temática de entrevistas | `07_Datos/datos_crudos/codificacion.csv` | Codificación cualitativa utilizada por la cadena de análisis |

El archivo se conserva aquí como fuente canónica de datos crudos. Su transformación
está documentada en `07_Publicacion/diccionario_datos.md`.

## Contenido previsto

- Salidas sin procesar de las ejecuciones del modelo de lenguaje sobre las
  transcripciones.
- Registros de tiempo y de identificación de tratamiento por unidad experimental.
- Cualquier medición registrada durante la ejecución del protocolo descrito en
  `../../06_Experimento/protocolo.pdf`.

## Estado de las dependencias

El experimento aún no se ha ejecutado, de modo que estos datos todavía no
existen. No se depositan datos sintéticos, simulados ni de ejemplo en esta
carpeta: un archivo con forma de dato crudo que no procede de una medición real
es indistinguible de un dato fabricado una vez que pasa al análisis.
