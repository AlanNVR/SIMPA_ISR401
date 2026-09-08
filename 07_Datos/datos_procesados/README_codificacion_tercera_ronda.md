# Codificación temática — tercera ronda

**Acción:** ACC-01 del Plan de Acción Operativo de Cierre Final SIMPA  
**Estado:** codificación realizada; pendiente revisión cruzada del integrante de apoyo antes de cerrar formalmente la acción.  
**Responsable principal:** Villafuerte Rosero Allan Noé  
**Identificador del analista en el CSV:** `AVR`

## Alcance

Este bloque contiene la codificación temática de las ocho entrevistas ejecutadas en la tercera ronda:

- `ENTR-09` a `ENTR-12`: 31 de agosto de 2026.
- `ENTR-13` a `ENTR-16`: 1 de septiembre de 2026.

Se codificaron **89 fragmentos**, correspondientes a **31 códigos temáticos distintos**. De esos códigos, **20 reutilizan códigos ya presentes** en la codificación de las rondas anteriores y **11 aparecen por primera vez** en la tercera ronda.

## Fuente

La codificación se deriva únicamente de las transcripciones anonimizadas versionadas en:

`02_Evidencias/Transcripciones/`

No se incorporaron fragmentos ni requisitos que no estuvieran respaldados por esas transcripciones o por el ERS vigente.

## Convención de identificadores

La adenda A.14 identifica a los participantes de la tercera ronda como `ENTR-09` a `ENTR-16`. Esos identificadores se conservan aquí.

No se usan `EV-09` a `EV-16` para estas entrevistas porque el catálogo de evidencias del ERS ya utiliza identificadores `EV-09`, `EV-10`, `EV-11`, `EV-12` y `EV-13` para otros artefactos. Reutilizarlos para participantes distintos produciría una colisión de trazabilidad.

La codificación histórica de las ocho primeras entrevistas se conserva sin cambios en:

`../datos_crudos/codificacion.csv`

La integración de ambos bloques para el análisis de saturación se realizará en ACC-02, manteniendo separados el estrato de dominio y el estrato de contraste conforme a A.14/R-14.7.

## Códigos nuevos de la tercera ronda

- `CAPACITACION_USO`
- `CONFIANZA_DIAGNOSTICO`
- `CONTROL_INSUMOS`
- `GPS_EVIDENCIA_LABOR`
- `INTERFAZ_SIMPLE`
- `INTERFAZ_VISUAL`
- `OPERACION_OFFLINE`
- `PLANIFICACION_LABORES`
- `RESISTENCIA_CAMBIO`
- `TUTORIAL_GUIADO`
- `VERIFICACION_DIAGNOSTICO`

Los demás códigos reutilizan el vocabulario temático ya existente para evitar inflar artificialmente la saturación.

## Criterio de codificación

Cada fila contiene un fragmento analítico resumido, un código temático, su categoría, el requisito derivado cuando existe una correspondencia verificable, el identificador de la entrevista y el analista codificador.

Cuando una observación no permite vincular de forma responsable un requisito concreto, `Requisito_derivado` se deja vacío en lugar de inventar una asociación.

## Verificación local recomendada

```bash
python - <<'PY'
import csv
from collections import Counter

p = "07_Datos/datos_procesados/codificacion_tercera_ronda.csv"
with open(p, encoding="utf-8") as f:
    rows = list(csv.DictReader(f, delimiter=";"))

ids = sorted({r["ID_evidencia"] for r in rows})
print("Filas:", len(rows))
print("Entrevistas:", ids)
print("Cantidad de entrevistas:", len(ids))
print("Filas por entrevista:", Counter(r["ID_evidencia"] for r in rows))

assert len(rows) == 89
assert ids == [f"ENTR-{i:02d}" for i in range(9, 17)]
assert all(r["Analista_codificador"] == "AVR" for r in rows)
PY
```

La verificación correcta cuenta identificadores únicos; `grep -c "ENTR-"` no es suficiente porque contaría fragmentos, no entrevistas.
