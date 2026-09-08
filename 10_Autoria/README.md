# 10_Autoria

Esta carpeta centraliza la evidencia de autoría y trabajo propio del proyecto
SIMPA conforme a la guía de entrega.

## Estado

Únicamente se registra el trabajo real realizado en el repositorio. Los
elementos de autoría A1–A12 que todavía requieran evidencia adicional se
completarán posteriormente. **No se crean evidencias ficticias ni se declaran
como cumplidos elementos que todavía no hayan sido verificados.**

## Contenido

| Archivo | Qué es |
|---|---|
| `declaracion_identidades_git.md` | Declaración de identidades Git del equipo, con las correspondencias entre cuentas y personas, y la firma de cada integrante |
| `2026-09-06_DeclaracionIdentidadesGit_Enmascarado.pdf` | Copia pública de la declaración firmada, con cédula y firma manuscrita enmascaradas |
| `registro_reestructuracion_2026-09-03.md` | Resumen y commits de las correcciones realizadas durante la reestructuración del repositorio |

## Declaración de identidades Git

Documenta, con firma de cada integrante afectado, la correspondencia entre las
distintas identidades Git utilizadas durante el desarrollo y la persona real
que hay detrás de cada una. Respalda el archivo `.mailmap` del repositorio y
resuelve el hallazgo de identidades fragmentadas.

**Ninguna corrección de identidad altera el historial de Git.** No se ha
empleado `rebase`, `filter-branch`, `filter-repo` ni `push --force` en ningún
momento del proyecto: la unificación se realiza mediante `.mailmap`, que
corrige la atribución sin modificar ningún commit existente.

### Las dos versiones del documento

| Versión | Ubicación | Contiene |
|---|---|---|
| Pública, enmascarada | Esta carpeta | Firma y cédula tapadas; el resto del contenido íntegro |
| Original, sin enmascarar | Cifrada en el repositorio complementario | Firma y cédula visibles |

El original se deposita en `erizzov-boop/SIMPA_ISR401_Evidencias`, contenedor
`Declaracion_Identidades_git_original.7z`, con su fila propia en
`../02_Evidencias/00_Restringido/fichas_tecnicas.csv` bajo el código
`CONSOLIDADA-EQUIPO`. No lleva código `ENTR-XX` ni `WT-XX` porque no es un
documento de un participante individual, sino la firma conjunta de los seis
integrantes del equipo.

### Verificación

```bash
git shortlog -sne --all
```

Debe devolver exactamente seis líneas, una por integrante del equipo AHMRV,
todas con correo institucional y sin ninguna identidad ajena al equipo.

## Contenido pendiente

Los elementos A1–A12 de evidencia de autoría no cubiertos por esta carpeta
—bitácora de sesiones, capturas, grabaciones, notas de campo, aporte
individual— se incorporan según se generan. No se retroceden ni se
reconstruyen a partir del historial de Git para simular una evidencia que no
se produjo en su momento.
