# Correcciones aplicadas tras la miembro-verificación

**Proyecto:** SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
**Equipo:** AHMRV — Universidad Técnica Estatal de Quevedo
**Ronda de miembro-verificación:** 4 de septiembre de 2026
**Participantes:** ENTR-01, ENTR-02, ENTR-13
**Documento asociado:** `Acta_MemberChecking_00_Consolidada_P.md`

---

> **Estado del documento.** Las columnas de evidencia y análisis recogen lo efectivamente
> registrado en la ronda. La decisión de cada caso figura como **propuesta del equipo** y debe
> ser ratificada en reunión antes del cierre de la entrega; una vez ratificada, sustitúyase el
> estado por *Aplicada* e indíquese el responsable y la fecha.

---

## 1. Alcance

Se registran aquí los enunciados interpretativos sobre los que se produjo **desacuerdo, matiz
sustantivo o ausencia de posición** durante la ronda de miembro-verificación, junto con la
decisión adoptada por el equipo sobre cada uno.

Los enunciados confirmados sin discrepancia por los tres participantes —4, 5 y 6— no aparecen
en este documento por no requerir corrección.

**Criterio metodológico aplicado:** cuando dos participantes sostienen posiciones incompatibles
sobre un mismo hecho, la discrepancia **se reporta, no se concilia**. El equipo no adjudica cuál
de las fuentes tiene razón salvo que exista evidencia documental independiente que lo permita.

---

## 2. Registro de desacuerdos y decisiones

### D-01 · Enunciado 1 — Inexistencia de un formato fijo de reporte

| Campo | Contenido |
|---|---|
| **Enunciado original** | La información diaria del campo se anota en una libreta que lleva el jefe de campo y llega a la administración por WhatsApp. No hay un formato fijo para ese reporte. |
| **ENTR-01** | **Rechaza.** Afirma que sí existen formatos establecidos, que varían según la empresa y la función desempeñada (fitosanidad, jefatura de campo, entre otras), y que se entregan al final de la jornada. Su cumplimiento constituye un requisito. |
| **ENTR-02** | **Confirma parcialmente.** Válido para haciendas pequeñas, entre ellas la unidad de estudio. En haciendas de más de 500 hectáreas existe sistema informático y personal administrativo dedicado. |
| **ENTR-13** | **Confirma.** |
| **Naturaleza del desacuerdo** | Sustantivo. Afecta a la premisa de que no existe formalización del reporte diario, que sostiene requisitos de captura estructurada. |
| **Análisis** | Las tres posiciones son compatibles si el enunciado se delimita: ENTR-01 describe la existencia de formatos por función a nivel sectorial; ENTR-02 la condiciona a la escala de la explotación; ENTR-13 confirma la práctica observada. Lo que no se sostiene es la formulación absoluta. |
| **Decisión propuesta** | **Reformular con delimitación de alcance.** Nueva redacción: *«En la unidad de estudio el registro diario se realiza en libreta y se comunica por WhatsApp. Existen formatos establecidos por función a nivel sectorial, cuya aplicación depende de la escala de la explotación y de la gestión de la persona responsable.»* |
| **Impacto en requisitos** | Revisar los requisitos de captura de labores: el sistema no debe presuponer ausencia de formato, sino permitir configurar formatos por tipo de labor. |
| **Estado** | Propuesta — pendiente de ratificación |
| **Responsable** | Por definir |

---

### D-02 · Enunciado 2 — Insuficiencia de detalle del reporte

| Campo | Contenido |
|---|---|
| **Enunciado original** | Ese reporte a veces llega sin el detalle suficiente, lo que obliga a volver a preguntar o a esperar la visita presencial. |
| **ENTR-01** | **Rechaza.** El contenido se ajusta al formato correspondiente y su cumplimiento íntegro es exigible. |
| **ENTR-02** | **Confirma.** Describe la cadena jerárquica que compensa la insuficiencia: mantenimiento y sanidad reportan al administrador, que consolida. |
| **ENTR-13** | **Confirma.** En ocasiones la información carece de detalle y es necesario reiterar la consulta o esperar la visita. |
| **Naturaleza del desacuerdo** | Sustantivo e irreconciliable. Dos participantes afirman un hecho que un tercero niega. |
| **Análisis** | La posición de ENTR-01 puede reflejar la exigencia normativa del proceso; las de ENTR-02 y ENTR-13, su cumplimiento efectivo. No se dispone de evidencia documental independiente que permita adjudicar entre ambas lecturas. |
| **Decisión propuesta** | **Conservar el enunciado y reportar la discrepancia.** Se mantiene la interpretación por contar con el respaldo de dos de tres fuentes, dejando constancia expresa de la posición divergente en el apartado de amenazas a la validez, sin conciliarla. |
| **Impacto en requisitos** | Ninguno inmediato. Refuerza la pertinencia de los requisitos de validación de completitud en el registro. |
| **Estado** | Propuesta — pendiente de ratificación |
| **Responsable** | Por definir |

---

### D-03 · Enunciado 7 — Barrera de adopción localizada en el personal manual

| Campo | Contenido |
|---|---|
| **Enunciado original** | La dificultad para usar una aplicación no estaría en los técnicos ni en los administradores, sino en el personal de labores manuales del campo. |
| **ENTR-01** | **Rechaza.** Numerosas labores pueden aprenderse sin conocimiento experto previo, incluida la comprensión de los programas informáticos. |
| **ENTR-02** | **Confirma con matiz.** Atribuye la dificultad a la fase inicial de la plantación, a la menor difusión del cultivo de palma y a la exigencia de un manejo diferenciado por variedad; señala que el personal está en formación. |
| **ENTR-13** | **Confirma parcialmente.** Condiciona la mayor dificultad a la falta de familiaridad previa con este tipo de herramientas. |
| **Naturaleza del desacuerdo** | De alcance. Ningún participante niega la existencia de una brecha; discrepan sobre si es atribuible al perfil del trabajador o a condiciones coyunturales. |
| **Análisis** | Las tres posiciones convergen si la barrera se formula como **condicionada y transitoria** —dependiente de la formación recibida y de la familiaridad previa— en lugar de como un atributo del perfil ocupacional. |
| **Decisión propuesta** | **Reformular.** Nueva redacción: *«La barrera de adopción no reside en el perfil ocupacional sino en la familiaridad previa con herramientas digitales y en la formación recibida. Es una barrera condicionada y reducible mediante capacitación.»* |
| **Impacto en requisitos** | Refuerza los requisitos de usabilidad —interfaz sencilla, pocas pantallas, apoyo gráfico— y añade la necesidad de material de apoyo o introducción guiada, coincidente con el hallazgo del walkthrough 06. |
| **Estado** | Propuesta — pendiente de ratificación |
| **Responsable** | Por definir |

---

### D-04 · Enunciado 8 — Formalización asociada al tamaño de la finca

| Campo | Contenido |
|---|---|
| **Enunciado original** | En las fincas pequeñas las labores se anotan de forma empírica en libreta o cuaderno; solo en las fincas grandes se llevan formatos impresos al campo que en la tarde se pasan a un sistema. |
| **ENTR-01** | **Rechaza.** Existen fincas pequeñas organizadas y ordenadas. El factor determinante es la persona al frente de la propiedad, no su extensión. |
| **ENTR-02** | **Confirma con matiz.** Sitúa el umbral en torno a las 500 hectáreas y describe el circuito documental de las explotaciones grandes. |
| **ENTR-13** | **Confirma.** |
| **Naturaleza del desacuerdo** | Sobre la variable explicativa, no sobre el hecho observado. |
| **Análisis** | ENTR-01 no niega la existencia de los dos modos de registro, sino que discute su causa. La corrección es sustantiva: si el factor es la gestión y no la escala, el sistema no puede segmentarse por tamaño de explotación. |
| **Decisión propuesta** | **Reformular incorporando la gestión como variable explicativa.** Nueva redacción: *«Coexisten dos modos de registro: empírico en libreta y formalizado con paso posterior a sistema. La adopción de uno u otro depende principalmente de la gestión de la persona responsable, y de forma secundaria de la escala de la explotación.»* |
| **Impacto en requisitos** | El sistema debe soportar ambos modos de registro con independencia del tamaño de la explotación. |
| **Estado** | Propuesta — pendiente de ratificación |
| **Responsable** | Por definir |

---

### D-05 · Enunciado 10 — Desconfianza en los reportes climáticos

| Campo | Contenido |
|---|---|
| **Enunciado original** | Para programar las labores del día el trabajador se guía por cómo ve el cielo, no por los reportes del clima, porque no confía en ellos. |
| **ENTR-01** | **Rechaza.** Se emplean pluviómetro y datos informáticos como base para la toma de decisiones. |
| **ENTR-02** | **No abordado.** La sub-sesión concluyó antes de este enunciado. |
| **ENTR-13** | **Confirma parcialmente.** Reconoce el peso de la observación directa, pero precisa que también se emplean instrumentos e información climática. |
| **Naturaleza del desacuerdo** | Sustantivo. El componente de desconfianza no se sostiene. |
| **Análisis** | Ninguno de los dos participantes que abordaron el enunciado respalda la atribución de desconfianza. Ambos confirman el uso de instrumentos. La observación directa coexiste con la instrumentación en lugar de sustituirla. |
| **Decisión propuesta** | **Reformular eliminando la atribución de desconfianza.** Nueva redacción: *«La programación de las labores diarias combina la observación directa de las condiciones con el uso de instrumentos de medición —pluviómetro— e información climática consultada.»* |
| **Impacto en requisitos** | Sostiene el requisito de registro de lluvia y refuerza la pertinencia de integrar información climática, que el enunciado original desaconsejaba implícitamente. |
| **Estado** | Propuesta — pendiente de ratificación |
| **Responsable** | Por definir |

---

### D-06 · Enunciado 11 — Formulación ambigua

| Campo | Contenido |
|---|---|
| **Enunciado original** | Cuando una herramienta nueva se abandona en el campo, la causa principal es la resistencia al cambio, no que la herramienta sea mala. Se adopta si es sencilla, con pocas ventanas y con gráficos antes que números. |
| **ENTR-01** | **Sin posición.** El término *herramienta* admitió una lectura referida a las herramientas físicas de trabajo; la respuesta se orientó al control y la responsabilidad sobre estas, no al ámbito informático. |
| **ENTR-02** | **No abordado.** |
| **ENTR-13** | **Confirma.** Una herramienta puede abandonarse si resulta complicada de utilizar; debe ser sencilla, con pocas opciones y con interfaz visual. |
| **Naturaleza del desacuerdo** | No es desacuerdo sino **defecto de instrumento**: la formulación permitió dos lecturas. |
| **Análisis** | El fallo es del equipo, no del participante. La ambigüedad redujo de tres a dos las posiciones obtenibles sobre este enunciado. |
| **Decisión propuesta** | **Reformular el enunciado** sustituyendo *herramienta* por *aplicación o programa de computadora*, y **declarar el defecto** en el apartado de amenazas a la validez. No se recaba nuevamente la posición de ENTR-01 por encontrarse cerrado el trabajo de campo. |
| **Impacto en requisitos** | Ninguno. El contenido sustantivo mantiene el respaldo de ENTR-13 y coincide con los hallazgos de los walkthroughs. |
| **Estado** | Propuesta — pendiente de ratificación |
| **Responsable** | Por definir |

---

## 3. Ampliaciones derivadas de precisiones no contradictorias

Los siguientes enunciados fueron confirmados por todos los participantes que los abordaron, pero
recibieron precisiones de alcance operativo que obligan a ampliarlos.

### A-01 · Enunciado 3 — Distinción entre incidencias agrícolas y sanitarias

**Precisión aportada (ENTR-02):** los problemas de naturaleza agrícola admiten un margen de uno o
dos días; los de naturaleza sanitaria no admiten espera, dado que determinadas plagas —larvas
defoliadoras, coleópteros de hábitos nocturnos— pueden arrasar una plantación en una sola
jornada.

**Decisión propuesta:** ampliar el enunciado e incorporar la distinción al tratamiento de las
alertas del sistema, diferenciando el nivel de urgencia según la naturaleza de la incidencia
reportada. **Estado:** propuesta — pendiente de ratificación.

### A-02 · Enunciado 9 — Criterio de madurez por variedad

**Precisiones aportadas:** ENTR-02 señala que en la variedad híbrida presente en la plantación la
coloración del racimo no constituye indicador suficiente de madurez; el corte procede con entre
cuatro y seis frutos desprendidos, considerándose plenamente madura a partir de seis, y no debe
realizarse con uno a tres. ENTR-13 indica que deben considerarse factores adicionales al
desprendimiento.

**Decisión propuesta:** ampliar el enunciado incorporando el criterio diferenciado por variedad y
revisar los requisitos relacionados con la programación de la cosecha. **Estado:** propuesta —
pendiente de ratificación.

---

## 4. Resumen de decisiones

| Caso | Enunciado | Decisión propuesta | Estado |
|---|---|---|---|
| D-01 | 1 | Reformular con delimitación de alcance | Pendiente de ratificación |
| D-02 | 2 | Conservar y reportar la discrepancia | Pendiente de ratificación |
| D-03 | 7 | Reformular como barrera condicionada | Pendiente de ratificación |
| D-04 | 8 | Reformular incorporando la gestión como variable | Pendiente de ratificación |
| D-05 | 10 | Reformular eliminando la atribución de desconfianza | Pendiente de ratificación |
| D-06 | 11 | Reformular por ambigüedad y declarar el defecto | Pendiente de ratificación |
| A-01 | 3 | Ampliar con la distinción agrícola/sanitaria | Pendiente de ratificación |
| A-02 | 9 | Ampliar con el criterio de madurez por variedad | Pendiente de ratificación |

**Balance:** de los doce enunciados sometidos a verificación, **tres se mantienen sin cambios**
(4, 5 y 6), **cinco se reformulan**, **dos se amplían** y **uno se conserva reportando la
discrepancia** (enunciado 2). El enunciado 12 no requiere corrección: fue confirmado por los dos
participantes que lo abordaron.

---

## 5. Trazabilidad

Cada caso registrado en este documento debe reflejarse en:

- El apartado de **amenazas a la validez** del manuscrito, en particular D-02 y D-06.
- El **registro de cambios** del proyecto, con la versión del enunciado antes y después.
- La **matriz de trazabilidad**, cuando la corrección afecte a un requisito.
- El **registro de desviaciones** del preregistro, en lo relativo a la ejecución de la ronda en
  sub-sesiones individuales.

---

## 6. Control del documento

- **Versión:** 1.0 — borrador para ratificación
- **Fecha de elaboración:** No registrado
- **Fecha de ratificación:** Pendiente
- **Zona del repositorio:** Pública `[P]`
