# Metadatos previstos para Zenodo — Dataset SIMPA

## Estado

**Predepósito. DOI reservado; publicación pendiente.**

Este archivo documenta los metadatos que deben utilizarse al crear el registro en Zenodo.
No sustituye al registro de Zenodo ni activa por sí mismo el DOI.

## Identificación del recurso

- **Título:** SIMPA — Estadística descriptiva agregada del cuestionario de trabajadores para ingeniería de requisitos
- **Tipo de recurso:** Dataset
- **Versión:** 2.0
- **Fecha del material:** 2026-08-31
- **Idioma:** Español
- **Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Proyecto:** SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
- **Institución:** Universidad Técnica Estatal de Quevedo
- **Asignatura:** Ingeniería de Requerimientos (ISR-401)

## Descripción

Resumen estadístico agregado derivado de un cuestionario estructurado aplicado a 62 personas trabajadoras de una unidad productiva de palma africana identificada públicamente mediante el seudónimo `Palmicultora M`.

La versión preparada para depósito abierto representa 15 preguntas sustantivas mediante 64 filas de categorías agregadas y 7 columnas descriptivas. Cada fila corresponde a una opción dentro de una distribución marginal y no a una persona. El archivo no contiene identificadores individuales, nombres, correos electrónicos, marcas temporales, comentarios ni combinaciones de respuestas por participante.

Catorce preguntas son de respuesta simple y una es multirrespuesta. El archivo informa pregunta, tipo de respuesta, opción, frecuencia, número de respuestas válidas y porcentaje. En la pregunta multirrespuesta los porcentajes pueden sumar más de 100 %.

El paquete incluye el CSV agregado, el script que lo genera reproduciblemente, el diccionario del conjunto, estos metadatos y un manifiesto SHA-256. El XLSX crudo, los registros individuales, consentimientos, firmas, grabaciones y demás material identificable no forman parte del depósito abierto.

## Autores

1. Allan Noe Villafuerte Rosero — Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación
2. Denisses Fabiola Huilcapi León — Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación
3. Edson Nagib Rizzo Vélez — Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación
4. Josthyn Esteban Macías Herrera — Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación
5. Francisco Javier Arboleda Yanza — Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación
6. Anderson Adonis Alcívar Vélez — Universidad Técnica Estatal de Quevedo, Facultad de Ciencias de la Computación

Los ORCID se incorporarán únicamente si cada autor dispone de un identificador verificado. No se inventan identificadores.

## Palabras clave

- ingeniería de requisitos
- estadística descriptiva
- datos agregados
- cuestionario
- agroindustria
- palma africana
- Elaeis guineensis
- SIMPA
- Ecuador

## Relación con el repositorio

- **Repositorio:** https://github.com/AlanNVR/SIMPA_ISR401
- **Ruta del paquete:** `AHMRV/07_Publicacion/dataset_zenodo/`
- **Commit con DOI reservado previo a la agregación:** `b5c703e`

## Archivos previstos para el depósito

- `respuestas_zenodo_agregadas.csv`
- `diccionario_zenodo.md`
- `preparar_dataset_zenodo_agregado.py`
- `readme.md`
- `zenodo_metadata.md`
- `checksums_zenodo.sha256`

## Exclusiones expresas

No deben incorporarse al depósito abierto:

- el archivo XLSX crudo del cuestionario;
- `respuestas_zenodo.csv` ni otros registros fila a fila;
- archivos de `AHMRV/02_Evidencias/00_Restringido/`;
- consentimientos con datos personales o firmas;
- grabaciones de audio o video sin anonimizar;
- nóminas o documentos con datos identificables;
- documentos internos cuya licencia no autorice publicación abierta.

## DOI

**DOI reservado en Zenodo: `10.5281/zenodo.22236500`. Registro pendiente de publicación.**

El DOI reservado debe mantenerse sincronizado con `dataset_zenodo/readme.md`, `CITATION.cff` y los demás puntos documentales correspondientes antes de la publicación final.
