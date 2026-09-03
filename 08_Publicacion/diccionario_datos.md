# Diccionario de datos — `respuestas_anonimizadas.csv`

**Proyecto SIMPA · Equipo AHMRV · ISR-401 · UTEQ**

---

## 1. Identificación del conjunto

| Campo | Valor |
|---|---|
| Archivo | `07_Publicacion/respuestas_anonimizadas.csv` |
| Codificación | UTF-8 con BOM |
| Separador | coma (`,`) |
| Fin de línea | CRLF |
| Registros | 62 respuestas (una por participante) |
| Columnas | 34 |
| Instrumento | Cuestionario estructurado autoadministrado, aplicado a trabajadores de la unidad productiva `Palmicultora M` |
| Periodo de aplicación | junio de 2026 |

## 2. Procedencia y procesamiento

El archivo **crudo** es la exportación directa de Google Forms:
`02_Evidencias/Cuestionario/Respuestas/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx`.
Ese archivo permanece intacto como evidencia primaria y **no se modifica**.

Este CSV es su única versión procesada. Se genera de forma reproducible con:

```bash
python3 07_Publicacion/scripts/anonimizar_encuesta.py \
  "02_Evidencias/Cuestionario/Respuestas/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx" \
  --out 07_Publicacion/respuestas_anonimizadas.csv
```

El script **elimina columnas, no altera respuestas**: no imputa, no recodifica y no recalcula ningún valor.

### Columnas suprimidas respecto del archivo crudo

| Columna eliminada | Motivo |
|---|---|
| `Nombre` | Dato identificativo directo (checklist §9.3) |
| `Correo electrónico` | Dato identificativo directo |
| Columnas `Puntos: …` | Artefacto de la plantilla *quiz* de Google Forms, sin uso analítico |

En el archivo crudo las columnas `Nombre` y `Correo electrónico` figuraban ya sin contenido real (`anonymous` / vacío), porque el formulario se aplicó sin recolección de identidad. Su supresión elimina también la **cabecera**, que es lo que exige el checklist.

## 3. Estructura de columnas

El formulario genera para cada pregunta un par de columnas: la respuesta y una columna `Comentarios: …` asociada. Las columnas de comentarios están vacías en la totalidad de los 62 registros y se conservan únicamente para preservar la correspondencia uno a uno con el archivo crudo.

| # | Columna | Tipo | Dominio observado |
|---|---|---|---|
| 1 | `ID` | Entero secuencial | 1–62. **No es un identificador de persona**: es el número de orden de recepción asignado por Google Forms |
| 2 | `Hora de inicio` | Marca temporal | `AAAA-MM-DD HH:MM:SS` |
| 3 | `Hora de finalización` | Marca temporal | `AAAA-MM-DD HH:MM:SS` |
| 4 | `Comentarios del cuestionario` | Texto libre | Vacía en los 62 registros |
| 5 | Labor principal que realiza | Nominal | Polinización (18) · Control fitosanitario (18) · Labores de mantenimiento (13) · Riego (11) · Otra (2) |
| 7 | Años de experiencia en el cultivo | Ordinal | Menos de 1 año (14) · De 1 a 5 años (26) · De 6 a 10 años (15) · Más de 10 años (7) |
| 9 | Cómo se registra hoy la labor diaria | Nominal | En papel (42) · El administrador lo anota (13) · No se registra (6) · Otro (1) |
| 11 | Mayor dificultad en el trabajo diario | Nominal múltiple | Respuestas separadas por `;`. Categorías: detectar plagas a tiempo · llevar la cuenta de lo realizado · el clima · saber qué producto aplicar · comunicación con el administrador · otra |
| 13 | Frecuencia de observación de plagas | Ordinal | Nunca (2) · Rara vez (14) · A veces (21) · Frecuentemente (21) · Muy frecuentemente (4) |
| 15 | Usa teléfono inteligente | Dicotómica | `si` (55) · `no` (7). **Valores en minúscula en origen; no se normalizaron** |
| 17 | Comodidad usando aplicaciones | Likert 1–5 | 1 = nada cómodo → 5 = muy cómodo. Distribución: 1(3) 2(5) 3(13) 4(16) 5(25) |
| 19 | Señal de internet en la zona de trabajo | Ordinal | Nunca (1) · Casi nunca (13) · A veces (32) · Siempre (16) |
| 21 | Utilidad — diagnóstico de plaga por foto | Likert 1–5 | 1(1) 3(12) 4(17) 5(32) |
| 23 | Utilidad — deficiencia nutricional por foto de hoja | Likert 1–5 | 1(1) 2(2) 3(15) 4(16) 5(28) |
| 25 | Utilidad — registro de labores en el teléfono | Likert 1–5 | 1(1) 2(4) 3(17) 4(15) 5(25) |
| 27 | Utilidad — conteo automático de flores polinizadas por GPS | Likert 1–5 | 1(2) 2(1) 3(18) 4(19) 5(22) |
| 29 | Utilidad — alertas ante problemas detectados | Likert 1–5 | 1(1) 3(10) 4(19) 5(32) |
| 31 | Preocupación por el registro GPS del recorrido | Ordinal | No me preocupa (46) · Me preocupa un poco (11) · Me preocupa mucho (5) |
| 33 | Usaría la aplicación si fuera fácil y en español | Ordinal | Sí (53) · Tal vez (7) · No (2) |

Las columnas pares 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 y 34 son las columnas `Comentarios: …` de cada pregunta anterior. Todas vacías.

## 4. Advertencias de uso

- **La columna `ID` no permite reidentificación** y no se corresponde con los códigos `ENTR-XX` de las entrevistas. Son poblaciones y técnicas distintas.
- **No hay valores perdidos** en las preguntas cerradas: las 62 respuestas están completas.
- Las marcas temporales se conservan porque no constan entre los datos identificativos que el checklist §9.3 exige suprimir. Si se depositan en un repositorio abierto, considérese su truncamiento a fecha.
- Los tamaños por perfil ocupacional (máximo 18, en Polinización y en Control fitosanitario) están **por debajo del mínimo de 60 respuestas por perfil dominante** que fija la guía. Este conjunto no debe presentarse como si alcanzara ese umbral; la justificación del tamaño alcanzado corresponde al cálculo de potencia, pendiente de elaboración.

## 5. Integridad

El hash SHA-256 de este archivo y de los demás componentes del paquete consta en `07_Publicacion/checksums_paquete.sha256`. Verificación desde `07_Publicacion/`:

```bash
sha256sum -c checksums_paquete.sha256
```
