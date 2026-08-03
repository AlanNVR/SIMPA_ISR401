# Análisis de revistas objetivo

**Proyecto SIMPA · Equipo AHMRV · ISR-401 · UTEQ**
Versión 1.0 — 3 de agosto de 2026

---

## Estado de este documento

⚠️ **Análisis preliminar.** La guía establece que la selección definitiva se decide en la semana 16, ejecutando las tres herramientas oficiales con el **título y el resumen del propio manuscrito**. Ese manuscrito está en versión 1.0 y solo tiene cerradas las secciones de introducción, trabajo relacionado y metodología.

Este documento cumple dos funciones: registrar las candidatas identificadas con datos verificados a la fecha, y dejar establecido el procedimiento que la persona autora principal debe ejecutar antes del envío.

Las celdas marcadas **`[verificar]`** requieren consulta directa en el sitio de la editorial. Los valores de APC cambian anualmente y varían según país e institución; no se consignan de memoria.

---

## Título y resumen empleados en la búsqueda

**Título preliminar (13 palabras):**

> Calidad de requisitos elicitados por analistas humanos frente a un modelo grande de lenguaje en un sistema agroindustrial

**Palabras clave:** ingeniería de requisitos · estudio empírico · modelos grandes de lenguaje · calidad de requisitos · explicabilidad

**Resumen preliminar (para pegar en las herramientas):** véase `07_Publicacion/manuscrito_borrador.pdf`, sección *Abstract*.

---

## Candidatas por editorial

La guía exige registrar al menos dos candidatas de cada editorial: una en acceso abierto con APC y otra por suscripción o híbrida sin cargo obligatorio.

### Springer Nature

| | **Requirements Engineering** | **Empirical Software Engineering** |
|---|---|---|
| Editorial | Springer London | Springer |
| ISSN | 0947-3602 / 1432-010X | 1382-3256 / 1573-7616 |
| Factor de impacto | **3,63** (2024) | `[verificar]` |
| Cuartil JCR | `[verificar]` | `[verificar]` |
| SJR | 0,522 | `[verificar]` |
| Índice h | 66 | `[verificar]` |
| Modelo de acceso | **Híbrida** — publicación por suscripción sin cargo obligatorio | Híbrida |
| APC si se opta por acceso abierto | `[verificar]` — rango habitual Springer hybrid: USD 2.000–3.500 | `[verificar]` |
| Tiempo a primera decisión | `[verificar]` | `[verificar]` |
| Ajuste temático | **Alto.** Es la revista de referencia del área; publica los tres artículos de Chazette sobre explicabilidad que sustentan el RNF-16 | Alto. Publica estudios empíricos con protocolo y análisis estadístico |

> **Nota sobre la vía sin cargo.** *Requirements Engineering* es híbrida: se puede publicar por suscripción **sin pagar APC**. Esta es la candidata sin cargo obligatorio del grupo Springer.

### Elsevier

| | **Information and Software Technology** | **Journal of Systems and Software** |
|---|---|---|
| Editorial | Elsevier BV | Elsevier |
| ISSN | 0950-5849 / 1873-6025 | 0164-1212 |
| Factor de impacto | **4,6** (datos de citación 2025, publicado jun. 2026) | `[verificar]` |
| Cuartil JCR | **Q1** | `[verificar]` |
| SJR | 1,054 | `[verificar]` |
| Modelo de acceso | Híbrida | Híbrida |
| APC acceso abierto | **USD 3.350** | `[verificar]` |
| Vía sin cargo | Sí, publicación por suscripción | Sí |
| Tiempo a primera decisión | `[verificar]` | `[verificar]` |
| Ajuste temático | **Muy alto.** Publicó a Molléri, Petersen y Mendes sobre listas de verificación para encuestas, referencia metodológica de este estudio. Tiene número especial activo sobre GenAI y factor humano | Alto |

### IEEE

| | **IEEE Transactions on Software Engineering** | **IEEE Software** |
|---|---|---|
| Editorial | IEEE Computer Society | IEEE Computer Society |
| ISSN | 0098-5589 | 0740-7459 |
| Factor de impacto | `[verificar]` | `[verificar]` |
| Cuartil JCR | `[verificar]` | `[verificar]` |
| Modelo de acceso | Híbrida | Híbrida |
| APC acceso abierto | **USD 2.800** (tarifa IEEE para envíos de 2026) | `[verificar]` |
| Vía sin cargo | Sí, publicación por suscripción | Sí |
| Ajuste temático | Alto, pero exigencia metodológica muy elevada | Medio-alto. Formato más corto, orientado a práctica profesional |

---

## Recomendación preliminar

**Primera opción: *Information and Software Technology*.**
Es la única candidata con cuartil Q1 confirmado y factor de impacto verificado (4,6). Su vía híbrida permite publicar sin pagar APC. Publicó la referencia metodológica principal del diseño de encuestas de este proyecto, y mantiene un número especial activo sobre inteligencia artificial generativa y factor humano, que encaja con el enfoque empírico elegido.

**Segunda opción: *Requirements Engineering*.**
Menor factor de impacto (3,63) pero mejor ajuste temático estricto: es la revista donde se publicó el marco de explicabilidad que sustenta el RNF-16 del ERS.

**Restricción económica.** El equipo no dispone de financiamiento para APC. Los USD 3.350 de *Information and Software Technology* y los USD 2.800 de IEEE están fuera de alcance. **Ambas primeras opciones se abordan por la vía híbrida sin cargo**, que no exige pago alguno a las personas autoras.

---

## Ajuste de la categoría de envío

La §7.11 de la guía condiciona la categoría al volumen de datos empíricos alcanzado.

| Escenario | Categoría de envío |
|---|---|
| Se alcanza el objetivo 2B | Artículo completo en revista JCR |
| Entre el mínimo 2A y el objetivo 2B | Artículo corto o *tool paper* |
| Por debajo del mínimo 2A | Póster o demostración |

**Situación real del proyecto a la fecha:**

| Evidencia | Mínimo 2A | Objetivo 2B | Alcanzado |
|---|---|---|---|
| Consentimientos 2ª ronda | 8 | 16 | **8** ✅ |
| Videos | 8 | 16 | **14** ✅ |
| Audios | 8 | 16 | **8** ✅ |
| Respuestas de cuestionario | n≥30 | n≥60 | **n=62** ✅ |
| Documentos de la organización | 3 tipos | 5 | 2 tipos ⚠️ |
| Sesiones de walkthrough | 3 | 6 | pendiente ⚠️ |

El proyecto se sitúa **entre el mínimo 2A y el objetivo 2B**. La categoría que corresponde en este momento es **artículo corto**, con posibilidad de escalar a artículo completo si antes de la Entrega 4 se completan las sesiones de validación y el tercer tipo documental.

---

## Procedimiento pendiente para la semana 16

Ejecutar **la persona autora principal**, con el título y el resumen definitivos:

1. **Springer** — `journalsuggester.springer.com`
   Registrar: coincidencia temática, cuartil JCR, tiempo medio a primera decisión, modalidad de acceso y tarifa APC.

2. **Elsevier** — `journalfinder.elsevier.com`
   Registrar: emparejamiento con revistas indexadas en Scopus, puntuación de coincidencia con el resumen, CiteScore y factor de impacto.

3. **IEEE** — `publication-recommender.ieee.org`
   Registrar: coincidencia con *transactions* y *letters*, factor de impacto, estado de acceso abierto y tiempo medio de revisión.

Para cada resultado, completar las celdas `[verificar]` de las tablas anteriores y adjuntar la captura de pantalla del resultado en `07_Publicacion/capturas_herramientas/`.

> La guía prohíbe justificar la elección únicamente por familiaridad o presencia previa en la editorial. La justificación debe sustentarse en la puntuación de ajuste de la herramienta oficial, en la coherencia entre el resumen y el alcance publicado de la revista, y en la viabilidad económica y temporal del envío.

---

## Fuentes de los datos consignados

Los valores no marcados como `[verificar]` proceden de consulta directa realizada el 3 de agosto de 2026:

- Factor de impacto, cuartil JCR y APC de *Information and Software Technology*: registro de métricas de la revista, datos de citación 2025 publicados en junio de 2026.
- Factor de impacto, SJR e índice h de *Requirements Engineering*: registro de métricas basado en datos de Scopus.
- Tarifa APC de IEEE: tabla de cargos por procesamiento de artículo para envíos de 2026.

⚠️ Estos valores deben reconfirmarse en el sitio oficial de cada revista antes del envío. Las tarifas de APC y los cuartiles se actualizan anualmente.
