# Registro de desviaciones y limitaciones

Proyecto SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
Equipo AHMRV
Fecha de actualización: 2026-09-03

Este documento registra únicamente desviaciones, limitaciones y estados
verificados del trabajo realizado. No contiene resultados simulados ni
evidencia fabricada.

---

## D-01 — Potencia experimental prevista inferior al objetivo

**Estado:** abierta / declarada antes de la ejecución.

El diseño experimental contempla 25 pares de requisitos.

La documentación del experimento establece como referencia:

- α = 0,05
- potencia objetivo = 0,80
- tamaño de efecto medio esperado = d = 0,5
- tamaño aproximado requerido = 34 pares

Por tanto, los 25 pares previstos se encuentran por debajo del tamaño requerido
para alcanzar la potencia objetivo bajo esos supuestos.

No se incrementará artificialmente el tamaño muestral mediante duplicación de
requisitos u observaciones.

Esta condición deberá reportarse como amenaza a la validez de conclusión
cuando se ejecute el experimento.

**Fuente documental:**
`06_Experimento/readme.md` y protocolo prerregistrado.

---

## D-02 — Experimento comparativo humano–LLM todavía no ejecutado

**Estado:** abierta.

El protocolo experimental y el registro público en OSF existen, pero el
experimento comparativo entre requisitos generados por el equipo humano y por
el modelo de lenguaje todavía no ha sido ejecutado completamente.

En consecuencia, actualmente no se presentan como resultados reales:

- evaluación a ciegas completa;
- comprobación de ceguera;
- kappa con intervalo de confianza;
- tamaño del efecto con IC del 95 %;
- análisis estadístico final del experimento;
- conclusiones derivadas de dicho experimento.

Los resultados actualmente existentes dentro de `07_Datos/resultados/`
pertenecen al análisis de codificación temática y saturación de entrevistas y
no deben confundirse con los resultados del experimento humano–LLM.

No se incorporarán cifras hipotéticas para completar los entregables.

---

## D-03 — Codificación temática limitada a EV-01–EV-08

**Estado:** abierta.

La versión actualmente documentada de:

`07_Datos/datos_crudos/codificacion.csv`

contiene la codificación real disponible para las evidencias EV-01 a EV-08.

La ejecución de:

`07_Datos/scripts/curva_saturacion.py`

produce actualmente:

- 138 fragmentos codificados;
- 68 códigos únicos;
- análisis de ocho evidencias.

Aunque el proyecto dispone de entrevistas adicionales, EV-09 a EV-16 no están
incorporadas todavía en la codificación temática versionada.

Por esta razón, el script y la curva permanecen limitados a las ocho evidencias
efectivamente codificadas. No se añaden entrevistas a la secuencia sin contar
con una codificación real asociada.

---

## D-04 — Cobertura del cuestionario por perfil ocupacional

**Estado:** limitación documentada.

El conjunto procesado contiene 62 respuestas totales.

Los perfiles con mayor representación observada son:

- Polinización: 18
- Control fitosanitario: 18

Por tanto, no existe un perfil ocupacional individual con 60 respuestas.

El proyecto no debe afirmar que alcanzó un mínimo de 60 respuestas por perfil
dominante cuando los datos disponibles no sostienen esa afirmación.

Esta limitación debe mantenerse visible al interpretar la generalización de los
resultados del cuestionario.

---

## D-05 — Archivo XLSX crudo excluido de publicación abierta

**Estado:** control deliberado de privacidad.

El archivo:

`07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx`

se conserva como exportación primaria para trazabilidad y reproducibilidad.

Sin embargo, no forma parte del depósito abierto ni queda cubierto por la
licencia CC BY 4.0 de los datos abiertos.

Para análisis y publicación se utilizan:

- `07_Datos/datos_procesados/respuestas_anonimizadas.csv`
- `07_Datos/datos_procesados/respuestas_zenodo_agregadas.csv`

La restricción está documentada también en `07_Datos/LICENSE-DATA.txt`.

---

## D-06 — Orquestador único de análisis

**Estado:** cerrada el 2026-09-03.

Se implementó:

`07_Datos/scripts/run_all.py`

La cadena reproducible disponible puede ejecutarse desde la raíz mediante:

`python 07_Datos/scripts/run_all.py`

La ejecución fue verificada sobre los datos reales y reproduce:

- 62 filas × 34 columnas en `respuestas_anonimizadas.csv`;
- 64 filas × 7 columnas en `respuestas_zenodo_agregadas.csv`;
- 8 filas × 7 columnas en `tabla_saturacion.csv`;
- el SHA-256 publicado del dataset agregado de Zenodo.

También se verificaron dos ejecuciones consecutivas con resultados idénticos
para los productos de saturación.

Esta desviación queda cerrada sin extender el alcance al experimento
humano–LLM todavía pendiente.

---

## Cierre de desviaciones

Una desviación solo puede marcarse como cerrada cuando exista evidencia
versionada que demuestre su resolución.

La eliminación de una entrada de este registro no sustituye su cierre:
las desviaciones resueltas deben conservarse con su estado actualizado para
mantener trazabilidad histórica.
