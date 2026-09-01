# Metadatos previstos para Zenodo — Dataset SIMPA

## Estado

**Predepósito. DOI pendiente.**

Este archivo documenta los metadatos que deben utilizarse al crear el registro en Zenodo.
No sustituye al registro de Zenodo ni asigna por sí mismo un DOI.

## Identificación del recurso

- **Título:** SIMPA — Dataset anonimizado del cuestionario de trabajadores para ingeniería de requisitos
- **Tipo de recurso:** Dataset
- **Versión:** 2.0
- **Fecha del material:** 2026-08-31
- **Idioma:** Español
- **Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Proyecto:** SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
- **Institución:** Universidad Técnica Estatal de Quevedo
- **Asignatura:** Ingeniería de Requerimientos (ISR-401)

## Descripción

Conjunto de datos anonimizado derivado de un cuestionario estructurado aplicado a 62 personas trabajadoras de una unidad productiva de palma africana identificada públicamente mediante el seudónimo `Palmicultora M`.

La versión preparada para depósito abierto contiene 62 registros y 16 columnas. Conserva un `ID` secuencial de recepción y 15 variables sustantivas del cuestionario. Se excluyen las columnas directas `Nombre` y `Correo electrónico`, las marcas temporales `Hora de inicio` y `Hora de finalización`, `Comentarios del cuestionario` y todas las columnas `Comentarios: ...`.

El paquete incluye el CSV publicable, el script que lo genera reproduciblemente, el diccionario específico del conjunto y un manifiesto SHA-256. El archivo XLSX crudo, consentimientos, firmas, grabaciones y demás material identificable no forman parte del depósito abierto.

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
- dataset anonimizado
- cuestionario
- agroindustria
- palma africana
- Elaeis guineensis
- SIMPA
- Ecuador

## Relación con el repositorio

- **Repositorio:** https://github.com/AlanNVR/SIMPA_ISR401
- **Ruta del paquete:** `AHMRV/07_Publicacion/dataset_zenodo/`
- **Commit fuente del predepósito:** `7bb587c5c575e00b8204e8ff80ae66a77c30e6ea`

## Archivos previstos para el depósito

- `respuestas_zenodo.csv`
- `diccionario_zenodo.md`
- `preparar_dataset_zenodo.py`
- `readme.md`
- `zenodo_metadata.md`
- `checksums_zenodo.sha256`

## Exclusiones expresas

No deben incorporarse al depósito abierto:

- el archivo XLSX crudo del cuestionario;
- archivos de `AHMRV/02_Evidencias/00_Restringido/`;
- consentimientos con datos personales o firmas;
- grabaciones de audio o video sin anonimizar;
- nóminas o documentos con datos identificables;
- documentos internos cuya licencia no autorice publicación abierta.

## DOI

**Pendiente de reserva/asignación en Zenodo.**

Una vez reservado el DOI, debe registrarse en este archivo, en `dataset_zenodo/readme.md`, en `CITATION.cff` y en los demás puntos documentales que correspondan antes de la publicación final.
