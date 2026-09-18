# Retrospectiva formal del proyecto SIMPA

**Proyecto:** Sistema Inteligente de Mantenimiento de Palma Africana (SIMPA)
**Equipo:** AHMRV — ISR-401 — UTEQ
**Período:** 2026–2027 PPA
**Fecha de consolidación:** 18 de septiembre de 2026

## Propósito

Esta retrospectiva documenta problemas reales detectados durante el cierre del proyecto, sus causas e impactos, las acciones correctivas aplicadas y la evidencia versionada que permite verificarlas.

No se reconstruyen actividades inexistentes ni se incorporan evidencias retrospectivas que no puedan comprobarse mediante artefactos, commits o documentos del repositorio.

## Registro de retrospectiva

| Problema detectado | Causa | Impacto | Acción correctiva aplicada | Responsable(s) | Estado | Evidencia verificable |
|---|---|---|---|---|---|---|
| La codificación temática y el análisis de saturación cubrían inicialmente solo las primeras ocho entrevistas, aunque la tercera ronda amplió el corpus a 16. | La tercera ronda fue realizada después de la construcción inicial de la cadena de análisis y sus nuevos datos todavía no habían sido integrados al cálculo de saturación. | La curva existente no representaba el corpus completo y no permitía analizar por separado el estrato de dominio y el estrato de contraste comprometidos metodológicamente. | Se codificaron ENTR-09 a ENTR-16, se integraron ambas rondas en la cadena reproducible y se generaron curvas separadas de dominio, contraste y vista agregada, además de una tabla de saturación de 16 entrevistas. | Villafuerte Rosero Allan Noe; revisión cruzada de la codificación por Macías Herrera Josthyn Esteban. | Cerrado | Commits `cbcdab5` — `Codificar entrevistas de tercera ronda` y `5337230` — `feat: integrar analisis de saturacion de 16 entrevistas`; `07_Datos/datos_procesados/codificacion_tercera_ronda.csv`; `07_Datos/resultados/tabla_saturacion.csv`. |
| Las decisiones derivadas del member-checking permanecieron inicialmente como propuestas pendientes de ratificación y sin responsable definitivo. | El documento fue elaborado primero como registro de hallazgos y requería una decisión posterior del equipo antes de convertir las propuestas en acciones formales. | No era posible propagar legítimamente las correcciones al manuscrito ni declarar cerradas las discrepancias mientras continuaran en estado provisional. | El equipo ratificó las ocho decisiones, asignó responsables y posteriormente incorporó al manuscrito los casos D-02 y D-06 como amenazas del componente cualitativo. | Rizzo Vélez Edson Nagib en la coordinación de ratificación; Huilcapi León Denisses Fabiola en la incorporación al manuscrito. | Cerrado | Commit `6ff131d` — `ratificar las ocho decisiones de member-checking`; commit `7e16365` — `docs: incorporar amenazas del componente cualitativo a la validez`; `02_Evidencias/Member_Checking/correcciones_aplicadas.md`; `08_Publicacion/manuscrito_final.tex`. |
| El historial de Git contenía identidades fragmentadas y tres commits con el nombre local de un integrante y el correo institucional de otro. | En un equipo utilizado durante una sesión previa quedó heredada una configuración local de `user.name`; posteriormente se cambió la cuenta utilizada para publicar, pero no se corrigió esa configuración antes de confirmar nuevos cambios. | El historial podía atribuir incorrectamente contribuciones y afectar la evaluación individual del equipo. | Se documentaron las identidades reales, se aclaró el caso cruzado, se normalizó la visualización mediante `.mailmap` y se preservó el historial sin reescribir commits compartidos. | Alcívar Vélez Anderson Adonis y Rizzo Vélez Edson Nagib; consolidación documental del equipo. | Cerrado | Commit `bc8ad0a` — `aclarar la identidad cruzada`; `10_Autoria/declaracion_identidades_git.md`; `.mailmap`; copia pública firmada `10_Autoria/2026-09-06_DeclaracionIdentidadesGit_Enmascarado.pdf`. |
| El proyecto no disponía de un documento único que consolidara el aporte individual verificable de los seis integrantes. | La evidencia de contribución se encontraba distribuida entre el historial Git, artefactos, actas y distintas identidades normalizadas. | La evaluación individual requería reconstruir manualmente la participación y podía confundirse cantidad de commits con autoría o porcentaje de contribución. | Se creó un documento consolidado que describe el aporte verificable de cada integrante y relaciona sus contribuciones con commits, artefactos e identidades documentadas. | Villafuerte Rosero Allan Noe, con apoyo de Alcívar Vélez Anderson Adonis. | Cerrado | Commit `01639b5` — `docs: documentar aporte individual del equipo AHMRV`; `10_Autoria/aporte_individual.md`; actualización posterior de `10_Autoria/README.md` en `1b0c17d`. |
| La instantánea depositada en Zenodo conservaba rutas y un estado de predepósito anteriores a la reestructuración del repositorio. | El paquete de Zenodo fue congelado antes de que la estructura `AHMRV/.../07_Publicacion` migrara a las rutas actuales del repositorio. Modificar el snapshot habría roto su correspondencia con los hashes del depósito. | Las rutas históricas podían parecer referencias rotas o dar la impresión de que el DOI continuaba pendiente, aunque el depósito ya había sido publicado. | Se preservó intacto el snapshot y se documentó externamente la correspondencia entre rutas antiguas y actuales, además del estado vigente del depósito. | Huilcapi León Denisses Fabiola. | Cerrado | Commit `84adf94` — `docs: documentar correspondencia de rutas y estado del snapshot Zenodo`; `08_Publicacion/readme.md`; snapshot congelado `08_Publicacion/dataset_zenodo/`. |
| La documentación del registro OSF podía interpretarse como si el protocolo hubiese sido prerregistrado antes de todo el trabajo de campo, aunque el material fuente de entrevistas ya existía. | Se utilizó inicialmente una formulación amplia sobre prerregistro que no distinguía entre la recolección previa del material fuente y la ejecución futura del experimento humano–LLM. | La cronología podía ser interpretada incorrectamente y generar una afirmación metodológica más fuerte de la que sostenía el historial del proyecto. | Se aclaró que el registro es retrospectivo respecto a la recolección del material fuente, pero anterior a la ejecución del experimento comparativo humano–LLM; no se presenta como prerregistro de las entrevistas ni del proyecto completo. | Villafuerte Rosero Allan Noe. | Cerrado | Commit `734a42f` — `docs: aclarar alcance temporal del registro OSF`; `06_Experimento/protocolo.tex`; `06_Experimento/readme.md`. |
| La aplicación anónima del cuestionario y del formulario de consentimiento complementario no generó, en su momento, un registro de consentimiento informado individual y verificable, ni fotografías presenciales de la aplicación. | Se interpretó el anonimato del cuestionario como ausencia total de necesidad de un registro de consentimiento independiente, sin separar consentimiento y encuesta; tampoco se documentó fotográficamente la sesión de aplicación original. | No existía un registro independiente de aceptación de los participantes ni la evidencia fotográfica exigida, y la exportación cruda de las 62 respuestas conservaba columnas de identidad (correo electrónico y nombre) generadas automáticamente por Google Forms sin que esto estuviera declarado. | Por indicación del docente responsable (aclaración del 14/09/2026), se creó un formulario de consentimiento informado independiente (Microsoft Forms), aplicado a 5 trabajadores localizables en una sesión complementaria real el 15/09/2026, con fotografías originales verificadas por EXIF; se registró la evidencia técnica bajo la serie `CUEST-01` a `CUEST-05`; se documentó la procedencia, el anonimato, la captura automática de identidad y la limitación del consentimiento original de las 62 respuestas; y se actualizó el manuscrito en consecuencia. Los nuevos consentimientos no se vinculan con ninguna respuesta específica de las 62 respuestas originales del cuestionario. | Huilcapi León Denisses Fabiola. | Cerrado | Commit `c011dc3` — `docs: documentar consentimiento informado complementario`; commit `cc54d89` — `docs: agregar readme faltante de consentimiento informado complementario`; `02_Evidencias/Cuestionario/Consentimiento_Complementario/`; commit `8f7aea2` y commit `3747fb8` — registro en `02_Evidencias/00_Restringido/fichas_tecnicas.csv` y `checksums_evidencias.sha256`; commit `3dedb75` — actualización de `README.md`; commit `76860d2` — `02_Evidencias/Cuestionario/Respuestas/readme.md`; commit `605b46c` — `08_Publicacion/manuscrito_final.tex`. |

## Lecciones obtenidas

1. Los artefactos derivados deben regenerarse cuando cambia el conjunto de datos que los alimenta.
2. Las decisiones metodológicas provisionales no deben propagarse como definitivas hasta que exista una ratificación verificable.
3. La identidad Git debe comprobarse antes de cada jornada de trabajo, especialmente en equipos compartidos.
4. La evidencia de aporte individual debe consolidarse durante el proyecto y no únicamente al final.
5. Los depósitos científicos congelados deben conservarse intactos; los cambios estructurales posteriores se documentan mediante tablas de correspondencia externas.
6. La terminología de prerregistro debe expresar con precisión qué actividad ocurrió antes y cuál después del registro.

## Estado final

Las siete situaciones anteriores cuentan con una acción correctiva aplicada y con evidencia verificable en el repositorio.

La retrospectiva no implica que todo posible trabajo futuro del proyecto esté cerrado; documenta únicamente los problemas de cierre aquí enumerados y las medidas que efectivamente fueron ejecutadas.


## Cierre del examen suspenso — síntesis final

**Fecha de esta síntesis:** 16 de septiembre de 2026

Esta sección resume las correcciones realizadas en respuesta a la revisión
del docente del 15 de septiembre de 2026, posteriores a las entradas
individuales registradas arriba.

**Qué se corrigió y quién:**

- Villafuerte Rosero Allan Noé: documentó los tres marcadores de evidencia
  vacíos (Member_Checking/Actas, Validacion_Walkthrough/Acta y
  Consentimientos), registró la entrada del CHANGELOG del examen suspenso,
  incorporó el acta firmada enmascarada de Palmicultora M, y actualizó
  README y CITATION.cff tras la transferencia del repositorio a
  `gleiston-guerrero/SIMPA_ISR401`.
- Huilcapi León Denisses Fabiola: formulario de consentimiento
  complementario del cuestionario, documentación de procedencia y
  limitaciones de las 62 respuestas, las secciones de saturación
  temática, kappa ponderado y amenaza de consentimiento retrospectivo en
  el manuscrito, y el renombrado de las cinco fotografías de la sesión
  complementaria en `ac5820c` (17/09 12:53).
- Macías Herrera Josthyn Esteban: auditoría de fichas técnicas y EXIF,
  auditoría de cierre de §15 (correspondencia, capturas y bitácora),
  verificación de que los resultados del manuscrito coinciden con los
  archivos canónicos de `07_Datos/resultados`, e incorporación original
  de las cinco fotografías reales de la sesión complementaria
  (`e4bab0c`, `71e67c0`, `1a20cbe`, `57a3086`, `24a81c2`).
- Arboleda Yanza Francisco Javier: sus tres capturas propias de autoría,
  regeneración de manifiestos de integridad y corrección de rutas y
  órdenes de verificación.

**Qué aprendió el equipo:**

Varios de estos hallazgos (marcadores vacíos, discrepancia entre lo
declarado como anónimo y lo efectivamente capturado por los formularios,
notas de campo mal comparadas contra la bitácora) no eran evidentes
revisando el repositorio de forma superficial; solo aparecieron al correr
las mismas verificaciones exactas que usa el docente. El equipo confirma
que "parece completo" y "está verificado con el mismo método de auditoría
del docente" no son equivalentes.

**Qué controles se aplicarán para no repetirlas:**

- Ningún archivo de evidencia se deja como marcador vacío; se documenta el
  contenido o se retira la carpeta en el mismo commit que la crea.
- Toda limitación metodológica se declara explícitamente en el momento en
  que se detecta, en vez de esperar a una auditoría externa.
- Antes de declarar cerrado cualquier punto de la rúbrica, se ejecuta el
  comando de verificación exacto que especifica el docente para ese
  punto, no una revisión visual.


---

## Segunda ronda de cierre — 18 de septiembre de 2026

**Fecha de esta sección:** 18 de septiembre de 2026

Esta sección documenta las correcciones posteriores a la evaluación oficial
del 17/09/2026 a las 17:50. Las atribuciones que siguen fueron contrastadas
contra el historial Git mediante `git log --follow` y `git for-each-ref`
antes de este cierre documental.

### Trabajo y atribuciones verificadas

| Corrección o evidencia | Responsable verificado | Evidencia |
|---|---|---|
| Intervalos de confianza al 95 % de Krippendorff y kappa ponderado, figuras de saturación por estrato y recompilación del manuscrito | Huilcapi León Denisses Fabiola | Manuscrito compilado el 17/09 después de la última regeneración de resultados |
| Renombrado de las cinco fotografías de la sesión complementaria | Huilcapi León Denisses Fabiola | `ac5820c`, 17/09 12:53 |
| Incorporación original de las cinco fotografías reales de la sesión complementaria | Macías Herrera Josthyn Esteban | `e4bab0c`, `71e67c0`, `1a20cbe`, `57a3086`, `24a81c2`, 15/09 |
| Regeneración de manifiestos y corrección de rutas y órdenes de verificación | Arboleda Yanza Francisco Javier | Historial de cierre y manifiestos versionados |
| Renombrado de la retrospectiva al nombre exigido por la guía | Arboleda Yanza Francisco Javier | `6026853`, 17/09 |
| Etiquetas anotadas `baseline-v6.0`, `baseline-v6.1` y `baseline-v6.2` | Macías Herrera Josthyn Esteban | Etiquetas creadas el 17/09 a las 16:15, 16:19 y 16:30 |
| Etiqueta anotada `baseline-v6.3` | Huilcapi León Denisses Fabiola | Etiqueta creada el 17/09 a las 17:17 sobre `1424f05` |
| Depósito de la tercera captura propia de autoría de Alcívar | Alcívar Vélez Anderson Adonis | `32a8e7f`, 17/09 18:13; equipo `Usuario@DESKTOP-4PFJJQ5` |
| Retirada de la captura tomada en equipo ajeno | Macías Herrera Josthyn Esteban | `5a787f2`, 17/09 18:14 |
| Renombrado posterior de la captura válida y corrección final de su nombre para evitar colisión histórica | Alcívar Vélez Anderson Adonis (`d0b32f2`) y Huilcapi León Denisses Fabiola (renombrado final del 18/09) | `d0b32f2` y renombrado final a `..._gitlog_verificar_fichas.png` |

### Problemas detectados en esta ronda

| Problema | Causa | Impacto | Acción correctiva incorporada | Responsable | Estado |
|---|---|---|---|---|---|
| Una de las tres capturas de autoría de Alcívar se tomó en el equipo de Macías Herrera y se depositó como evidencia propia. | Se documentó el trabajo de un integrante desde el equipo de otro sin advertir que el ítem exigía evidencia propia. | La evidencia acreditaba revisión por un tercero, no una captura propia del integrante; §15 permaneció en `Por modificar` en la evaluación del 17/09. | Alcívar depositó desde su equipo una captura del historial de un archivo escrito por él; la captura ajena se retiró y la evidencia válida quedó con un nombre distinto al archivo cuestionado. | Alcívar Vélez Anderson Adonis; retirada por Macías Herrera Josthyn Esteban. | Corrección incorporada; pendiente validación del docente |
| La síntesis del 16/09 atribuía a Arboleda Yanza las cinco fotografías de la sesión complementaria. | La atribución se redactó sin contrastarla con el historial antes de consolidar el documento. | La retrospectiva declaraba una autoría que el historial Git desmentía. | Se corrigió la atribución: Macías Herrera incorporó las cinco fotografías y Huilcapi León realizó su renombrado posterior; Arboleda conserva únicamente las contribuciones que el historial y la evaluación le atribuyen. | Equipo de cierre. | Corrección incorporada; pendiente validación del docente |
| Se crearon cuatro líneas base durante la misma jornada (`baseline-v6.0` a `baseline-v6.3`). | Se etiquetó después de varios ajustes documentales sucesivos en lugar de esperar al cierre completamente verificado. | La secuencia dificulta distinguir una instantánea intermedia de una línea base realmente cerrada. | Las etiquetas históricas se preservan intactas y se documenta su autoría real. La siguiente línea base solo se creará después de verificar el estado final desde clon limpio. | Equipo de cierre. | Control incorporado |
| El manifiesto raíz quedó desfasado después de sustituir y renombrar la captura de autoría. | Los cambios posteriores a `baseline-v6.3` modificaron la ruta y posteriormente los bytes asociados a la evidencia sin regenerar `checksums.sha256`. | El manifiesto que verificaba correctamente en `baseline-v6.3` dejó de corresponder con `main` después de esos commits. | Se estableció como regla regenerar `checksums.sha256` únicamente después de terminar todas las ediciones del cierre y comprobarlo antes de crear la nueva línea base. | Equipo de cierre. | Cerrado — el manifiesto raíz se regenera como último cambio de esta ronda |

### Lecciones añadidas

7. Una captura de autoría solo acredita adecuadamente esa evidencia cuando corresponde al propio integrante y su procedencia puede verificarse; documentar el trabajo desde el equipo de un compañero acredita revisión, no sustituye la evidencia propia.
8. Toda atribución nominal debe contrastarse contra el historial Git antes de consolidarse, no contra el reparto de tareas planificado.
9. La autoría de etiquetas anotadas se comprueba con `git for-each-ref`, no se infiere por rol dentro del equipo.
10. El manifiesto raíz se regenera como último cambio antes del commit de cierre; cualquier modificación posterior vuelve a invalidarlo.
11. Una línea base se crea después de que el estado a congelar haya superado la verificación de cierre, no después de cada ajuste documental.
12. Un archivo de evidencia retirado no debe reutilizarse como nombre de su sustituto cuando eso vuelve ambigua la trazabilidad histórica.

### Corrección posterior dentro de la misma ronda

Tras consolidar esta ronda se detectó que `10_Autoria/verificacion_seccion15.md`
y `10_Autoria/README.md` conservaban dos afirmaciones —anteriores a la
evaluación oficial— que declaraban §15 cerrado por cuenta del equipo, en
contradicción con el propio apéndice de este cierre, que remite al docente la
determinación del estado del ítem. Ambas se reformularon para acotarlas a la
verificación interna del 16/09, sin borrar la conclusión histórica ni alterar
su fecha. El manifiesto raíz se regeneró tras esa edición.

| Corrección | Responsable verificado | Evidencia |
|---|---|---|
| Contextualización de las dos afirmaciones de cierre de §15 y regeneración del manifiesto | Huilcapi León Denisses Fabiola | `1550947`, 18/09 09:18 |

**Lección 13.** Un documento de auditoría no declara cerrado el ítem que audita:
describe lo verificado y deja la calificación al evaluador.

### Estado de esta segunda ronda

Las correcciones documentales descritas se incorporan para atender las
observaciones de §15 y §16 formuladas en la evaluación del 17/09/2026.
La determinación del estado final de esos ítems y cualquier calificación
corresponden al docente.

La verificación de integridad del árbol y la creación de una nueva línea
base se realizan después de terminar las ediciones documentales; esta
retrospectiva no las sustituye.

Esta sección se consolida en el commit de congelación documental que la
incorpora, junto con la ampliación correspondiente del CHANGELOG y la
regeneración del manifiesto raíz. Ese commit no introduce cambios de contenido
adicionales a los aquí descritos; su identificador se publica en el mensaje de
la etiqueta anotada `baseline-v6.4`, porque un commit no puede contener su
propio hash. La ronda de cierre termina ahí.
