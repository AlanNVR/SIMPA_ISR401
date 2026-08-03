# ⚠️ Zona restringida — Git LFS

Los archivos `.7z` de esta carpeta se versionan con **Git Large File Storage**.
En la vista web de GitHub aparecen con 133 bytes: eso es el **puntero**, no el archivo.

Tamaños reales:
- evidencias_entrevistas_audios_01.7z — audios de 8 entrevistas
- evidencias_entrevistas_videos_01..04.7z — 14 videos de entrevista
- evidencias_entrevistas_consentimientos_01.7z — 8 consentimientos originales

Para obtener el contenido real:

    git clone https://github.com/AlanNVR/Villafuerte_Grupo_AHMRV.git
    cd Villafuerte_Grupo_AHMRV
    git lfs pull

Total aproximado: 1,8 GB. La contraseña de los contenedores se entregó
al docente por el espacio de la actividad en el SGA.

Los hashes SHA-256 constan en `checksums.sha256` (raíz) y el inventario
en `fichas_tecnicas.csv`.
