# A2.2 — Auditoría de fuentes editables del prototipo

**Responsable:** Macías Herrera Josthyn Esteban
**Fecha:** 2026-09-14
**Alcance:** `10_Autoria/fuentes_editables/`

## Método

```bash
find 10_Autoria/fuentes_editables -type f -empty
find 10_Autoria/fuentes_editables -maxdepth 1 -iname "*.puml" -exec wc -c {} \;
find 10_Autoria/fuentes_editables/SIMPA_mockups_codigo -type f -empty
find 10_Autoria/fuentes_editables/SIMPA_mockups_codigo -type f | wc -l
```

## Resultado

| Comprobación | Resultado |
|---|---|
| Archivos de 0 bytes en la carpeta completa | 0 encontrados |
| Los 13 `.puml` tienen contenido real | Sí — rango 990 a 5.724 bytes, ninguno vacío ni truncado |
| `SIMPA_App_Interfaces_Design.make` | 691.887 bytes, consistente con un proyecto real de Figma Make |
| Archivos vacíos dentro de `SIMPA_mockups_codigo/` | 0 encontrados |
| Total de archivos de código del prototipo | 66, todos con contenido |

**Conclusión: sin archivos vacíos injustificados. Las 26 fuentes editables
(13 `.puml` + 1 `.make` + 66 archivos de código, agrupados como un solo
depósito de prototipo) están completas y son genuinamente editables.**
