# SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana

Prototipo funcional de interfaz desarrollado para el proyecto grupal de Ingeniería de Requerimientos (ISR-401).

> **Estado actual:** prototipo académico frontend. La persistencia se realiza localmente en el navegador. No existe todavía un backend productivo, una base de datos remota, inferencia de IA validada ni geolocalización real.

## Repositorios

- Repositorio grupal y documentación: https://github.com/AlanNVR/SIMPA_ISR401
- Repositorio del código del prototipo: https://github.com/jmaciasherr4/Prottotipo_Simpa
- Commit evaluado del prototipo: `ba33002dcf680f8b39d42df04553733bd5389f6d` (2026-08-31)

## Prototipos en vivo

### V1 — versión anterior

https://prototipo-simpa.netlify.app/

### V2 — versión actual recomendada

https://simpav2-prototipo.netlify.app/

### Cuentas de demostración

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `supervisor` | `super123` | Supervisor |
| `operario` | `oper123` | Operario |

> Las cuentas son únicamente de demostración. No deben utilizarse para información real o sensible.

## Funcionalidades cubiertas por el prototipo V2

La V2 incorpora o refuerza los siguientes flujos:

| ID | Funcionalidad | Estado del prototipo |
|---|---|---|
| RF-01 | Autenticación y control de acceso por rol | ✅ Funcional |
| RF-02 | Gestión de plantaciones y lotes | ✅ Funcional |
| RF-03 | Gestión de personal y equipos | ✅ Funcional |
| RF-04 | Registro de labores agrícolas | ✅ Funcional |
| RF-05 | Registro de monitoreo fitosanitario | ✅ Funcional |
| RF-07 | Detección de plagas por imagen | ⚠️ Interfaz simulada |
| RF-08 | Diagnóstico nutricional por imagen | ⚠️ Interfaz simulada |
| RF-10 | Gestión de variedades y umbrales | ✅ Funcional |
| RF-12 | Generación de alertas tempranas | ✅ Funcional |
| RF-13 | Registro del proceso de polinización | ✅ Flujo incorporado |
| RF-14 | Conteo georreferenciado de flores | ⚠️ Datos GPS simulados |
| RF-18 | Estimación de producción | ✅ Cálculo demostrativo |
| RF-19 | Generación de reportes | ✅ Funcional / exportación CSV |
| RF-21 | Clasificación de madurez del racimo | ⚠️ Flujo demostrativo |
| RF-22 | Alerta preventiva de fruta verde | ✅ Flujo incorporado |
| RF-26 | Planificación semanal con presupuesto | ✅ Funcional |
| RF-28 | Registro de avance por unidad de labor | ✅ Funcional |
| RF-30 | Reporte de incidencia desde campo | ✅ Funcional |
| RF-35 | Registro delegado del avance | ✅ Funcional |
| RF-36 | Catálogo de tarifas por labor | ✅ Funcional |
| RF-37 | Cálculo de remuneración semanal | ✅ Funcional |
| RF-40 | Exportación de datos personales | ✅ Flujo incorporado |
| RF-41 | Rectificación con bitácora | ✅ Flujo incorporado |
| RF-42 | Supresión/disociación del histórico | ✅ Flujo incorporado |

## Limitaciones declaradas

**IA / análisis de imágenes.** RF-07, RF-08 y la clasificación visual relacionada con RF-21 se presentan como flujos de interfaz. La versión entregada no debe afirmar que realiza inferencia real o que cumple métricas de exactitud sin un modelo entrenado y un conjunto de datos del dominio.

**GPS.** RF-14 usa información demostrativa. La versión entregada no consulta necesariamente el receptor GPS real del dispositivo.

**Persistencia y seguridad.** La información del prototipo se almacena en `localStorage`. Esto permite probar los flujos sin servidor, pero no sustituye una arquitectura con API, base de datos, control de sesiones, cifrado, respaldo y auditoría de producción.

## Tecnologías

React · Vite · TypeScript/JavaScript · Tailwind CSS · Radix UI · Recharts · Lucide.

También se proporciona un archivo `SIMPA_V2_COMPLETO.html` independiente para demostración rápida sin instalar dependencias.

## Ejecución local del proyecto V2

```bash
git clone https://github.com/jmaciasherr4/Prottotipo_Simpa.git
cd Prottotipo_Simpa/prototipo_v2/Prottotipo_Simpa-main/Prototipo
npm install
npm run dev
```

Vite mostrará en la terminal la URL local, normalmente `http://localhost:5173`.

## Ejecución del HTML independiente

Abre `SIMPA_V2_COMPLETO.html` directamente en un navegador moderno. El archivo contiene HTML, CSS y JavaScript en un solo documento y guarda los registros de demostración en `localStorage`.

## Video demostrativo

https://github.com/AlanNVR/SIMPA_ISR401/releases/download/v1.0-mvp-demo/video_demo.mp4

## Trabajo pendiente para una versión productiva

- Integrar backend y base de datos.
- Implementar autenticación segura y manejo de sesiones.
- Añadir servicio real de respaldo.
- Entrenar y validar modelos de IA con datos del cultivo.
- Integrar geolocalización real y permisos del dispositivo.
- Crear pruebas automatizadas y trazabilidad verificable entre requisitos, código y evidencias.
- Validar los RNF de rendimiento, seguridad, disponibilidad y recuperación sobre infraestructura real.
