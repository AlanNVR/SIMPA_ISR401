# Publicación

Material orientado a la publicación de los resultados del proyecto.

| Archivo / carpeta | Contenido |
|---|---|
| `analisis_revistas.md` | Candidatas a revista/editorial, título y palabras clave preliminares |
| `dataset_zenodo/` | Instantánea exacta del depósito publicado en Zenodo — DOI de versión `10.5281/zenodo.22236500` |
| — | Los datos procesados vivos **no residen aquí**: ver `../07_Datos/datos_procesados/` |
| `fair_assessment.pdf` | Evidencia visual de la evaluación FAIR realizada con F-UJI |
| `fair_assessment.json` | Resultado estructurado y reproducible de la evaluación F-UJI |
| `manuscrito_final.tex` | Fuente LaTeX autónoma del manuscrito empírico con resultados y discusión del experimento humano–LLM |
| `manuscrito_final.pdf` | Versión interna no anónima compilada del manuscrito |
| `referencias.bib` | Bibliografía específica del manuscrito, con 23 entradas citadas |

## Evaluación FAIR con F-UJI

El DOI de versión `10.5281/zenodo.22236500` fue evaluado con F-UJI 4.0.0, métrica 0.8 y soporte DataCite habilitado. El resultado global fue **24/26 puntos (92.31 %), nivel advanced**.

| Dimensión | Puntuación | Porcentaje |
|---|---:|---:|
| Findable | 7/7 | 100 % |
| Accessible | 6/7 | 85.71 % |
| Interoperable | 6/6 | 100 % |
| Reusable | 5/6 | 83.33 % |

La evaluación comprendió 17 métricas. Los resultados completos se conservan en `fair_assessment.json` y la evidencia visual en `fair_assessment.pdf`.

La carpeta `dataset_zenodo/` se conserva sin modificaciones como instantánea exacta de los seis archivos depositados en la versión 2.0. Por trazabilidad, sus archivos `readme.md` y `zenodo_metadata.md` mantienen el estado de predepósito que tenían al momento de la carga. Esto preserva la correspondencia con `checksums_zenodo.sha256` y con los archivos publicados en Zenodo.

El manuscrito científico incorpora la ejecución real del experimento comparativo humano–LLM, sus resultados, discusión, amenazas a la validez, limitaciones y conclusiones. El registro OSF se presenta de forma transparente como retrospectivo respecto al material fuente de entrevistas y anterior a la ejecución del experimento.

La fuente `manuscrito_final.tex` es autónoma y compila junto con `referencias.bib`. La versión interna no anónima actual genera un PDF de 11 páginas y conserva 23 referencias bibliográficas citadas.

Los tres archivos del manuscrito (`manuscrito_final.tex`, `manuscrito_final.pdf` y `referencias.bib`) están expresamente excluidos del alcance de la licencia CC BY 4.0 general del material de publicación; véase la sección 4 del `LICENSE` en la raíz del repositorio.

## Ubicación de los datos

Esta carpeta contiene material orientado a la publicación, no la copia operativa
de los datos. Los conjuntos vivos y regenerables residen en `../07_Datos/`:

| Qué | Dónde |
|---|---|
| Datos crudos | `../07_Datos/datos_crudos/` |
| Datos procesados | `../07_Datos/datos_procesados/` |
| Scripts y orquestador `run_all.py` | `../07_Datos/scripts/` |
| Diccionario de datos vigente | `../07_Datos/diccionario_datos.csv` |
| Manifiesto de integridad | `../07_Datos/checksums_datos.sha256` |

La única excepción es `dataset_zenodo/`, que es la instantánea congelada de lo
depositado bajo el DOI `10.5281/zenodo.22236500` y se conserva sin modificar,
incluidas sus rutas internas históricas.

### Correspondencia de rutas y estado del snapshot Zenodo

Los archivos de `dataset_zenodo/` conservan el estado de predepósito que tenían al
momento de la carga. **No se corrigen**, porque `checksums_zenodo.sha256` incluye el
hash de `readme.md` y cualquier edición invalidaría la correspondencia con el
material depositado. Esta sección traduce ese estado al del repositorio actual.

**Estado de publicación.** El `readme.md` del snapshot declara el DOI como reservado
y la publicación como pendiente. Esa declaración era correcta al momento de la carga
y hoy está superada: el depósito se publicó el **2026-09-01** como **versión 2.0**,
en acceso abierto, bajo el DOI de versión `10.5281/zenodo.22236500`
(concept DOI `10.5281/zenodo.22236499`), verificable en
<https://zenodo.org/records/22236500>.

**Rutas.** Los archivos del snapshot citan rutas con el prefijo `AHMRV/` y la
numeración `07_Publicacion`, eliminadas en la reestructuración del 2026-09-03. La
equivalencia con el árbol actual es la siguiente:

| Ruta citada en el snapshot | Ruta vigente |
|---|---|
| `AHMRV/07_Publicacion/` | `08_Publicacion/` |
| `AHMRV/07_Publicacion/dataset_zenodo/` | `08_Publicacion/dataset_zenodo/` |
| `../respuestas_anonimizadas.csv` | `07_Datos/datos_procesados/respuestas_anonimizadas.csv` |
| `../scripts/anonimizar_encuesta.py` | `07_Datos/scripts/anonimizar_encuesta.py` |

**Script duplicado.** `preparar_dataset_zenodo_agregado.py` existe en dos versiones
con hash distinto: la congelada en `dataset_zenodo/` (`edb58364…`) y la viva en
`07_Datos/scripts/` (`72995db5…`). La divergencia es deliberada: la primera
documenta cómo se generó el depósito, la segunda es la que ejecuta `run_all.py`.

Se retiraron de esta carpeta tres archivos que duplicaban o contradecían a
`07_Datos/`: `respuestas_anonimizadas.csv`, `diccionario_datos.md` y
`checksums_paquete.sha256`. El motivo se registra en
`../07_Datos/desviaciones.md`.
