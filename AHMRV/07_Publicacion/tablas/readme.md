# Tablas del manuscrito

**Estado: pendiente — depende de que el análisis se ejecute.**

Esta carpeta alojará las tablas del manuscrito en formato LaTeX, listas para ser
incluidas desde el documento principal.

## Regla de generación

Igual que en `../figuras/`: cada tabla debe ser **regenerable** ejecutando un
script de `06_Experimento/scripts_analisis/` sobre los datos de
`06_Experimento/datos_procesados/`. No se escriben tablas a mano con cifras
transcritas: una cifra copiada manualmente rompe la cadena que va del dato al
resultado publicado, y es exactamente el punto donde un error deja de ser
detectable.

## Contenido previsto

- Descriptivos por condición experimental.
- Resultados de las pruebas de supuestos aplicadas.
- Contrastes por pregunta de investigación, con estadístico, grados de libertad,
  valor *p* con al menos tres decimales, tamaño de efecto e intervalo de
  confianza del 95 %.
- Caracterización de la muestra.

## Tablas ya existentes en el repositorio

Las tablas de requisitos y de trazabilidad se mantienen como datos vivos en
formato CSV y no se duplican aquí:

| Tabla | Ubicación |
|---|---|
| Matriz de trazabilidad | `04_Trazabilidad/matriz_trazabilidad.csv` |
| Priorización MoSCoW/Kano | `04_Trazabilidad/priorizacion_moscow_kano.csv` |
| Codificación temática | `02_Evidencias/Codificacion_Tematica/codificacion.csv` |

Su conversión a formato LaTeX se hará cuando el manuscrito las requiera, mediante
script y no a mano.

## Estado de las dependencias

- Datos procesados del experimento: **pendientes**.
- Scripts de análisis: **pendientes**.
- Plantilla de la publicación objetivo: **pendiente de incorporación**.

No se depositan tablas con cifras simuladas ni estructuras vacías rellenas con
valores de ejemplo.
