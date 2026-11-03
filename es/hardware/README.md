# Hardware

Hornero se construye sobre Arch Linux y Hyprland. Por eso, el soporte de
dispositivos depende del kernel, el firmware, los drivers y la
configuración del dispositivo en la máquina. El instalador provisional
Calamares de la ISO Preview no selecciona ni configura un perfil de
hardware de Hornero por vos, y todavía no existe validación en hardware
físico.

## Empezá con un chequeo de solo lectura

El Centro de control expone controles comunes de red, Bluetooth, audio,
brillo, batería y micrófono. La CLI puede informar varios de esos
estados:

```sh
horneroctl doctor
horneroctl hardware network status
horneroctl hardware brightness status
horneroctl hardware battery status
horneroctl hardware mic status
```

Para detección de gráficos o pantallas, reuní la vista de
dispositivos/drivers del kernel y la lista de monitores del compositor:

```sh
lspci -nnk
hyprctl monitors -j
journalctl -b -k -p warning
```

Estos comandos inspeccionan el estado. No instalan drivers ni cambian tu
configuración de arranque.

Para hardware creativo y límites de rendimiento de Studio, ver
[Hardware de Studio](../../hardware/studio.md).

## NVIDIA y gráficos híbridos

La configuración de drivers y PRIME depende de la generación de la GPU,
el paquete del kernel, el firmware de la laptop y qué puertos están
conectados a qué GPU. No copies un comando de una guía de una máquina
personal sin chequear esos datos en tu propio hardware.

Usá la [guía NVIDIA actual de ArchWiki](https://wiki.archlinux.org/title/NVIDIA)
para la elección de drivers y [PRIME](https://wiki.archlinux.org/title/PRIME)
para el renderizado híbrido. Seguí la guía que coincide con tu kernel
instalado y el estado de tu distribución. Hornero no mantiene actualmente
un instalador de drivers NVIDIA separado ni un perfil universal de GPU
híbrida.

Para un reporte, incluí los modelos de GPU, el paquete de kernel y
driver, si el problema pasa antes o después del login, y las líneas de
error relevantes. Sacá nombres de usuario, hostnames, números de serie,
identificadores de red y contenido de logs personal no relacionado antes
de compartir logs públicamente.
Ver [cómo reportar un bug](../development/README.md#reportá-un-bug).

## Más guías de dispositivos

- [Red](../troubleshooting/README.md#red-y-bluetooth)
- [Pantalla y gráficos](../troubleshooting/README.md#pantalla-y-gráficos)
- [Diagnóstico de Shell y Ajustes](../troubleshooting/README.md)

Las notas históricas de configuración de la antigua wiki de dotfiles
describen una estación de trabajo. Sus modelos de GPU, opciones de
módulos, elecciones de paquetes y cableado de monitores no son valores
por defecto de Hornero.
