# SIMPA_ISR401_Evidencias

Repositorio complementario de evidencias audiovisuales del **Proyecto Fin de Curso SIMPA**
(equipo AHMRV, Ingeniería de Requerimientos ISR-401, UTEQ, Período 2026-2027 PPA).

> **Repositorio principal (documentación, ERS, manuscrito, código):**
> https://github.com/AlanNVR/SIMPA_ISR401

## 1. Por qué existe este repositorio

Los contenedores cifrados de audio y video de las entrevistas de campo superaban
la cuota de almacenamiento/ancho de banda de Git LFS del repositorio principal,
lo que impedía incluso clonar el proyecto con normalidad. Por esa razón el
material audiovisual pesado se aloja aquí, como *assets* de un Release de
GitHub, y no como archivos versionados con Git.

**Este repositorio no contiene código ni documentos del proyecto.** Solo aloja
los contenedores cifrados. Toda la trazabilidad, el ERS, el manuscrito y el
paquete de replicación están en el repositorio principal.

## 2. Origen de la decisión

El uso de un repositorio complementario para el material audiovisual fue
recomendado por el docente responsable de la asignatura.

## 3. Release y contenedores disponibles

**Release:** [`v1.0-evidencias`](https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/tag/v1.0-evidencias)

| Contenedor | Contenido | Participantes cubiertos |
|---|---|---|
| `evidencias_entrevistas_audios.7z` | Audios de entrevista (mp3) | ENTR-01 a ENTR-16 |
| `evidencias_entrevistas_consentimientos.7z` | Consentimientos originales sin enmascarar | ENTR-01 a ENTR-16 |
| `evidencias_entrevistas_videos_01.7z` | Video de entrevista | ENTR-01 |
| `evidencias_entrevistas_videos_02.7z` | Video de entrevista | ENTR-02 |
| `evidencias_entrevistas_videos_03.7z` | Video de entrevista | ENTR-03, ENTR-04 |
| `evidencias_entrevistas_videos_04.7z` | Video de entrevista | ENTR-05 a ENTR-08 |
| `evidencias_entrevistas_videos_05.7z` | Video de entrevista | ENTR-09 a ENTR-16 |

El inventario detallado por archivo individual (nombre, tipo, fecha, código
de participante, duración/tamaño, SHA-256 y contenedor de origen) está en
[`fichas_tecnicas.csv`](https://github.com/AlanNVR/SIMPA_ISR401/blob/main/AHMRV/02_Evidencias/00_Restringido/fichas_tecnicas.csv)
del repositorio principal — no se duplica aquí.

## 4. Procedimiento de descarga, descifrado y verificación

1. Descargar el contenedor `.7z` correspondiente desde la sección
   [Releases](https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases)
   de este repositorio (no requiere `git clone` ni `git lfs`).
2. Descifrar con la contraseña entregada por el canal académico.
3. Verificar la integridad del contenido extraído contra
   `checksums_evidencias.sha256`, en la raíz del repositorio principal:
```bash
   sha256sum -c checksums_evidencias.sha256
```
4. Contrastar cada archivo contra su fila correspondiente en
   `fichas_tecnicas.csv` para confirmar el código de participante (`ENTR-XX`)
   y la técnica asociada.

Cadena de trazabilidad completa:


## 5. Contraseña y acceso

La contraseña de los contenedores cifrados **no se publica en este
repositorio ni en el principal**. Se entrega exclusivamente por el canal
académico correspondiente (Sistema de Gestión Académica), al docente
responsable de la asignatura.

## 6. Licencia y alcance

Este repositorio **no está cubierto por la licencia CC BY 4.0** del
repositorio principal. El material aquí alojado es identificable
(consentimientos originales, video y audio sin anonimizar) y permanece en
zona restringida [R] según la Sección 3 de la guía de la Entrega 4. No se
redistribuye ni forma parte del depósito abierto en Zenodo.
