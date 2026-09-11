# EXP-02 — Material fuente congelado: ENTR-04

**Proyecto:** SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana  
**Equipo:** AHMRV — ISR-401 — UTEQ  
**Responsable:** Allan Villafuerte  
**Fecha de congelación:** 2026-09-11  
**Estado:** CERRADO PARA USO EXPERIMENTAL

---

## 1. Fuente seleccionada

El material fuente único para el experimento comparativo humano–LLM es la transcripción anonimizada de la entrevista `ENTR-04`.

- **Ruta canónica:** `02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md`
- **Commit congelado:** `06e241b7ba0ec43d8541c8908bca31a9f7327ffb`
- **Git blob SHA-1:** `0efa1033b697a1b1fa37c4c52235e5ae978f258f`
- **SHA-256 del archivo UTF-8:** `5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313`
- **Tamaño:** `12616` bytes

La combinación de commit, ruta y hashes identifica de forma inequívoca la versión del material que debe emplearse en todas las fases posteriores del experimento.

---

## 2. Verificación de anonimización

Se revisó la versión congelada antes de utilizarla como insumo experimental.

### Identificadores directos

No se observaron en la transcripción:

- nombre o apellido de la persona entrevistada;
- número de cédula o identificador personal;
- teléfono;
- dirección domiciliaria;
- correo electrónico de la persona entrevistada;
- firma;
- nombre de finca asociado a una persona concreta;
- matrícula/placa real de un vehículo;
- nombre propio de la empresa en la que trabaja la persona entrevistada.

La persona aparece únicamente como `ENTREVISTADO-04` y se conserva el rol genérico `Técnico de extractora`, necesario para interpretar el contexto de los requisitos.

### Información contextual conservada

La transcripción menciona lugares geográficos (`Santo Domingo`, `Quinindé`, `San Lorenzo`) y a `Agrocalidad`. Estas referencias describen el contexto sectorial y normativo del discurso y no identifican directamente a la persona entrevistada.

También se describen campos que un sistema o ticket puede contener —por ejemplo nombre del productor, finca, transportista, placa o correo—, pero la transcripción no contiene valores reales de esos campos.

**Conclusión:** la versión congelada se considera apta como material fuente anonimizado para el experimento.

---

## 3. Regla de uso experimental

A partir de este registro:

1. El conjunto de requisitos humanos y el conjunto de requisitos generados por el LLM deben fundamentarse en **esta misma versión de `ENTR-04`**.
2. No se utilizará una versión posterior de la transcripción aunque el archivo canónico sea editado en `main`.
3. No se añadirán al LLM datos de otras entrevistas, contexto del ERS, requisitos existentes, comentarios del equipo ni conocimiento posterior que no forme parte de esta fuente, salvo que el protocolo o la consigna congelada indiquen explícitamente lo contrario.
4. No se recortará selectivamente el contenido para favorecer a uno de los dos grupos.
5. Cualquier transformación puramente de formato deberá conservar el contenido semántico completo y quedar documentada.
6. Antes de ejecutar el LLM o preparar material de evaluación, debe verificarse el SHA-256 del archivo utilizado contra el valor registrado arriba.

---

## 4. Verificación reproducible

Desde un clon del repositorio se puede recuperar exactamente la versión congelada mediante:

```bash
git show 06e241b7ba0ec43d8541c8908bca31a9f7327ffb:02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md > ENTR-04_fuente_experimento.md
```

Verificar SHA-256:

```bash
sha256sum ENTR-04_fuente_experimento.md
```

El resultado esperado es:

```text
5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313  ENTR-04_fuente_experimento.md
```

También puede comprobarse el objeto Git:

```bash
git rev-parse 06e241b7ba0ec43d8541c8908bca31a9f7327ffb:02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md
```

Resultado esperado:

```text
0efa1033b697a1b1fa37c4c52235e5ae978f258f
```

---

## 5. Relación con EXP-01 y tareas siguientes

La desviación metodológica previa al experimento ya se encuentra registrada en `06_Experimento/osf_deviations.md`. EXP-02 no modifica el plan estadístico; únicamente fija el material de entrada para evitar deriva de la fuente durante la ejecución.

Con EXP-02 cerrado, las tareas que pueden continuar son:

- **EXP-03:** seleccionar y congelar el conjunto de requisitos humanos vinculados a esta fuente;
- **EXP-04:** ejecutar el LLM con la consigna congelada y esta misma fuente;
- posteriormente, normalización, cegamiento, aleatorización y evaluación.

---

## 6. Criterio de cierre de EXP-02

EXP-02 se considera cerrado cuando se cumplen simultáneamente estas condiciones:

- [x] `ENTR-04` identificada como fuente común;
- [x] versión fijada mediante commit inmutable;
- [x] Git blob identificado;
- [x] SHA-256 calculado;
- [x] tamaño del archivo registrado;
- [x] anonimización revisada;
- [x] regla de uso común humano–LLM documentada;
- [x] procedimiento de recuperación y verificación reproducible documentado.
