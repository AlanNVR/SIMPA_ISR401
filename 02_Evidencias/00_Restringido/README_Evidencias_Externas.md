# SIMPA_ISR401_Evidencias

Repositorio complementario de evidencias audiovisuales del **Proyecto Fin de Curso SIMPA**
(equipo AHMRV, Ingeniería de Requerimientos ISR-401, UTEQ, Período 2026-2027 PPA).

> **Repositorio principal (documentación, ERS, manuscrito, código):**
> https://github.com/AlanNVR/SIMPA_ISR401
>
> **Repositorio de evidencias (este material vive allí):**
> https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias

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

### Evidencia de entrevistas semiestructuradas

| Contenedor | Contenido | Participantes cubiertos |
|---|---|---|
| `evidencias_entrevistas_audios.7z` | Audios de entrevista (mp3) | ENTR-01 a ENTR-16 |
| `evidencias_entrevistas_consentimientos.7z` | Consentimientos originales sin enmascarar | ENTR-01 a ENTR-16 |
| `evidencias_entrevistas_videos_01.7z` | Video de entrevista | ENTR-01 |
| `evidencias_entrevistas_videos_02.7z` | Video de entrevista | ENTR-02 |
| `evidencias_entrevistas_videos_03.7z` | Video de entrevista | ENTR-03, ENTR-04 |
| `evidencias_entrevistas_videos_04.7z` | Video de entrevista | ENTR-05 a ENTR-08 |
| `evidencias_entrevistas_videos_05.7z` | Video de entrevista | ENTR-09 a ENTR-16 |

### Evidencia de validación por walkthrough

| Contenedor | Contenido | Participantes cubiertos |
|---|---|---|
| `Consentimientos_Walkthrough_Originales.7z` | Consentimientos originales sin enmascarar | WT-01 a WT-06 |
| `Actas_Walkthrough_Originales.7z` | Actas de sesión originales firmadas | WT-01 a WT-06 |
| `evidencias_walkthrough_videos.7z` | Grabaciones de pantalla de las sesiones | WT-01 a WT-06 |

### Evidencia de miembro-verificación

| Contenedor | Contenido | Participantes cubiertos |
|---|---|---|
| `Actas_MemberCheck_Originales.7z` | Actas individuales originales firmadas | ENTR-01, ENTR-02, ENTR-13 |
| `Actas_MemberCheck_consolidada_original.7z` | Acta consolidada de la ronda, original firmada | Ronda completa — código `CONSOLIDADA-MC` |

### Evidencia de gobernanza del equipo

| Contenedor | Contenido | Participantes cubiertos |
|---|---|---|
| `Declaracion_Identidades_git_original.7z` | Declaración de identidades Git, impresa, firmada por los seis integrantes y escaneada | Equipo AHMRV — código `CONSOLIDADA-EQUIPO` |

**Ningún nombre de contenedor lleva sufijo `_01`** salvo los cinco de video de
entrevistas, numerados de `_01` a `_05`.

El inventario detallado por archivo individual (nombre, tipo, fecha, código
de participante, duración/tamaño, SHA-256 y contenedor de origen) está en
[`fichas_tecnicas.csv`](https://github.com/AlanNVR/SIMPA_ISR401/blob/main/02_Evidencias/00_Restringido/fichas_tecnicas.csv),
en esta misma carpeta, con **71 filas** — no se duplica aquí. El reporte
[`verificacion_fichas.md`](https://github.com/AlanNVR/SIMPA_ISR401/blob/main/02_Evidencias/00_Restringido/verificacion_fichas.md)
comprueba por petición HTTP que cada contenedor declarado existe con ese nombre
exacto.

> **Sobre los dos últimos contenedores.** El acta consolidada de
> miembro-verificación y la declaración de identidades Git no corresponden a un
> participante individual, sino a la ronda completa y al equipo en su
> conjunto. Por ello se identifican con los códigos `CONSOLIDADA-MC` y
> `CONSOLIDADA-EQUIPO` en lugar de un código `ENTR-XX` o `WT-XX`, y sus
> SHA-256 se calcularon sobre el documento original antes de cifrar, igual que
> el resto del inventario.

## 4. Cifrado

Todos los contenedores son `.7z` generados con **cifrado de cabecera**
(`-mhe=on`): sin la contraseña no puede listarse siquiera el nombre de los
archivos que contienen. Es una medida deliberada, porque esos nombres incluyen
el rol o el perfil del participante.

## 5. Procedimiento de descarga, descifrado y verificación

1. Descargar el contenedor `.7z` correspondiente desde la sección
   [Releases](https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases)
   de este repositorio (no requiere `git clone` ni `git lfs`).
2. Verificar la suma del contenedor descargado contra el SHA-256 que GitHub
   publica junto a cada asset en la página del Release.
3. Descifrar con la contraseña entregada por el canal académico.
4. Verificar la integridad del contenido extraído contra
   `checksums_evidencias.sha256`, en la raíz del repositorio principal:

```bash
sha256sum -c checksums_evidencias.sha256
```

5. Contrastar cada archivo contra su fila correspondiente en
   `fichas_tecnicas.csv` para confirmar el código de participante y la técnica
   asociada.

Cadena de trazabilidad completa:

```text
ENTR-XX / WT-XX → archivo → fila en fichas_tecnicas.csv → SHA-256
                → contenedor .7z → Release del repositorio complementario → URL
```

## 6. Códigos de participante

| Código | Alcance |
|---|---|
| `ENTR-XX` | Entrevistas semiestructuradas y miembro-verificación individual — ENTR-01 a ENTR-16 |
| `WT-XX` | Validación por walkthrough — WT-01 a WT-06 |
| `CONSOLIDADA-MC` | Acta consolidada de la ronda de miembro-verificación, no de un participante |
| `CONSOLIDADA-EQUIPO` | Declaración de identidades Git, firmada por los seis integrantes |

Las series `ENTR-XX` y `WT-XX` no se cruzan. Cuando un participante de
walkthrough fue también entrevistado, recibe igualmente un código `WT-XX`
propio, y la correspondencia entre ambos códigos se registra únicamente en la
zona restringida. Publicar esa correspondencia aumentaría el riesgo de
reidentificación.

Los dos códigos `CONSOLIDADA-*` no son una serie de participantes: se usan una
sola vez cada uno, para el documento específico que describen.

## 7. Contraseña y acceso

La contraseña de los contenedores cifrados **no se publica en este
repositorio ni en el principal**. Se entrega exclusivamente por el canal
académico correspondiente (Sistema de Gestión Académica), al docente
responsable de la asignatura.

## 8. Licencia y alcance

Este repositorio **no está cubierto por la licencia CC BY 4.0** del
repositorio principal. El material aquí alojado es identificable
(consentimientos y actas originales, firmas manuscritas, video y audio sin
anonimizar) y permanece en zona restringida [R] según la Sección 3 de la guía
de la Entrega 4. No se redistribuye ni forma parte del depósito abierto en
Zenodo.
