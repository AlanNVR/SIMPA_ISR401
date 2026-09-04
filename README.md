# SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana

Especificación de Requisitos de Software (ERS/SRS) conforme a **ISO/IEC/IEEE 29148:2018**, con prototipo funcional y paquete de replicación.

> **Proyecto Fin de Curso · Ingeniería de Requerimientos (ISR-401) · 4to Nivel**
> Universidad Técnica Estatal de Quevedo · Facultad de Ciencias de la Computación
> Período 2026–2027 PPA

---

## El sistema

SIMPA da soporte a la gestión, el monitoreo y el diagnóstico asistido del cultivo de palma africana (*Elaeis guineensis* e híbridos interespecíficos) en una explotación de aproximadamente cien hectáreas.

Sustituye un proceso que hoy se registra en libretas de papel y se comunica por mensajería instantánea: registro de labores, control de lotes, detección de plagas y enfermedades, alertas tempranas, seguimiento de recorridos de polinización y reportes. Incorpora un **componente inteligente** especificado conforme al Reglamento (UE) 2024/1689, con requisitos de predicción, explicabilidad, equidad, supervisión humana, monitoreo posterior al despliegue y clasificación de nivel de riesgo.

**Organización cliente:** Palmicultora M (seudónimo) · Cantón El Empalme, Guayas, Ecuador
**Segunda organización fuente:** Extractora R (seudónimo)

> **Estado del prototipo:** aplicación frontend académica con persistencia en el navegador. No existe backend productivo, base de datos remota, inferencia de IA validada ni geolocalización real. Los flujos afectados están declarados uno a uno en [`05_MVP/readme.md`](05_MVP/readme.md).

---

## Los tres repositorios del proyecto

| Repositorio | Qué contiene | Enlace |
|---|---|---|
| **Principal** | Documentación, ERS, modelado, trazabilidad, datos, publicación, ética y defensa. Es este repositorio | <https://github.com/AlanNVR/SIMPA_ISR401> |
| **Prototipo** | Código fuente del MVP (V1 y V2) | <https://github.com/jmaciasherr4/Prottotipo_Simpa> |
| **Evidencias** | Audio, video y consentimientos originales, en contenedores cifrados publicados como assets de release | <https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias> |

La separación no es arbitraria. El material audiovisual supera la cuota de almacenamiento de Git LFS, y el contenido identificable no puede residir en un repositorio público sin cifrar. Ambas decisiones están documentadas.

---

## Estructura del repositorio

```
SIMPA_ISR401/
├── 01_ERS/            Documento ERS/SRS v2.0, fuente LaTeX modular, anexos CCB y RFC
├── 02_Evidencias/     Transcripciones, consentimientos, cuestionario, codificación, walkthrough
├── 03_Modelado/       13 diagramas UML e i* en PlantUML (PNG y SVG) + mockups
├── 04_Trazabilidad/   Matriz extremo a extremo, matriz CSV, backlog de Jira, priorización
├── 05_MVP/            Documentación del prototipo y puntero al repositorio de código
├── 06_Experimento/    Protocolo, registro previo en OSF, consignas de LLM
├── 07_Datos/          Paquete de datos: crudos, procesados, scripts, resultados, diccionario
├── 08_Publicacion/    Manuscrito LNCS, evaluación FAIR, instantánea del depósito Zenodo
├── 09_Etica/          Anexos A01–A14, adendas, documentación de Categoría C
├── 10_Autoria/        Evidencia de autoría y declaración de identidades de Git
├── 11_Defensa/        Guion de exposición, guion de demostración, preguntas previsibles
├── CHANGELOG.md · CITATION.cff · LICENSE · README.md
├── checksums.sha256 · checksums_evidencias.sha256
└── .gitattributes · .gitignore · .mailmap
```

---

## Obtener el repositorio

```bash
git clone https://github.com/AlanNVR/SIMPA_ISR401.git
cd SIMPA_ISR401
```

Eso es todo. **No se requiere Git LFS**: se evaluó su uso para la evidencia audiovisual y se descartó al agotarse la cuota de almacenamiento. No queda ninguna regla `filter=lfs` ni ningún puntero en el árbol. La evidencia pesada se obtiene desde el repositorio complementario, como se explica más abajo.

---

## Dónde está el prototipo

El código vive en un repositorio propio; aquí reside su documentación.

| Recurso | Ubicación |
|---|---|
| Documentación del prototipo | [`05_MVP/readme.md`](05_MVP/readme.md) |
| Código fuente | <https://github.com/jmaciasherr4/Prottotipo_Simpa> |
| Commit evaluado | `ba33002dcf680f8b39d42df04553733bd5389f6d` (2026-08-31) |
| Árbol canónico de la V2 | `prototipo_v2/Prottotipo_Simpa-main/Prototipo/` |
| **Demostración en vivo (V2)** | <https://simpav2-prototipo.netlify.app/> |
| Demostración en vivo (V1, anterior) | <https://prototipo-simpa.netlify.app/> |

### Cuentas de demostración

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `supervisor` | `super123` | Supervisor |
| `operario` | `oper123` | Operario |

> Cuentas de demostración únicamente. No deben utilizarse con información real.

`05_MVP/readme.md` declara, requisito por requisito, qué flujos son funcionales y cuáles son interfaz simulada. Los flujos de análisis por imagen (`RF-07`, `RF-08` y la clasificación visual de `RF-21`) y el conteo georreferenciado (`RF-14`) **no realizan inferencia ni geolocalización reales**.

---

## Dónde está la evidencia

La evidencia se organiza en dos zonas, conforme a la Ley Orgánica de Protección de Datos Personales del Ecuador.

### Zona pública — en este repositorio

`02_Evidencias/` contiene transcripciones anonimizadas bajo `ENTREVISTADO-NN`, consentimientos con nombre y firma enmascarados, fotografías sin rostros identificables ni coordenadas, respuestas del cuestionario sin columnas identificativas, y el inventario técnico de cada archivo multimedia.

### Zona restringida — en el repositorio complementario

El material identificable —audio, video y consentimientos originales— se publica cifrado como assets de release en <https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias>, release `v1.0-evidencias`.

Los contenedores `.7z` llevan **la cabecera cifrada**: sin la contraseña no puede listarse siquiera el nombre de los archivos, que incluyen el rol del participante.

> **La contraseña se entrega únicamente al docente responsable, por el espacio de la actividad en el SGA.** No consta en este repositorio ni en ningún archivo público.

### Inventario y verificación

| Archivo | Qué contiene |
|---|---|
| [`02_Evidencias/00_Restringido/fichas_tecnicas.csv`](02_Evidencias/00_Restringido/fichas_tecnicas.csv) | Una fila por archivo: tipo, fecha, código de participante, duración, códec, tamaño, SHA-256 precifrado, contenedor, ruta interna y URL del release |
| [`02_Evidencias/00_Restringido/verificacion_fichas.md`](02_Evidencias/00_Restringido/verificacion_fichas.md) | Reporte generado por script que comprueba **por petición HTTP** que cada contenedor declarado existe con ese nombre exacto |
| `checksums_evidencias.sha256` | Sumas del contenido interno de los contenedores, calculadas antes de cifrar |

El inventario usa delimitador `;` y cubre las dos series de códigos: `ENTR-01` a `ENTR-16` para las entrevistas semiestructuradas y `WT-01` a `WT-06` para las sesiones de validación por walkthrough. Las series son independientes y no se cruzan.

---

## Reproducir el documento

Desde `01_ERS/`, con TeX Live completo:

```bash
pdflatex ERS_SRS_2B_v2.0.tex
bibtex   ERS_SRS_2B_v2.0
pdflatex ERS_SRS_2B_v2.0.tex
pdflatex ERS_SRS_2B_v2.0.tex
```

Alternativa sin instalación local: subir el contenido de `01_ERS/` a Overleaf, marcar `ERS_SRS_2B_v2.0.tex` como *Main File* y compilar con pdfLaTeX.

**Resultado esperado:** 108 páginas, sin errores graves ni referencias o citas indefinidas.

### Regenerar los diagramas

Desde `03_Modelado/Diagramas_UML/`:

```bash
plantuml -DPLANTUML_LIMIT_SIZE=32768 -tpng -Sdpi=300 -o png *.puml
plantuml -DPLANTUML_LIMIT_SIZE=32768 -tsvg -o svg *.puml
```

> El parámetro `PLANTUML_LIMIT_SIZE` es necesario: el valor por defecto de 4096 px **recorta** diez de los trece diagramas.

---

## Reproducir el análisis de datos

Punto de entrada único, desde la raíz del repositorio:

```bash
python 07_Datos/scripts/run_all.py
```

La cadena parte de los datos crudos y regenera todo lo derivado:

```
XLSX del cuestionario  → anonimizar_encuesta.py            → respuestas_anonimizadas.csv
                       → preparar_dataset_zenodo_agregado.py → respuestas_zenodo_agregadas.csv
codificacion.csv       → curva_saturacion.py               → tabla_saturacion.csv
                                                           → curva_saturacion.png / .pdf
```

**Resultado esperado:** 62 × 34, 64 × 7 y 8 × 7 respectivamente.

Verificar la integridad de lo regenerado:

```bash
cd 07_Datos && sha256sum -c checksums_datos.sha256
```

> Los tres CSV son idénticos bit a bit entre entornos. Las figuras pueden diferir en bytes según la versión de Matplotlib y de las fuentes del sistema, sin que cambie su contenido.

Cada columna de cada conjunto está documentada en [`07_Datos/diccionario_datos.csv`](07_Datos/diccionario_datos.csv). Las limitaciones conocidas están registradas en [`07_Datos/desviaciones.md`](07_Datos/desviaciones.md).

---

## Estudio empírico

El protocolo está registrado en OSF con fecha anterior a cualquier recolección de datos. El material reside en `06_Experimento/`.

**Estado: protocolo diseñado y preregistrado; ejecución pendiente.** El cuasi-experimento comparativo requiere evaluadores externos y no se ha realizado. En consecuencia, el manuscrito no contiene secciones de resultados ni de discusión, y así lo declara su propio encabezado.

Esta limitación se declara en lugar de suplirse con cifras estimadas.

---

## Publicación y datos abiertos

| Recurso | Referencia |
|---|---|
| Depósito de datos | DOI de versión `10.5281/zenodo.22236500` · DOI conceptual `10.5281/zenodo.22236499` |
| Registro | <https://zenodo.org/records/22236500> |
| Instantánea depositada | [`08_Publicacion/dataset_zenodo/`](08_Publicacion/dataset_zenodo/) |
| Evaluación FAIR | [`08_Publicacion/fair_assessment.pdf`](08_Publicacion/) — F-UJI 4.0.0: **24/26 indicadores, 92,31 %, nivel avanzado** |
| Manuscrito | [`08_Publicacion/manuscrito_final.pdf`](08_Publicacion/) — plantilla oficial Springer LNCS |
| Archivado de código | Software Heritage, SWHID declarado en [`CITATION.cff`](CITATION.cff) |

`08_Publicacion/dataset_zenodo/` es una **instantánea congelada** atada al DOI. Sus rutas internas son deliberadamente históricas y no se corrigen: alterarlas rompería la correspondencia con lo depositado.

---

## Equipo AHMRV

| Integrante | Rol |
|---|---|
| Villafuerte Rosero Allan Noé | Analista líder |
| Huilcapi León Denisses Fabiola | Documentadora |
| Rizzo Vélez Edson Nagib | Verificador y gestor de evidencias |
| Macías Herrera Josthyn Esteban | Modelador |
| Arboleda Yanza Francisco Javier | Apoyo modelado y repositorio |
| Alcívar Vélez Anderson Adonis | Apoyo repositorio |

**Docente responsable:** Ing. Gleiston Cicerón Guerrero Ulloa, PhD

Las contribuciones se atribuyen mediante `.mailmap`, que normaliza el historial a seis autores con correo institucional. El detalle consta en [`10_Autoria/declaracion_identidades_git.md`](10_Autoria/declaracion_identidades_git.md).

---

## Licencia

Ver [`LICENSE`](LICENSE). En resumen:

- **CC BY 4.0** — documento ERS/SRS y conjunto de datos anonimizado
- **MIT** — código fuente del prototipo
- **Sin licencia y sin redistribución** — contenido identificable de la zona restringida

## Cómo citar

Ver [`CITATION.cff`](CITATION.cff) o usar el botón *Cite this repository* de GitHub.
