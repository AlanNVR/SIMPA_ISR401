# Codificación temática

Codificación cualitativa de las 8 entrevistas y su curva de saturación.

| Archivo | Contenido |
|---|---|
| `../../07_Datos/datos_crudos/codificacion.csv` | Códigos aplicados a fragmentos de las transcripciones, por entrevista |
| `../../07_Datos/scripts/curva_saturacion.py` | Script que genera la figura y tabla de saturación a partir del CSV |
| `curva_saturacion.png` | Figura de saturación temática (generada por el script) |

Para regenerar la figura tras editar `../../07_Datos/datos_crudos/codificacion.csv`:
```bash
python3 07_Datos/scripts/curva_saturacion.py 07_Datos/datos_crudos/codificacion.csv
```
Requiere `matplotlib`.
