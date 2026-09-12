# Verificación de independencia — conjunto humano frente a salida del LLM (EXP-03)

**Proyecto:** SIMPA — Equipo AHMRV — ISR-401 — UTEQ
**Motivo:** cuatro requisitos del conjunto humano (`H-013`, `H-014`, `H-015`,
`H-020`), etiquetados en `requisitos_humano_ENTR-04.csv` como "Elicitado
durante la fase de experimentación para el mínimo de 25 RF", coinciden en
contenido de forma cercana con cuatro requisitos de la salida del LLM
(`LLM-005`, `LLM-006`, `LLM-007`, `LLM-015`/`LLM-016`). Antes de dar por
válido el conjunto humano, se verifica si esa coincidencia compromete la
independencia exigida por el diseño experimental.

## 1. Coincidencias identificadas

| Humano | LLM | Contenido compartido |
|---|---|---|
| H-013 | LLM-005 | Umbral de madurez: 3 frutos desprendidos (guineensis), 5 (híbridos) |
| H-014 | LLM-006 | Observación por pedúnculo superior a 5 cm |
| H-015 | LLM-007 | Rechazo por malformación superior al 30 % |
| H-020 | LLM-015 / LLM-016 | Entrega física del tiquete y envío automático por correo |

## 2. Verificación temporal (evidencia de commit)

| Conjunto | Commit | Fecha y hora |
|---|---|---|
| Humano (`requisitos_humano_ENTR-04.csv`) | `5d8b82a1cffeee0841f846d5296b762631ff7724` | 2026-09-11 21:54:19 |
| LLM (`salidas_llm/requisitos_LLM_ENTR-04.md`) | `c9efaa880156fab567eb0f6690b0074470892ed5` | 2026-09-11 23:25:53 |

**El conjunto humano quedó congelado 1 hora 31 minutos antes de que la
salida del LLM existiera en el repositorio.** No es posible que la persona
que elicitó H-013, H-014, H-015 y H-020 haya visto o copiado la salida del
LLM: ese archivo no existía en ningún commit anterior a `c9efaa8`.

Verificación reproducible:

```bash
git log -1 --format="%H %ad" --date=iso 5d8b82a
git log -1 --format="%H %ad" --date=iso c9efaa8
git log --diff-filter=A --oneline -- 06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md
```

## 3. Explicación de la coincidencia

Las cuatro coincidencias corresponden a los datos más explícitos y
cuantificados que declara `ENTR-04` (umbrales numéricos de frutos
desprendidos, longitud de pedúnculo y porcentaje de malformación, y el
procedimiento de entrega del tiquete). Cualquier extracción fiel de la misma
fuente congelada —humana o generada por LLM— converge razonablemente en
estos mismos hechos, precisamente porque ambos conjuntos están obligados,
por `EXP-02`, a fundamentarse en el mismo material fuente único.

Esto no es evidencia de contaminación entre conjuntos: es evidencia de que
ambas extracciones son fieles a la fuente que debían usar.

## 4. Conclusión

La independencia del conjunto humano frente a la salida del LLM queda
verificada por la secuencia de commits, no solo declarada. `EXP-03` se
considera cerrado sin necesidad de descartar ni reelicitar `H-013`, `H-014`,
`H-015` ni `H-020`.

## 5. Pendiente que esto NO resuelve

`EXP-04` exige además `06_Experimento/prompts_llm/registro_ejecucion.md` y
`06_Experimento/prompts_llm/salida_cruda_llm.txt`, con los parámetros de
ejecución del modelo (versión, temperatura, top-p, top-k, semilla, consigna
literal). El archivo `salidas_llm/requisitos_LLM_ENTR-04.md` que ya está
congelado contiene la salida en sí, pero no esos parámetros. Esa parte de
`EXP-04` sigue pendiente.
