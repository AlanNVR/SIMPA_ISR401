# Declaración de identidades Git del equipo AHMRV

**Proyecto:** SIMPA — ISR-401 — UTEQ — 2026-2027 PPA
**Fecha:** [FECHA DE FIRMA]
**Propósito:** Documentar, con firma de cada integrante afectado, la correspondencia
entre las distintas identidades Git usadas durante el desarrollo y la persona real
que hay detrás de cada una. Este documento respalda el archivo `.mailmap` del
repositorio y resuelve el hallazgo de identidades fragmentadas (P4, criterio de piso).

---

## Tabla de correspondencia

| Identidad Git tal como aparece en el historial | Persona real | Naturaleza |
|---|---|---|
| `AlanNVR <avillafuerter@uteq.edu.ec>` | Villafuerte Rosero Allan Noe | Cuenta principal |
| `Cocolizo <avillafuerter@uteq.edu.ec>` | Villafuerte Rosero Allan Noe | Mismo correo exacto — mismo usuario en otro dispositivo/configuración |
| `jmaciasherr4 <jmaciash4@uteq.edu.ec>` | Macías Herrera Josthyn Esteban | Cuenta principal |
| `artyjmt <117947536+artyjmt@users.noreply.github.com>` | Macías Herrera Josthyn Esteban | Cuenta personal secundaria, usada el 28/06/2026 para 5 commits sobre `AHMRV/modelos/mockups/diagrama_*.drawio` |
| `farboleday-wq <farboleday@uteq.edu.ec>` | Arboleda Yanza Francisco Javier | Cuenta principal |
| `farboleda074-oss <farboleda074@gmail.com>` | Arboleda Yanza Francisco Javier | Cuenta personal secundaria |
| `huilcapi <dhuilcapil@uteq.edu.ec>` | Huilcapi León Denisses Fabiola | Cuenta principal (correo institucional correcto) |
| `huilcapi <dhulcapil@uteq.edu.ec>` | Huilcapi León Denisses Fabiola | Mismo correo institucional, con error tipográfico (falta la segunda "i") |
| `Fabi06-ux <fabiolahuilcapi309@gmail.com>` | Huilcapi León Denisses Fabiola | Cuenta personal secundaria |
| `Huilcapi León Denisses Fabiola <dhuilcapil@uteq.edu.ec>` / `Denisses Fabiola Huilcapi León <dhuilcapil@uteq.edu.ec>` | Huilcapi León Denisses Fabiola | Mismo correo, nombre completo escrito en distinto orden en distintos commits |
| `erizzov-boop <erizzov@uteq.edu.ec>` | Rizzo Vélez Edson Nagib | Cuenta principal y única. Su nombre de usuario aparece además en 3 commits con correo ajeno que **no le pertenecen** — ver fila siguiente |
| `AdonisAlcivar <aalcivarv4@uteq.edu.ec>` | Alcívar Vélez Anderson Adonis | Cuenta principal |
| `erizzov-boop <aalcivarv4@uteq.edu.ec>` | Alcívar Vélez Anderson Adonis | Correo institucional propio con nombre de usuario ajeno, heredado de la configuración local de Git del equipo utilizado. 3 commits del 04/09/2026 |

Todas las correspondencias anteriores están reflejadas en el archivo `.mailmap`
de la raíz del repositorio, que unifica el conteo de contribuciones sin alterar
ningún commit existente.

---

## Declaraciones individuales

Cada integrante con más de una identidad declara y firma lo siguiente:

**Villafuerte Rosero Allan Noe** — Confirmo que `Cocolizo <avillafuerter@uteq.edu.ec>`
corresponde a commits realizados por mí, bajo el mismo correo institucional, en un
entorno de trabajo donde el nombre de usuario de Git local no estaba configurado
con mi nombre de cuenta principal.

Firma: _____________________  C.I.: _____________________  Fecha: __________

**Macías Herrera Josthyn Esteban** — Confirmo que la cuenta de GitHub `artyjmt`
(ID 117947536, correo `117947536+artyjmt@users.noreply.github.com`) es de mi
propiedad y uso personal. Los 5 commits firmados por esa cuenta el 28/06/2026
sobre `AHMRV/modelos/mockups/diagrama_*.drawio` (tres eliminaciones y dos
incorporaciones de archivos) los realicé yo, subiendo los cambios directamente
desde la interfaz web de GitHub en lugar de mi entorno local configurado con
`jmaciasherr4`.

Firma: josthynmacias  C.I.: 1206991026  Fecha: 7/09/2026

**Arboleda Yanza Francisco Javier** — Confirmo que `farboleda074-oss
<farboleda074@gmail.com>` corresponde a commits realizados por mí desde una
cuenta personal, en paralelo a mi cuenta institucional `farboleday-wq`.

Firma: _____________________  C.I.: _____________________  Fecha: __________

**Huilcapi León Denisses Fabiola** — Confirmo que las identidades
`huilcapi <dhulcapil@uteq.edu.ec>` (con error tipográfico en el correo
institucional) y `Fabi06-ux <fabiolahuilcapi309@gmail.com>` (cuenta personal)
corresponden a commits realizados por mí. Mi identidad canónica a partir de
esta declaración es `huilcapi <dhuilcapil@uteq.edu.ec>`.

Firma: _____________________  C.I.: _____________________  Fecha: __________

**Alcívar Vélez Anderson Adonis** — Confirmo que los commits `98ad2ba`,
`baf348a` y `253cc53`, del 4 de septiembre de 2026, registrados como
`erizzov-boop <aalcivarv4@uteq.edu.ec>`, fueron realizados por mí desde mi
equipo personal y bajo mi correo institucional. El nombre de usuario
`erizzov-boop` corresponde a la configuración local de Git que quedó en ese
equipo tras una sesión de trabajo previa de mi compañero Edson Rizzo. Al clonar
el repositorio se actualizó la cuenta de GitHub pero no el `user.name` de Git, y
la discrepancia no se detectó antes de confirmar los cambios. Los tres commits
corresponden a la regeneración del inventario `fichas_tecnicas.csv`, a su
reporte de verificación y a la reposición del consolidado de transcripciones.
Mi identidad canónica es `AdonisAlcivar <aalcivarv4@uteq.edu.ec>`.

Firma: _____________________  C.I.: _____________________  Fecha: __________

**Rizzo Vélez Edson Nagib** — Confirmo que los commits `98ad2ba`, `baf348a` y
`253cc53` **no fueron realizados por mí**, pese a figurar bajo mi nombre de
usuario de Git. Corresponden a Anderson Alcívar, y el nombre de usuario procede
de la configuración local que quedó en su equipo tras una sesión de trabajo mía
anterior. Mi identidad es `erizzov-boop <erizzov@uteq.edu.ec>` y ningún otro
commit del historial se aparta de ella.

Firma: _____________________  C.I.: _____________________  Fecha: __________

---

## Verificación

Cualquier evaluador puede confirmar la unificación ejecutando, sobre un clon del
repositorio:

```bash
git shortlog -sne --all
```

---

## Medida adoptada para evitar nuevas inconsistencias

Tras detectar el caso anterior, el equipo adopta la siguiente práctica:

1. **Verificar la configuración de Git antes de commitear** en cualquier clon
   nuevo o en un equipo compartido:

```bash
   git config user.name && git config user.email
```

2. **Configurar la identidad explícitamente a nivel de repositorio**, no solo de
   forma global, para que la configuración heredada de otra persona no se
   aplique de manera silenciosa:

```bash
   git config user.name "<usuario institucional>"
   git config user.email "<correo institucional>"
```

3. **Comprobar la atribución después de cada jornada de trabajo** con
   `git shortlog -sne --all`, que debe devolver exactamente seis líneas.

Esta comprobación se incorpora a la rutina de cierre del repositorio.

---

El resultado debe mostrar seis líneas, una por integrante del equipo AHMRV, sin
ninguna identidad ajena al equipo.
