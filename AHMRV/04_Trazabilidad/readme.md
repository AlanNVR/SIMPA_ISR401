# Trazabilidad

Esta carpeta contiene la cadena que conecta **el origen de cada requisito con su
implementación**, y la justificación de por qué unos requisitos se construyen
antes que otros.

Son dos archivos y responden a preguntas distintas: la matriz responde *«¿de
dónde salió este requisito y dónde acaba?»*; la priorización responde *«¿por qué
este requisito primero?»*.

---

## 1. `matriz_trazabilidad.csv`

**52 filas**, una por relación trazada. Separador `;`. Los campos con varios
valores van entre comillas (`"EV-01; EV-09"`), de modo que `cut -d';'` los rompe:
use un lector de CSV real.

### Las trece columnas

| # | Columna | Contenido | Ejemplo |
|---|---|---|---|
| 1 | `ID` | Identificador de la fila | `TR-01` |
| 2 | `Ley` | Norma que obliga al requisito, si la hay | `LOPDP` |
| 3 | `Articulo` | Artículo concreto | `Art. 7` |
| 4 | `Objetivo` | Objetivo del proyecto al que sirve | `O6` |
| 5 | `Stakeholder` | Quién lo necesita | `Administrador` |
| 6 | `ID-EV` | **Evidencia de campo que lo origina** | `"EV-01; EV-09"` |
| 7 | `ID-RF` | Requisito resultante | `RF-01` |
| 8 | `Tipo` | Naturaleza del requisito | `RF`, `RNF`, `RD` |
| 9 | `ID-CU` | Caso de uso que lo modela | `CU-11` |
| 10 | `ID-HU` | Historia de usuario | `HU-01` |
| 11 | `ID-CA` | Criterio de aceptación | `CA-01` |
| 12 | `ID-Componente` | Componente que lo implementa | `C-AUTH` |
| 13 | `ID-Mockup` | Interfaz que lo materializa | `MU-01` |

El guion `-` significa que esa relación no aplica, no que falte por rellenar.

### Cómo se lee una fila

De izquierda a derecha, la fila cuenta el recorrido completo de un requisito:

```text
Ley/Artículo  →  Objetivo  →  Stakeholder  →  Evidencia de campo
                                                     ↓
                                            Requisito (RF/RNF/RD)
                                                     ↓
                              Caso de uso → Historia de usuario → Criterio de aceptación
                                                     ↓
                                        Componente  →  Mockup
```

`TR-01`, por ejemplo, dice: la LOPDP en su artículo 7 obliga a algo que sirve al
objetivo O6, que el Administrador necesita, que se observó en las evidencias
EV-01 y EV-09, que se especificó como RF-01, se modeló en CU-11, se escribió como
HU-01 con el criterio CA-01, se implementa en el componente C-AUTH y se ve en el
mockup MU-01.

La cadena permite recorrerla **en los dos sentidos**. Hacia adelante responde
«¿dónde acabó lo que dijo este participante?»; hacia atrás responde «¿por qué
existe esta pantalla?». La segunda dirección es la que un evaluador suele usar.

### Qué contiene actualmente

| Dimensión | Distribución |
|---|---|
| Tipo de requisito | 44 funcionales · 6 no funcionales · 2 de dominio |
| Requisitos distintos trazados | 47 |
| Objetivos del proyecto | O2 (15) · O1 (12) · O4 (11) · O3 (7) · O5 (4) · O6 (3) |
| Origen normativo | 7 filas derivan de la LOPDP; 45 no tienen origen legal |
| Cobertura de modelado | 52 de 52 filas con caso de uso y componente asignados |

### Límites conocidos

- **32 de 52 filas tienen historia de usuario**; las 20 restantes llevan `-`
  porque corresponden a requisitos no funcionales o de dominio, que no se
  expresan como historia.
- **Se utilizan 12 de las 13 evidencias del catálogo.** `EV-10` está declarada en
  el ERS pero no aparece en ninguna fila de la matriz. Es una inconsistencia
  pendiente de resolver: o se traza a algún requisito, o se retira del catálogo.
- La matriz refleja las evidencias de las rondas de campo ya realizadas. Las
  filas correspondientes a la tercera ronda se añadirán cuando esa ronda se
  ejecute.

## 2. `priorizacion_moscow_kano.csv`

**39 requisitos funcionales** priorizados con dos marcos combinados y un cálculo
de coste de retraso.

### Las nueve columnas

| Columna | Contenido |
|---|---|
| `ID-RF` | Requisito priorizado |
| `MoSCoW` | `Must` (21) · `Should` (16) · `Could` (2) |
| `Kano` | Clasificación de satisfacción: `Basica`, `Lineal`, `Atractiva` |
| `Valor_negocio` | Puntuación del valor aportado |
| `Criticidad_temporal` | Cuánto se degrada ese valor si se retrasa |
| `Reduccion_riesgo` | Riesgo que su implementación elimina |
| `Tamano` | Esfuerzo estimado |
| `WSJF` | *Weighted Shortest Job First*: `(valor + criticidad + riesgo) / tamaño` |
| `Justificacion` | Razón textual, **anclada en una evidencia concreta** |

### La columna que importa

`Justificacion` es lo que impide que la priorización sea una opinión. Cada
justificación cita la evidencia que la sostiene:

> `RF-35` · *Bajo costo y alto impacto: evita excluir al 11,3 % del personal sin
> dispositivo (EV-12).*

Un requisito marcado como `Must` sin una evidencia que lo respalde es una
preferencia del equipo, no un hallazgo. Al revisar este archivo, la comprobación
útil es que cada `Must` remita a una `EV-XX` que exista en el catálogo.

### Relación entre ambos archivos

`ID-RF` es la clave que los une. La priorización dice **cuándo** construir cada
requisito; la matriz dice **de dónde viene y en qué se convierte**. Un requisito
que aparece en la priorización pero no en la matriz está priorizado sin origen
trazado, y viceversa.

## 3. Verificación rápida

```bash
# Requisitos priorizados que no aparecen en la matriz
comm -23 <(tail -n +2 priorizacion_moscow_kano.csv | cut -d';' -f1 | sort -u) \
         <(tail -n +2 matriz_trazabilidad.csv | cut -d';' -f7 | tr -d '"' | sort -u)

# Evidencias del catálogo sin ninguna fila que las use
grep -ohE 'EV-[0-9]{2}' matriz_trazabilidad.csv | sort -u
```

## 4. Dónde están los artefactos referenciados

| Referencia | Ubicación |
|---|---|
| `RF-XX`, `RNF-XX`, `RD-XX` | Catálogo de requisitos en `../01_ERS/` |
| `CU-XX` | Casos de uso en `../01_ERS/` y `../03_Modelado/Diagramas_UML/` |
| `MU-XX` | `../03_Modelado/Mockups/` |
| `C-XXXX` | Diagrama de componentes en `../03_Modelado/Diagramas_UML/` |
| `EV-XX` | Catálogo de evidencias en el ERS; los archivos, en `../02_Evidencias/` |
| `O1`–`O6` | Objetivos del proyecto, en el ERS |
