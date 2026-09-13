#!/usr/bin/env python3
"""
AUT-04 — Verificación de que las grabaciones de trabajo existen realmente
como Release assets accesibles.

Hace una petición HTTP HEAD contra cada URL declarada (sin descargar el
archivo completo) y confirma que responde 200 OK, exactamente el mismo
método ya usado para verificar los contenedores de entrevistas en
02_Evidencias/00_Restringido/verificacion_fichas.md.

Uso: python verificar_grabaciones.py
Requiere conexión a internet.
"""
import urllib.request
import sys

GRABACIONES = [
    {
        "nombre": "Grabación 1 — Allan + Josthyn",
        "url": "https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-autoria/2026-09-12_grabacion01_allan_josthyn_datos_experimento.mp4",
        "sha256": "0d13bf0975daa1507dcbc1854baf1ea7c4a0626fdec45325f36bc23c00ec8b72"[:64],
    },
    {
        "nombre": "Grabación 2 — Denisses + Edson + Francisco",
        "url": "https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias/releases/download/v1.0-autoria/2026-09-12_Grabacion02_ManuscritoEvidenciasDocumentacion.mp4",
        "sha256": "3c7a9c07132028fd30b6fc80b40766c68e118b1e76df837201457bd479cd880b"[:64],
    },
]

def verificar(url):
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, resp.headers.get("Content-Length")
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return None, str(e)

def main():
    print("=" * 70)
    print("AUT-04 — Verificación HTTP de grabaciones (Release assets)")
    print("=" * 70)
    fallos = 0
    for g in GRABACIONES:
        status, extra = verificar(g["url"])
        ok = status in (200, 302)  # GitHub Release assets suelen redirigir (302) al CDN antes del 200 final
        estado = "OK" if ok else "FALLO"
        if not ok:
            fallos += 1
        print(f"\n{g['nombre']}")
        print(f"  URL: {g['url']}")
        print(f"  SHA-256 declarado: {g['sha256']}")
        print(f"  Estado HTTP: {status} -> {estado}")

    print("\n" + "=" * 70)
    if fallos == 0:
        print("OK: ambas grabaciones son accesibles en el repositorio de evidencias.")
    else:
        print(f"ATENCIÓN: {fallos} grabación(es) no respondieron correctamente.")
    print("=" * 70)
    sys.exit(1 if fallos else 0)

if __name__ == "__main__":
    main()
