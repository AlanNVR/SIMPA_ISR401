# Respuestas del cuestionario

Resultados crudos del cuestionario aplicado a trabajadores (ver
`../cuestionario_aplicado_a_encuestas.md` para el instrumento).

| Archivo | Contenido | Estado |
|---|---|---|
| `../../../07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx` | 62 respuestas individuales, exportación cruda directa del formulario (Google Forms) |  **Evidencia restringida — contiene datos personales** |
| [`../../../07_Datos/datos_procesados/respuestas_anonimizadas.csv`](../../../07_Datos/datos_procesados/respuestas_anonimizadas.csv) | Las mismas 62 respuestas, generadas por script a partir del `.xlsx` de esta carpeta |  Zona pública / uso analítico |

##  Estado de anonimización de este archivo

El `.xlsx` canónico ubicado en `07_Datos/datos_crudos/` es la **exportación cruda** del formulario y
**conserva las columnas `Correo electrónico` y `Nombre`** tal como las
generó Google Forms. Por esa razón se trata como **evidencia restringida**,
igual que los audios y videos de `02_Evidencias/00_Restringido/`, y **no**
corresponde a la afirmación de "zona pública sin columnas identificativas"
que hace el `README.md` raíz del proyecto para el resto de `02_Evidencias/`.

No se edita el `.xlsx` a mano para evitar contaminar la evidencia primaria.
En su lugar, el script
[`07_Datos/scripts/anonimizar_encuesta.py`](../../../07_Datos/scripts/anonimizar_encuesta.py)
lee este archivo, elimina las columnas `Correo electrónico` y `Nombre` (y las
columnas auxiliares `Puntos:` sin uso analítico, artefacto de haber aplicado
el formulario como quiz de Forms), y genera
`07_Datos/datos_procesados/respuestas_anonimizadas.csv`.

**Cualquier análisis, cifra del reporte o dato publicado debe partir de
`respuestas_anonimizadas.csv`, nunca de este `.xlsx`.** El `.xlsx` crudo
se conserva en `07_Datos/datos_crudos/` como evidencia primaria verificable, con el mismo
tratamiento de acceso restringido que el resto de la evidencia con datos
personales.

Para regenerar el CSV anonimizado tras cualquier cambio en el crudo:

```bash
python3 07_Datos/scripts/anonimizar_encuesta.py \
    "07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx" \
    --out 07_Datos/datos_procesados/respuestas_anonimizadas.csv
```

El resumen y análisis de estas respuestas está en
`../Resultados de la encuesta aplicada a trabajadores.pdf`.

## Procedencia, consentimiento y limitaciones

**Aplicación.** El cuestionario se aplicó a través de Google Forms. Allan
Villafuerte compartió el enlace con el administrador de Palmicultora M.,
quien lo distribuyó entre los trabajadores operativos. Se recibieron
**62 respuestas**.

**Anonimato del instrumento.** El texto de presentación del cuestionario
indicaba explícitamente: "Su participación es voluntaria y anónima, y la
información se utilizara solo con fines académicos." Ninguna de las 16
preguntas del instrumento solicita nombre, cédula ni ningún dato que
identifique al respondiente (ver `../cuestionario_aplicado_a_encuestas.md`).

**Captura automática de identidad.** Como se explica arriba, en "Estado
de anonimización de este archivo", la exportación cruda sí conserva
columnas `Correo electrónico` y `Nombre` generadas automáticamente por
Google Forms. Ese archivo crudo nunca se usa para análisis ni se
publica; todo resultado se calcula sobre `respuestas_anonimizadas.csv`,
sin esas columnas.

**Consentimiento informado.** La aplicación anónima del cuestionario no
generó, en su momento, un registro de consentimiento informado
independiente y verificable. Por indicación del docente responsable
(aclaración del 14/09/2026), esta limitación se regularizó mediante un
formulario de consentimiento complementario, aplicado a 5 trabajadores
localizables el 15 de septiembre de 2026 — ver
`../Consentimiento_Complementario/readme.md`.
