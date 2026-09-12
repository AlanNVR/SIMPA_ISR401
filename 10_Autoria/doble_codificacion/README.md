# AUT-07 — Doble codificación con acuerdo reproducible

**Responsable:** Josthyn Macías · **Codificador 1:** Allan Villafuerte ·
**Codificador 2:** Josthyn Macías · **Apoyo metodológico:** Denisses Huilcapi

## Subconjunto congelado

Se seleccionaron **39 fragmentos** (~17% del corpus total de 227),
estratificados entre las dos rondas de campo:

- **EV-04** (ronda dominio) — 26 fragmentos
- **ENTR-13** (ronda contraste) — 13 fragmentos

Se eligió por estratificación deliberada (una entrevista de cada ronda), no
al azar sobre fragmentos sueltos, para que cada codificador tenga contexto
completo de la entrevista al codificar, no fragmentos descontextualizados.

**El subconjunto quedó congelado el [completar fecha real] con el script
`00_extraer_subconjunto.py`.** No debe volver a ejecutarse: generaría un
nuevo orden de `ID_fragmento` y rompería la comparabilidad.

## Archivos de este directorio

| Archivo | Qué es | Estado |
|---|---|---|
| `subconjunto_fragmentos.csv` | Los 39 fragmentos, SOLO texto + ID de evidencia, sin código | ✅ Generado |
| `codificacion_allan.csv` | Plantilla para que Allan codifique de forma independiente | ⏳ Vacía — pendiente que Allan la complete |
| `codificacion_josthyn.csv` | Plantilla para que Josthyn codifique de forma independiente | ⏳ Vacía — pendiente que Josthyn la complete |
| `calcular_acuerdo.py` | Calcula Kappa de Cohen + IC 95% por bootstrap | ✅ Probado y funcional |
| `resultado_acuerdo.csv` | Salida del script anterior | ⏳ Se genera al correr el script |

## Procedimiento (en este orden, sin saltarse pasos)

1. **Congelar el subconjunto** — ya hecho, no repetir.
2. **Codificación independiente.** Allan y Josthyn completan cada uno su
   propia copia (`codificacion_allan.csv` / `codificacion_josthyn.csv`),
   llenando las columnas `Codigo` y `Categoria` para los 39 fragmentos.
   **Sin verse las hojas entre sí ni consultar la codificación original**
   del corpus completo (`07_Datos/.../codificacion.csv`), para que el
   ejercicio mida acuerdo real, no memoria del esquema ya usado.
3. **Conservar ambas hojas originales** tal como quedaron, sin editarlas
   después de calcular el acuerdo.
4. **Correr el script de cálculo:**
   ```bash
   cd 10_Autoria/doble_codificacion
   pip install scikit-learn numpy --break-system-packages
   python3 calcular_acuerdo.py
   ```
5. **Documentar el resultado** en este README (sección de abajo) y en la
   retrospectiva si el acuerdo resulta bajo — un Kappa bajo no se oculta,
   se declara y se explica (ej. diferencias en el nivel de granularidad del
   esquema de códigos).

## Resultado

*(completar después de que ambas hojas estén codificadas y se corra el
script — no rellenar con datos de prueba ni estimaciones)*

- Porcentaje de acuerdo observado (Po):
- Kappa de Cohen:
- IC 95%:
- Interpretación:
- Fecha de codificación de Allan:
- Fecha de codificación de Josthyn:

## Resultado (actualizado)

- **Fragmentos comparados:** 39
- **Porcentaje de acuerdo observado (Po):** 0,0%
- **Kappa de Cohen:** ~0.000
- **IC 95%:** [0.000, 0.000]
- **Interpretación:** acuerdo insignificante

### Explicación del resultado

El acuerdo salió bajo no por un error de procedimiento, sino por una diferencia
real de esquema de codificación entre ambos codificadores: Josthyn categorizó
por **contenido temático del dominio agrícola** (ej. "Calidad de la fruta",
"Registro operativo", "Tratamiento"), mientras que Allan categorizó por
**tipo de proceso organizacional/cognitivo** (ej. "Comprensión del proceso",
"Gestión de datos", "Control operativo"). Ambos esquemas son coherentes
internamente, pero al no partir de un libro de códigos compartido antes de
codificar, el acuerdo a nivel de código exacto resultó prácticamente nulo.

Esto es un hallazgo metodológico legítimo, no un defecto de los datos: indica
que, de repetirse el ejercicio, el equipo debería acordar un esquema de
codificación común (o al menos las categorías de primer nivel) antes de que
cada codificador trabaje de forma independiente, para que el coeficiente de
acuerdo mida consistencia de aplicación del esquema y no la existencia de
esquemas distintos.

- Fecha de codificación de Josthyn: 2026-09-11
- Fecha de codificación de Allan: 2026-09-11
