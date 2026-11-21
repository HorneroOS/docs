# Kernel y arranque de respaldo

HorneroOS no trae un kernel propio. Un sistema instalado corre los
paquetes de kernel de su base Arch, y HorneroOS no activa por
defecto tweaks de kernel, scheduler, governor ni memoria. Esta
guía cubre qué kernel estás corriendo y cómo arrancar el otro
kernel instalado cuando una actualización deja la máquina
inestable.

## Ver qué corre y qué hay instalado

```sh
uname -r
pacman -Q | grep -E '^(linux|linux-lts|linux-zen) '
```

`uname -r` es el kernel en ejecución. Un paquete listado por
`pacman -Q` está instalado; solo es arrancable si tiene entrada
de arranque. HorneroOS no mantiene un gestor de kernels ni una
pantalla propia de elección de kernel.

## Guardá un kernel de respaldo antes de necesitarlo

Un kernel de repuesto solo ayuda si está instalado y tiene
entrada de arranque antes de la actualización que rompe el
principal. Si elegís mantener un kernel LTS junto al principal,
instalalo con tu flujo normal de paquetes, confirmá que aparece
una entrada nueva en el menú de arranque y probá arrancarlo una
vez con el sistema sano.

No borres el kernel en ejecución y no trates el respaldo como
rollback de sistema: solo cambia el kernel que arrancás, no los
paquetes, la configuración ni los archivos que una actualización
ya escribió. El rollback de sistema hoy no existe; mirá
[Actualizaciones y recuperación](updates-and-rollback.md).

## Arrancar el otro kernel desde GRUB

1. Reiniciá y mostrá el menú GRUB si no aparece.
2. Abrí las opciones avanzadas de HorneroOS.
3. Elegí la entrada del kernel de respaldo y arrancá.
4. Confirmá que aterrizaste en ese kernel:

   ```sh
   uname -r
   horneroctl doctor
   ```

Arrancar el respaldo es un paso de diagnóstico. Si la máquina
queda estable, seguí ahí, guardá la salida de doctor y reportá
el fallo con las dos versiones de kernel. Si los dos kernels
fallan, el problema está por debajo o más allá de esa elección;
mirá [Solución de problemas por síntoma](../troubleshooting/by-symptom.md).

## Después de actualizar el kernel

- Reiniciá pronto cuando una actualización reemplaza el kernel;
  si no, kernel en ejecución y módulos pueden no coincidir.
- Los módulos gráficos por kernel (por ejemplo NVIDIA vía DKMS)
  tienen que compilar para el kernel nuevo antes de confiar en
  esa sesión. Pantalla negra tras actualizar kernel es primero
  un síntoma gráfico; mirá
  [Gráficos híbridos y NVIDIA](../hardware/hybrid-graphics-nvidia.md).
- Las entradas GRUB de snapshots no son recuperación: arrancar
  un snapshot de solo lectura es un fallo registrado, no una
  vía de respaldo. Rigen los límites Btrfs manuales de
  [Actualizaciones y recuperación](updates-and-rollback.md),
  incluido mismo kernel únicamente.

Este procedimiento es el uso ordinario de GRUB en un sistema
instalado. No está cualificado por máquina; probá tu respaldo
una vez en sano en vez de descubrir su menú en una emergencia.
