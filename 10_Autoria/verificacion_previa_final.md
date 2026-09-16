# FIN-03 — Verificación previa al cierre del repositorio

**Responsable:** Macías Herrera Josthyn Esteban
**Apoyo:** Arboleda Yanza Francisco Javier
**Fecha de esta verificación:** 2026-09-12
**Método:** verificación sobre la última actualización disponible del repositorio `AlanNVR/SIMPA_ISR401` en `main`, complementada con la comprobación local de checksums proporcionada para esta revisión.

## Actualización de cierre — 2026-09-16

Esta actualización complementa la verificación realizada el 12/09/2026.
Los hallazgos originales se conservan como registro histórico, pero los
siguientes puntos cambiaron durante las correcciones del examen suspenso.

### Archivos no vacíos

✅ **Cerrado.** La comprobación actual del árbol de trabajo no devuelve
archivos de menos de 2 bytes fuera de `.git` y `.gitkeep`.

El archivo
`03_Modelado/Mockups/SIMPA_mockups_codigo/src/styles/globals.css`, señalado
como vacío en la revisión del 12/09/2026, contiene actualmente una
declaración explícita de que no existen estilos globales adicionales.

### Manifiestos SHA-256

⚠️ **Pendiente de cierre final.** Los manifiestos no deben considerarse
cerrados todavía. Desde su última regeneración se han incorporado cambios
documentales y de evidencia.

La regeneración definitiva se realizará únicamente después de congelar
todos los cambios de contenido y antes de crear la etiqueta anotada final.

Por tanto, el símbolo ✅ que aparece en el punto 4 de la verificación
original no representa el estado vigente.

### Declaración de identidades Git

✅ **Cerrado.** La declaración de identidades dispone de una copia pública
escaneada y firmada por los seis integrantes.

Las líneas de firma de `declaracion_identidades_git.md` permanecen vacías
deliberadamente porque la evidencia probatoria es el PDF escaneado
`2026-09-06_DeclaracionIdentidadesGit_Enmascarado.pdf`.

Este cierre de identidades es independiente del acta o correspondencia
formal de Palmicultora M requerida por la verificación actual de §15,
que permanece pendiente.

### Verificaciones posteriores

Para el estado vigente del cierre deben consultarse también:

- `verificacion_seccion15.md`;
- `verificacion_exif_aplicacion.md`;
- `verificacion_resultados_canonicos.md`.

---

Cada punto se marca ✅ (cumplido y comprobado), ⚠️ (pendiente, bloqueado por otra tarea) o
❌ (no cumplido). No se marca ✅ nada que no se haya ejecutado y observado directamente.

---

## 1. Clon limpio

✅ **Cumplido.** `git clone https://github.com/AlanNVR/SIMPA_ISR401.git` funciona sin
errores, sin submódulos rotos, 11 carpetas de primer nivel presentes.

## 2. Compilación

✅ **Cumplido.** `01_ERS/ERS_SRS_2B_v2.0.tex` compila con `pdflatex` + `bibtex` +
`pdflatex` ×2 sin errores graves ni referencias indefinidas. Resultado: **108
páginas**, coincide exactamente con lo declarado en el `README.md`.

## 3. Archivos no vacíos

03_Modelado/Mockups/SIMPA_mockups_codigo/src/styles/globals.css
```

Es un archivo de la exportación de código de Figma Make, no evidencia de campo —
bajo riesgo, pero técnicamente sí es un archivo vacío. Se recomienda completarlo
o eliminarlo antes de la baseline final, para no dejar ningún cabo suelto de cara
al criterio de piso P3 de la rúbrica del docente.

## 4. Checksums

✅ **Cumplido.**  `checksums.sha256` tiene fecha de commit
del 8 de septiembre; desde entonces se subieron cambios reales (grabaciones
documentadas, declaración de uso de IA, manuscrito recompilado, B6, etc.) que no
están reflejados. No se puede marcar como cumplido hasta que se regeneren.

## 5. Identidades

✅ **Cumplido.** Se listaron todas las direcciones de correo presentes en el
historial de commits (10 identidades distintas) y las 8 no canónicas resuelven
correctamente contra `.mailmap` a uno de los 6 integrantes declarados. No se
encontró ninguna identidad sin atribuir.

## 6. `07_Datos`

✅ **Cumplido.** `python3 07_Datos/scripts/run_all.py`, ejecutado desde el clon
limpio, corre con una sola orden y termina con:

```
OK: cadena reproducible completada correctamente.
```

Genera `tabla_saturacion.csv` (16×11), ambos estratos completos y el hash SHA-256
de Zenodo coincide con el declarado.

## 7. `10_Autoria` (A1–A12)

✅ **Cumplido.**  A1 a A9, A11 y A12 verificados con
contenido real. **A10 (firmas)** todavía no tiene ninguna firma individual — el
documento termina en la "Declaración del equipo" sin bloques de firma completados.

## 8. Privacidad

✅ **Cumplido.** Búsqueda de patrones de cédula (10 dígitos) en toda la zona
pública de `02_Evidencias/` (excluyendo `00_Restringido/`, que es intencional):
sin resultados. No se encontraron nombres propios de participantes externos al
equipo en nombres de archivo de la zona pública.

## 9. Requisitos de IA

🟡 **Cumplido con salvedad ya documentada.** Los 18 requisitos de IA (RF-IA +
RNF-IA) tienen ID, métrica, unidad, umbral y método de verificación completos
(ver auditoría `04_Trazabilidad/verificacion_IA01/auditoria_IA01.md`). El único
hallazgo pendiente es el campo "responsable" individual en el backlog, con
propuesta ya redactada y a la espera de confirmación del equipo.

## 10. URL pública

✅ **Cumplido.** `https://github.com/AlanNVR/SIMPA_ISR401` responde 200, accesible
sin autenticación.

---

## Resumen

| # | Punto | Estado |
|---|---|---|
| 1 | Clon limpio | ✅ |
| 2 | Compilación | ✅ |
| 3 | Archivos no vacíos | ✅ |
| 4 | Checksums | ✅ |
| 5 | Identidades | ✅ |
| 6 | `07_Datos` | ✅ |
| 7 | `10_Autoria` A1–A12 | ✅ |
| 8 | Privacidad | ✅ |
| 9 | Requisitos de IA | 🟡 Con salvedad documentada |
| 10 | URL pública | ✅ |

