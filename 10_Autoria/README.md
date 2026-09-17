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
| `retrospectiva_equipo.md` | Retrospectiva formal del cierre: problemas, causas, impactos, acciones correctivas, responsables, estado y evidencia verificable |
| `declaracion_identidades_git.md` | Declaración de identidades Git del equipo, con las correspondencias entre cuentas y personas, y la firma de cada integrante |
| `2026-09-06_DeclaracionIdentidadesGit_Enmascarado.pdf` | Copia pública de la declaración firmada, con cédula y firma manuscrita enmascaradas |
| `registro_reestructuracion_2026-09-03.md` | Resumen y commits de las correcciones realizadas durante la reestructuración del repositorio |
| `correspondencia/readme.md` | Registro y delimitación de la correspondencia escrita verificable; incluye la coordinación de entrevistas y el acta formal firmada de Palmicultora M |
| `bitacora_sesiones.csv` | Registro consolidado de 30 sesiones: 26 jornadas sin nota de campo aplicable y 4 jornadas de elicitación con notas reales asociadas |
| `capturas/` | Evidencia visual de trabajo y contribución individual conservada para la verificación de autoría |
| `notas_campo/readme.md` | Índice de las 16 notas de campo reales (`NC-01` a `NC-16`, una por entrevista ENTR-01 a ENTR-16), con su relación al resto de la evidencia de cada sesión (AUT-05) |
| `verificacion_seccion15.md` | Auditoría de cierre de §15: constancia formal, capturas, bitácora y notas de campo verificadas; sección cerrada |
| `verificacion_exif_aplicacion.md` | Verificación técnica de `DateTimeOriginal` y modelo de cámara de las cinco fotografías de la sesión complementaria del cuestionario |
| `verificacion_resultados_canonicos.md` | Cruce de resultados estadísticos canónicos contra el manuscrito final: kappa ponderado, Krippendorff, saturación y modelo ordinal |
| `exif_inventario.csv` | Inventario consolidado de metadatos EXIF de la evidencia fotográfica |

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

## Estado de cierre de la evidencia de autoría

La evidencia de autoría actualmente disponible incluye la bitácora consolidada
de sesiones, capturas individuales, notas de campo reales, correspondencia
escrita existente, declaración de identidades Git y documentación del aporte
individual.

La auditoría vigente se encuentra en `verificacion_seccion15.md`.

En esa verificación se encuentran cerradas las capturas individuales, las 30
sesiones de bitácora, las notas de campo y la constancia formal de Palmicultora
M.

El **16 de septiembre de 2026** se incorporó una copia pública enmascarada del
acta firmada por el responsable de la unidad productiva. Con esta incorporación,
**§15 queda cerrado en su totalidad**.

El acta conserva su fecha real de firma y se presenta como una constancia
emitida durante el cierre del proyecto sobre actividades previamente realizadas.
No se utiliza para reconstruir retrospectivamente evidencia inexistente.
