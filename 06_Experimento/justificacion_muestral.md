# Justificación del tamaño muestral — Experimento humano vs. LLM

**Fecha de esta declaración:** [completar fecha real antes de subir]
**Responsable:** Villafuerte Rosero Allan Noe
**Apoyo:** Macías Herrera Josthyn Esteban, Huilcapi León Denisses Fabiola

## Declaración honesta sobre el método de definición del tamaño

**No se realizó un cálculo formal de potencia estadística antes de definir
el tamaño de la muestra de requisitos ni el número de evaluadores.** Esta
justificación se redacta después de tener los tamaños ya definidos y
ejecutados, y describe el criterio práctico que efectivamente se usó, no
un procedimiento de cálculo de potencia que no se llevó a cabo.

Se declara así, en vez de construir retroactivamente un cálculo de potencia
que aparente haberse hecho de antemano, siguiendo el mismo criterio de
honestidad aplicado en el resto del cierre del proyecto (ej.
`06_Experimento/osf_deviations.md`, `10_Autoria/notas_campo/readme.md`).

## Tamaño de la muestra de requisitos: 25 humanos + 25 LLM (50 por dimensión)

**Criterio real usado:** restricción práctica de tiempo y recursos propia
de un proyecto académico de curso, no un cálculo de potencia estadística
a priori. Se buscó un número:

- suficientemente grande para permitir un análisis ordinal mixto con
  efectos aleatorios por evaluador y por requisito sin que el modelo
  quedara subdeterminado;
- alcanzable dentro del cronograma del semestre, dado que cada requisito
  debía ser evaluado por los 3 evaluadores en las 5 dimensiones (lo que ya
  representa 150 evaluaciones por origen, 300 en total);
- vinculado al mismo material fuente congelado (`ENTR-04`), para mantener
  coherencia temática entre el conjunto humano y el generado por LLM.

**Limitación reconocida:** con n=25 por grupo, el estudio tiene poder
estadístico limitado para detectar diferencias pequeñas entre origen
humano y LLM. Los resultados no significativos obtenidos
(`07_Datos/resultados/resumen_modelos_ordinales.txt`) deben interpretarse
considerando esta limitación: la ausencia de diferencia significativa no
equivale a evidencia de equivalencia entre ambos orígenes.

## Número de evaluadores: 3 (EV-01, EV-02, EV-03)

**Criterio real usado:** también una decisión práctica, no un cálculo de
potencia:

- es el mínimo recomendado en la práctica habitual de estudios de acuerdo
  entre evaluadores para poder calcular el alfa de Krippendorff con más de
  dos observadores (con 2 evaluadores el análisis de acuerdo queda mucho
  más limitado y no permite distinguir patrones de discrepancia);
- disponibilidad real de personas externas dispuestas a evaluar de forma
  voluntaria, sin conflicto de interés con el equipo, dentro del plazo del
  cierre del curso.

**Limitación reconocida:** 3 evaluadores es un número pequeño; el acuerdo
interevaluador obtenido (α de Krippendorff entre -0,015 y 0,027 según
dimensión) debe leerse también considerando que una muestra tan chica de
evaluadores es sensible a la variabilidad individual de cada uno.

## Qué NO se afirma en este documento

Este documento no afirma que 25 requisitos o 3 evaluadores sean el tamaño
"correcto" u "óptimo" para este tipo de estudio. Afirma únicamente qué
criterio real se usó para llegar a esos números, y reconoce abiertamente
que no hubo un cálculo de potencia estadística formal detrás de esa
decisión.
