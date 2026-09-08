# Registro de desviaciones y limitaciones

Proyecto SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana
Equipo AHMRV
Fecha de actualización: 2026-09-07

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

Esta condición deberá reportarse como amenaza a la validez de conclusión cuando
se ejecute el experimento.

**Fuente documental:**
`06_Experimento/readme.md` y protocolo experimental.

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

Los resultados existentes dentro de `07_Datos/resultados/` pertenecen al
análisis de codificación temática y saturación de entrevistas y no deben
confundirse con los resultados del experimento humano–LLM.

No se incorporarán cifras hipotéticas para completar los entregables.

---

## D-03 — Codificación temática limitada inicialmente a las primeras ocho entrevistas

**Estado:** cerrada el 2026-09-07.

La versión histórica de:

`07_Datos/datos_crudos/codificacion.csv`

continúa conservando la codificación de las primeras ocho entrevistas:

- 138 fragmentos;
- 68 códigos únicos;
- identificadores históricos `EV-01` a `EV-08`.

La tercera ronda se codificó de forma separada en:

`07_Datos/datos_procesados/codificacion_tercera_ronda.csv`

con:

- `ENTR-09` a `ENTR-16`;
- 89 fragmentos;
- 31 códigos distintos;
- 20 códigos ya presentes en el estrato de dominio;
- 11 códigos nuevos frente al estrato de dominio.

El script:

`07_Datos/scripts/curva_saturacion.py`

integra ambas fuentes sin reescribir la codificación histórica.

La ejecución verificada produce:

- 227 fragmentos totales;
- 79 códigos únicos en la vista agregada;
- 8 entrevistas en el estrato de dominio;
- 8 entrevistas en el estrato de contraste;
- tres curvas separadas: dominio, contraste y agregada;
- `tabla_saturacion.csv` con 16 filas × 11 columnas.

La separación por estratos responde a la medida metodológica declarada en la
adenda A.14 frente al riesgo de contaminar la interpretación de saturación al
mezclar poblaciones diferentes.

La vista agregada se conserva como descripción global y no como prueba de
saturación homogénea.

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

**Estado:** cerrada; verificación ampliada el 2026-09-07.

Se implementó:

`07_Datos/scripts/run_all.py`

La cadena reproducible puede ejecutarse desde la raíz mediante:

```bash
python 07_Datos/scripts/run_all.py
```

La ejecución verificada sobre datos reales reproduce y comprueba:

- 62 filas × 34 columnas en `respuestas_anonimizadas.csv`;
- 64 filas × 7 columnas en `respuestas_zenodo_agregadas.csv`;
- 16 filas × 11 columnas en `tabla_saturacion.csv`;
- 8 entrevistas de dominio;
- 8 entrevistas de contraste;
- 79 códigos agregados al cierre;
- el SHA-256 publicado del dataset agregado de Zenodo:
  `b40ab460fc1d3d931beebaf5dd3037f564db8774559feee1ec1d371fa01b39b9`.

La ampliación de la cadena incorpora la codificación real de la tercera ronda y
las tres vistas de saturación sin extender el alcance al experimento humano–LLM
todavía pendiente.

---

## D-07 — Rutas históricas del snapshot Zenodo no corregidas

**Estado:** control deliberado de integridad, documentado el 2026-09-06.

Los seis archivos de `08_Publicacion/dataset_zenodo/` citan rutas con el prefijo
`AHMRV/` y la numeración histórica `07_Publicacion`, eliminadas en la
reestructuración del repositorio.

Su `readme.md` declara además el DOI como reservado y la publicación como
pendiente, estado que era correcto al momento de la carga.

Estas referencias no se corrigen. El manifiesto:

`08_Publicacion/dataset_zenodo/checksums_zenodo.sha256`

incluye el hash del propio `readme.md` de la carpeta, por lo que editar el
snapshot rompería la correspondencia con el material efectivamente depositado
bajo el DOI `10.5281/zenodo.22236500`.

La equivalencia entre rutas históricas y rutas vigentes, junto con el estado
real de publicación del depósito, se documenta fuera del snapshot.

---

## Cierre de desviaciones

Una desviación solo puede marcarse como cerrada cuando exista evidencia
versionada que demuestre su resolución.

La eliminación de una entrada de este registro no sustituye su cierre: las
desviaciones resueltas deben conservarse con su estado actualizado para mantener
trazabilidad histórica.
