# Componente experimental

Enfoque 1 de la Sección 5 de la guía: comparación de la calidad de los requisitos funcionales elicitados por el equipo humano frente a los generados por un modelo grande de lenguaje a partir del mismo material fuente.

## Estado

**Protocolo diseñado y registrado. Experimento no ejecutado.**

En consecuencia, el ERS/SRS de la Entrega 3 (2A) no contiene sección de resultados ni de discusión de este estudio. Ambas corresponden a la Entrega 4 (2B), una vez recogidos y analizados los datos primarios.

## Contenido

| Archivo o carpeta | Contenido | Estado |
|---|---|---|
| `protocolo.pdf` | PICOC, hipótesis, variables, procedimiento, plan de análisis estadístico y amenazas a la validez | ✅ |
| `protocolo.tex` | Fuente LaTeX del protocolo | ✅ |
| `osf_registration.pdf` | Comprobante de registro previo con URL persistente y marca temporal | ⏳ pendiente |
| `instrumentos/` | Guiones, cuestionario, rúbrica y consentimientos | 🟡 parcial |
| `prompts_llm/` | Consignas exactas con modelo, temperatura, top-p y semilla | ⏳ pendiente de ejecución |
| `resultados/` | Datos crudos y procesados, tablas y figuras | ⏳ pendiente de ejecución |
| `scripts_analisis/` | Scripts en R o Python que reproducen cada tabla y figura | ⏳ pendiente |

## Secuencia obligatoria

```
registrar el protocolo en OSF
        ↓
ejecutar el experimento
        ↓
analizar los datos con los scripts versionados
        ↓
recién entonces redactar los resultados
```

⚠️ Redactar resultados hipotéticos «para completar la estructura», o hacer que un modelo invente cifras para llenar las tablas, es fabricación de evidencia. El plan de análisis de la Sección 8 del protocolo se fijó **antes** de disponer de datos y no se modificará en función de los resultados obtenidos.

## Limitación declarada de antemano

El diseño contempla 25 pares de requisitos. Con α = 0,05, potencia objetivo de 0,80 y tamaño de efecto medio (d = 0,5), el tamaño requerido sería de aproximadamente 34 pares. **La potencia alcanzable queda por debajo del objetivo.**

Se declara antes de ejecutar y se reportará como amenaza a la validez de conclusión. No se incrementará artificialmente el tamaño muestral duplicando requisitos.
