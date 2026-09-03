# Respuestas del cuestionario

Resultados crudos del cuestionario aplicado a trabajadores (ver
`../cuestionario_aplicado_a_encuestas.md` para el instrumento).

| Archivo | Contenido | Estado |
|---|---|---|
| `Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx` | 62 respuestas individuales, exportación cruda directa del formulario (Google Forms) |  **Evidencia restringida — contiene datos personales** |
| [`../../../07_Publicacion/respuestas_anonimizadas.csv`](../../../07_Publicacion/respuestas_anonimizadas.csv) | Las mismas 62 respuestas, generadas por script a partir del `.xlsx` de esta carpeta |  Zona pública / uso analítico |

##  Estado de anonimización de este archivo

El `.xlsx` de esta carpeta es la **exportación cruda** del formulario y
**conserva las columnas `Correo electrónico` y `Nombre`** tal como las
generó Google Forms. Por esa razón se trata como **evidencia restringida**,
igual que los audios y videos de `02_Evidencias/00_Restringido/`, y **no**
corresponde a la afirmación de "zona pública sin columnas identificativas"
que hace el `README.md` raíz del proyecto para el resto de `02_Evidencias/`.

No se edita el `.xlsx` a mano para evitar contaminar la evidencia primaria.
En su lugar, el script
[`07_Publicacion/scripts/anonimizar_encuesta.py`](../../../07_Publicacion/scripts/anonimizar_encuesta.py)
lee este archivo, elimina las columnas `Correo electrónico` y `Nombre` (y las
columnas auxiliares `Puntos:` sin uso analítico, artefacto de haber aplicado
el formulario como quiz de Forms), y genera
`07_Publicacion/respuestas_anonimizadas.csv`.

**Cualquier análisis, cifra del reporte o dato publicado debe partir de
`respuestas_anonimizadas.csv`, nunca de este `.xlsx`.** El `.xlsx` crudo
permanece aquí únicamente como evidencia primaria verificable, con el mismo
tratamiento de acceso restringido que el resto de la evidencia con datos
personales.

Para regenerar el CSV anonimizado tras cualquier cambio en el crudo:

```bash
python3 07_Publicacion/scripts/anonimizar_encuesta.py \
    "02_Evidencias/Cuestionario/Respuestas/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx" \
    --out 07_Publicacion/respuestas_anonimizadas.csv
```

El resumen y análisis de estas respuestas está en
`../Resultados de la encuesta aplicada a trabajadores.pdf`.
