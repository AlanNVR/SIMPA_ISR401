# Registro de depósito de datos

Proyecto SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
Equipo AHMRV — Universidad Técnica Estatal de Quevedo

Fecha de actualización: 2026-09-03

---

## 1. Estado del depósito

**Estado:** publicado en Zenodo.

| Campo | Valor |
|---|---|
| Plataforma | Zenodo |
| Tipo de recurso | Dataset |
| Versión | 2.0 |
| DOI de versión | `10.5281/zenodo.22236500` |
| Concept DOI | `10.5281/zenodo.22236499` |
| Registro | `https://zenodo.org/records/22236500` |
| Licencia del dataset abierto | CC BY 4.0 |
| Institución | Universidad Técnica Estatal de Quevedo |
| Proyecto | SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana |

El cierre de la publicación quedó registrado en el historial Git mediante:

`66c4c48 Cerrar publicación del dataset en Zenodo`

---

## 2. Conjunto publicado

El depósito abierto corresponde a estadística descriptiva agregada derivada del
cuestionario aplicado a 62 participantes.

El archivo canónico reproducible dentro de la estructura actual es:

`07_Datos/datos_procesados/respuestas_zenodo_agregadas.csv`

Características:

- participantes de origen: 62;
- preguntas sustantivas: 15;
- filas agregadas: 64;
- columnas: 7;
- unidad de análisis: una opción de respuesta dentro de una distribución
  marginal por pregunta.

Ninguna fila del dataset agregado representa a una persona individual.

---

## 3. Reproducción del conjunto

El archivo agregado se genera mediante:

`07_Datos/scripts/preparar_dataset_zenodo_agregado.py`

Entrada:

`07_Datos/datos_procesados/respuestas_anonimizadas.csv`

Salida:

`07_Datos/datos_procesados/respuestas_zenodo_agregadas.csv`

Durante la reestructuración del repositorio se ejecutó nuevamente el script y
se verificó que la salida reproducida fuera idéntica bit a bit al dataset
agregado conservado en el snapshot de publicación.

SHA-256 verificado del CSV agregado:

`b40ab460fc1d3d931beebaf5dd3037f564db8774559feee1ec1d371fa01b39b9`

---

## 4. Snapshot histórico de publicación

La carpeta:

`08_Publicacion/dataset_zenodo/`

se conserva como snapshot congelado del proceso de publicación.

No debe modificarse para adaptar rutas, estados o textos a reorganizaciones
posteriores del repositorio.

Algunos documentos internos de ese snapshot fueron preparados antes del cierre
definitivo del registro y, por ello, pueden conservar expresiones como
"predepósito", "DOI reservado" o "publicación pendiente".

Esas expresiones documentan el estado que existía cuando se preparó el paquete;
no representan el estado actual del depósito.

El estado vigente se documenta en este archivo.

---

## 5. Exclusiones del depósito abierto

No forman parte del depósito público:

- el XLSX crudo del cuestionario;
- respuestas individuales identificables;
- nombres o direcciones de correo;
- consentimientos con datos personales;
- firmas;
- grabaciones de audio o video sin anonimizar;
- documentación de la zona restringida;
- cualquier tabla que permita reconstruir respuestas individuales.

El archivo crudo:

`07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx`

se conserva únicamente para trazabilidad y reproducibilidad controlada.

---

## 6. Licencia

El dataset agregado se publica bajo:

**Creative Commons Attribution 4.0 International — CC BY 4.0**

La separación entre datos abiertos, datos restringidos y código de análisis se
documenta en:

`07_Datos/LICENSE-DATA.txt`

---

## 7. Integridad

La integridad de los archivos de `07_Datos/` se documentará mediante:

`07_Datos/checksums_datos.sha256`

Ese manifiesto se generará una vez estabilizada la cadena de análisis para no
registrar hashes transitorios durante la reestructuración.
