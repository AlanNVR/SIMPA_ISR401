# MVP — Prototipo funcional del SIMPA

Prototipo de interfaz del **Sistema Inteligente de Mantenimiento de Palma Africana**.

> **Estado:** prototipo funcional de interfaz. La lógica de negocio se ejecuta en el navegador y la persistencia es local. No existe todavía servicio de respaldo ni base de datos.

---
## Enlace de video demostrativo


```
https://github.com/AlanNVR/SIMPA_ISR401/releases/download/v1.0-mvp-demo/video_demo.mp4
```
---
## Repositorio del código

El código fuente reside en un repositorio separado:

```
https://github.com/jmaciasherr4/Prottotipo_Simpa
```

> Aún no está enlazado como submódulo del repositorio principal. Esa vinculación (`.gitmodules`) está pendiente — ver acción 71 del plan operativo.

---

## Cobertura sobre los requisitos *Must*

Tabla corregida conforme a la auditoría realizada en PE5. La versión anterior
incluía incorrectamente como *Must* a RF-15 y RF-20, que son *Should*, y omitía
RF-36 y RF-37.

| ID-RF | Funcionalidad | Estado | Pantalla |
|---|---|---|---|
| RF-01 | Autenticación y control de acceso por rol | ✅ Implementado | Login |
| RF-02 | Gestión de plantaciones y lotes | ✅ Implementado | Detalle de lote |
| RF-03 | Gestión de personal y equipos | ✅ Implementado | Personal |
| RF-04 | Registro de labores agrícolas | ✅ Implementado | Labores |
| RF-05 | Registro de monitoreo fitosanitario | ✅ Implementado | Análisis |
| RF-12 | Generación de alertas tempranas | ✅ Implementado | Alertas |
| RF-19 | Generación de reportes | ✅ Implementado | Reportes |
| RF-30 | Reporte de incidencia desde campo | ✅ Implementado | Análisis |
| RF-13 | Registro del proceso de polinización | 🟡 Parcial | Labores |
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
| RF-36 | Catálogo de tarifas por labor | ❌ No implementado | — |
| RF-37 | Cálculo de remuneración semanal | ❌ No implementado | — |

**Cobertura al momento de construcción del prototipo:** 8 de 21 requisitos
*Must* implementados completamente (**38,1 %**).

Si las dos implementaciones parciales se ponderan con peso medio, la cobertura
es 9/21 (**42,9 %**).

Después del Change Control Board se incorporaron RF-40, RF-41 y RF-42 como
*Must*, elevando el catálogo vigente a 24 requisitos *Must*. Contra ese
denominador, la cobertura completa del prototipo es **8/24 = 33,3 %**.

> ⚠️ **La §3.6 de la guía exige al menos el 60 %. El prototipo no alcanza ese
> umbral.** La versión anterior de este README declaraba 9/19 = 47,4 %, cifra
> corregida formalmente durante PE5. Se conserva la cifra auditada aunque sea
> menos favorable.

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

1. Aumentar la cobertura de requisitos *Must*. Con 8 implementados de 21 se requieren al menos 13 completos para alcanzar el 60 % sobre el alcance de construcción del prototipo; frente al catálogo vigente de 24 se requieren al menos 15.
2. Corregir las desviaciones `D-01` a `D-03`
3. Conectar un servicio de respaldo real en sustitución del almacenamiento local
4. Construir el conjunto de datos etiquetado del cultivo para sustituir la simulación de RF-07
5. Integrar la geolocalización real del dispositivo para RF-14

---

## 🔗 Demo en vivo

Prueba el prototipo funcionando aquí: **[prototipo-simpa.netlify.app](https://prototipo-simpa.netlify.app/)**

**Cuentas de prueba:**

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `supervisor` | `super123` | Supervisor |
| `operario` | `oper123` | Operario |
