# Compilar el ERS 2A en Overleaf

**Equipo AHMRV · ISR-401 · UTEQ**

---

## Pasos

1. Entra a [overleaf.com](https://www.overleaf.com) e inicia sesión.
2. **New Project → Upload Project**.
3. Arrastra `overleaf_ERS_SIMPA_2A.zip`. Overleaf lo descomprime solo.
4. En el panel izquierdo, clic derecho sobre **`ERS_SRS_2A_v1.0.tex` → Set as Main File**.
   Este paso es obligatorio: hay seis `.tex` y Overleaf podría elegir el equivocado.
5. **Menu (arriba a la izquierda) → Compiler → pdfLaTeX**.
6. Botón verde **Recompile**.

La primera compilación tarda entre 40 y 90 segundos. Overleaf ejecuta `pdflatex → bibtex → pdflatex → pdflatex` automáticamente; no hay que correr `bibtex` a mano.

**Resultado esperado:** 79 páginas, sin errores. Los avisos amarillos son normales.

---

## Estructura que debe quedar en el proyecto

```
ERS_SRS_2A_v1.0.tex          ← ARCHIVO PRINCIPAL
seccion4_uml.tex
seccion5_priorizacion.tex
seccion6_7_mvp_conclusiones.tex
apendices.tex
referencias.bib
img/
  contexto.pdf
  istar_sd.pdf
  istar_sr.pdf
  casos_uso_general.pdf
  clases_refinado.pdf
  secuencia_CU01.pdf
  secuencia_CU03.pdf
  secuencia_CU06.pdf
  actividad_ciclo_semanal.pdf
  estados_racimo.pdf
  estados_alerta.pdf
  componentes.pdf
  despliegue.pdf
```

Si los `.tex` quedaron dentro de una subcarpeta en vez de la raíz, arrástralos a la raíz o vuelve a subir el ZIP.

---

## Dos paquetes: cuál usar

| | `overleaf_ERS_SIMPA_2A.zip` | `overleaf_ERS_SIMPA_2A_PNG.zip` |
|---|---|---|
| Figuras | PDF vectorial | PNG a 300 dpi |
| Peso del ZIP | **341 KB** | 8,5 MB |
| PDF resultante | **820 KB** | 11 MB |
| Nitidez al ampliar | infinita | limitada |
| Tiempo de compilación | rápido | más lento |

**Usa el primero.** El segundo existe solo por si algún diagrama se viera raro con las figuras vectoriales; ambos producen el mismo documento de 79 páginas.

---

## Ventaja de Overleaf sobre la compilación local

Overleaf trae TeX Live completo, así que **encuentra `IEEEtran.bst`** y la bibliografía sale en formato IEEE de verdad. En instalaciones básicas de TeX Live ese estilo no existe y el documento cae automáticamente a `unsrt`.

Esto lo resuelve solo, gracias a esta línea del preámbulo:

```latex
\IfFileExists{IEEEtran.bst}{\bibliographystyle{IEEEtran}}{\bibliographystyle{unsrt}}
```

No hay que tocar nada. **Verifica al final que la sección de Referencias tenga el formato IEEE**, con los autores en versalitas y el título en cursiva. Es un requisito del gatekeeper G7.

---

## Paquetes que usa el documento

Todos vienen preinstalados en Overleaf:

`inputenc` · `fontenc` · `amsmath` · `geometry` · `graphicx` · `longtable` · `array` · `booktabs` · `xcolor` · `colortbl` · `fancyhdr` · `enumitem` · `caption` · `lastpage` · `titlesec` · `url` · `hyperref` · `hyphenat` · `adjustbox`

Dos merecen mención porque resuelven problemas concretos:

- **`hyphenat`** con la opción `[htt]` permite dividir identificadores como `02_Evidencias/Cuestionario/` dentro de las celdas. Sin él, el texto se sale de las tablas.
- **`adjustbox`** con `max height=0.86\textheight` impide que cualquier figura desborde la página vertical.

---

## Si algo falla

**No compila y el error menciona `bibtex`**
El nombre del archivo tiene dos puntos (`v1.0.tex`). En Overleaf funciona, pero si diera problemas renombra el principal a `ERS_SRS_2A.tex` y vuelve a marcarlo como Main File. No hay que cambiar nada dentro del documento.

**Salen `??` en lugar de números de página o de figura**
Falta una pasada. Pulsa **Recompile** otra vez. Overleaf a veces necesita dos.

**La bibliografía aparece vacía**
Comprueba que `referencias.bib` esté en la raíz, no dentro de `img/`. Luego **Logs → Clear cached files** y recompila.

**Una figura no aparece y sale un recuadro con el nombre**
Falta el archivo en `img/`. Súbelo ahí; el nombre debe coincidir exactamente, respetando mayúsculas.

**Aparece "Compile timed out"**
Solo puede pasar con el paquete PNG. Cambia al paquete de figuras vectoriales.

---

## Antes de entregar

- [ ] 79 páginas, sin errores rojos en el log
- [ ] Tabla de contenido con números correctos, sin `??`
- [ ] Las 13 figuras se ven completas, ninguna cortada
- [ ] Referencias en formato IEEE, 31 entradas
- [ ] El enlace de GitHub en la portada es correcto y está en una sola línea
- [ ] **Download PDF** y renombrar a `ERS_SIMPA_v3.0_A.pdf` para subir al SGA

---

## Recordatorio importante

El repositorio exige el `.tex` fuente junto al PDF en `01_ERS/`. Sube **los seis `.tex`, el `.bib` y la carpeta `img/` completa**, no solo el PDF. El gatekeeper G2 pide que el documento sea reproducible desde el fuente siguiendo las instrucciones del `README.md`.
