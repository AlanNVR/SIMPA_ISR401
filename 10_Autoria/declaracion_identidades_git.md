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
| `erizzov-boop <erizzov@uteq.edu.ec>` | Rizzo Vélez Edson Nagib | Identidad única, sin fragmentación |
| `AdonisAlcivar <aalcivarv4@uteq.edu.ec>` | Alcívar Vélez Anderson Adonis | Identidad única, sin fragmentación |

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

Firma: _____________________  C.I.: _____________________  Fecha: __________

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

---

## Verificación

Cualquier evaluador puede confirmar la unificación ejecutando, sobre un clon del
repositorio:

```bash
git shortlog -sne --all
```

El resultado debe mostrar seis líneas, una por integrante del equipo AHMRV, sin
ninguna identidad ajena al equipo.
