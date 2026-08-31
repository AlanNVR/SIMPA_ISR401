# Zona restringida `[R]` — índice de la evidencia sensible

**Esta carpeta no contiene evidencia. Contiene el índice que permite localizarla,
descargarla y verificarla.**

Si usted está evaluando este repositorio, esto es lo que necesita saber para
interpretar lo que encuentra aquí.

---

## 1. Qué evidencia se referencia desde esta carpeta

Los archivos originales del trabajo de campo, en su estado sin enmascarar:

| Tipo | Cantidad | Participantes |
|---|---|---|
| Audios de entrevista (`.mp3`) | 8 | ENTR-01 a ENTR-08 |
| Videos de entrevista (`.mp4`) | 14 archivos | ENTR-01 a ENTR-08 (ENTR-03 en 7 partes) |
| Consentimientos originales firmados | 8 | ENTR-01 a ENTR-08 |

Total inventariado: **30 archivos**, cada uno con una fila propia en
`fichas_tecnicas.csv`.

## 2. Por qué no están publicados aquí

Por dos motivos distintos, y conviene no confundirlos.

**Motivo de privacidad.** Estos archivos contienen voz, rostro, nombre manuscrito
y firma de personas reales. Publicarlos violaría el compromiso adquirido con cada
participante y la normativa de protección de datos personales. Las versiones
publicables —consentimientos enmascarados, transcripciones anonimizadas,
fotografías sin rostros— están en las carpetas hermanas de `02_Evidencias/` y son
artefactos distintos, no copias.

**Motivo técnico.** Los contenedores cifrados suman varios gigabytes. Se alojaban
en este repositorio mediante Git LFS hasta que la cuota se agotó, lo que llegó a
impedir el clonado normal del proyecto. Se trasladaron a un repositorio
complementario y se publican allí como *Release assets*, que no consumen cuota de
LFS.

Estos dos motivos son independientes: aunque el problema de cuota no existiera,
el material seguiría sin publicarse en abierto.

## 3. Los tres archivos de esta carpeta

| Archivo | Qué es | Para qué sirve |
|---|---|---|
| `fichas_tecnicas.csv` | Inventario de los 30 archivos, una fila por archivo | Es el índice. Ver sección 4 |
| `README_Evidencias_Externas.md` | Ubicación de los contenedores y procedimiento de descarga | Explica dónde está el material y cómo obtenerlo |
| `readme.md` | Este documento | Orientación general |

## 4. Cómo leer `fichas_tecnicas.csv`

Quince columnas. Las que importan para verificar:

| Columna | Contenido |
|---|---|
| `id_archivo` | Nombre del archivo dentro del contenedor |
| `tipo` | `audio`, `video` o `consentimiento` |
| `codigo_participante` | `ENTR-XX`. **Nunca el nombre de la persona** |
| `duracion_segundos` | Medida con `ffprobe`, con decimales |
| `codec` | Códec real del flujo, no la extensión del archivo |
| `tamano_bytes` | Tamaño exacto |
| `sha256` | Hash calculado **antes** de cifrar el contenedor |
| `contenedor` | Contenedor `.7z` que lo incluye |
| `ruta_en_contenedor` | Ruta interna, relativa a la raíz del contenedor |
| `repositorio` / `url_release` | Dónde descargarlo |

**Ninguna celda contiene el valor `PENDIENTE`.** Cada dato procede de una medición
real sobre el archivo, no de una estimación.

## 5. Relación con los archivos de checksums

Hay dos manifiestos y comprueban cosas distintas. Confundirlos produce fallos que
parecen corrupción y no lo son.

| Manifiesto | Ubicación | Qué comprueba | Cómo se usa |
|---|---|---|---|
| `checksums.sha256` | Raíz del repositorio | Los archivos versionados en este repositorio | `sha256sum -c checksums.sha256` desde la raíz |
| `checksums_evidencias.sha256` | Raíz del repositorio | El **contenido interno** de los contenedores `.7z` | Desde la carpeta donde se extrajo el contenedor |

El segundo no puede ejecutarse contra el repositorio: sus rutas
(`audios/…`, `videos/…`) son internas al contenedor. Su cabecera explica el
procedimiento paso a paso.

Los hashes de `checksums_evidencias.sha256` son los mismos que figuran en la
columna `sha256` de `fichas_tecnicas.csv`. Son dos presentaciones del mismo dato:
una para verificación automática, otra para inspección por participante.

## 6. Cómo debe interpretar esta carpeta un evaluador

**Lo que puede comprobar sin la contraseña:** que el inventario está completo, que
ninguna celda queda sin valor, que cada archivo declarado tiene código de
participante y hash, y que la URL de descarga responde.

**Lo que requiere la contraseña:** descifrar un contenedor, ejecutar `ffprobe`
sobre un archivo y contrastar duración, códec, tamaño y hash contra su fila. Esa
es la verificación completa, y la cadena está diseñada para soportarla:

```text
ENTR-XX → archivo → fila en fichas_tecnicas.csv → SHA-256
        → contenedor .7z → Release del repositorio complementario → URL
```

**La contraseña no está en ningún repositorio**, ni en este ni en el
complementario. Se entrega por el canal académico correspondiente. Un repositorio
que publicara la contraseña junto al contenedor cifrado no estaría protegiendo
nada.

**Si encuentra una discrepancia**, el orden de comprobación es: primero que el
contenedor descargado esté completo, después que la extracción no haya alterado
los terminadores de línea, y sólo entonces sospechar del hash.
