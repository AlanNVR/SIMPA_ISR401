# Componente experimental

Enfoque 1 de la Sección 5 de la guía: comparación de la calidad de los requisitos funcionales elicitados por el equipo humano frente a los generados por un modelo grande de lenguaje a partir del mismo material fuente.

## Estado

**Protocolo diseñado y registrado públicamente en OSF. El registro es retrospectivo respecto a la recolección del material fuente y anterior a la ejecución del experimento humano–LLM, que permanece pendiente.**

**Registro público OSF:** https://osf.io/4z35d/

### Aclaración temporal del registro

El registro OSF **no se presenta como prerregistro de la recolección de entrevistas ni del proyecto completo**. Al momento de formalizarlo ya existía material fuente procedente de entrevistas realizadas durante el desarrollo de SIMPA.

Su alcance temporal es más preciso: constituye un **registro retrospectivo respecto a la recolección del material fuente**, pero fue realizado **antes de ejecutar el experimento comparativo humano–LLM** descrito en este protocolo. Ese experimento continúa pendiente.

Por tanto, el registro se utiliza para dejar congelados y públicamente trazables la pregunta de investigación, las hipótesis, las variables, el procedimiento y el plan de análisis del experimento comparativo, sin afirmar una secuencia temporal que el historial no sostiene.

El registro OSF conserva la versión del protocolo presentada al momento del registro.
La versión 1.2 mantenida en el repositorio incorpora esta aclaración documental
del alcance temporal del registro, sin modificar hipótesis, variables, muestra,
procedimiento ni plan de análisis.

En consecuencia, el ERS/SRS de la Entrega 3 (2A) no contiene sección de resultados ni de discusión de este estudio. Ambas corresponden a la Entrega 4 (2B), una vez recogidos y analizados los datos primarios.

## Contenido

| Archivo o carpeta | Contenido | Estado |
|---|---|---|
| `protocolo.pdf` | PICOC, hipótesis, variables, procedimiento, plan de análisis estadístico y amenazas a la validez | ✅ |
| `protocolo.tex` | Fuente LaTeX del protocolo | ✅ |
| `osf_registration.pdf` | Comprobante del registro público OSF: https://osf.io/4z35d/ | ✅ |
| `instrumentos/` | Guiones, cuestionario, rúbrica y consentimientos | 🟡 parcial |
| `prompts_llm/` | Consignas exactas con modelo, temperatura, top-p y semilla | ⏳ pendiente de ejecución |
| `../07_Datos/` | Datos crudos, procesados, scripts y resultados | 🟡 estructura activa; experimento principal pendiente |
| `../07_Datos/scripts/` | Scripts Python de transformación y análisis | ✅ cadena reproducible disponible mediante `run_all.py` |

## Secuencia obligatoria

```
material fuente de entrevistas ya disponible
        ↓
registrar públicamente el protocolo experimental en OSF
        ↓
ejecutar el experimento comparativo humano–LLM
        ↓
analizar los datos experimentales con los scripts versionados
        ↓
recién entonces redactar los resultados del experimento
```

⚠️ Redactar resultados hipotéticos «para completar la estructura», o hacer que un modelo invente cifras para llenar las tablas, es fabricación de evidencia. El plan de análisis de la Sección 8 quedó fijado antes de disponer de los **datos producidos por el experimento humano–LLM** y no se modificará en función de sus resultados. Esta afirmación no se extiende al material fuente de entrevistas, que ya existía.

## Limitación declarada de antemano

El diseño contempla 25 pares de requisitos. Con α = 0,05, potencia objetivo de 0,80 y tamaño de efecto medio (d = 0,5), el tamaño requerido sería de aproximadamente 34 pares. **La potencia alcanzable queda por debajo del objetivo.**

Se declara antes de ejecutar y se reportará como amenaza a la validez de conclusión. No se incrementará artificialmente el tamaño muestral duplicando requisitos.

El mapa de correspondencia R-ID ↔ origen se custodia en un repositorio privado independiente (evidencia_mapa), acceso restringido al custodio designado (Edson Rizzo) y al docente.
