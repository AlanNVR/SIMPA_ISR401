# Registro de cambios

Todas las modificaciones relevantes de este proyecto se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

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
