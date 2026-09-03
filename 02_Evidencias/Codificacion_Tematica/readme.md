# Codificación temática

Codificación cualitativa de las 8 entrevistas y su curva de saturación.

| Archivo | Contenido |
|---|---|
| `codificacion.csv` | Códigos aplicados a fragmentos de las transcripciones, por entrevista |
| `curva_saturacion.py` | Script que genera la figura y tabla de saturación a partir del CSV |
| `curva_saturacion.png` | Figura de saturación temática (generada por el script) |

Para regenerar la figura tras editar `codificacion.csv`:
```bash
python3 curva_saturacion.py codificacion.csv
```
Requiere `matplotlib`.
