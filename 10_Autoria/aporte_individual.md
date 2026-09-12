# Aporte individual del equipo AHMRV

**Proyecto:** SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana  
**Asignatura:** Ingeniería de Requerimientos (ISR-401)  
**Institución:** Universidad Técnica Estatal de Quevedo (UTEQ)  
**Equipo:** AHMRV  
**Propósito:** documentar el aporte individual verificable de los seis integrantes del equipo a partir de evidencia versionada y artefactos existentes en el repositorio.

---

## 1. Criterio de elaboración

Este documento resume contribuciones individuales que pueden relacionarse con evidencia verificable del proyecto SIMPA.

La atribución se apoya principalmente en:

1. historial Git del repositorio;
2. archivos y directorios versionados;
3. correspondencias de identidad registradas en `.mailmap`;
4. declaración de identidades Git disponible en `10_Autoria/declaracion_identidades_git.md`;
5. artefactos concretos modificados por commits atribuibles a cada integrante.

El historial Git se utiliza como evidencia de trabajo versionado, pero **no se interpreta como una medición directa del esfuerzo total ni como prueba de autoría exclusiva sobre artefactos colaborativos**.

---

## 2. Integrantes e identidades Git reconocidas

| Integrante | Identidad principal | Identidades adicionales documentadas |
|---|---|---|
| Villafuerte Rosero Allan Noe | `AlanNVR <avillafuerter@uteq.edu.ec>` | `Cocolizo <avillafuerter@uteq.edu.ec>` |
| Macías Herrera Josthyn Esteban | `jmaciasherr4 <jmaciash4@uteq.edu.ec>` | `artyjmt <117947536+artyjmt@users.noreply.github.com>` |
| Arboleda Yanza Francisco Javier | `farboleday-wq <farboleday@uteq.edu.ec>` | `farboleda074-oss <farboleda074@gmail.com>` |
| Huilcapi León Denisses Fabiola | `huilcapi <dhuilcapil@uteq.edu.ec>` | `huilcapi <dhulcapil@uteq.edu.ec>`; `Fabi06-ux <fabiolahuilcapi309@gmail.com>`; variantes del nombre completo |
| Rizzo Vélez Edson Nagib | `erizzov-boop <erizzov@uteq.edu.ec>` | Sin una segunda identidad propia declarada |
| Alcívar Vélez Anderson Adonis | `AdonisAlcivar <aalcivarv4@uteq.edu.ec>` | Tres commits aparecen con nombre local `erizzov-boop` pero con el correo institucional de Anderson |

Las equivalencias anteriores se mantienen mediante `.mailmap` y documentación de autoría, sin reescribir commits históricos.

---

# 3. Villafuerte Rosero Allan Noe

## Identidad

- Cuenta principal: `AlanNVR`
- Correo institucional: `avillafuerter@uteq.edu.ec`
- Alias histórico: `Cocolizo`
- El alias utiliza el mismo correo institucional y se encuentra documentado como perteneciente a Allan.

## Áreas de aporte verificable

### 3.1 Inicio y mantenimiento del repositorio

Participación desde las primeras versiones del repositorio y carga de documentación inicial del proyecto.

Commits representativos:

- `26c2de8` — `Initial commit`
- `da05f75` — `Añadí el documento sobre el proyecto`

### 3.2 ERS y cierre documental

Participación en la corrección de auditoría de cierre y consolidación de la ERS.

- `3486021` — `Corregir auditoria de cierre P1-P4 y consolidar ERS v2.0`

### 3.3 Tercera ronda de entrevistas

Participación en la incorporación de la adenda de tercera ronda y en la codificación temática posterior.

- `9a982f3` — `Adenda del proyecto para la tercera ronda.`
- `cbcdab5` — `Codificar entrevistas de tercera ronda`

El artefacto de codificación de tercera ronda:

`07_Datos/datos_procesados/codificacion_tercera_ronda.csv`

contiene:

- 8 entrevistas, `ENTR-09` a `ENTR-16`;
- 89 fragmentos codificados;
- 31 códigos temáticos distintos;
- reutilización de códigos anteriores cuando existía correspondencia;
- analista identificado como `AVR`.

La revisión cruzada de esta codificación fue realizada por Macías Herrera Josthyn Esteban durante el cierre.

### 3.4 Datos y reproducibilidad

Participación directa en la reorganización de los datos y scripts hacia `07_Datos/`.

Commits representativos:

- `0cd8643` — mover datos crudos
- `fefbfc3` — mover datos procesados
- `afb0e8a` — mover resultados
- `510d0ed` — mover scripts de análisis
- `0ec46a6` — centralizar scripts de datos
- `1236a21` — centralizar datos crudos y análisis de saturación
- `4686757` — integrar dataset agregado reproducible
- `4aebea3` — implementar cadena reproducible de `07_Datos`
- `b2ccce6` — completar documentación base de `07_Datos`

### 3.5 Reestructuración del repositorio

Ejecución técnica de parte importante de la migración de la estructura histórica hacia la raíz actual del repositorio.

Commits representativos del 03/09/2026:

- `2624c0f` — mover `01_ERS`
- `e7c0a23` — mover `02_Evidencias`
- `fa7fbae` — mover `03_Modelado`
- `b6f1389` — mover `04_Trazabilidad`
- `d35118d` — mover `05_MVP`
- `88b2be0` — mover `06_Experimento`
- `a6720f6` — renumerar publicación
- `c19c34f` — renumerar ética
- `c271a1c` — renumerar defensa

Estos commits evidencian la ejecución de la reestructuración, no autoría exclusiva del contenido trasladado.

### 3.6 Privacidad, integridad y autoría

Commits representativos:

- `43a6cb2` — `Anonimización de nombres.`
- `9319537` — documentar zona restringida y trazabilidad
- `7d34ea3` — corregir checksums y documentar diccionario de datos
- `ee39f5d` — reconciliar manifiesto de integridad
- `abdf60d` — crear `10_Autoria` y registrar reestructuración
- `4db7483` — firmar declaración de identidad de Allan
- `7aea24f` — eliminar duplicado de respuestas anonimizadas

### 3.7 Publicación y registro del protocolo

- `25455ea` — excluir manuscrito científico de licencia CC BY
- `8bc6bde` — registrar públicamente el protocolo experimental en OSF

La referencia al registro OSF se limita a documentar la acción versionada y no implica clasificarla en este documento como prerregistro.

### 3.8 Cierre del experimento y codificación de tercera ronda (7–12 de septiembre)

- `5d8b82a` — congelar el conjunto humano de referencia de `ENTR-04`
- `c9efaa8` — congelar los requisitos generados por el LLM sobre `ENTR-04`
- `d40ebca` — congelar el material fuente `ENTR-04` para el experimento
- `cbcdab5` — codificar entrevistas de la tercera ronda
- `5337230` — integrar el análisis de saturación de las 16 entrevistas
- `01639b5` — redactar la primera versión de `aporte_individual.md`
- `1b0c17d` — actualizar evidencia de autoría del equipo
- `734a42f` — aclarar el alcance temporal del registro OSF
- `7c53724` — actualizar README y manifiesto de cierre
- `2001ace` — agregar datos al CSV de fichas técnicas

---

# 4. Macías Herrera Josthyn Esteban

## Identidad

- Cuenta principal: `jmaciasherr4`
- Correo institucional: `jmaciash4@uteq.edu.ec`
- Cuenta secundaria documentada: `artyjmt`

La cuenta `artyjmt` fue declarada por Josthyn como propia y corresponde a cinco commits históricos sobre archivos de mockups y diagramas.

## Áreas de aporte verificable

### 4.1 Prototipado y fuente de Figma Make

Participación en la preservación de la fuente del prototipo y documentación de las limitaciones del entorno utilizado.

Commits representativos:

- `ac14839` — actualizar README con información de fuente de Figma Make
- `cbb6ce5` — agregar copia local y código fuente de Figma Make

### 4.2 Verificación de consistencia de requisitos

Ejecución y documentación de una comprobación cruzada entre:

- requisitos funcionales;
- requisitos no funcionales;
- requisitos asociados a IA;
- matriz de trazabilidad E2E;
- backlog;
- manuscrito.

Commit representativo:

- `5757b1b` — script y evidencia de verificación RF/RNF/IA frente a matriz E2E, backlog y manuscrito

### 4.3 Autoría e identidades Git

Participación en el saneamiento documental de las identidades históricas del equipo.

- `9e882c1` — firma/declaración de la identidad secundaria `artyjmt`

### 4.4 Revisión cruzada de codificación cualitativa

Durante el cierre, Josthyn realizó la revisión cruzada del archivo de codificación temática de `ENTR-09` a `ENTR-16` elaborado por Allan, confirmando su conformidad antes de continuar con el análisis de saturación.

Esta revisión se registra como control colaborativo del cierre y no como autoría original de los 89 fragmentos codificados.

### 4.5 Auditoría de IA, doble codificación y diseño del experimento (7–12 de septiembre)

- `f9b5fa8` — auditoría de los seis aspectos del componente de IA (IA-01)
- `b6455aa` — congelar el subconjunto de doble codificación (39 fragmentos) y script de cálculo de acuerdo (AUT-07)
- `011283c` — codificación independiente de Josthyn sobre el subconjunto congelado (AUT-07)
- `e91287a` — corrección de formato y resultado real del acuerdo, Kappa insignificante explicado (AUT-07)
- `751f8f7` — capturas de trabajo propio, trazabilidad y scripts (AUT-02)
- `969929b` — inventario de fuentes editables de diagramas y mockups (AUT-03)
- `b41c67b`, `82ae999` — verificación de independencia del conjunto humano frente a la salida del LLM, con corrección posterior (EXP-03)
- `41618dd`, `a1c1c8e`, `8a0a787` — script de cegado y aleatorización, y documentación de la ubicación del mapa confidencial (EXP-05)
- `d954fbe` — documentar la Grabación 1 (Allan + Josthyn) como release asset (AUT-04)
- `18fe8a5` — justificación honesta del tamaño muestral, sin cálculo formal de potencia previo (B4)
- `ad44687`, `43c22fa` — secciones de tratamiento de datos y limpieza de formato en `README_Etica.md`

---

# 5. Arboleda Yanza Francisco Javier

## Identidad

- Cuenta principal: `farboleday-wq`
- Correo institucional: `farboleday@uteq.edu.ec`
- Cuenta secundaria documentada: `farboleda074-oss <farboleda074@gmail.com>`

## Áreas de aporte verificable

### 5.1 Modelado UML

Participación sostenida en artefactos de modelado, especialmente diagramas asociados a casos de uso y secuencias.

Entre los commits observables se encuentran modificaciones y regeneraciones de artefactos bajo:

`03_Modelado/Diagramas_UML/`

### 5.2 Caso de uso CU06 — clasificación de madurez

Participación concreta en el diagrama de secuencia correspondiente a la clasificación de madurez.

Commits representativos:

- `80ad1dd` — `05 secuencia CU06 clasificar madurez`
- `38c415d` — `secuencia_CU06 en ingles`

También constan operaciones de sustitución de versiones anteriores de los archivos `.puml` y `.svg` asociados al mismo diagrama.

### 5.3 Diagramas generales de casos de uso

Participación en la actualización de material gráfico de casos de uso generales.

- `c5ce28d` — `casos_de_uso_generales en ingles`

### 5.4 Mantenimiento de artefactos de modelado

El historial muestra trabajo de actualización, reemplazo y depuración de versiones de diagramas UML, por lo que su contribución documentada se concentra principalmente en el área de modelado visual y representación de comportamiento del sistema.

### 5.5 Traducción completa de diagramas UML al inglés (7–12 de septiembre)

Traducción de los 13 diagramas UML restantes de `03_Modelado/Diagramas_UML/`
(fuente `.puml` y exportaciones `.png`/`.svg`), uno por commit:

- `ae524e3` — `.gitkeep` inicial de la carpeta de trabajo
- `5819219` — `activity_weekly_cycle`
- `1720d4c` — `classes_refined`
- `01cf463` — `components`
- `82fecf8` — `context`
- `b1346d2` — `deployment`
- `6b4ac55` — `istar_sd`
- `153c5b5` — `istar_sr`
- `c5b05a0` — `sequence_CU01`
- `5e6440a` — `sequence_CU03`
- `29b8cb4` — `sequence_CU06`
- `1d09516` — `states_alert`
- `daf4d8c` — `states_bunch`
- `d7b3dce` — `use_cases_general`
- `e76330a`, `94bffd4`, `43bc339` — limpieza de capturas duplicadas en `10_Autoria/capturas/`

---

# 6. Huilcapi León Denisses Fabiola

## Identidad

- Identidad principal: `huilcapi <dhuilcapil@uteq.edu.ec>`
- Variante histórica con error tipográfico: `huilcapi <dhulcapil@uteq.edu.ec>`
- Cuenta personal documentada: `Fabi06-ux <fabiolahuilcapi309@gmail.com>`
- También aparecen variantes de su nombre completo en el historial.

## Áreas de aporte verificable

### 6.1 Metodología y amenazas a la validez

Participación en el fortalecimiento metodológico del componente cualitativo.

- `7e16365` — incorporar amenazas del componente cualitativo a la validez

Esta contribución mejora la transparencia sobre limitaciones y riesgos de interpretación del estudio.

### 6.2 Alcance del análisis y resultados

Participación en la documentación explícita del alcance de los resultados al inicio del plan de análisis.

- `aacdba8` — declarar el alcance de resultados al inicio del plan de análisis

### 6.3 Reproducibilidad y snapshot Zenodo

Participación en la documentación de las rutas históricas correspondientes al snapshot depositado.

- `61e0ecd` — registrar `D-07`, rutas históricas del snapshot Zenodo

Esta tarea ayuda a distinguir el estado histórico del paquete depositado de la estructura actual del repositorio.

### 6.4 Documentación metodológica de cierre

Sus contribuciones verificadas más recientes se concentran en:

- validez del componente cualitativo;
- alcance de resultados;
- documentación de reproducibilidad;
- relación entre el repositorio vivo y el snapshot publicado.

### 6.5 Desviación metodológica, ejecución del LLM y análisis final del experimento (7–12 de septiembre)

- `93d798d` — creación de `osf_deviations.md` (EXP-01)
- `1849a48` — versión PDF de la desviación metodológica (EXP-01)
- `003b029` — actualizar `desviaciones.md`
- `b1d6681`, `f3bdb93` — declaración de uso de IA generativa y su firma
- `3577cbc`, `9e6c6f8`, `037f995` — registro de ejecución del LLM confirmado (EXP-04)
- `d7c474a` — preparar el dataset analítico con el origen desvelado
- `7bbdd58` — calcular el acuerdo entre evaluadoras (kappa ponderado)
- `9e9a075` — analizar la comparación humano-LLM con modelo ordinal mixto
- `766a026` — actualizar estado y resultados del experimento en `06_Experimento/readme.md`
- `5e8bd80` — actualizar el manuscrito con resultados y discusión
- `23a997c` — agregar referencia OSF en `manuscrito_final.tex`
- `11ebd7d` — incorporar la retrospectiva formal del proyecto
- `9903c80` — recompilar el manuscrito y el ERS de cierre

Estas contribuciones incluyen el análisis estadístico completo de RQ1 y RQ2
del experimento. Revisión cruzada de primer nivel (código fuente y
consistencia numérica contra el manuscrito) documentada en
`06_Experimento/revision_cruzada_analisis_experimento.md`; pendiente de
confirmación por un integrante del equipo distinto de Denisses.

---

# 7. Rizzo Vélez Edson Nagib

## Identidad

- Cuenta principal: `erizzov-boop`
- Correo institucional: `erizzov@uteq.edu.ec`

La declaración de identidades establece que los commits donde aparece el nombre local `erizzov-boop` pero el correo `aalcivarv4@uteq.edu.ec` no pertenecen a Edson, sino a Anderson Alcívar. Esta distinción se mantiene en este documento.

## Áreas de aporte verificable

### 7.1 Preparación de defensa

Participación en la actualización del guion de defensa del proyecto.

- `1338f4f` — `Update guion_defensa.md`

### 7.2 Evidencias externas

Participación en la actualización de la documentación de evidencias almacenadas fuera del repositorio principal.

- `223129c` — actualizar `README_Evidencias_Externas.md`

Esta documentación es relevante debido al uso del repositorio complementario para material audiovisual y archivos restringidos.

### 7.3 Autoría e identidades

Participación en la revisión y actualización de la declaración de identidades del equipo.

- `a49e51c` — actualizar `declaracion_identidades_git.md`

### 7.4 Separación de atribución histórica

Edson participa además en la resolución documental del caso de tres commits que heredaron su nombre local de Git en otro equipo, pero que fueron ejecutados bajo el correo institucional de Anderson Alcívar.

Su declaración deja explícito que dichos commits no forman parte de su aporte individual.

### 7.5 Bitácora, evidencia de autoría y cierre del experimento humano (7–12 de septiembre)

- Reconstrucción y corrección sucesiva de `10_Autoria/bitacora_sesiones.csv`
  a partir del historial real de Git (varios commits)
- `d6222ef` — declaración de ausencia de correspondencia escrita (AUT-08)
- `b59d4ef`, `48d22f9` — declaración de ausencia de notas de campo físicas (AUT-05)
- `83fe193`, `f6472c9`, `039b80a` — incorporación de las fotografías reales del equipo (AUT-06)
- `f5224a3`, `2449907` — creación de `exif_inventario.csv` y su documentación (AUT-11)
- `fc393be`, `ef3939d`, `520524a` — instrucciones de cegado y registro de evaluadores (EXP-06)
- `3b7a319`, `c56ac39`, `6c1b597` — incorporación de las tres hojas de puntuación completas (EXP-06)
- `f27ecdd`, `18fe301` — consolidado de puntuaciones reales en formato largo (EXP-07)
- `fe2315d` — actualización del `CHANGELOG.md` con el cierre de septiembre
- Correcciones repetidas de nomenclatura de `readme.md` para asegurar el
  renderizado automático en GitHub

Es, en volumen de commits, la mayor contribución individual del cierre de
septiembre (49 commits en este tramo), concentrada en documentación de
autoría y en la operación del experimento humano-LLM.

---

# 8. Alcívar Vélez Anderson Adonis

## Identidad

- Cuenta principal: `AdonisAlcivar`
- Correo institucional: `aalcivarv4@uteq.edu.ec`

Tres commits del 04/09/2026 aparecen con el nombre local `erizzov-boop` pero con el correo institucional de Anderson. La declaración firmada del equipo los atribuye a Anderson y `.mailmap` corrige su visualización sin modificar el historial.

## Áreas de aporte verificable

### 8.1 Inventario de evidencias restringidas

Participación en la actualización y verificación de `fichas_tecnicas.csv`, utilizada para inventariar los contenedores cifrados y evidencias externas.

Commit representativo:

- `baf348a` — actualizar `fichas_tecnicas.csv` a los contenedores publicados

El mensaje de commit documenta:

- incorporación de contenedores de actas originales;
- incorporación de walkthrough y member-checking;
- corrección del contenedor de consentimientos de walkthrough;
- verificación de 69 filas y 11 contenedores.

### 8.2 Regeneración de inventarios y transcripciones

La declaración de identidades del equipo atribuye a Anderson los commits:

- `98ad2ba`
- `baf348a`
- `253cc53`

Estos corresponden a tareas relacionadas con:

- regeneración del inventario `fichas_tecnicas.csv`;
- reporte de verificación;
- reposición del consolidado de transcripciones.

### 8.3 Saneamiento de identidad Git

Participación directa en la normalización de su identidad.

- `3d38b5f` — agregar `AdonisAlcivar` a `.mailmap`
- `13e1d23` — actualizar las entradas de identidad en `declaracion_identidades_git.md`

### 8.4 Integridad de evidencias

Su aporte verificable se concentra particularmente en el inventario, control y correspondencia de evidencia restringida y transcripciones con los contenedores externos publicados.

### 8.5 Nota sobre el período del 7 al 12 de septiembre

**No se encontró ningún commit con la identidad de Anderson (`AdonisAlcivar`
ni el correo `aalcivarv4@uteq.edu.ec`) en este período.** El equipo aclara
que esto no corresponde a trabajo no versionado ni a coordinación verbal
pendiente de documentar: **Anderson Alcívar dejó de colaborar con el
proyecto** durante este tramo. Su aporte verificable queda circunscrito al
documentado en las secciones 8.1 a 8.4, correspondiente al período en que
sí participó activamente.

Las tareas que el plan de cierre le había asignado como apoyo (`AUT-06`,
`EXP-02`, `EXP-06`) y como custodio de datos crudos (`EXP-07`) fueron
cubiertas por el resto del equipo; queda pendiente que el propio documento
de reparto de tareas se actualice para reflejar esta reasignación, fuera
del alcance de este archivo.

---

# 9. Trabajo colaborativo del equipo

El proyecto SIMPA fue desarrollado de forma colaborativa. La separación anterior busca mostrar evidencia atribuible a cada integrante, pero varios artefactos fueron construidos, revisados o corregidos por más de una persona.

En particular, se consideran de naturaleza colaborativa:

- ERS/SRS consolidada;
- matriz de trazabilidad;
- backlog;
- manuscrito;
- evidencias de entrevistas;
- material de defensa;
- prototipo;
- documentación de cierre;
- revisión de consistencia entre artefactos.

Por ello, un commit individual sobre uno de estos archivos demuestra intervención versionada, pero no autoría exclusiva de todo su contenido.

---

# 10. Verificación reproducible

## 10.1 Identidades normalizadas

Desde un clon del repositorio:

```bash
git shortlog -sne --all
```

El resultado esperado, con `.mailmap`, es una identidad canónica por cada uno de los seis integrantes.

## 10.2 Inspeccionar contribuciones por correo

### Allan

```bash
git log --all --author="avillafuerter@uteq.edu.ec" --oneline
```

### Josthyn

```bash
git log --all --author="jmaciash4@uteq.edu.ec" --oneline
```

### Francisco

```bash
git log --all --author="farboleday@uteq.edu.ec" --oneline
```

### Denisses

```bash
git log --all --author="dhuilcapil@uteq.edu.ec" --oneline
```

Para revisar la variante histórica:

```bash
git log --all --author="dhulcapil@uteq.edu.ec" --oneline
```

### Edson

```bash
git log --all --author="erizzov@uteq.edu.ec" --oneline
```

### Anderson

```bash
git log --all --author="aalcivarv4@uteq.edu.ec" --oneline
```

## 10.3 Verificar equivalencias de identidad

Ejemplos:

```bash
git check-mailmap "Cocolizo <avillafuerter@uteq.edu.ec>"
git check-mailmap "erizzov-boop <aalcivarv4@uteq.edu.ec>"
```

## 10.4 Inspeccionar commits representativos

```bash
git show --stat cbcdab5
git show --stat 5757b1b
git show --stat 38c415d
git show --stat 7e16365
git show --stat 1338f4f
git show --stat baf348a
```

---

# 11. Límites de la evidencia

Este documento no utiliza el número de commits como porcentaje de participación.

Se adoptan las siguientes precauciones:

- no se reconstruyen retroactivamente actividades que no dejaron evidencia;
- no se atribuye a una persona todo el contenido de un archivo solo porque realizó el último commit;
- los movimientos o renombrados de archivos evidencian mantenimiento técnico, no creación original de todo el contenido trasladado;
- las identidades históricas se interpretan únicamente conforme a la declaración del equipo y `.mailmap`;
- el trabajo presencial, coordinación, revisión oral y otras tareas no versionadas pueden no estar representadas en Git;
- las contribuciones aquí listadas son representativas y verificables, no necesariamente exhaustivas.

---

# 12. Declaración del equipo

Los integrantes del equipo AHMRV reconocen que SIMPA es un proyecto colaborativo.

El presente documento tiene como finalidad dejar una referencia verificable del trabajo individual observado en el historial y los artefactos del repositorio, manteniendo separada la evidencia de contribución de cualquier afirmación de autoría exclusiva.

Las correspondencias de identidad se respaldan mediante:

- `.mailmap`;
- `10_Autoria/declaracion_identidades_git.md`;
- `10_Autoria/2026-09-06_DeclaracionIdentidadesGit_Enmascarado.pdf`.

La verificación definitiva puede realizarse directamente sobre el historial Git del repositorio.

---

# 13. Firmas

Cada integrante firma en conformidad con el contenido de su propia
sección (3 a 8), confirmando que las contribuciones ahí listadas son
correctas y que no reclama como propio el trabajo colaborativo descrito en
la sección 9.

| Integrante | Firma | Fecha |
|---|---|---|
| Villafuerte Rosero Allan Noe | | |
| Macías Herrera Josthyn Esteban |josthynmacias |2026-09-12|
| Arboleda Yanza Francisco Javier | | |
| Huilcapi León Denisses Fabiola | | |
| Rizzo Vélez Edson Nagib | RizzoNagib|2026-09-12|
| Alcívar Vélez Anderson Adonis | | |

**Sobre la firma de Anderson Alcívar.** Aunque dejó de colaborar con el
proyecto (sección 8.5), su firma sigue siendo pertinente: el documento
declara aporte suyo real y verificable (secciones 8.1 a 8.4) y su firma
confirma únicamente la exactitud de esa parte, no una reincorporación al
equipo ni conformidad con el resto del documento.

