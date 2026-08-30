# Ética — Proyecto SIMPA · Equipo AHMRV

Este documento reúne, en un solo lugar y en orden cronológico, la traza completa
de los anexos éticos (A.01–A.14), las desviaciones de procedimiento detectadas en
rondas anteriores, cómo fueron subsanadas, y la explicación de la reescritura del
historial de Git realizada por motivos de privacidad. Su propósito es que
cualquier persona evaluadora pueda reconstruir, sin preguntar al equipo, qué pasó
y en qué estado quedó cada punto.

---

## 1. Traza de anexos A.01–A.14

| Anexo | Contenido | Estado |
|---|---|---|
| A.01 | Protocolo de investigación | Vigente desde Entrega 1 |
| A.02 | Instrumentos de recolección | Vigente, ampliado en Entrega 3 con los instrumentos de la segunda ronda de campo |
| A.03 | Consentimiento informado (formato base) | Vigente. Las copias públicas firmadas se anonimizaron — ver sección 2 |
| A.04 | Plan de gestión de datos | Vigente |
| A.05 | Aval institucional | Vigente |
| A.06 | Declaración de conflicto de intereses | Vigente |
| A.07 | Compromiso de confidencialidad | Vigente |
| A.08 | CV del docente responsable | Vigente |
| A.09 | Nómina del equipo | Vigente, seis integrantes |
| A.10 | Cronograma Gantt | Vigente |
| A.11 | Análisis de riesgos | Vigente |
| A.12 | Certificado de ética | Vigente |
| A.13 | Participantes externos | Vigente, incorporado en Entrega 3 junto con la organización externa |
| — | Adenda ética, segunda ronda (`Adenda_Segunda_Ronda.pdf`) | Declara la desviación de procedimiento de la segunda ronda de campo — ver sección 2 |
| A.14 | Adenda tercera ronda (`A14_Adenda_Tercera_Ronda.pdf`) | Documento de trazabilidad y subsanación de la desviación anterior; no constituye una nueva solicitud de permiso |

Categoría C (participación de la organización externa): `C1` Aval de la unidad
productiva, `C2` Compromiso de confidencialidad estratégica, `C3` Protocolo de
anonimización, `C4` Normativa sectorial aplicable.

---

## 2. Desviación de procedimiento (segunda ronda) y su subsanación

**Qué ocurrió.** Durante la segunda ronda de trabajo de campo (Entrega 3, agosto
2026) se detectaron deficiencias de anonimización en la evidencia fotográfica y en
los consentimientos informados publicados: nombres propios de los participantes
visibles en los nombres de archivo, cédula y firma sin enmascarar en las copias
públicas de consentimiento, y metadatos GPS presentes en fotografías publicadas.
Esta desviación quedó declarada en `Adenda_Segunda_Ronda.pdf`.

**Cómo se subsanó (Entrega 3, `CHANGELOG.md` [3.0.0]).**

- Cédula y firma enmascaradas en la copia pública de cada consentimiento; los
  originales sin enmascarar se trasladaron a la zona restringida cifrada
  (`02_Evidencias/00_Restringido/`).
- Metadatos GPS eliminados de todas las fotografías publicadas.
- Nomenclatura de archivos multimedia migrada al patrón
  `AAAA-MM-DD_TipoParticipante_ENTR-XX_Tecnica.ext`, sustituyendo los nombres
  propios por el código de participante correspondiente.

**Criterio de convalidación.** Conforme a la decisión operativa del equipo (plan
de cierre 2B, sección 0.2), esta desviación se considera **aceptada y cerrada**:
la A.14 no vuelve a pedir una nueva aprobación sobre este punto, sino que
documenta históricamente qué se hizo mal, cómo se corrigió y qué medida evita que
se repita.

---

## 3. Reescritura del historial de Git por privacidad

**Motivo.** Con posterioridad a la corrección descrita en la sección 2, una
auditoría del repositorio confirmó que el historial de Git seguía conservando,
en la rama `reorganizar-estructura-ahmrv`, versiones anteriores y sin anonimizar
de los consentimientos firmados y de las fotografías de entorno — con nombres
reales de los participantes visibles tanto en el nombre de archivo como en el
contenido — recuperables aunque la zona pública actual ya mostrara las versiones
corregidas.

**Qué se hizo.** Se reescribió el historial de dicha rama con `git filter-repo`,
retirando por completo las rutas que contenían las versiones sin anonimizar
(`AHMRV/evidencias/`, `AHMRV/02_Evidencias/formularios/`,
`AHMRV/02_Evidencias/fotos/`, entre otras equivalentes), verificado mediante
auditoría directa de los objetos del historial (`git rev-list --objects --all`).

**Por qué se migró a un repositorio nuevo.** La reescritura de la rama, por sí
sola, resultó insuficiente: GitHub conserva de forma permanente e inmutable la
referencia de un Pull Request (`refs/pull/2/head`) abierto en algún momento desde
esa rama, la cual seguía sirviendo el contenido original sin anonimizar y no
puede eliminarse mediante `git push --force` ni ninguna operación estándar de
Git. Por esta limitación, ajena al equipo, el proyecto se migró a un repositorio
nuevo — `https://github.com/AlanNVR/SIMPA_ISR401` — que no hereda referencias de
Pull Requests ni historial previo. El repositorio original quedó archivado en
modo privado. Se verificó de forma independiente que el repositorio nuevo no
contiene ninguna referencia adicional (`refs/pull/*` ni de otro tipo) ni ningún
dato identificable en su historial completo.

Esta operación queda registrada también en `CHANGELOG.md` y referenciada en la
A.14, conforme a lo exigido por el STOP A del plan de cierre: la corrección no
sustituye ni oculta la traza de lo ocurrido, se documenta hacia adelante.

---

## 4. Estado de privacidad al cierre

- La zona pública no contiene nombre, firma, cédula, rostro identificado por
  nombre, ni coordenadas GPS.
- Los ocho consentimientos públicos muestran el código de participante
  (`ENTR-01` a `ENTR-08`) en lugar de datos identificables.
- Las versiones históricas sensibles fueron saneadas en la medida técnicamente
  posible; la limitación encontrada (refs de Pull Request) y la solución aplicada
  quedan documentadas en la sección 3 de este documento.
- La contraseña de los contenedores cifrados no se publica en ningún
  repositorio; se entrega únicamente por el canal académico correspondiente.
