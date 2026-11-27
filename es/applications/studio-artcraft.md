# ArtCraft Launcher (experimental)

ArtCraft Launcher es una aplicación experimental en etapa alpha temprana de
Studio del proyecto ArtCraft. Instala y actualiza las aplicaciones Craft; qué
aplicaciones existen lo decide el lanzador y puede cambiar sin una
actualización de HorneroOS, por eso HorneroOS nunca las lista ni las cuenta.

## Solo opt-in

El lanzador es una única aplicación opcional de Studio (`artcraft-launcher`).
Nunca se instala al elegir una especialización de Studio ni una carga de
trabajo amplia, y el instalador de HorneroOS nunca lo descarga. Registrar la
elección solo guarda tu intención:

```bash
horneroctl studio selection set --application artcraft-launcher
horneroctl studio app show artcraft-launcher --json
```

El segundo comando informa si el archivo desktop del lanzador
(`ai.storyteller.artcraft-launcher`) está presente. Su versión y estado de
actualización los informa el propio lanzador.

## Instalación

La instalación es manual y aprobada por el usuario, siguiendo el runbook en
inglés en HorneroOS/hornero (`docs/studio-artcraft.md`): descargá el paquete
Arch firmado del fabricante fijado en el catálogo, verificá la huella digital
fijada de firma de release y las sumas SHA256, y recién ahí instalalo con
`pacman -U`. Una verificación fallida detiene la instalación. No instales
releases que HorneroOS no haya fijado y verificado.

## Actualizaciones y deriva

El lanzador se actualiza a sí mismo y a sus aplicaciones Craft por fuera de
los repositorios de paquetes del sistema. HorneroOS no fija, espeja ni
revierte esas actualizaciones, así que la versión instalada puede derivar del
pin del catálogo; eso es esperado en esta entrada experimental, y el lanzador
es la fuente de verdad sobre su propio estado.

## Desinstalación

Quitá primero las aplicaciones Craft desde adentro del lanzador, después
desinstalá el paquete del lanzador (`pacman -R ai.storyteller.artcraft-launcher`)
y borrá los archivos locales residuales del usuario (por ejemplo una copia
AppImage en `~/Applications` y los datos gestionados por el lanzador que ya no
quieras). Quitar la selección de Studio en `horneroctl` o el Centro de control
nunca desinstala nada por sí solo.

## Requisitos previos y solución de problemas

Se requiere una sesión Wayland nativa con `xdg-desktop-portal` y el backend de
portal de Hyprland (más el backend GTK para diálogos de archivos). Si se usa
una build AppImage en vez del paquete, además necesita FUSE funcionando o
`APPIMAGE_EXTRACT_AND_RUN=1`. Los cierres inesperados y bugs de aplicaciones
Craft son problemas upstream: reportalos al proyecto ArtCraft con los propios
logs del lanzador.

## Estado y marca registrada

La aceptación en HorneroOS para esta entrada se sigue en HorneroOS/qa#36 y
permanece pendiente hasta que exista evidencia real de Studio Preview; nada
acá es una afirmación de soporte. ArtCraft, el nombre ArtCraft y la marca A
son marcas registradas de ArtCraft Team, usadas solo sin modificaciones como
parte del lanzador sin modificar; no están licenciadas bajo MIT ni Apache-2.0.
El instalador en sí sigue siendo el límite de propiedad del futuro instalador
de Panda Foss — Calamares es solo el puente provisional.
