# Gráficos híbridos y NVIDIA

La mayoría de las laptops con dos GPU renderizan el escritorio
en la integrada y deberían correr solo el trabajo pesado en la
NVIDIA dedicada. HorneroOS hoy no mantiene un instalador propio
de driver NVIDIA ni un perfil híbrido universal, y esta guía no
cualifica ningún modelo de GPU. Lo que sigue es identificar tu
hardware, correr un programa en la dedicada y reportar un
problema con evidencia.

## Identificá primero las dos GPU

```sh
lspci -nnk
horneroctl doctor
hyprctl monitors -j
```

Anotá qué driver de kernel usa cada GPU y a qué GPU está cableado
cada monitor. Los puertos externos suelen ir directos a la
dedicada; ese cableado, no un ajuste, decide qué GPU usa una
pantalla externa.

## Instalá el driver correcto para tu kernel

La elección depende de generación de GPU y paquete de kernel.
Seguí la [guía NVIDIA de ArchWiki](https://wiki.archlinux.org/title/NVIDIA)
vigente para tu hardware, y [PRIME](https://wiki.archlinux.org/title/PRIME)
para render híbrido. No copies paquetes de driver, opciones de
módulo ni layouts de otra máquina: contrastalos con tu propia
salida de `lspci -nnk`.

## Correr un programa en la dedicada

El offload PRIME corre un solo programa en la dedicada mientras
la sesión queda en la integrada. Las variables de entorno y
ajustes de launcher son los de ArchWiki PRIME enlazados arriba;
en Steam, poné las variables de offload en las opciones de
lanzamiento de ese juego antes de `%command%`. Confirmá que
funcionó desde el renderer o reporte de GPU del propio programa,
no porque el comando corrió.

Si un juego no arranca solo con offload, probalo una vez en la
integrada: eso separa un problema de offload de uno de juego o
Proton. Mirá [Gaming](../applications/gaming-proton-gamemode.md).

## Límites honestos

- Hoy no hay instalador NVIDIA de HorneroOS ni cualificación por
  modelo; que funcione en una laptop no prueba nada para otra
  generación o firmware.
- NVENC, corrección Vulkan y captura HDMI no se testearon
  específicamente en la aceptación en hardware registrada.
  Tratalos como no verificados hasta que tu propio chequeo pase.
- Una actualización de kernel puede dejar el módulo NVIDIA sin
  compilar para el kernel nuevo. Arrancá el
  [kernel de respaldo](../desktop/kernel-and-fallback.md) para
  confirmar y reportá con las dos versiones.

## Reportar con evidencia

Incluí los dos modelos de GPU, paquetes de kernel y driver, si
el fallo es antes o después del login, y las primeras líneas de
`journalctl -b -k -p warning`. Quitá usuarios, hostnames,
seriales e identificadores de red antes de compartir logs. Mirá
[Solución de problemas por síntoma](../troubleshooting/by-symptom.md).
