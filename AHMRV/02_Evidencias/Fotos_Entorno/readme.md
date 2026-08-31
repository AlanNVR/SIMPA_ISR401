# Fotografías de entorno y de sesión

**Estado: completo para las rondas realizadas — 16 imágenes, todas anonimizadas.**

Esta carpeta contiene la evidencia fotográfica del trabajo de campo: el entorno
del cultivo y las sesiones de entrevista.

## Criterio de anonimización

Todas las imágenes publicadas aquí cumplen tres condiciones, verificadas antes de
cada carga:

1. **Sin rostros identificables.** Los rostros de participantes están
   enmascarados con un recuadro opaco aplicado sobre la imagen, no mediante una
   capa que pudiera retirarse.
2. **Sin nombres propios en el nombre del archivo.** La nomenclatura es
   `AAAA-MM-DD_Descripcion_ENTR-XX_Tipo.ext`, con el código del participante
   cuando la imagen corresponde a una sesión concreta.
3. **Sin metadatos de geolocalización.** Los datos EXIF, incluida cualquier
   coordenada GPS, se purgan antes de la publicación.

Los originales sin enmascarar no se publican: residen en la zona restringida,
dentro del contenedor cifrado.

## Contenido

**Fotografías de sesión** (una por entrevista, con código de participante):
`ENTR-01`, `ENTR-02` (dos imágenes), `ENTR-03`, `ENTR-04`, `ENTR-05`, `ENTR-06`,
`ENTR-07`, `ENTR-08`.

**Fotografías de entorno** (sin personas, sin código de participante): fruta de
palma polinizada, bomba de riego, detección de plaga, mayón encontrado en la
palma, prueba de humedad, vista general del cultivo y evidencia general de
trabajo de campo.

## Verificación

Estas dos órdenes deben devolver salida vacía desde la raíz del repositorio:

```bash
ls AHMRV/02_Evidencias/Fotos_Entorno/ | grep -E " |[áéíóúñ]"
exiftool -gps:all -r AHMRV/02_Evidencias/Fotos_Entorno/
```

La primera comprueba la nomenclatura; la segunda, la ausencia de geolocalización.
La integridad de cada archivo consta en `checksums.sha256` de la raíz.

## Pendiente

Fotografías de la tercera ronda de trabajo de campo, que aún no se ha ejecutado.
