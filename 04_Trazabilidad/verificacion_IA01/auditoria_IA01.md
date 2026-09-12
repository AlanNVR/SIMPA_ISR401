# IA-01 — Auditoría final de los 6 aspectos del componente inteligente

**Responsable:** Josthyn Macías · **Apoyo:** Francisco Arboleda · **Apoyo
documental:** Denisses Huilcapi · **Verificador:** Allan Villafuerte

**Método:** para cada uno de los 6 aspectos exigidos por la guía se verificó,
contra archivos reales del repositorio (`01_ERS/seccion9_ia.tex`,
`04_Trazabilidad/matriz_e2e.xlsx`, `04_Trazabilidad/backlog_export.csv` y
`04_Trazabilidad/verificacion_IA01/responsables_asignados_IA.csv`), la
presencia de: ID propio, métrica, unidad, umbral, método de verificación,
responsable, frecuencia, vínculo a diseño, caso de prueba.

Convención de esta tabla: **✅** = campo presente y verificado · **⚠️** = campo
ausente o parcial (hallazgo real, no inventado) · **—** = no aplica a ese
aspecto.

**Nota de cierre sobre responsables:** `backlog_export.csv` conserva el estado
histórico exportado desde Jira y, por tanto, mantiene vacío el campo
`Persona asignada` de los 18 requisitos de IA. Como Jira no será modificado,
las responsabilidades finales para el cierre del proyecto se formalizan en
`responsables_asignados_IA.csv`. No se modificó el CSV histórico para simular
asignaciones que no existieron en la exportación original.
---

## 1. Predicción (rendimiento del modelo)

| Campo | IA-01 (clasificador fitosanitario) | IA-02 (madurez / fruta verde) |
|---|---|---|
| ID propio | `RNF-IA-01`, `RNF-IA-02`, `RNF-IA-03` | `RNF-IA-07`, `RNF-IA-08`, `RNF-IA-09` |
| Métrica | Macro-F1; recall de "con afectación" | MAE del % fruta verde; exactitud de madurez |
| Unidad | Adimensional [0,1] | Puntos porcentuales; adimensional |
| Umbral | Macro-F1 ≥ 0,80 · recall ≥ 0,85 · latencia ≤ 10 s (p95) | MAE ≤ 2 p.p. · exactitud ≥ 0,85 · latencia ≤ 15 s (p95) |
| Método de verificación | Conjunto de evaluación del Anexo de datos, antes de cada despliegue | Conjunto de evaluación, antes de cada despliegue |
| Responsable | ✅ Formalizado en `responsables_asignados_IA.csv`; Josthyn Macías para los requisitos de predicción de IA-01 | ✅ Formalizado en `responsables_asignados_IA.csv`; Josthyn Macías para los requisitos de predicción de IA-02 |
| Frecuencia | Antes de cada despliegue (no periódica) | Antes de cada despliegue (no periódica) |
| Vínculo a diseño | `RD-05` (latencia) | — |
| Caso de prueba | ✅ CP-58 a CP-60 (matriz E2E) | ✅ CP-68 a CP-70 (matriz E2E) |

**Estado:** ✅ 9/9 campos completos. La responsabilidad quedó formalizada en el artefacto de cierre; el backlog histórico se conserva sin alterar.

---

## 2. Explicabilidad

| Campo | IA-01 | IA-02 |
|---|---|---|
| ID propio | `RNF-IA-06` | `RNF-IA-12` |
| Métrica | Presencia no omisible de rasgo visual determinante + confianza cualitativa | Presencia no omisible de intervalo de confianza + región de la imagen + comparación histórica |
| Unidad | Booleano (presente/ausente) | Booleano (presente/ausente) |
| Umbral | 100% de las clasificaciones deben incluirlo, sin poder omitirse | 100% de las estimaciones deben incluirlo |
| Método de verificación | Revisión de interfaz — el requisito es de presentación, no numérico | Revisión de interfaz, igual |
| Responsable | ✅ Josthyn Macías, formalizado en `responsables_asignados_IA.csv` | ✅ Josthyn Macías, formalizado en `responsables_asignados_IA.csv` |
| Frecuencia | Cada inferencia (no es una medición periódica) | Cada inferencia |
| Vínculo a diseño | `RNF-19` (equipo de protección/reingreso) | Comparación con calificación histórica del lote |
| Caso de prueba | ✅ CP-67 | ✅ CP-73 |

**Estado:** ✅ 9/9 campos completos. La responsabilidad quedó formalizada en el artefacto de cierre.

---

## 3. Equidad

| Campo | IA-01 | IA-02 |
|---|---|---|
| ID propio | `RNF-IA-04` (variedad), `RNF-IA-05` (gama de dispositivo) | `RNF-IA-10` (cuadrilla), `RNF-IA-11` (variedad) |
| Métrica | Diferencia de macro-F1 entre grupos | Diferencia de MAE entre grupos |
| Unidad | Puntos porcentuales | Puntos porcentuales |
| Umbral | ≤ 5 p.p. (variedad) · ≤ 7 p.p. (dispositivo) | ≤ 1,5 p.p. (cuadrilla) · ≤ 1,5 p.p. (variedad) |
| Método de verificación | Medición trimestral sobre registro de decisiones (`RF-IA-03`) | Medición trimestral sobre registro de decisiones, cuadrilla excluida de entrada |
| Responsable | ✅ Denisses Huilcapi, formalizado en `responsables_asignados_IA.csv` | ✅ Denisses Huilcapi, formalizado en `responsables_asignados_IA.csv` |
| Frecuencia | Trimestral | Trimestral |
| Vínculo a diseño | `RD-01` (dispositivo propio del personal) | `RF-24` (trazabilidad de penalización a cuadrilla) |
| Caso de prueba | ✅ CP-65, CP-66 | ✅ CP-71, CP-72 |

**Estado:** ✅ 9/9 campos completos. Es el aspecto con **mayor severidad de
consecuencia** declarada en el ERS (brecha por cuadrilla → única acción de
suspensión de todo el plan de monitoreo). La responsabilidad quedó formalizada
en el artefacto de cierre.

---

## 4. Supervisión humana

| Campo | Detalle |
|---|---|
| ID propio | `RF-IA-06` |
| Métrica | Tasa de discrepancia humana (persona autorizante se aparta de la estimación del modelo) |
| Unidad | Porcentaje de despachos |
| Umbral | Alerta si > 30% de los despachos |
| Método de verificación | Registro obligatorio de valor humano + valor del modelo + motivo, cuando hay discrepancia |
| Responsable | ✅ Allan Villafuerte, formalizado en `responsables_asignados_IA.csv` |
| Frecuencia | Mensual (según plan de monitoreo) |
| Vínculo a diseño | CU-10 (caso de uso de despacho) |
| Caso de prueba | ✅ CP-61 |

**Estado:** ✅ 9/9 campos completos. La responsabilidad quedó formalizada en el artefacto de cierre.

**Nota de diseño verificada:** el sistema nunca decide de forma vinculante:
`RF-IA-06` exige que la persona pueda apartarse de la estimación en cualquier
momento, y esa discrepancia se usa como señal de monitoreo, no se descarta.

---

## 5. Monitoreo posterior al despliegue

| Campo | Detalle |
|---|---|
| ID propio | No tiene ID de requisito propio — vive como tabla completa en `01_ERS/seccion9_ia.tex`, "Plan de monitoreo en producción" |
| Métrica | 8 indicadores: macro-F1, tasa de abstención, MAE, 3 brechas de equidad, tasa de discrepancia humana, deriva de distribución |
| Unidad | Varía por indicador (p.p., %, distancia estadística) |
| Umbral | Definido individualmente por indicador (ver tabla del ERS) |
| Método de verificación | Comparación contra el umbral de alerta, con acción correctiva declarada por indicador |
| Responsable | ⚠️ No se declara un responsable humano del monitoreo (solo el mecanismo, no la persona) |
| Frecuencia | Mensual (5 indicadores) / Trimestral (3 indicadores) — declarada explícitamente por indicador |
| Vínculo a diseño | Criterio de retirada: 3 incumplimientos consecutivos tras 2 reentrenamientos → vuelve al procedimiento manual (plan de degradación) |
| Caso de prueba | ⚠️ No hay `CP-XX` específico para el plan de monitoreo en sí (los CP existentes verifican los requisitos, no el proceso de monitoreo continuo) |

**Estado:** ⚠️ 6/9 campos completos. Es el aspecto con más hallazgos: **no
tiene ID propio de requisito**, **no tiene responsable humano nombrado**, y
**no tiene caso de prueba propio** — es un plan operativo declarado en texto,
no un requisito trazado en la matriz.

---

## 6. Clasificación de riesgo

| Campo | Detalle |
|---|---|
| ID propio | No tiene ID de requisito — es un análisis narrativo en `01_ERS/seccion9_ia.tex`, "Bloque 5" |
| Métrica | Encaje en las categorías del Reglamento (UE) 2024/1689: alto riesgo (Anexo III) vs. riesgo mínimo |
| Unidad | Categórica (alto riesgo / riesgo mínimo) |
| Umbral | — (no es una métrica numérica, es una determinación normativa) |
| Método de verificación | Análisis razonado: `RF-16` (evaluación de desempeño) es función determinista, no un "sistema de IA" en sentido del reglamento; `IA-01`/`IA-02` clasifican material vegetal, no personas |
| Responsable | ⚠️ No consta un responsable nombrado del análisis de clasificación de riesgo |
| Frecuencia | Una sola vez (análisis de diseño), sin reevaluación periódica declarada |
| Vínculo a diseño | Conecta con `RF-16` y con la decisión de excluir la cuadrilla de las variables de entrada de IA-02 |
| Caso de prueba | ⚠️ No aplica un caso de prueba tradicional — es una determinación documental, no verificable por ejecución |

**Estado:** ⚠️ 5/9 campos aplicables completos (2 campos son "no aplica" por
naturaleza del aspecto, no por omisión). Hallazgo: sin responsable nombrado ni
reevaluación periódica — si el reglamento cambia o el sistema se extiende
(ej. a evaluación de personas), no hay quién revise la clasificación de nuevo.

---

### Hallazgo cerrado durante la auditoría

El campo `Persona asignada` permanece vacío en la exportación histórica de Jira.
Como esa fuente no será modificada, se formalizó la asignación final de los
18 requisitos de IA en `responsables_asignados_IA.csv`. El archivo contiene
18 IDs únicos, sin duplicados, faltantes ni IDs adicionales.

| # | Hallazgo | Aspecto afectado | Acción sugerida |
|---|---|---|---|
| 1 | El plan de monitoreo no tiene ID de requisito propio | Monitoreo posterior | Formalizar el monitoreo como requisito trazable sin alterar los indicadores ya definidos |
| 2 | El plan de monitoreo no tiene caso de prueba en la matriz | Monitoreo posterior | Incorporar el requisito y su caso de prueba correspondiente en la matriz E2E |
| 3 | La clasificación de riesgo no tiene responsable nombrado ni reevaluación periódica | Clasificación de riesgo | Formalizar responsable y condición/frecuencia de reevaluación |

**Nota sobre monitoreo y clasificación de riesgo (hallazgos 2-4):** al no tener
ID de requisito propio, no se pueden asignar en el backlog por fila individual
como los otros 16. Propuesta de responsable a nivel de aspecto, pendiente de
que el equipo decida si se formalizan con ID propio:
- **Monitoreo posterior al despliegue** → Rizzo Vélez Edson Nagib (Verificador,
  coincide con su rol de verificación de calidad continua)
- **Clasificación de riesgo** → Villafuerte Rosero Allan Noe (Analista líder,
  es un análisis normativo/estratégico de alcance del proyecto)

## Lo que SÍ está bien y no requiere acción

- Los 18 requisitos de IA (6 RF-IA + 12 RNF-IA) tienen ID propio, métrica,
  unidad, umbral y método de verificación completos y verificables contra el
  ERS.
- Los 18 tienen caso de prueba trazado en la matriz E2E (`CP-56` a `CP-73`),
  todos con estado de traza "Completa".
- La frecuencia de medición está declarada explícitamente para cada aspecto
  medible (antes de despliegue / mensual / trimestral).
- El vínculo a diseño (RD-01, RD-05, RF-16, RF-24, etc.) es consistente y
  verificable, no una referencia hueca.

---

## Según el plan, próximo paso

> "Si falta un campo: actualizar ERS; matriz E2E; backlog; caso de prueba
> correspondiente. Después volver a ejecutar la verificación ACC-14."

La asignación individual de los 18 requisitos de IA quedó cerrada
documentalmente sin modificar la exportación histórica de Jira. Permanecen
abiertos los aspectos relativos al monitoreo posterior al despliegue y a la
clasificación de riesgo.
