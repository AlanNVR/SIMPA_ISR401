# Dataset SIMPA — paquete de predepósito Zenodo

## Estado

**Paquete preparado para revisión previa al depósito. DOI reservado: `10.5281/zenodo.22236500`; publicación pendiente.**

El DOI `10.5281/zenodo.22236500` ha sido reservado en Zenodo. El registro continúa como borrador y el DOI se activará al publicar el depósito.

## Contenido

| Archivo | Propósito |
|---|---|
| `respuestas_zenodo.csv` | Dataset preparado para depósito abierto |
| `preparar_dataset_zenodo.py` | Genera reproduciblemente el dataset abierto desde `../respuestas_anonimizadas.csv` |
| `diccionario_zenodo.md` | Diccionario específico de las 16 columnas publicables |
| `zenodo_metadata.md` | Metadatos previstos para crear el registro en Zenodo |
| `checksums_zenodo.sha256` | Integridad SHA-256 del paquete de predepósito |

## Procedencia

El conjunto deriva de `../respuestas_anonimizadas.csv`.

Ese archivo, a su vez, se genera reproduciblemente desde la exportación cruda del cuestionario mediante `../scripts/anonimizar_encuesta.py`.

El archivo crudo original no forma parte del paquete abierto.

## Transformaciones para depósito abierto

Respecto de `respuestas_anonimizadas.csv`, `respuestas_zenodo.csv`:

- conserva los 62 registros;
- conserva `ID` como número secuencial de recepción, no como identificador personal;
- conserva las 15 variables sustantivas del cuestionario;
- elimina `Hora de inicio`;
- elimina `Hora de finalización`;
- elimina `Comentarios del cuestionario`;
- elimina las 15 columnas `Comentarios: ...`;
- no imputa, recodifica ni modifica las respuestas conservadas.

El resultado tiene 16 columnas.

## Privacidad

Las columnas directas `Nombre` y `Correo electrónico` fueron eliminadas en la etapa previa de anonimización.

Para el paquete abierto también se retiran las marcas temporales con precisión individual y todas las columnas de texto libre, aun cuando estas últimas se encontraban vacías en los 62 registros analizados.

El paquete no contiene el archivo XLSX crudo ni documentación de consentimiento, nóminas, firmas u otros documentos que puedan contener información identificable.

## Reproducción

Desde la raíz del repositorio:

    python AHMRV/07_Publicacion/dataset_zenodo/preparar_dataset_zenodo.py

La generación es determinista: una segunda ejecución sobre la misma entrada debe producir exactamente el mismo SHA-256.

## Integridad

Desde `AHMRV/07_Publicacion/dataset_zenodo/`:

    sha256sum -c checksums_zenodo.sha256

## DOI y licencia

DOI reservado: `10.5281/zenodo.22236500`. El registro permanece en borrador y todavía no se ha publicado.

La licencia prevista para el depósito es Creative Commons Attribution 4.0 International (CC BY 4.0), de acuerdo con la licencia del material publicado en .
