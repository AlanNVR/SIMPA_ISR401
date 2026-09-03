# Registro de consigna — Experimento del Enfoque 1

> Un archivo por cada ejecución del modelo. Nombrar
> `YYYY-MM-DD_HHMM_modelo.md`. **No editar tras la ejecución.**

---

## Identificación

| Campo | Valor |
|---|---|
| Fecha y hora de la consulta | `YYYY-MM-DD HH:MM` (zona horaria: UTC-5) |
| Persona que ejecuta | Código de integrante |
| Material fuente | `02_Evidencias/Transcripciones/..._ENTR-04_Transcripcion.txt` |
| Hash SHA-256 del material fuente | |

## Parámetros del modelo

| Parámetro | Valor |
|---|---|
| Modelo y versión exacta | |
| Temperatura | |
| top-p | |
| top-k | |
| Semilla | |
| Longitud máxima de respuesta | |
| Instrucción de sistema | (transcribir literal, o indicar «ninguna») |

> Si el modelo no admite semilla, consignar «no soportado» y declararlo como amenaza a la reproducibilidad.

## Consigna literal

Transcribir **exactamente** el texto enviado, sin reformular:

```
A partir del siguiente material fuente, redacta requisitos funcionales del
sistema descrito, con los ocho atributos de la plantilla del sílabo.

[a continuación, el contenido íntegro de la transcripción anonimizada]
```

## Respuesta completa

Pegar la respuesta **íntegra y sin editar**, incluidos preámbulos, advertencias o texto que no sean requisitos. La depuración se documenta aparte.

```
[respuesta del modelo]
```

## Depuración aplicada

| Acción | Justificación |
|---|---|
| | |

> Solo se admite depuración de formato: numeración, orden de campos, eliminación de preámbulo conversacional. **No se admite** modificar el contenido de ningún requisito, ni descartar requisitos por considerarlos de baja calidad. Descartar requisitos débiles sesgaría la comparación a favor del modelo.

## Resultado

| Métrica | Valor |
|---|---|
| Requisitos producidos | |
| Requisitos con los 8 atributos completos | |
| ¿Alcanza el mínimo de 25? | |

## Verificación de anonimización previa al envío

- [ ] El material fuente no contiene nombres propios
- [ ] No contiene cargos que identifiquen de forma unívoca
- [ ] No contiene el nombre real de ninguna organización
- [ ] No contiene números de cédula, teléfonos ni direcciones
