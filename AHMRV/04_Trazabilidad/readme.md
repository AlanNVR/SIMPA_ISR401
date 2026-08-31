# Trazabilidad

Esta carpeta concentra los artefactos de trazabilidad extremo a extremo del
proyecto SIMPA.

A partir de la consolidación de la Entrega PE5, la matriz vigente es
`matriz_e2e.xlsx`.

---

## 1. Matriz vigente: `matriz_e2e.xlsx`

`matriz_e2e.xlsx` corresponde a la matriz extremo a extremo consolidada en PE5.

Contiene:

- **73 filas de trazabilidad**, identificadas de `TR-01` a `TR-73`.
- Trazas correspondientes al catálogo vigente posterior al Change Control Board.
- Relaciones entre fuentes/evidencias, requisitos, casos de uso, historias,
  criterios de aceptación y demás artefactos asociados.
- Hojas adicionales de diagnóstico y sincronización utilizadas durante la
  auditoría de calidad de PE5.

Esta es la **matriz que debe utilizarse como referencia vigente** para la
evaluación del proyecto.

### Cómo debe leerse

La cadena se recorre de izquierda a derecha para responder:

> ¿De dónde se originó este requisito y en qué artefactos terminó?

Y puede recorrerse en sentido inverso para responder:

> ¿Por qué existe este caso de uso, criterio, componente o elemento del sistema?

La trazabilidad debe permitir conectar una decisión del sistema con la evidencia
que la originó.

---

## 2. Matriz anterior: `matriz_trazabilidad.csv`

`matriz_trazabilidad.csv` se conserva temporalmente como evidencia de la versión
anterior del proyecto.

Contiene **52 filas** y corresponde al estado previo a la consolidación de PE5.

Por tanto:

- **no debe utilizarse como matriz vigente**;
- se conserva para mantener trazabilidad de la evolución del proyecto;
- sus cifras pueden diferir de las del catálogo aprobado posteriormente por el
  Change Control Board.

La matriz vigente es:

`matriz_e2e.xlsx`

---

## 3. Estado del catálogo consolidado en PE5

La consolidación de PE5 establece los siguientes valores:

| Métrica | Valor vigente |
|---|---:|
| Requisitos funcionales | 42 |
| Requisitos no funcionales | 19 |
| Requisitos de dominio | 10 |
| Requisitos legales | 8 |
| Historias de usuario | 24 |
| Casos de uso identificados | 18 |
| Casos de uso especificados | 18 |
| Filas de trazabilidad | 73 |
| Must | 24 |
| Should | 16 |
| Could | 2 |
| Won't | 0 |

Los valores anteriores provienen de los artefactos consolidados y auditados en
PE5.

---

## 4. `priorizacion_moscow_kano.csv`

Este archivo contiene la priorización MoSCoW/Kano del catálogo funcional.

La migración de PE5 incorporó RF-40, RF-41 y RF-42, aprobados mediante RFC-03
por el Change Control Board, por lo que el catálogo contenido en el archivo es
ahora de 42 requisitos funcionales:

- 24 Must;
- 16 Should;
- 2 Could.

Para RF-40, RF-41 y RF-42 se conserva únicamente la clasificación MoSCoW
documentada en PE5. Los campos Kano, Valor de negocio, Criticidad temporal,
Reducción de riesgo, Tamaño y WSJF permanecen vacíos porque PE5 no dejó una
puntuación cuantitativa post-CCB para esos requisitos.

No se asignaron valores retrospectivos ni estimaciones no documentadas con el
fin de evitar presentar como auditada una priorización que no fue realizada.

---

## 5. Evidencia de gestión del backlog

`backlog_export.csv` contiene el export del backlog utilizado en PE5.

La carpeta:

`Capturas/`

conserva las capturas de respaldo de la configuración y trazabilidad en Jira.

Actualmente incluye evidencias relacionadas con:

- backlog y épicas;
- campos y enlaces de RF;
- campos y enlaces de requisitos de IA;
- requisitos posteriores al CCB;
- estadísticas del proyecto SIMPA.

Estos archivos constituyen evidencia complementaria de la gestión y
sincronización del backlog.

---

## 6. Relación entre los principales artefactos

| Artefacto | Función |
|---|---|
| `matriz_e2e.xlsx` | Matriz vigente extremo a extremo de PE5 |
| `matriz_trazabilidad.csv` | Versión anterior de 52 filas |
| `priorizacion_moscow_kano.csv` | Priorización; pendiente de sincronización con el catálogo post-CCB |
| `backlog_export.csv` | Export del backlog de PE5 |
| `Capturas/` | Evidencia visual de Jira y de la sincronización |

---

## 7. Regla de interpretación

Ante cualquier discrepancia numérica durante la migración:

1. se utiliza como fuente principal la línea base consolidada de PE5;
2. no se recalculan manualmente cifras que PE5 ya auditó;
3. se documenta explícitamente cuándo un archivo corresponde a una versión
   previa;
4. no se elimina un artefacto histórico hasta que su reemplazo haya sido
   verificado.

La reconciliación definitiva de las cifras del MVP y de la priorización se
realizará después de completar la migración de los anexos de auditoría y del
Change Control Board.