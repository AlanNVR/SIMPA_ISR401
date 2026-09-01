# Dataset SIMPA — paquete de predepósito Zenodo

## Estado

**Paquete preparado para revisión previa al depósito. DOI reservado: `10.5281/zenodo.22236500`; publicación pendiente.**

El DOI `10.5281/zenodo.22236500` ha sido reservado en Zenodo. El registro continúa como borrador y el DOI se activará al publicar el depósito.

## Contenido

| Archivo | Propósito |
|---|---|
| `respuestas_zenodo_agregadas.csv` | Estadística descriptiva agregada de las 15 preguntas sustantivas |
| `preparar_dataset_zenodo_agregado.py` | Genera reproduciblemente el resumen agregado desde `../respuestas_anonimizadas.csv` |
| `diccionario_zenodo.md` | Diccionario de las 7 columnas del archivo agregado |
| `zenodo_metadata.md` | Metadatos previstos para crear el registro en Zenodo |
| `checksums_zenodo.sha256` | Integridad SHA-256 del paquete de predepósito |

## Procedencia

El resumen deriva de `../respuestas_anonimizadas.csv`, que contiene 62 respuestas al cuestionario.

Ese archivo, a su vez, se genera reproduciblemente desde la exportación cruda mediante `../scripts/anonimizar_encuesta.py`.

El archivo crudo y los registros individuales no forman parte del paquete abierto.

## Transformación para depósito abierto

`respuestas_zenodo_agregadas.csv` publica únicamente distribuciones marginales por pregunta y opción:

- 15 preguntas sustantivas agregadas;
- 64 filas de categorías agregadas;
- 7 columnas descriptivas;
- ninguna fila representa a una persona;
- no contiene `ID`, nombres, correos, marcas temporales ni comentarios;
- para preguntas simples, las frecuencias suman el número de respuestas válidas;
- la pregunta de mayor dificultad es multirrespuesta y usa `;` como separador en el origen, por lo que sus porcentajes pueden sumar más de 100 %;
- no se publican cruces entre variables ni combinaciones de respuestas por participante.

La agregación conserva los valores categóricos observados y calcula frecuencia, número de respuestas válidas y porcentaje para cada opción.

## Privacidad y alcance ético

El consentimiento contempla fines académicos y de publicación científica sin divulgar datos identificables.

El Plan de Gestión de Datos establece que la encuesta se publica como estadística descriptiva y excluye nombres, cédulas, cargos específicos asociados a declaraciones y demás información identificable.

Por ello, el paquete abierto contiene únicamente resultados agregados. El archivo XLSX crudo, los registros individuales, consentimientos, firmas, grabaciones y documentación identificable quedan fuera del depósito.

## Reproducción

Desde la raíz del repositorio:

    python AHMRV/07_Publicacion/dataset_zenodo/preparar_dataset_zenodo_agregado.py

La generación es determinista: una segunda ejecución sobre la misma entrada debe producir exactamente el mismo SHA-256.

## Integridad

Desde `AHMRV/07_Publicacion/dataset_zenodo/`:

    sha256sum -c checksums_zenodo.sha256

## DOI y licencia

DOI reservado: `10.5281/zenodo.22236500`. El registro permanece en borrador y todavía no se ha publicado.

La licencia prevista para el depósito es Creative Commons Attribution 4.0 International (CC BY 4.0), de acuerdo con la licencia de `AHMRV/07_Publicacion/`.
