# 10_Autoria

Esta carpeta centraliza la evidencia de autoría y trabajo propio del proyecto
SIMPA conforme a la guía de entrega.

## Estado

Únicamente se registra trabajo real y evidencia verificable del proyecto.
Los elementos de autoría que todavía requieran evidencia adicional se
incorporarán conforme existan, sin reconstruir retroactivamente actividades
que no hayan dejado registro.

**No se crean evidencias ficticias ni se declaran como cumplidos elementos que
todavía no hayan sido verificados.**

## Contenido

| Archivo | Qué es |
|---|---|
| `aporte_individual.md` | Declaración consolidada del aporte individual verificable de los seis integrantes del equipo AHMRV, sustentada en historial Git, artefactos versionados e identidades documentadas |
| `retrospectiva.md` | Retrospectiva formal del cierre: problemas, causas, impactos, acciones correctivas, responsables, estado y evidencia verificable |
| `declaracion_identidades_git.md` | Declaración de identidades Git del equipo, con las correspondencias entre cuentas y personas, y la firma de cada integrante |
| `2026-09-06_DeclaracionIdentidadesGit_Enmascarado.pdf` | Copia pública de la declaración firmada, con cédula y firma manuscrita enmascaradas |
| `registro_reestructuracion_2026-09-03.md` | Resumen y commits de las correcciones realizadas durante la reestructuración del repositorio |

## Aporte individual

`aporte_individual.md` documenta por separado el aporte verificable de:

- Villafuerte Rosero Allan Noe;
- Macías Herrera Josthyn Esteban;
- Arboleda Yanza Francisco Javier;
- Huilcapi León Denisses Fabiola;
- Rizzo Vélez Edson Nagib;
- Alcívar Vélez Anderson Adonis.

La atribución utiliza el historial Git, `.mailmap`, la declaración de
identidades y los artefactos existentes en el repositorio.

El número de commits no se interpreta como porcentaje de participación ni como
autoría exclusiva de los documentos colaborativos.

## Declaración de identidades Git

`declaracion_identidades_git.md` documenta, con firma de cada integrante
afectado, la correspondencia entre las distintas identidades Git utilizadas
durante el desarrollo y la persona real que hay detrás de cada una.

Respalda el archivo `.mailmap` del repositorio y resuelve el hallazgo de
identidades fragmentadas sin modificar los commits históricos ya publicados.

### Integridad del historial

La normalización de identidades se realiza mediante `.mailmap`; no se utilizó
`filter-branch`, `filter-repo` ni `push --force` para alterar el historial
compartido.

Durante el trabajo de cierre sí se utilizó `git pull --rebase` de forma local
para integrar commits remotos antes de publicar cambios propios. Este uso
reordenó únicamente commits locales todavía no publicados y no reescribió el
historial remoto ni eliminó contribuciones de otros integrantes.

## Versiones de la declaración de identidades

| Versión | Ubicación | Contiene |
|---|---|---|
| Pública, enmascarada | Esta carpeta | Firma y cédula tapadas; el resto del contenido íntegro |
| Original, sin enmascarar | Cifrada en el repositorio complementario | Firma y cédula visibles |

El original se deposita en `erizzov-boop/SIMPA_ISR401_Evidencias`, contenedor
`Declaracion_Identidades_git_original.7z`, con su fila propia en
`../02_Evidencias/00_Restringido/fichas_tecnicas.csv` bajo el código
`CONSOLIDADA-EQUIPO`.

No lleva código `ENTR-XX` ni `WT-XX` porque no es un documento de un
participante individual, sino una declaración conjunta de los seis integrantes
del equipo.

## Verificación

### Identidades normalizadas

```bash
git shortlog -sne --all
```

El resultado esperado es una identidad canónica por cada integrante del equipo
AHMRV, conforme a las correspondencias registradas en `.mailmap`.

### Aporte individual

Las contribuciones pueden inspeccionarse mediante el correo institucional de
cada integrante. Por ejemplo:

```bash
git log --all --author="avillafuerter@uteq.edu.ec" --oneline
git log --all --author="jmaciash4@uteq.edu.ec" --oneline
git log --all --author="farboleday@uteq.edu.ec" --oneline
git log --all --author="dhuilcapil@uteq.edu.ec" --oneline
git log --all --author="erizzov@uteq.edu.ec" --oneline
git log --all --author="aalcivarv4@uteq.edu.ec" --oneline
```

Para una explicación de las identidades alternativas y casos históricos debe
consultarse `declaracion_identidades_git.md`.

## Evidencia todavía no incorporada

La existencia de esta carpeta no implica que todos los posibles tipos de
evidencia de autoría estén disponibles.

Si existen bitácoras de sesiones, capturas, grabaciones o notas de campo
producidas durante el desarrollo, podrán incorporarse únicamente cuando puedan
identificarse y verificarse de forma legítima.

No se recrearán retroactivamente estas evidencias a partir del historial de Git
para simular que fueron producidas en su momento.
