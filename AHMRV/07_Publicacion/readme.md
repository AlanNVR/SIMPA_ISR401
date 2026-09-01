# Publicación

Material orientado a la publicación de los resultados del proyecto.

| Archivo / carpeta | Contenido |
|---|---|
| `analisis_revistas.md` | Candidatas a revista/editorial, título y palabras clave preliminares |
| `dataset_zenodo/` | Instantánea exacta del depósito publicado en Zenodo — DOI de versión `10.5281/zenodo.22236500` |
| `fair_assessment.pdf` | Evidencia visual de la evaluación FAIR realizada con F-UJI |
| `fair_assessment.json` | Resultado estructurado y reproducible de la evaluación F-UJI |
| `manuscrito_final.tex` | Fuente LaTeX autónoma del Research Preview prerregistrado, sin resultados experimentales |
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

El manuscrito científico se conserva como un **Research Preview prerregistrado**: describe el protocolo, el contexto, las preguntas de investigación y el plan de análisis, pero **no incorpora resultados experimentales**, ya que el experimento permanece pendiente de ejecución. La fuente `manuscrito_final.tex` es autónoma y compila junto con `referencias.bib`; la versión interna no anónima actual genera un PDF de 9 páginas y contiene 23 referencias bibliográficas citadas.

Los tres archivos del manuscrito (`manuscrito_final.tex`, `manuscrito_final.pdf` y `referencias.bib`) están expresamente excluidos del alcance de la licencia CC BY 4.0 general del material de publicación; véase la sección 4 del `LICENSE` en la raíz del repositorio.
