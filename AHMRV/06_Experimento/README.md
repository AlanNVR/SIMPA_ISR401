# MVP — Prototipo funcional del SIMPA

Prototipo de interfaz del **Sistema Inteligente de Mantenimiento de Palma Africana**.

> **Estado:** prototipo funcional de interfaz. La lógica de negocio se ejecuta en el navegador y la persistencia es local. No existe todavía servicio de respaldo ni base de datos.

---

## Repositorio del código

El código fuente reside en un repositorio separado, enlazado como submódulo para que quede trazado el *commit* exacto evaluado:

```
https://github.com/jmaciasherr4/Prottotipo_Simpa
```

```bash
# desde la raíz del repositorio principal
git submodule update --init --recursive
```

---

## Cobertura sobre los requisitos *Must*

Tabla verificada por inspección del código fuente, no por declaración.

| ID-RF | Funcionalidad | Estado | Pantalla |
|---|---|---|---|
| RF-01 | Autenticación y control de acceso por rol | ✅ Implementado | Login |
| RF-02 | Gestión de plantaciones y lotes | ✅ Implementado | Detalle de lote |
| RF-03 | Gestión de personal y equipos | ✅ Implementado | Personal |
| RF-04 | Registro de labores agrícolas | ✅ Implementado | Labores |
| RF-05 | Registro de monitoreo fitosanitario | ✅ Implementado | Análisis |
| RF-12 | Generación de alertas tempranas | ✅ Implementado | Alertas |
| RF-19 | Generación de reportes | ✅ Implementado | Reportes |
| RF-20 | Historial de actividades y eventos | ✅ Implementado | Detalle de lote |
| RF-30 | Reporte de incidencia desde campo | ✅ Implementado | Análisis |
| RF-13 | Registro del proceso de polinización | 🟡 Parcial | Labores |
| RF-15 | Visualización de recorridos del personal | 🟡 Parcial | Mapa GPS |
| RF-28 | Registro de avance por unidad de labor | 🟡 Parcial | Labores |
| RF-07 | Detección de plagas por imagen | ⚠️ **Simulado** | Análisis |
| RF-14 | Conteo georreferenciado de flores | ⚠️ **Simulado** | Mapa GPS |
| RF-08 | Diagnóstico nutricional por imagen | ❌ No implementado | — |
| RF-10 | Gestión de variedades y umbrales | ❌ No implementado | — |
| RF-18 | Estimación de producción | ❌ No implementado | — |
| RF-21 | Clasificación de madurez del racimo | ❌ No implementado | — |
| RF-22 | Alerta preventiva de fruta verde | ❌ No implementado | — |
| RF-26 | Planificación semanal con presupuesto | ❌ No implementado | — |
| RF-35 | Registro delegado del avance | ❌ No implementado | — |

**Cobertura: 9 de 19 requisitos *Must* completos (47,4 %)**, o 55,3 % contabilizando los parciales con peso medio.

> ⚠️ **La §3.6 de la guía exige al menos el 60 %. El prototipo no alcanza ese umbral.** Se declara el valor real en lugar de computar como implementadas las funcionalidades simuladas, lo que habría permitido reportar un 73,7 % sin sustento verificable. Esta limitación consta como `L-10` en la §7.3 del ERS.

---

## Funcionalidades simuladas

Dos pantallas presentan interfaz completa con resultado no real. Se declaran de forma expresa.

**Análisis de imagen (RF-07).** La pantalla captura la imagen, muestra el indicador de calidad y presenta un diagnóstico, pero el resultado se genera mediante una función pseudoaleatoria y no mediante inferencia sobre la imagen. La arquitectura de integración —orquestador, interfaz del servicio y presentación de la explicación— sí está construida.

**Conteo georreferenciado (RF-14).** El mapa presenta recorridos y totales de polinización a partir de datos de ejemplo fijos; no se consulta el receptor GPS del dispositivo.

**Por qué no se implementó la inferencia real.** Un clasificador con utilidad requiere un conjunto de datos etiquetado del propio cultivo; la literatura del dominio reporta conjuntos de entre 850 y varios miles de imágenes para superar el 90 % de exactitud. El equipo no dispone de ese material. Integrar un modelo preentrenado de propósito general habría producido una demostración convincente pero sin validez: las predicciones no serían atribuibles al dominio y los valores objetivo de RNF-01 y RNF-02 no podrían verificarse.

---

## Despliegue local

**Requisitos:** Node.js 18 o superior y un navegador moderno.

```bash
git clone https://github.com/jmaciasherr4/Prottotipo_Simpa.git
cd Prottotipo_Simpa
npm install
npm run dev
```

La aplicación queda disponible en `http://localhost:5173`.

### Cuentas de demostración

| Usuario | Rol | Acceso |
|---|---|---|
| `admin` | Administrador | Todos los módulos, incluida la gestión de cuentas |
| `supervisor` | Supervisor | Operación de campo, sin gestión de cuentas |
| `operario` | Operario | Registro de labores y consulta |

> ⚠️ **Cuentas de demostración únicamente.** Las credenciales se almacenan sin derivación de clave en el almacenamiento local del navegador, en contradicción con RNF-13. No debe usarse con datos reales. Declarado como desviación `D-02` en la §6.4 del ERS.

---

## Stack tecnológico

React · Vite · Tailwind CSS · Radix UI · Recharts · Lucide

**Persistencia:** almacenamiento local del navegador (`localStorage`). No hay servicio de respaldo ni base de datos. Los requisitos no funcionales de fiabilidad (RNF-10, RNF-11) y de seguridad (RNF-13, RNF-14) **no son verificables** sobre el prototipo en su estado actual.

---

## Desviaciones declaradas

| ID | Desviación | Corrección programada |
|---|---|---|
| `D-01` | El catálogo de datos no corresponde al dominio real: emplea lotes con nomenclatura alfanumérica, cinco tipos de labor genéricos y nombres de personas ficticios | Sustituir por la estructura real anonimizada: lotes 1 a 6, catálogo de labores de EV-11 y EV-13, códigos `ENTR-XX` |
| `D-02` | Credenciales en texto plano en el navegador | Trasladar la autenticación a un servicio con derivación de clave |
| `D-03` | El código se distribuye comprimido, lo que impide la revisión por archivo y el seguimiento de cambios | Publicar el árbol de fuentes sin comprimir y declarar la procedencia en `package.json` |

**Procedencia del prototipo.** La interfaz se generó inicialmente con una herramienta de prototipado visual y se adaptó después. Se declara de forma expresa para evitar cualquier ambigüedad sobre su autoría.

---

## Video de demostración

`video_demo.mp4` — duración máxima 3 minutos. Recorrido:

1. Inicio de sesión con los tres perfiles y verificación del control de acceso
2. Consulta del panel principal
3. Registro de una labor con su avance
4. Reporte de incidencia con fotografía
5. Consulta de alertas y de reportes

---

## Trabajo pendiente para la Entrega 4

1. Incorporar RF-10, RF-26 y RF-35 — los tres son de implementación acotada y elevarían la cobertura por encima del 60 %
2. Corregir las desviaciones `D-01` a `D-03`
3. Conectar un servicio de respaldo real en sustitución del almacenamiento local
4. Construir el conjunto de datos etiquetado del cultivo para sustituir la simulación de RF-07
5. Integrar la geolocalización real del dispositivo para RF-14
