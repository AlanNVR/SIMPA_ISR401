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

## 2. Verificación temporal

### 2.1 Evidencia de commit (insuficiente por sí sola — ver 2.2)

| Conjunto | Commit | Fecha y hora |
|---|---|---|
| Humano (`requisitos_humano_ENTR-04.csv`) | `5d8b82a1cffeee0841f846d5296b762631ff7724` | 2026-09-11 21:54:19 |
| LLM, subida al repositorio (`salidas_llm/requisitos_LLM_ENTR-04.md`) | `c9efaa880156fab567eb0f6690b0074470892ed5` | 2026-09-11 23:25:53 |

Verificación reproducible:

```bash
git log -1 --format="%H %ad" --date=iso 5d8b82a
git log -1 --format="%H %ad" --date=iso c9efaa8
git log --diff-filter=A --oneline -- 06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md
```

Estas horas de commit **no bastan** para probar independencia: solo indican
cuándo cada archivo llegó al repositorio compartido, no cuándo se generó de
verdad el contenido. Al completar `06_Experimento/prompts_llm/2026-09-11_1300_claude-sonnet-5.md`
(EXP-04), se confirmó que la consulta real al modelo se hizo a las
**13:00 del 11 de septiembre** — casi 9 horas *antes* de que el conjunto
humano quedara congelado (21:54), no después como sugería únicamente el
orden de los commits. La salida del LLM ya existía, en la conversación de
Denisses Huilcapi, mientras el conjunto humano todavía se estaba
completando esa tarde.

### 2.2 Confirmación directa del equipo (la prueba real)

Dado que el argumento de commits no cierra la pregunta, se preguntó
directamente a Allan Villafuerte —responsable de `EXP-03` y quien elicitó
`H-013`, `H-014`, `H-015` y `H-020`— si tuvo acceso a la conversación de
Denisses con el modelo antes de terminar el conjunto humano.

**Respuesta de Allan Villafuerte: no tuvo acceso ni conocimiento del
contenido de esa conversación en ningún momento antes de la congelación del
conjunto humano.** La independencia del conjunto humano se sostiene en esta
confirmación directa, no en el orden de los commits.

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
respaldada por la confirmación directa de Allan Villafuerte (Sección 2.2),
no por la secuencia de commits, que por sí sola habría sido insuficiente e
incluso engañosa en este caso. `EXP-03` se considera cerrado sin necesidad
de descartar ni reelicitar `H-013`, `H-014`, `H-015` ni `H-020`.

Se deja constancia de que la primera versión de este documento se apoyó
únicamente en horas de commit y llegó a la conclusión correcta por un
razonamiento incompleto; se corrige aquí en cuanto se dispuso de la hora
real de la consulta al modelo (EXP-04) y de la confirmación directa del
equipo.

## 5. Pendiente que esto NO resuelve

`EXP-04` exige además `06_Experimento/prompts_llm/registro_ejecucion.md` y
`06_Experimento/prompts_llm/salida_cruda_llm.txt`, con los parámetros de
ejecución del modelo (versión, temperatura, top-p, top-k, semilla, consigna
literal). El archivo `salidas_llm/requisitos_LLM_ENTR-04.md` que ya está
congelado contiene la salida en sí, pero no esos parámetros. Esa parte de
`EXP-04` sigue pendiente.
