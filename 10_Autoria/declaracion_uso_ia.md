# Declaración de uso de IA generativa — SIMPA

**Equipo:** AHMRV — ISR-401 — UTEQ
**Responsable de esta declaración:** Huilcapi León Denisses Fabiola
**Verificador:** Macías Herrera Josthyn Esteban
**Última actualización:** 2026/09/11

## Cómo leer este documento

Esta declaración cubre **las 9 áreas del proyecto**, incluidas aquellas donde
**no** se usó ninguna herramienta generativa — la ausencia de uso también se
declara explícitamente, no se omite.

---

## 1. ERS (Especificación de Requisitos)

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí** |
| Herramienta | Claude (Anthropic), vía claude.ai — del 2026-09-03 al 2026-09-08 (confirmado por `git log` sobre `01_ERS`) |
| Finalidad | Asistencia en la redacción y estructuración del documento: migración del ERS a LaTeX, redacción de requisitos funcionales y no funcionales sobre ISO/IEC 25010:2023, formulación de historias de usuario Connextra con criterios Gherkin, construcción de la matriz de trazabilidad extendida e incorporación de los RF-01 a RF-03 en la v3.1. El contenido de dominio procede de las entrevistas y evidencias de campo del equipo, no del modelo. |
| Responsable | Huilcapi León Denisses Fabiola |
| Quién verificó | Rizzo Vélez Edson Nagib |
| Método de verificación | Revisión de cada requisito contra la evidencia de campo que lo origina en la matriz de trazabilidad; compilación LaTeX sin errores; inspección Fagan de la PE4 sobre esta ERS |

## 2. Modelado (diagramas UML, i*)

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | Para la **creación**: No — los diagramas se elaboraron manualmente en draw.io. Para la **verificación**: Sí, con apoyo de Claude |
| Herramienta | draw.io (creación) + Claude, Anthropic (apoyo a la verificación) |
| Finalidad | Creación manual de los diagramas UML e i* en draw.io; verificación cruzada del contenido de los diagramas asistida por Claude |
| Responsable | Macías Herrera Josthyn Esteban / Arboleda Yanza Francisco Javier (creación) |
| Quién verificó | Rizzo Vélez Edson Nagib |
| Método de verificación | Comparación manual del contenido de cada diagrama contra el ERS, con apoyo de Claude para contrastar consistencia entre ambos |

## 3. Trazabilidad (matriz E2E, verificación ACC-14)

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí** |
| Herramienta | Claude (Anthropic) |
| Finalidad | Generación de los scripts `verificar_consistencia.py` (ACC-14) y de la auditoría de los 6 aspectos del componente IA (`auditoria_IA01.md`), a partir de datos extraídos directamente del repositorio |
| Responsable | Macías Herrera Josthyn Esteban |
| Quién verificó | Macías Herrera Josthyn Esteban — se ejecutaron los scripts contra el repositorio real y se contrastaron los resultados antes de aceptarlos |
| Método de verificación | Ejecución directa de los scripts sobre clones limpios del repositorio; comparación manual de las cifras obtenidas contra el ERS y la matriz vigente |

## 4. MVP / Prototipo

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí** |
| Herramienta | Figma Make (generación de interfaces) + Claude, Anthropic (apoyo en la verificación) |
| Finalidad | Generación de las interfaces del prototipo (mockups funcionales) en Figma Make; apoyo de Claude para contrastar la correspondencia entre pantallas y catálogo de requisitos |
| Responsable | Macías Herrera Josthyn Esteban |
| Quién verificó | Rizzo Vélez Edson Nagib |
| Método de verificación | Revisión pantalla por pantalla contra el catálogo de requisitos, con apoyo de Claude para esa verificación |

## 5. Datos (`07_Datos`, scripts de análisis)

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí** |
| Herramienta | Claude (Anthropic), vía claude.ai — del 2026-09-03 al 2026-09-11 (confirmado por `git log` sobre `07_Datos`) |
| Finalidad | Generación y depuración de scripts Python de análisis y de generación de entregables: `openpyxl` para los workbooks de métricas, `matplotlib` para las figuras, `pypdf` para inspección de PDF, y la compilación LaTeX de dos pasadas. Asistencia en código, no en la interpretación de los resultados. |
| Responsable | Villafuerte Rosero Allan Noe |
| Quién verificó | Macías Herrera Josthyn Esteban |
| Método de verificación | Ejecución reproducible de `run_all.py` en modo estricto y contraste de las salidas contra los datos crudos de `07_Datos` |

**Nota aparte — doble codificación (AUT-07):** el script `calcular_acuerdo.py`
y `00_extraer_subconjunto.py` en `10_Autoria/doble_codificacion/` sí fueron
generados con **Claude (Anthropic)**, responsable Macías Herrera Josthyn
Esteban, verificado ejecutándolos contra los datos reales de codificación de
Allan y Josthyn.

## 6. Experimento (humano vs. LLM)

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí, por definición del propio diseño experimental** — un modelo LLM genera uno de los dos conjuntos de requisitos comparados |
| Herramienta | Claude (Anthropic) y Gemini (Google) |
| Finalidad | Generar el conjunto de requisitos "LLM" (LLM-001 a LLM-025) para la comparación humano vs. LLM |
| Responsable | Huilcapi León Denisses Fabiola |
| Quién verificó | Macías Herrera Josthyn Esteban |
| Método de verificación | Registro de la salida cruda sin editar en `06_Experimento/prompts_llm/LLM-001_a_LLM-025_ENTR-04.md`; pendiente completar `registro_ejecucion.md` con prompt y parámetros exactos (modelo, temperatura, top-p, semilla) |

## 7. Manuscrito (publicación)

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí** |
| Herramienta | Claude (Anthropic), vía claude.ai — del 2026-09-03 al 2026-09-08 (confirmado por `git log` sobre `08_Publicacion`) |
| Finalidad | Apoyo únicamente en la redacción del texto (no en la generación de datos, resultados ni cifras, que provienen del análisis real del equipo). Se confirma que los cuatro usos aplican: redacción y estructuración de secciones según la plantilla de la revista objetivo; organización del cuadro comparativo de trabajo relacionado; redacción de la sección de metodología en formato PICOC; corrección de estilo y revisión de coherencia. |
| Responsable | Villafuerte Rosero Allan Noe |
| Quién verificó | Macías Herrera Josthyn Esteban |
| Método de verificación | Verificación individual de que cada referencia bibliográfica citada existe y respalda lo afirmado; contraste de cada tabla y figura contra los scripts que las generan |

## 8. Scripts (general, fuera de `07_Datos` y trazabilidad)

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí** |
| Herramienta | Claude (Anthropic) |
| Finalidad | Ver secciones 3, 4 y 5 arriba para el detalle específico por script |
| Responsable | Macías Herrera Josthyn Esteban |
| Quién verificó | Macías Herrera Josthyn Esteban |
| Método de verificación | Ejecución real de cada script contra datos del repositorio antes de aceptar sus resultados |

## 9. Defensa oral

| Campo | Detalle |
|---|---|
| ¿Se usó IA? | **Sí** |
| Herramienta | Claude (Anthropic) |
| Finalidad | Apoyo en la redacción de guiones de exposición individuales, a partir de datos y cifras ya existentes en el repositorio (no se generó contenido nuevo, solo se organizó y redactó el discurso) |
| Responsable | Macías Herrera Josthyn Esteban |
| Quién verificó | Macías Herrera Josthyn Esteban — cada cifra y afirmación del guion fue contrastada contra el ERS, la matriz de trazabilidad y otros documentos fuente antes de su uso |
| Método de verificación | Revisión cruzada de cada dato citado en el guion contra el archivo fuente correspondiente |

---

## Áreas donde NO se usó IA generativa (declaración explícita)

- **Fotografías, videos, grabaciones de audio de entrevistas y consentimientos**: son evidencia primaria real, no generada ni asistida por IA.
- **Transcripciones de entrevistas**: no fueron 100 % manuales — se usó **TurboScribe** (turboscribe.ai) como herramienta de transcripción automática (voz a texto) del audio original. Se aclara que esta herramienta transcribe el contenido ya existente y no genera texto nuevo, por lo que se distingue de un uso de IA generativa, pero se declara igualmente por transparencia. Verificado por Rizzo Vélez Edson Nagib mediante cotejo de la transcripción contra el audio original.
- **Codificación temática y doble codificación**: los códigos y categorías asignados a cada fragmento fueron decisión de criterio humano de Allan y Josthyn — la IA solo generó el script de *cálculo* del coeficiente de acuerdo, no los códigos en sí.
