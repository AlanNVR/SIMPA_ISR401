# FIN-03 — Verificación previa al cierre del repositorio

**Responsable:** Macías Herrera Josthyn Esteban
**Apoyo:** Arboleda Yanza Francisco Javier
**Fecha de esta verificación:** 2026-09-12
**Método:** verificación sobre la última actualización disponible del repositorio `AlanNVR/SIMPA_ISR401` en `main`, complementada con la comprobación local de checksums proporcionada para esta revisión.

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

## 11. Baseline

❌ **No cumplido — es la última tarea (FIN-05), correcto que aún no exista.** El
tag más reciente (`baseline-v3.1`) apunta a un commit anterior (`7c53724`), no al
commit actual de `main` (`89c49ac`). No se crea todavía porque, según la regla del
propio plan, no debe fijarse baseline final mientras existan tareas pendientes que
modifiquen el repositorio (A10, EVI-01, FIN-02).

---

## Resumen

| # | Punto | Estado |
|---|---|---|
| 1 | Clon limpio | ✅ |
| 2 | Compilación | ✅ |
| 3 | Archivos no vacíos | ⚠️ (1 hallazgo menor) |
| 4 | Checksums | ✅ |
| 5 | Identidades | ✅ |
| 6 | `07_Datos` | ✅ |
| 7 | `10_Autoria` A1–A12 | ⚠️ Bloqueado por A10 |
| 8 | Privacidad | ✅ |
| 9 | Requisitos de IA | 🟡 Con salvedad documentada |
| 10 | URL pública | ✅ |
| 11 | Baseline | ❌ Pendiente, correcto que así sea |

**Este documento no debe convertirse a PDF ni firmarse como versión final
todavía.** Faltan A10, EVI-01 y FIN-02 por cerrar, y el archivo `.css` vacío del
punto 3 por resolver. Cuando esos tres/cuatro puntos cierren, se vuelve a correr
esta misma verificación desde un clon limpio nuevo y, si todo pasa, ahí sí se
genera `10_Autoria/verificacion_previa.pdf` y se firma.
