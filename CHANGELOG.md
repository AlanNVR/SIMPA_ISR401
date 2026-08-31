# Registro de cambios

Todas las modificaciones relevantes de este proyecto se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

---

## [4.1.1] - 2026-08-31 - Correcciones post-auditoría de cierre

### Corregido

- Se armonizó la identificación del ERS como Entrega 4 (2B), versión 2.0,
  con fecha 31/08/2026.
- Se añadió la revisión interna 3.2 correspondiente a ERS v2.0 y se aclaró
  la relación histórica con la línea base ERS v1.1 de PE5.
- `CITATION.cff` se actualizó al catálogo vigente de 42 RF y 19 RNF.
- Se sustituyeron las referencias editables al repositorio anterior por
  `https://github.com/AlanNVR/SIMPA_ISR401`, preservando sin modificación
  los documentos firmados.
- `README_Etica.md` incorpora una tabla de correspondencia entre rutas
  históricas y rutas vigentes.
- El criterio muestral se actualizó al umbral vigente de n >= 60,
  distinguiendo el perfil ocupacional agregado (n=60) de los subperfiles
  por labor (18, 18, 13 y 11), sin declarar cumplimiento por subperfil.
- Las referencias a gatekeepers de la Entrega 3 se identificaron
  explícitamente como criterios históricos de la 2A.

### Bibliografía y reproducibilidad

- Se eliminó el fallback silencioso de IEEEtran a `unsrt`.
- Se incorporó `IEEEtran.bst` al directorio del ERS para hacer determinista
  el estilo bibliográfico.
- Se eliminaron los marcadores de trabajo `[RECIENTE]` de la bibliografía.
- Se completaron DOI, ISBN o URL verificables en las referencias citadas
  cuando correspondía.
- La referencia `arora2024` se corrigió a su publicación bibliográfica
  verificable.
- La compilación completa `pdflatex -> bibtex -> pdflatex -> pdflatex`
  finalizó sin errores LaTeX graves, sin errores de BibTeX y sin citas o
  referencias indefinidas.
- El PDF resultante contiene 108 páginas.

## [4.1.0] - 2026-08-31 - Migración y consolidación de la Entrega PE5

### Cambiado

## 31/08/2026 — Migración y consolidación de la Entrega PE5

Se integró al repositorio principal el trabajo consolidado durante la Entrega PE5,
preservando los cambios posteriores que ya existían en `SIMPA_ISR401`.

### ERS

- Se retiró la versión anterior:
  - `ERS_SRS_2A_v1.0.tex`
  - `ERS_SRS_2A_v1.0.pdf`
- Se incorporó y compiló la línea base:
  - `ERS_SRS_2B_v2.0.tex`
  - `ERS_SRS_2B_v2.0.pdf`
- Se migraron las secciones de DFD, inteligencia artificial, casos de uso
  CU-11 a CU-18 y el apéndice BDD.
- Se conservó `declaracion_uso_ia.tex`, creado después de PE5, y se integró
  en la nueva compilación.
- La compilación final se verificó sin errores LaTeX graves ni referencias
  o citas indefinidas.

### Auditoría y control de cambios

Se incorporaron como anexos de soporte:

- `AnexoA_auditoria_calidad.xlsx`
- `AnexoB_registro_defectos.xlsx`
- `Acta_CCB.pdf`
- `RFC-01.pdf`
- `RFC-02.pdf`
- `RFC-03.pdf`

Estos documentos sustentan la evolución de la línea base y las modificaciones
aprobadas mediante el Change Control Board.

### Trazabilidad

- Se incorporó `matriz_e2e.xlsx` como matriz vigente de PE5.
- La matriz contiene 73 filas de trazabilidad.
- Se incorporaron `backlog_export.csv` y las capturas de sincronización con Jira.
- Se corrigió la traza de `RNF-11`, sustituyendo `EV-12` por `EV-10`:
  `EV-07, EV-10`.
- La matriz anterior de 52 filas se conserva como artefacto histórico.

### Priorización

El catálogo funcional quedó reconciliado en:

- 42 RF;
- 24 Must;
- 16 Should;
- 2 Could;
- 0 Won't.

Se incorporaron RF-40, RF-41 y RF-42 como Must conforme a RFC-03.
No se asignaron retrospectivamente valores Kano o WSJF que no estuvieran
documentados en PE5.

### MVP

Se corrigió la cobertura publicada anteriormente como `9/19 = 47,4 %`.

Los valores auditados son:

- 8/21 = 38,1 % respecto al catálogo utilizado durante la construcción del MVP;
- 8/24 = 33,3 % respecto al catálogo vigente post-CCB.

La cifra antigua se conserva únicamente en las notas históricas que documentan
la corrección.

## [4.0.1] — 2026-08-31 · Higiene del historial y portabilidad de checksums

### Corregido

- Se realizó una segunda reescritura del historial, independiente del saneamiento de privacidad anterior, para retirar material ajeno al PFC que permanecía únicamente en commits históricos.
- Se eliminaron del historial las rutas `Tareas_Villafuerte/`, `Grupo_C/`, `MRV_Equipo_B/` y `cambios_fase0_v2.patch`.
- El historial pasó de 281 a 241 commits tras retirar 40 commits asociados exclusivamente a dicho material.
- Se verificó nuevamente que `Hacienda La Manuela` no aparece en los commits alcanzables y que el seudónimo `Palmicultora M` permanece correctamente aplicado.
- El tag `v1.0-mvp-demo` fue reescrito durante el saneamiento y quedó asociado al commit limpio equivalente.
- Se añadió `.gitattributes` en la raíz con la regla `* -text` para impedir conversiones automáticas LF/CRLF entre plataformas.
- `checksums.sha256` fue regenerado para incorporar `.gitattributes` y permitir su verificación directa mediante `sha256sum -c checksums.sha256` también en Windows.
- La verificación final se realizó desde un clon fresco del repositorio, sin presentar archivos `FAILED`.

---

## [3.0.0] — 2026-08-03 · Entrega 3 (2A)

Especificación completa con componente empírico. Segunda ronda de trabajo de campo
e incorporación de una organización externa como fuente de requisitos.

### Añadido

**Requisitos**
- 19 requisitos funcionales nuevos (`RF-21` a `RF-39`), derivados en su totalidad
  de la segunda ronda de campo.
- 9 requisitos no funcionales nuevos, completando la cobertura de las nueve
  características de calidad de ISO/IEC 25010:2023.
- `RNF-16`: requisito de explicabilidad obligatorio para los tres componentes
  basados en inteligencia artificial (`RF-07`, `RF-08`, `RF-21`).
- 8 requisitos legales (`RL-01` a `RL-08`) con trazabilidad artículo de la
  LOPDP → requisito del sistema.
- 3 restricciones de diseño nuevas (`RD-08`, `RD-09`, `RD-10`).
- 19 historias de usuario en formato Connextra con criterios INVEST verificados
  y escenarios de aceptación en Gherkin.

**Modelado**
- Modelado organizacional i\*: diagramas de Dependencia Estratégica (SD) y de
  Razón Estratégica (SR).
- Cinco tipos de diagrama nuevos: secuencia (3), actividad, estados (2),
  componentes y despliegue.
- 5 casos de uso detallados adicionales (`CU-06` a `CU-10`), completando 10.
- Diagrama de clases refinado con operaciones además de atributos.

**Evidencia**
- Cinco entrevistas nuevas (`EV-04` a `EV-08`), dos de ellas con personal de una
  organización externa.
- Cuestionario ampliado de 4 a 62 respondientes (`EV-12`).
- Dos tipos documentales de la organización: plan semanal de labores (`EV-11`) y
  hoja de liquidación de presupuesto contra ejecución (`EV-13`).
- Adenda ética de la segunda ronda con declaración de desviación de procedimiento.

**Otros**
- Prototipo funcional (MVP) con nueve pantallas y control de acceso por rol.
- Protocolo experimental registrado en OSF (Enfoque 1: comparación de calidad de
  requisitos humanos frente a los generados por un modelo grande de lenguaje).
- Los cinco archivos raíz obligatorios.

### Modificado
- Documento migrado de Word a LaTeX, reproducible desde el fuente.
- Matriz de trazabilidad ampliada de 24 a 52 filas, con nueve niveles de enlace.
- Bibliografía ampliada de 7 a 31 fuentes primarias, 12 de ellas del período
  2023–2026.
- Priorización: se añaden el modelo de Kano y el cálculo WSJF a la clasificación
  MoSCoW existente.
- Rol de `ENTR-02` corregido a Administrador / Asesor Técnico.

### Corregido
- `RF-17` y `RF-20` carecían de caso de uso asociado en la Entrega 2. La cobertura
  requisito-caso de uso es ahora del 100 %.
- Consentimientos informados: cédula y firma enmascaradas en la copia pública; los
  originales se trasladan a la zona restringida cifrada.
- Metadatos GPS eliminados de todas las fotografías publicadas.
- Nomenclatura de archivos multimedia migrada a
  `YYYY-MM-DD_TipoParticipante_CodigoParticipante_Tecnica.ext`, sustituyendo los
  nombres propios por códigos de participante.
- Archivo de evidencia fotográfica que era un marcador de 2 bytes, reemplazado por
  la imagen real.
- `fichas_tecnicas.csv` presentaba un conflicto de fusión sin resolver y contenía
  únicamente la plantilla de ejemplo. Reconstruido con el inventario real de 30
  archivos multimedia.
- `checksums.sha256`: rutas sin el prefijo `videos/`, carpeta duplicada
  `videos 2/` y un nombre de archivo con acentos.
- Audio de entrevista incorporado como archivo dentro del repositorio, en lugar de
  enlace externo a plataforma de video.

### Renumerado

Para asignar identificadores contiguos a las entrevistas de la segunda ronda, las
evidencias que no eran entrevistas se desplazaron:

| Entrega 2 (1B) | Entrega 3 (2A) | Contenido |
|---|---|---|
| `EV-04` | `EV-09` | Observación de campo |
| `EV-05` | `EV-10` | Cuestionario, aplicación piloto (n=4) |

Toda referencia a `EV-04` o `EV-05` en documentos anteriores a esta versión debe
leerse conforme a esta equivalencia.

### Suposiciones invalidadas

La ampliación del cuestionario a 62 respondientes refutó tres supuestos que la
Entrega 2 daba por establecidos a partir de cuatro respuestas:

1. **No todo el personal dispone de teléfono inteligente.** El 11,3 % declara no
   usarlo. Motivó `RF-35` (registro delegado) y `RD-10`.
2. **Existe conectividad permanente en algunas zonas.** El 25,8 % dispone de señal
   siempre, frente a la afirmación previa de que ninguna persona la tenía.
3. **El rastreo por GPS no goza de aceptación unánime.** El 25,8 % expresa
   reservas. Motivó que `RL-03` exija consentimiento revocable sin consecuencia
   laboral.

### Nota sobre la estructura del repositorio

La Sección 8.1 de la guía establece que la raíz del repositorio debe reproducir el
árbol del proyecto. En este repositorio el proyecto reside en `AHMRV/`.

La ruta se conserva de forma deliberada: es la declarada en la portada del
documento entregado en el SGA, cuya actividad se encuentra cerrada y no admite
modificación. Trasladar el contenido a la raíz produciría un error 404 en el
enlace evaluado y activaría el gatekeeper G1. Se optó por preservar la
verificabilidad del enlace y declarar la desviación estructural.

Los cinco archivos raíz obligatorios sí residen en la raíz del repositorio.

---

## [2.0.0] — 2026-06-26 · Entrega 2 (1B)

### Añadido
- 20 requisitos funcionales con la plantilla de ocho atributos.
- 9 requisitos no funcionales cuantificados según ISO/IEC 25010.
- 7 restricciones de diseño.
- Modelado UML: diagrama de casos de uso con 15 casos y 4 actores, especificación
  textual de 5 casos de uso, diagrama de clases conceptual con 18 clases.
- 8 prototipos de interfaz vinculados a requisitos funcionales.
- Matriz de trazabilidad parcial de 24 filas.
- Priorización MoSCoW de todos los requisitos.
- Cuestionario piloto aplicado a 4 personas trabajadoras.

### Modificado
- Documento unificado que acumula y reemplaza la Entrega 1 (1A).

---

## [1.1.0] — 2026-06-23

### Corregido
Incorporación de la retroalimentación docente sobre la Entrega 1 (1A):
- Diagrama de contexto del sistema.
- Actas formales de entrevista.
- Reformulación de los requisitos brutos con trazabilidad a su fuente.
- Depuración de secciones que no correspondían a la Entrega 1A.

---

## [1.0.0] — 2026-06-01 · Entrega 1 (1A)

### Añadido
- Planificación del proyecto de ingeniería de requisitos.
- Identificación de partes interesadas.
- Tres entrevistas semiestructuradas con consentimiento informado firmado.
- Observación directa del cultivo.
- 29 requisitos brutos trazados a su fuente.
- Repositorio GitHub con estructura inicial.
