## Inventario EXIF — AUT-11

`exif_inventario.csv` registra, para cada fotografía de cámara usada como
evidencia en el proyecto, su nombre, carpeta de origen, fecha de captura,
dispositivo y SHA-256.

### Alcance

Se incluyeron únicamente fotografías de cámara: `02_Evidencias/Fotos_Entorno/`,
`02_Evidencias/Documentos_Organizacion/`, `02_Evidencias/Consentimientos/` y
`10_Autoria/fotos_equipo/`.

No se incluyeron diagramas UML, mockups, gráficas generadas ni capturas de
pantalla (por ejemplo `03_Modelado/Diagramas_UML/png/`,
`03_Modelado/Mockups/`, `04_Trazabilidad/Capturas/`,
`07_Datos/resultados/*.png`, `10_Autoria/capturas/`). Ninguno de esos
archivos es una fotografía tomada por una cámara, así que nunca tendrían un
EXIF real que registrar; incluirlos habría significado o inventar un dato
inexistente o llenar el inventario de filas "No aplica" sin valor
informativo.

### Hallazgo

De 43 fotografías inventariadas, **solo 2 conservan metadato de fecha y
dispositivo embebido** en el propio archivo (`fotos_equipo/observacion_proceso_trabajo.png`
y `fotos_equipo/planificacion_entrevistas_organizacion.png`). Las 41
restantes —prácticamente todo `Fotos_Entorno/` y la totalidad de
`Consentimientos/`— no tienen ningún metadato de captura recuperable.

La causa más probable es el propio historial de edición de estas imágenes:
enmascarado de rostros y de cédula/firma, recortes por peso de archivo y
renombrados sucesivos. Cada reexportación durante esos procesos
probablemente eliminó los metadatos originales. Esto es consistente con lo
ya documentado para `equipo_visita_palmicultora.png` en
`10_Autoria/fotos_equipo/readme.md`.

### Qué significa esto para las fechas del proyecto

Las fechas que aparecen en los nombres de archivo (`AAAA-MM-DD_...`) siguen
siendo las fechas declaradas por el equipo para cada evidencia, y se
mantienen como tales en el resto de la documentación
(`fichas_tecnicas.csv`, `bitacora_sesiones.csv`). Lo que este inventario dice
es que, salvo las dos excepciones señaladas, **esas fechas ya no pueden
verificarse de forma independiente a partir del propio archivo de imagen**.
Se documenta así, en vez de presentar como verificado algo que no lo está.

### Verificación

```bash
sha256sum 02_Evidencias/Fotos_Entorno/*.jpeg 02_Evidencias/Fotos_Entorno/*.png \
          02_Evidencias/Documentos_Organizacion/*.png \
          02_Evidencias/Consentimientos/*.png \
          10_Autoria/fotos_equipo/*.png
```

Los valores deben coincidir con la columna `sha256` de
`exif_inventario.csv`.
