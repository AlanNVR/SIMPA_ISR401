# Miembro-verificación (*member checking*)

**Estado: ejecutada.** Ronda celebrada el 4 de septiembre de 2026 con tres
participantes de rondas anteriores: `ENTR-01`, `ENTR-02` y `ENTR-13`.

## En qué consiste

Participantes ya entrevistados confirman o corrigen **la interpretación que el
equipo hace de los resultados**, no responden preguntas nuevas. Por definición
requiere que los resultados existan primero:

```text
entrevistas → transcripciones → codificación → análisis
            → hallazgos preliminares → miembro-verificación
```

Se les presentó una síntesis de los hallazgos en lenguaje no técnico y se
recogió, enunciado por enunciado, si lo confirmaban, lo matizaban o lo
rechazaban.

## Contenido de esta carpeta — zona pública

| Ruta | Contenido |
|---|---|
| `Actas/` | Tres actas individuales con las firmas enmascaradas, una por participante |
| `Actas_consolidada/` | Acta consolidada de la ronda, con las tres posiciones enfrentadas enunciado por enunciado |
| `sintesis_hallazgos.pdf` | Material presentado a los participantes, en lenguaje no técnico |
| `correcciones_aplicadas.md` | Registro de los desacuerdos y de la decisión del equipo sobre cada uno |

Nomenclatura empleada:

```
AAAA-MM-DD_MemberCheck_ENTR-XX_Enmascarada.pdf
AAAA-MM-DD_MemberChecking_ActaConsolidada_Enmascarado.pdf
```

Los participantes se identifican únicamente por su código `ENTR-XX`, el mismo
que en las entrevistas semiestructuradas, porque se trata del mismo estudio y de
las mismas personas.

## Dónde está el material original — zona restringida

Los originales firmados sin enmascarar no residen en este repositorio. Se
depositan cifrados como assets de release en el repositorio complementario
<https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias>, y cada archivo tiene
su fila propia en `../00_Restringido/fichas_tecnicas.csv`, con su SHA-256
calculado antes de cifrar.

La contraseña de descifrado se entrega únicamente al docente responsable por el
canal académico correspondiente.

## Criterio metodológico aplicado

Dos decisiones gobiernan `correcciones_aplicadas.md` y conviene que un evaluador
las tenga presentes al leerlo:

**El desacuerdo es un resultado válido, no un fallo de la ronda.** Los
enunciados confirmados sin discrepancia no aparecen en el registro de
correcciones, porque no requieren ninguna. Lo que se documenta es lo que se
objetó.

**Cuando dos participantes sostienen posiciones incompatibles sobre un mismo
hecho, la discrepancia se reporta, no se concilia.** El equipo no adjudica cuál
de las fuentes tiene razón salvo que exista evidencia documental independiente
que lo permita. Elegir una versión por comodidad narrativa produciría un
hallazgo más limpio y menos cierto.

Si el equipo mantiene una interpretación pese a la objeción de un participante,
lo justifica por escrito y lo declara como amenaza a la validez.

## Estado de las decisiones

Las decisiones registradas en `correcciones_aplicadas.md` figuran como
**propuesta del equipo** y deben ratificarse en reunión antes del cierre de la
entrega. Una vez ratificada cada una, su estado pasa a *Aplicada*, con
responsable y fecha.

El documento declara ese estado de forma expresa en lugar de presentar las
decisiones como ya adoptadas.

## Limitaciones declaradas

- **La ronda cubre tres participantes** de los dieciséis entrevistados. Es el
  mínimo metodológico, no una muestra representativa del conjunto.
- Los tres pertenecen a estratos distintos —`ENTR-01` y `ENTR-02` al estrato de
  dominio, `ENTR-13` al de contraste—, lo que aporta variedad de perspectiva
  pero impide tratar la ronda como validación por estrato.
- Los enunciados sometidos a verificación se derivan de la codificación
  disponible, que hoy cubre `EV-01` a `EV-08`. La ampliación de la codificación
  al resto de las entrevistas está pendiente y podría generar enunciados nuevos
  no sometidos a esta ronda.

Estas limitaciones se declaran en lugar de omitirse, conforme al criterio que ha
guiado el proyecto.
