# Preguntas previsibles del tribunal — C12

Cada pregunta lleva **quién responde** y los hechos verificables en que se
apoya la respuesta. No son guiones para memorizar: son los datos que hay que
tener presentes para responder con precisión.

**Regla general:** si nadie sabe la respuesta, decirlo. Inventar en la sala es
el único error que no se puede corregir después.

---

## Bloque A — Sobre lo que no se ejecutó

### «¿Por qué no ejecutaron el estudio empírico?»
**Responde: Allan**

El cuasi-experimento comparativo humano frente a modelo de lenguaje está
**preregistrado** y requiere tres o más evaluadores externos reunidos, algo que
no depende solo del equipo. Están el protocolo, el registro en OSF `4z35d` y
los instrumentos. Lo que falta es la sesión.

**No decir** que está «casi listo». Decir qué falta y qué se necesita.

### «¿Por qué el manuscrito no tiene resultados ni discusión?»
**Responde: Allan**

Porque no puede tenerlos sin el estudio. El propio encabezado del `.tex`
declara que el género es *Research Preview* preregistrado. Se prefirió
declararlo a fabricar cifras.

### «¿Van a ampliar el cuasi-experimento a más entrevistas?»
**Responde: Allan**

No. El plan de análisis se fijó **antes de ver los datos**: 25 pares de
requisitos sobre la transcripción de ENTR-04. Ampliarlo ahora sería
exactamente lo que el preregistro existe para impedir.

---

## Bloque B — Sobre el prototipo

### «¿Por qué el prototipo no está en el repositorio entregado?»
**Responde: Francisco o Josthyn**

Vive en `jmaciasherr4/Prottotipo_Simpa`, documentado desde `05_MVP/readme.md`,
con el commit evaluado `ba33002` del 31 de agosto. **Es una observación que el
docente ya hizo** y la corrección prevista es integrarlo como submódulo o
publicar el código dentro del repositorio.

Reconocerla antes de defenderla.

### «¿El análisis de imagen funciona?»
**Responde: Francisco**

No. `RF-07`, `RF-08` y la clasificación visual de `RF-21` son **interfaz
simulada**. No hay modelo entrenado ni conjunto de datos del dominio, y por eso
no se reporta ninguna métrica de exactitud. Está declarado en `05_MVP/readme.md`
y en el ERS.

### «¿Dónde se guardan los datos?»
**Responde: Francisco**

En `localStorage` del navegador. No hay backend, ni base de datos remota, ni
control de sesiones de producción. Es un prototipo académico frontend y así se
declara.

### «¿Quién es `SIMPA Dev <dev@simpa.local>`?»
**Responde: Josthyn**

Una identidad no institucional que firma una confirmación en el repositorio del
prototipo. **El docente lo señaló** y la corrección es consolidarla.
Si a la fecha de la defensa no está resuelto, decirlo así.

---

## Bloque C — Sobre la evidencia y la ética

### «¿Por qué la evidencia audiovisual está en otro repositorio?»
**Responde: Edson o Anderson**

Los contenedores superaban la cuota de Git LFS del repositorio principal, lo
que impedía incluso clonarlo con normalidad. Se publican como assets de release
en `erizzov-boop/SIMPA_ISR401_Evidencias`, cifrados, e inventariados fila por
fila. **Fue una decisión recomendada por el propio docente** y está documentada.

### «¿Cómo sé que ese inventario es correcto?»
**Responde: Anderson**

`fichas_tecnicas.csv` tiene **60 filas**, una por archivo, con duración, códec,
tamaño, SHA-256 precifrado, contenedor y URL. Y hay un reporte,
`verificacion_fichas.md`, que comprueba **por petición HTTP** que cada
contenedor declarado existe con ese nombre exacto. Se generó por script, no a
mano.

### «¿Por qué las fotografías no conservan metadatos EXIF?»
**Responde: Edson**

Las 24 imágenes fueron procesadas y perdieron `DateTimeOriginal`, `DateTime` y
`Model`. **Solo se recuperaría desde los dispositivos de captura.** No se
inventaron fechas a partir del nombre de archivo ni del historial de Git.

*Antes de la defensa hay que saber si los originales existen. La respuesta
cambia según eso.*

### «¿Por qué no hay fotos de la aplicación del cuestionario?»
**Responde: Denisses**

Porque **se aplicó de forma completamente virtual**. Esas fotos nunca
existieron. La evidencia sustitutiva es más fuerte: las 62 respuestas tienen
marca temporal **de servidor**, del 30 de junio al 2 de agosto, con duraciones
de uno a dos minutos por respuesta. El EXIF lo escribe el dispositivo y es
trivialmente editable; la marca de servidor no la controla el equipo.

### «¿Cómo garantizan el anonimato?»
**Responde: Denisses**

Las transcripciones usan `ENTREVISTADO-NN`. Los consentimientos públicos van
enmascarados y los originales viajan cifrados. El cuestionario se configuró
como anónimo: las 62 celdas de correo contienen literalmente `anonymous` y la
columna de nombre está vacía. La base legal declarada es el artículo 7 de la
LOPDP, y se **rechaza razonadamente el consentimiento como base legal en
relación laboral**, porque en esa relación no es libre.

---

## Bloque D — Sobre el análisis cualitativo

### «¿Por qué reportan tres curvas de saturación y no una?»
**Responde: Denisses**

Porque son dos estratos distintos. Los participantes universitarios generan
pocos códigos nuevos de dominio **por construcción, no por saturación
alcanzada**. Mezclarlos produciría una inflexión artificial que parecería
saturación sin serlo. Es un compromiso adquirido en la adenda A14.

### «¿Cuántos codificadores hubo?»
**Responde: Denisses**

En las 138 filas actuales, uno solo (`VER`). La doble codificación con cálculo
de kappa está pendiente. **No inflar esto.**

---

## Bloque E — La incómoda

### «¿Quién es ALEX JOSE MORA DUARTE?»
**Responde: Edson**, que es el responsable del proyecto Jira.

Figura como informador o creador de **84 de los 175 elementos** del backlog y
no es integrante de AHMRV.

Con el se realizo la practica experimental en la que se creaba el proyecto de jira
y el era integrante de ese grupo de trabajo junto con Allan y mi persona.

### «¿Por qué 122 commits en un solo día?»
**Responde: Anderson o Allan**

El historial refleja jornadas de trabajo intensivo, sobre todo en el cierre de
la tercera ronda. El `.mailmap` normaliza las identidades a seis autores con
correo institucional, y no se ha reescrito el historial en ningún momento.

---

## Bloque F — Las que conviene que hagan

Preguntas donde el equipo está fuerte. Si surge la ocasión, llevarlas ahí.

### FAIR
92,31 %, **24 de 26 indicadores** con F-UJI 4.0.0, cien por cien en *Findable*
e *Interoperable*. El más alto del curso. Depositado como JSON y PDF.

### Zenodo
DOI de versión `10.5281/zenodo.22236500` y **DOI conceptual** de la serie, que
casi nadie declara. Seis archivos curados bajo CC BY 4.0, con diccionario,
script generador y manifiesto de sumas.

### Reproducibilidad
Punto de entrada único: `python 07_Datos/scripts/run_all.py`. Regenera los tres
CSV y las figuras desde los datos crudos. Verificado desde clon limpio.

### Control de cambios
Comité de control de cambios con acta, tres solicitudes formales y dos libros
de auditoría de calidad y registro de defectos. Los requisitos `RF-40` a
`RF-42` entraron por esa vía.

### Cifrado de la evidencia
Los contenedores `.7z` llevan **la cabecera cifrada**: sin la contraseña no se
puede ni listar los nombres de archivo. Como esos nombres incluyen el rol del
participante, es una medida de privacidad y no solo de confidencialidad.

---

## Antes de la defensa, decidir en grupo

Tres respuestas que hoy no existen y que el tribunal puede pedir:

1. **Quién es ALEX JOSE MORA DUARTE.**
2. **Si existen los originales con EXIF.**
3. **Qué se dice sobre la participación del docente como ENTR-16**, si sale el
   tema. El criterio del proyecto ha sido declarar con mitigación, no omitir.
