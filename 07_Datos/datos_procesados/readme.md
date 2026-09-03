# Datos procesados

**Estado: pendiente para el experimento — el único dato procesado existente
reside en `07_Publicacion/` junto a su diccionario.**

Esta carpeta alojará los conjuntos derivados del componente experimental: los
datos crudos ya limpiados, recodificados y listos para el análisis.

## Regla de reproducibilidad

Ningún archivo entra en esta carpeta sin cumplir tres condiciones:

1. Procede de un archivo de `../datos_crudos/`, que permanece intacto.
2. Existe el script versionado que lo produce, en `../scripts/`.
3. La transformación aplicada está documentada en un diccionario de datos.

Si un archivo procesado no puede regenerarse ejecutando su script sobre el dato
crudo, no es un dato procesado: es un dato nuevo.

## Datos procesados que ya existen en el repositorio

| Dato | Ubicación | Script que lo genera | Diccionario |
|---|---|---|---|
| Respuestas del cuestionario anonimizadas (62 registros, 34 columnas) | `07_Datos/datos_procesados/respuestas_anonimizadas.csv` | `07_Datos/scripts/anonimizar_encuesta.py` | `07_Publicacion/diccionario_datos.md` |

Se mantiene en `07_Publicacion/` porque forma parte del paquete destinado al
depósito abierto, cuya integridad se verifica con
`07_Publicacion/checksums_paquete.sha256`. No se duplica aquí.

## Contenido previsto

- Conjunto analítico del experimento, una fila por unidad experimental.
- Corpus de salidas del modelo de lenguaje, normalizado y etiquetado.
- Diccionario de datos correspondiente.

## Estado de las dependencias

Depende de que existan datos crudos del experimento, que a su vez dependen de la
ejecución del protocolo. Ambas cosas están pendientes.
