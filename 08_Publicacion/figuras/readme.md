# Figuras del manuscrito

**Estado: pendiente — depende de que el análisis se ejecute.**

Esta carpeta alojará las figuras del manuscrito, en el formato vectorial que
exija la plantilla de la revista o conferencia objetivo.

## Regla de generación

Cada figura de esta carpeta debe ser **regenerable** ejecutando un script de
`06_Experimento/scripts_analisis/` sobre los datos de
`06_Experimento/datos_procesados/`. No se depositan imágenes construidas a mano,
exportadas de una hoja de cálculo o editadas después de generarse: una figura que
no puede reproducirse desde los datos no es verificable.

Cada archivo llevará junto a sí la indicación del script que lo produce, en el
`readme` que se añada cuando la carpeta se pueble.

## Figuras ya existentes en el repositorio

| Figura | Ubicación | Script que la genera |
|---|---|---|
| Curva de saturación temática | `02_Evidencias/Codificacion_Tematica/curva_saturacion.png` | `02_Evidencias/Codificacion_Tematica/curva_saturacion.py` |

Se mantiene en su carpeta de evidencia. Se incorporará al manuscrito cuando la
curva se recalcule sobre el conjunto completo de entrevistas; la versión actual
corresponde únicamente a las entrevistas realizadas hasta la fecha y no debe
presentarse como definitiva.

## Estado de las dependencias

- Datos procesados del experimento: **pendientes**.
- Scripts de análisis: **pendientes**.
- Plantilla de la publicación objetivo: **pendiente de incorporación**.

No se depositan figuras con datos simulados ni marcadores de posición con aspecto
de resultado.
