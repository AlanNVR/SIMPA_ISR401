# Evidencias externas — contenedores audiovisuales

## 1. Motivo

Los contenedores cifrados de audio, video y consentimientos originales de las
entrevistas se alojaban en este repositorio mediante Git LFS. La cuota de
almacenamiento/ancho de banda de Git LFS del repositorio principal se agotó,
impidiendo incluso el clonado normal del proyecto. Por ese motivo, los
contenedores pesados se retiraron de este repositorio y se trasladaron a un
repositorio complementario.

## 2. Origen de la decisión

El uso de un repositorio complementario para el material audiovisual fue una
solución **recomendada personalmente por el docente responsable de la
asignatura**, comunicada de forma verbal. No constituye una autorización
escrita ni un documento formal aparte; se deja constancia de su origen aquí y
en la adenda A.14.

## 3. Repositorio complementario y Release

- Repositorio: `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias`
- Release: `v1.0-evidencias` — `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/tag/v1.0-evidencias`

## 4. Contenedor → participantes → Release → URL

| Contenedor | Participantes incluidos | Release | URL del asset |
|---|---|---|---|
| `evidencias_entrevistas_audios_01.7z` | ENTR-01 a ENTR-08 (8 audios de entrevista) | v1.0-evidencias | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-evidencias/evidencias_entrevistas_audios_01.7z` |
| `evidencias_entrevistas_consentimientos_01.7z` | ENTR-01 a ENTR-08 (8 consentimientos originales sin enmascarar) | v1.0-evidencias | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-evidencias/evidencias_entrevistas_consentimientos_01.7z` |
| `evidencias_entrevistas_videos_01.7z` | ENTR-01, ENTR-02 | v1.0-evidencias | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-evidencias/evidencias_entrevistas_videos_01.7z` |
| `evidencias_entrevistas_videos_02.7z` | ENTR-03 (7 partes), ENTR-04 | v1.0-evidencias | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-evidencias/evidencias_entrevistas_videos_02.7z` |
| `evidencias_entrevistas_videos_03.7z` | ENTR-05, ENTR-06 | v1.0-evidencias | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-evidencias/evidencias_entrevistas_videos_03.7z` |
| `evidencias_entrevistas_videos_04.7z` | ENTR-07, ENTR-08 | v1.0-evidencias | `https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-evidencias/evidencias_entrevistas_videos_04.7z` |

El inventario detallado por archivo individual (nombre, tipo, fecha, código de
participante, SHA-256 y contenedor de origen) está en
[`fichas_tecnicas.csv`](./fichas_tecnicas.csv), en esta misma carpeta.

## 5. Procedimiento de descarga, descifrado y verificación

1. Descargar el contenedor `.7z` correspondiente desde la URL del Release
   indicada en la tabla anterior (no requiere `git clone` ni `git lfs`).
2. Descifrar con la contraseña entregada por el canal académico (ver sección 6).
3. Verificar la integridad del contenido extraído contra
   [`checksums.sha256`](../../../checksums.sha256), en la raíz del repositorio
   principal:
   ```bash
   sha256sum -c checksums.sha256
   ```
4. Contrastar cada archivo contra su fila correspondiente en
   `fichas_tecnicas.csv` para confirmar el código de participante (`ENTR-XX`)
   y la técnica asociada.

La cadena de trazabilidad completa es:

```
ENTR-XX → archivo → fila en fichas_tecnicas.csv → SHA-256
        → contenedor .7z → Release complementario → URL
```

## 6. Contraseña

La contraseña de los contenedores cifrados **no se publica en ningún
repositorio, principal ni complementario**. Se entrega exclusivamente por el
canal académico correspondiente (Sistema de Gestión Académica), al docente
responsable de la asignatura.
