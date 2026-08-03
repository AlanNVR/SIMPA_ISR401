# SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana

Especificación de Requisitos de Software (ERS/SRS) conforme a **ISO/IEC/IEEE 29148:2018**.

> **Proyecto Fin de Curso · Ingeniería de Requerimientos (ISR-401) · 4to Nivel**
> Universidad Técnica Estatal de Quevedo · Facultad de Ciencias de la Computación
> Período 2026–2027 PPA

---

## ⚠️ Dónde está el proyecto

**Todo el contenido evaluable reside en la carpeta [`AHMRV/`](AHMRV/).**

Esta ruta se conserva porque es la declarada en la portada del documento entregado en el SGA. Moverla a la raíz produciría un enlace roto (error 404) y activaría el gatekeeper G1. La decisión y su justificación constan en el Apéndice E del ERS.

```
Villafuerte_Grupo_AHMRV/
├── README.md            ← este archivo
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── checksums.sha256
└── AHMRV/               ← RAÍZ FUNCIONAL DEL PROYECTO
    ├── 01_ERS/
    ├── 02_Evidencias/
    ├── 03_Modelado/
    ├── 04_Trazabilidad/
    ├── 05_MVP/
    ├── 06_Experimento/
    ├── 07_Publicacion/
    └── 08_Etica/
```

---

## El sistema

SIMPA es una aplicación móvil Android con respaldo en la nube para la gestión, el monitoreo y el diagnóstico asistido del cultivo de palma africana (*Elaeis guineensis* e híbridos interespecíficos) en una explotación de aproximadamente cien hectáreas.

Sustituye un proceso que hoy se registra en libretas de papel y se comunica por mensajería instantánea. Incorpora análisis de imágenes para detección de plagas, diagnóstico nutricional y clasificación de madurez del racimo, con requisito de explicabilidad para personal sin formación técnica.

**Organización cliente:** Palmicultora M (seudónimo) · Cantón El Empalme, Guayas, Ecuador
**Segunda organización fuente:** Extractora R (seudónimo)

---

## Equipo AHMRV

| Integrante | Rol |
|---|---|
| Villafuerte Rosero Allan Noe | Analista líder |
| Huilcapi León Denisses Fabiola | Documentadora |
| Rizzo Vélez Edson Nagib | Verificador |
| Macías Herrera Josthyn Esteban | Modelador |
| Arboleda Yanza Francisco Javier | Apoyo modelado |
| Alcívar Vélez Anderson Adonis | Apoyo repositorio |

**Docente responsable:** Ing. Gleiston Cicerón Guerrero Ulloa, PhD

---

## Enlaces principales

| Recurso | Ubicación |
|---|---|
| ERS/SRS completo (PDF) | [`AHMRV/01_ERS/ERS_SRS_2A_v1.0.pdf`](AHMRV/01_ERS/) |
| Fuente LaTeX reproducible | [`AHMRV/01_ERS/`](AHMRV/01_ERS/) |
| Diagramas UML e i\* | [`AHMRV/03_Modelado/`](AHMRV/03_Modelado/) |
| Matriz de trazabilidad | [`AHMRV/04_Trazabilidad/`](AHMRV/04_Trazabilidad/) |
| Prototipo funcional (MVP) | [`AHMRV/05_MVP/`](AHMRV/05_MVP/) |
| Documentación ética | [`AHMRV/08_Etica/`](AHMRV/08_Etica/) |

---

## 🔴 Obtención del repositorio: Git LFS es obligatorio

Los archivos multimedia y los contenedores cifrados se versionan con **Git Large File Storage**. Una clonación sin `git lfs pull` deja archivos de 133 bytes que son punteros, no contenido.

```bash
git clone https://github.com/AlanNVR/Villafuerte_Grupo_AHMRV.git
cd Villafuerte_Grupo_AHMRV
git lfs pull          # OBLIGATORIO — descarga ~1,8 GB de evidencia
```

Si `git lfs` no está instalado: `sudo apt install git-lfs && git lfs install`

---

## Zonas de evidencia

La evidencia se organiza en dos zonas, conforme a la Ley Orgánica de Protección de Datos Personales del Ecuador.

**Zona pública** — `AHMRV/02_Evidencias/`
Transcripciones anonimizadas, consentimientos con cédula y firma enmascaradas, fotografías sin rostros identificables ni coordenadas GPS, respuestas de cuestionario sin columnas identificativas, fichas técnicas de cada archivo multimedia.

**Zona restringida** — `AHMRV/02_Evidencias/00_Restringido/`
Consentimientos originales, videos y audios sin anonimizar. Contenedores cifrados con AES-256.

> **La contraseña de los contenedores se entrega únicamente al docente responsable por el espacio de la actividad en el SGA.** No consta en este repositorio ni en ningún archivo público.

### Verificación de integridad

El hash SHA-256 de cada archivo se calculó **antes** del cifrado y consta en `checksums.sha256` junto con la ficha técnica pública `fichas_tecnicas.csv`.

```bash
# tras descifrar los contenedores en una carpeta de trabajo
sha256sum -c checksums.sha256
```

---

## Reproducir el documento

Desde `AHMRV/01_ERS/`, con TeX Live completo:

```bash
pdflatex ERS_SRS_2A_v1.0.tex
bibtex   ERS_SRS_2A_v1.0
pdflatex ERS_SRS_2A_v1.0.tex
pdflatex ERS_SRS_2A_v1.0.tex
```

Alternativa sin instalación local: subir el contenido de `01_ERS/` a Overleaf, marcar `ERS_SRS_2A_v1.0.tex` como *Main File* y compilar con pdfLaTeX.

**Resultado esperado:** 79 páginas, sin errores.

### Regenerar los diagramas

Desde `AHMRV/03_Modelado/Diagramas_UML/`:

```bash
plantuml -DPLANTUML_LIMIT_SIZE=32768 -tpng -Sdpi=300 -o png *.puml
plantuml -DPLANTUML_LIMIT_SIZE=32768 -tsvg -o svg *.puml
```

> El parámetro `PLANTUML_LIMIT_SIZE` es necesario: el valor por defecto de 4096 px **recorta** diez de los trece diagramas.

---

## Reproducir el análisis experimental

El protocolo está registrado en OSF con fecha anterior a cualquier recolección de datos. El material reside en `AHMRV/06_Experimento/`:

| Archivo | Contenido |
|---|---|
| `protocolo.pdf` | Preguntas de investigación en formato PICOC, hipótesis, variables, plan de análisis estadístico |
| `osf_registration.pdf` | Comprobante de registro previo con URL persistente |
| `instrumentos/` | Guiones de entrevista, cuestionario, rúbrica de evaluación |
| `prompts_llm/` | Consignas exactas con modelo, temperatura, top-p y semilla |
| `scripts_analisis/` | Scripts que reproducen tablas y figuras a partir de los datos crudos |

**Estado:** protocolo diseñado y registrado; ejecución pendiente para la Entrega 4.

---

## Licencia

Ver [`LICENSE`](LICENSE). En resumen:

- **CC BY 4.0** — documento ERS/SRS y conjunto de datos anonimizado
- **MIT** — código fuente del prototipo (MVP)
- **Sin licencia y sin redistribución** — contenido de `02_Evidencias/00_Restringido/`

## Cómo citar

Ver [`CITATION.cff`](CITATION.cff) o usar el botón *Cite this repository* de GitHub.
