# Hallazgos de usabilidad — Validación por walkthrough

**Sesiones:** 6 · **Fecha:** 2026-09-03 · **Prototipo evaluado:** SIMPA V2
**Participantes:** `WT-01` a `WT-06`

Este documento consolida lo observado en las seis sesiones de validación por
walkthrough. Cada hallazgo procede de una intervención registrada en la
transcripción de la sesión correspondiente; no se han añadido hallazgos
inferidos ni observaciones que no consten en el material.

---

## 1. Composición de la muestra

| Código | Perfil declarado | Ocupación manifestada | Riqueza de la sesión |
|---|---|---|---|
| `WT-01` | No técnico | Sector comercial (cacao) | Baja |
| `WT-02` | Técnico | Estudiante de software | Media |
| `WT-03` | Técnico | Supervisor, con experiencia previa en desarrollo | **Alta** |
| `WT-04` | Técnico | Supervisor | **Alta** |
| `WT-05` | No técnico | Estudiante, trabajo ocasional en sector agrario | Muy baja |
| `WT-06` | No técnico | Estudiante de software, sin experiencia laboral | Media |

Tres sesiones concentran prácticamente todos los hallazgos (`WT-03`, `WT-04`,
`WT-06`). Las otras tres aportan sobre todo confirmación de que los flujos
principales se completan sin bloqueo.

---

## 2. Hallazgos

Severidad propuesta por el equipo a partir de lo observado. **Requiere
validación del equipo antes de considerarse definitiva.**

### H-01 · No hay indicación del módulo activo · Alta · `WT-03`

Al navegar a «historial de reportes», la pestaña cambia pero el indicador de
ubicación sigue mostrando el panel principal. El participante lo detectó de
inmediato: el sistema cambia de contexto sin informar al usuario de dónde está.

**Requisito afectado:** requisito no funcional de usabilidad.
**Acción sugerida:** indicador de módulo activo persistente en la navegación.

### H-02 · Las alertas muestran cuántas, no cuáles · Alta · `WT-04`

El panel presenta el número de alertas sin permitir ver de qué alertas se
trata desde ahí. Fue la primera observación de la participante sobre el panel.

**Requisito afectado:** `RF-12` (generación de alertas tempranas).

### H-03 · El registro fitosanitario no admite evidencia de respaldo · Alta · `WT-03`

Un problema fitosanitario se registra únicamente con datos declarados. El
participante señaló que no existe forma de contrastar que la información
agregada sea real, y propuso adjuntar pruebas o un diagnóstico técnico, además
de un indicador de cuarentena del lote.

**Requisito afectado:** `RF-05` (registro de monitoreo fitosanitario).

### H-04 · El cambio de etapa del lote no exige justificación · Alta · `WT-03`

El estado de un lote puede pasar de siembra a mantenimiento sin ningún
respaldo. El participante propuso una observación obligatoria o evidencia que
sustente el cambio.

**Requisito afectado:** `RF-02` (gestión de plantaciones y lotes).

### H-05 · El sistema no orienta sobre el flujo de trabajo · Alta · `WT-06`

Es el hallazgo más insistente de todo el conjunto: el participante lo formuló
tres veces. El sistema comunica qué se puede hacer, pero no cómo hacerlo ni en
qué orden. Terminó deduciendo la secuencia —gestionar, revisar problemas,
recurrir al análisis asistido— sólo tras varios intentos, y pidió expresamente
una introducción breve al ingresar que indique el flujo correcto.

**Requisito afectado:** requisito no funcional de usabilidad.
**Acción sugerida:** guía de primer uso o recorrido guiado inicial.

### H-06 · Terminología no comprendida · Media · `WT-03`, `WT-04`, `WT-06`

Cuatro términos generaron detención en tres participantes distintos:

| Término | Participante | Comentario |
|---|---|---|
| «chapia» | `WT-04` | «podría existir una especificación, porque yo no sé qué es eso» |
| «lotes activos» | `WT-04` | Pidió aclaración al moderador |
| «actualizar la etapa» | `WT-04` | No comprendió la función del botón |
| «cantidad» | `WT-06` | Se detuvo sin poder completar el campo |

Que la terminología del dominio detenga incluso a perfiles técnicos indica que
el problema no es de alfabetización digital.

**Requisito afectado:** requisito no funcional de usabilidad.
**Acción sugerida:** glosario contextual o texto de ayuda por campo.

### H-07 · Los registros no se pueden ordenar ni filtrar por gravedad · Media · `WT-04`

La tabla de registros fitosanitarios se ordena por fecha. La participante
esperaba verlos por gravedad, de mayor a menor, y propuso un botón de filtro.

**Requisito afectado:** `RF-05`.

### H-08 · Los KPI quedan por debajo del pliegue · Media · `WT-03`

Los indicadores están en la parte inferior del panel, lo que obliga a
desplazarse para lo que debería ser un vistazo rápido. El participante propuso
reorganizar el panel siguiendo patrones de lectura en T o en Z.

**Requisito afectado:** `RF-19` (generación de reportes) y panel principal.

### H-09 · El plan semanal es difícil de leer · Media · `WT-03`

La presentación tabular del plan semanal resulta densa. El participante propuso
una vista de tablero que permita mover actividades entre días de forma directa.

**Requisito afectado:** `RF-26` (planificación semanal con presupuesto).

### H-10 · Los reportes son de un solo tipo · Media · `WT-03`

Existe un reporte general. El participante enumeró varios que un supervisor
necesitaría: por lote, por trazabilidad del lote, por rendimiento.

**Requisito afectado:** `RF-19`.

### H-11 · Los controles no permitidos se muestran deshabilitados · Media · `WT-03`

El perfil de supervisor ve botones que no puede usar, como la liquidación
reservada al administrador. El participante fue explícito: es preferible
ocultarlos que mostrarlos inactivos.

**Requisito afectado:** `RF-01` (autenticación y control de acceso por rol).

### H-12 · El módulo de GPS no se comprende sin explicación · Media · `WT-03`, `WT-06`

Dos participantes pidieron que se les explicara para qué sirve. `WT-06`
declaró no entender «registrar marcación». `WT-03`, tras la explicación,
propuso que el sistema permita delimitar el área de la finca por coordenadas,
dado que una explotación puede tener varias sucursales en cantones distintos.

**Requisito afectado:** `RF-14` (conteo georreferenciado).

### H-13 · Las alertas no salen de la aplicación · Baja · `WT-03`

El participante preguntó por el canal de notificación y planteó la necesidad de
integración con mensajería o correo, ya que una alerta que solo existe dentro de
la aplicación web depende de que alguien la abra.

**Requisito afectado:** `RF-12`.

### H-14 · No se localiza dónde se visualiza lo registrado · Baja · `WT-06`

Tras guardar un registro fitosanitario, el participante preguntó dónde podía
verlo. `WT-02`, en cambio, sí encontró el historial y comprobó que el registro
queda asociado al lote correcto.

**Requisito afectado:** `RF-05`.

### H-15 · Fricción en el ingreso · Baja · `WT-05`

El participante necesitó asistencia para introducir las credenciales de
demostración, incluido un error de transcripción del nombre de usuario.

**Requisito afectado:** `RF-01`.

---

## 3. Comportamiento del componente de análisis por imagen

Los seis participantes llegaron al módulo de análisis asistido. Su lectura
difiere de forma relevante:

- `WT-02` completó el flujo y leyó el resultado, incluida la advertencia de que
  se trata de una demostración que debe ser validada por personal técnico.
- `WT-04` comprendió la función pero no pudo probarla, y lo lamentó
  expresamente: «sí llama la atención, pero ahorita no se puede probar».
- `WT-03` y `WT-06` pidieron que se les explicara el objetivo del módulo antes
  de poder usarlo.

`WT-03` aportó además una observación técnica sobre la vía de implementación
—entrenar un modelo propio frente a apoyarse en uno existente— que excede el
alcance de esta validación pero queda registrada.

**Esto no constituye un defecto de usabilidad.** `RF-07`, `RF-08` y la
clasificación visual asociada a `RF-21` están declarados como interfaz
simulada, sin inferencia real. Los hallazgos se registran porque muestran que
el módulo genera expectativa y que la advertencia en pantalla cumple su función
cuando el participante llega a leerla.

---

## 4. Lo que funcionó

Registrado por simetría: un informe que solo recoge defectos no describe la
sesión.

- **Los seis participantes completaron el registro de un problema
  fitosanitario** sin bloqueo, incluidos los tres de perfil no técnico.
- **La persistencia se comportó como se documenta.** `WT-02` la verificó de
  forma explícita abriendo una segunda pestaña, y comprobó también que un
  registro queda asociado al lote seleccionado y no a otro.
- **El control de acceso por rol se percibió.** `WT-03` identificó que la
  liquidación está reservada al administrador.
- **`WT-01` completó los flujos sin fricción declarada** y respondió que usaría
  el sistema en su trabajo diario porque «cada cosa estaba detallada».
- La valoración general fue positiva en las seis sesiones.

---

## 5. Limitaciones de esta validación

Se declaran porque condicionan cómo deben interpretarse los hallazgos.

### 5.1 Conflicto de interés en `WT-02`

**`WT-02` es integrante del equipo de desarrollo del proyecto.** La
transcripción recoge que el propio moderador validó su participación sobre la
base de que su rol en el equipo no interviene en la construcción del prototipo.

Ese razonamiento no elimina el conflicto: la participante conoce el dominio a
través del trabajo de campo del propio equipo, y su sesión es la más fluida y
la que menos fricción reporta de las seis. Sus observaciones se conservan por
transparencia, pero **no deben computarse como validación externa
independiente**, y ninguna conclusión de este documento se apoya únicamente en
su sesión.

### 5.2 Clasificación de perfiles no consistente

La clasificación técnico / no técnico presenta incoherencias:

- `WT-06`, estudiante de Ingeniería en Software, figura como **no técnico**.
- `WT-02`, también estudiante de software, figura como **técnico**.
- `WT-03` y `WT-04` declararon «Supervisor» como perfil, que describe una
  función y no un nivel de familiaridad con herramientas digitales.

El criterio declarado es la experiencia manifestada con herramientas digitales
de gestión, no la titulación ni el cargo. Aplicado con rigor, la muestra real
no se reparte tres y tres. **Pendiente de reconciliar antes de reportar
resultados por estrato.**

### 5.3 Desviación respecto del método

El protocolo de walkthrough establece que el moderador no explique las
pantallas antes de la tarea, precisamente para observar qué comprende el
participante sin ayuda. En varias sesiones el moderador explicó el
funcionamiento de módulos —análisis asistido, GPS, actualización de etapa— a
petición del participante.

Esas explicaciones **son en sí mismas un hallazgo**: que un participante deba
preguntar para qué sirve un módulo indica que el módulo no se explica solo. Pero
invalidan la observación posterior sobre ese módulo concreto, que ya no refleja
comprensión autónoma.

### 5.4 Profundidad desigual

La sesión de `WT-05` aporta muy poca información: el participante recorrió la
aplicación sin verbalizar y su valoración final fue general. La sesión de
`WT-01` es también breve y con conducción del moderador. Ninguna de las dos
sostiene por sí sola una conclusión.

---

## 6. Priorización sugerida

Ordenado por relación entre impacto observado y esfuerzo estimado. **Propuesta
del equipo, no resultado de la sesión.**

| Prioridad | Hallazgos | Justificación |
|---|---|---|
| 1 | H-05, H-01 | Afectan a la orientación general; H-05 fue el hallazgo más repetido |
| 2 | H-02, H-06 | Detuvieron a participantes de ambos perfiles |
| 3 | H-03, H-04 | Afectan a la fiabilidad del dato registrado, no solo a la comodidad |
| 4 | H-07, H-08, H-11 | Mejoras de presentación con implementación acotada |
| 5 | H-09, H-10, H-12, H-13 | Requieren rediseño o alcance nuevo |

---

## 7. Trazabilidad

| Requisito | Hallazgos asociados |
|---|---|
| `RF-01` | H-11, H-15 |
| `RF-02` | H-04 |
| `RF-05` | H-03, H-07, H-14 |
| `RF-12` | H-02, H-13 |
| `RF-14` | H-12 |
| `RF-19` | H-08, H-10 |
| `RF-26` | H-09 |
| Usabilidad (RNF) | H-01, H-05, H-06 |

La correspondencia entre cada código `WT-XX` y la persona participante se
registra únicamente en la zona restringida. Este documento y el resto de la
zona pública identifican a los participantes sólo por código.
