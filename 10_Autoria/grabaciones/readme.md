# Grabaciones de sesiones de trabajo — AUT-04

Esta carpeta no contiene los archivos de video — se alojan como *Release
assets* en el repositorio complementario de evidencias, por el mismo motivo
que los contenedores `.7z`: evitar la dependencia de Git LFS.

- Repositorio: `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias`
- Release: `v1.0-autoria`

## Grabaciones

| # | Archivo | Tema | Participantes | URL |
|---|---|---|---|---|
| 1 | `2026-09-12_grabacion01_allan_josthyn_datos_experimento.mp4` | Experimento, datos y análisis | Allan Villafuerte, Josthyn Macías | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-autoria/2026-09-12_grabacion01_allan_josthyn_datos_experimento.mp4` |
| 2 | `2026-09-12_Grabacion02_ManuscritoEvidenciasDocumentacion.mp4` | Manuscrito, evidencias y documentación final | Denisses Huilcapi, Edson Rizzo, Francisco Arboleda (apoyo técnico, sin intervención verbal) | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-autoria/2026-09-12_Grabacion02_ManuscritoEvidenciasDocumentacion.mp4` |

## Contenido verificable de la Grabación 1

En esta sesión, Allan compartió pantalla y se revisó en vivo:

1. Ejecución de `python 07_Datos/scripts/run_all.py` y explicación del
   arreglo aplicado a la cadena reproducible (regeneración correcta de las
   tres curvas de saturación por estrato, 16 filas × 11 columnas).
2. Historial de commits de `curva_saturacion.py` (`git log --follow`) y
   revisión del commit que corrigió la invocación del script.
3. Resultados reales de `07_Datos/resultados/acuerdo_krippendorff.csv`,
   `comparacion_descriptiva.csv` y `resumen_modelos_ordinales.txt`: acuerdo
   entre evaluadores prácticamente nulo (α de Krippendorff entre -0,015 y
   0,027 según dimensión) y ausencia de diferencia estadísticamente
   significativa entre requisitos humanos y generados por LLM en las cinco
   dimensiones evaluadas (p entre 0,35 y 0,41).
4. Discusión conjunta sobre los métodos de acuerdo aplicados (α de
   Krippendorff ordinal como medida principal, kappa de Cohen ponderado
   cuadrático por pares como medida secundaria).

## Contenido verificable de la Grabación 2

Conforme al guion usado (`06_Experimento`... ver guion completo en el
historial del equipo), en esta sesión se realizaron en vivo tres ediciones
reales del repositorio:

1. Cita a `06_Experimento/osf_deviations.md` agregada en
   `08_Publicacion/manuscrito_final.tex` (sección "Amenazas a la validez").
2. Entrada `[4.2.0]` agregada a `CHANGELOG.md`.
3. Incorporación de `PLANTILLA_hoja_puntuacion.csv` y
   `COMO_LLENAR_hoja_puntuacion.md` a `06_Experimento/evaluadores/`.

Los tres cambios son verificables directamente en el historial de commits
del repositorio principal, con marca de tiempo cercana a la grabación.
