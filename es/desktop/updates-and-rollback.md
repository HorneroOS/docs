# Actualizaciones y vuelta atrás del sistema

HorneroOS puede devolver todo tu sistema a como estaba antes de una
actualización. Antes de cada actualización guarda un **punto de
restauración**; si la actualización te deja una app rota, un escritorio que
no arranca o simplemente un cambio que no te gusta, elegís ese punto de
restauración y volvés a él en un solo paso.

> **Preview.** La vuelta atrás del sistema es nueva en esta preview. Leé el
> [estado de validación](#estado-de-validación) antes de depender de ella.

## Qué es un punto de restauración

Un punto de restauración junta tres cosas que se restauran juntas:

- **El sistema**: una instantánea Btrfs de la raíz del sistema operativo,
  que tiene los paquetes instalados, sus archivos y los ajustes del
  sistema en `/etc`.
- **Tus ajustes de Hornero**: la configuración de la shell (layout,
  barras, apariencia y el resto de lo que elegiste en el Centro de
  control).
- **Tu paleta Chromatic**: el estado de
  [Hornero Chromatic](chromatic.md) y los archivos que Chromatic generó
  para tus apps.

No tenés que restaurar las partes de a una. Elegir un punto de
restauración devuelve las tres al mismo momento, salvo que pidas solo el
sistema.

Algunas cosas **nunca vuelven atrás**, así que una vuelta atrás no puede
hacerte perder trabajo:

- tus archivos en `/home` (documentos, descargas, proyectos, datos de
  apps);
- los logs del sistema en `/var/log`;
- la caché de paquetes en `/var/cache` (así no hace falta volver a
  descargar paquetes).

## Viene activada en las instalaciones nuevas con Btrfs

Una instalación nueva de Desktop, Studio o Gaming sobre **Btrfs** deja
todo listo: las herramientas de instantáneas (snapper, snap-pac y
grub-btrfs), un almacén de instantáneas aparte en `/.snapshots`, un menú
de arranque "HorneroOS snapshots" y permiso para que quienes usan el
escritorio y están en el grupo `wheel` vean los puntos de restauración
sin escribir una contraseña.

Las instalaciones existentes **no** se convierten. Si instalaste una
preview anterior, o instalaste sobre ext4, leé
[Instalaciones sin Btrfs](#instalaciones-sin-btrfs).

Podés chequear qué soporta tu sistema en cualquier momento:

```sh
horneroctl recovery doctor
```

En un sistema listo todos los chequeos dan verde y el backend es
`snapper`.

## Cómo las actualizaciones crean puntos de restauración

Cuando actualizás desde el Centro de control o corrés `horneroctl package
upgrade --yes`, HorneroOS:

1. guarda tus ajustes de Hornero y tu paleta Chromatic;
2. te pide la contraseña una sola vez y toma una instantánea del sistema
   con la etiqueta **HorneroOS update** (la instantánea *pre*);
3. corre la actualización completa del sistema (`pacman -Syu`);
4. toma una segunda instantánea después de la actualización (la
   instantánea *post*). Si la actualización falló, se etiqueta
   **HorneroOS update (failed, exit N)** para que veas cuál salió mal.

Las instantáneas pre y post se guardan como un par y quedan vinculadas a
los ajustes guardados en el paso 1. Ese par es lo que ves como una sola
entrada en el historial de actualizaciones. Las instalaciones de paquetes
hechas por fuera de HorneroOS (por ejemplo un `sudo pacman -S` común)
también reciben un par de instantáneas más chico de snap-pac.

Para actualizar sin punto de restauración, desactivá
[Snapshot before upgrade](#ajustes) o corré:

```sh
horneroctl package upgrade --no-snapshot --yes
```

## Volver atrás desde el Centro de control

Abrí **Centro de control → Updates & backups → Update history & rollback**
(o corré `horneroctl config gui --pane updates`). Los nombres se muestran
en inglés, tal como aparecen en pantalla. La lista muestra los puntos de
restauración, del más nuevo al más viejo, con su fecha, su etiqueta y qué
contienen (sistema, ajustes de Hornero, paleta Chromatic).

Volver atrás tiene una protección de dos pasos a propósito, porque no hay
un deshacer de un clic:

1. Elegí un punto de restauración y tocá **Roll back**. Todavía no cambia
   nada. Un panel explica exactamente qué va a pasar: la fecha a la que
   volvés, qué vuelve a ese estado, qué se conserva y si hace falta
   reiniciar.
2. Si es lo que querés, confirmá con **Roll back and reboot later**.

Para un punto de restauración que incluye el sistema:

- El estado nuevo se aplica **después de reiniciar**. Seguí trabajando,
  guardá tus archivos y reiniciá cuando quieras.
- Antes de cambiar nada, HorneroOS toma una instantánea más llamada
  **Before rollback to #n** (n es el número del punto de restauración).
  Además conserva la raíz que dejás como un subvolumen llamado
  `@.pre-rollback-<hora>`. Esas dos cosas son tu deshacer manual: si el
  estado anterior resulta peor, volvé a la instantánea "Before rollback"
  de la misma manera.
- Tus ajustes de Hornero y tu paleta Chromatic vuelven al estado guardado
  enseguida; antes se guarda una copia de seguridad de los ajustes
  actuales.

Un punto de restauración que solo tiene ajustes de Hornero y la paleta
Chromatic se aplica en el momento y no necesita reiniciar.

## Cuando el escritorio no arranca

Si una actualización te deja sin un escritorio que funcione, arrancá un
estado anterior del sistema desde el menú de arranque y después hacelo
permanente:

1. Reiniciá la computadora. En el menú de GRUB abrí **HorneroOS
   snapshots** y elegí la instantánea de antes de la actualización (con
   la etiqueta **HorneroOS update** y su fecha).
2. El sistema arranca desde esa instantánea. Es un arranque temporal: los
   cambios que hagas en el sistema mientras lo usás se descartan en el
   próximo reinicio. Tus archivos de `/home` son los normales, los
   actuales.
3. Iniciá sesión, abrí una terminal y buscá el número del punto de
   restauración:

   ```sh
   horneroctl recovery list
   ```

4. Hacelo permanente y después reiniciá normalmente:

   ```sh
   horneroctl recovery rollback 42 --dry-run
   horneroctl recovery rollback 42 --yes
   ```

   Cambiá `42` por el número de tu punto de restauración. El dry run
   muestra la misma explicación que el panel del Centro de control sin
   cambiar nada.

Si el disco está cifrado con LUKS, arrancar una instantánea igual te pide
la frase de contraseña. Una instantánea nunca se saltea el cifrado.

## Actualizaciones del kernel

El kernel de Linux y su imagen de arranque viven en la partición de
arranque, fuera de las instantáneas del sistema. Cuando volvés atrás por
encima de una actualización que cambió el kernel, HorneroOS copia el
kernel guardado en la instantánea a la partición de arranque y regenera la
imagen de arranque, así el sistema restaurado arranca con el kernel que
le corresponde.

Arrancar una instantánea desde el menú **HorneroOS snapshots** es
distinto: usa el kernel que está ahora en la partición de arranque. Si la
actualización que rompió todo también reemplazó el kernel, una
instantánea anterior arrancada así puede no encontrar los módulos del
kernel que le corresponden y no arrancar. En ese caso volvé atrás desde
la ISO Live como se explica abajo.

## Volver atrás desde la ISO Live

Usá esto solo cuando ningún estado instalado del sistema arranca (por
ejemplo en una instalación con systemd-boot, o después de una
actualización del kernel como se explica arriba). Es el mismo cambio de
subvolúmenes que hace `horneroctl recovery rollback`, pero a mano.
Arrancá la ISO Live de HorneroOS, abrí una terminal y cambiá los nombres
de dispositivo por los tuyos (`lsblk -f` los lista):

```sh
sudo cryptsetup open /dev/nvme0n1p2 root      # solo instalaciones LUKS
sudo mount -o subvolid=5 /dev/mapper/root /mnt  # o la partición Btrfs
ls /mnt/@snapshots                             # buscá el número, p. ej. 42
sudo mv /mnt/@ /mnt/@.pre-rollback-manual
sudo btrfs subvolume snapshot /mnt/@snapshots/42/snapshot /mnt/@
sudo umount /mnt
```

Si la actualización había cambiado el kernel, también volvé a poner el
kernel que corresponde en la partición de arranque antes de reiniciar
(acá la partición de arranque es `/dev/nvme0n1p1` y el paquete del kernel
es `linux`; usá los tuyos):

```sh
sudo mount -o subvol=@ /dev/mapper/root /mnt
sudo mount /dev/nvme0n1p1 /mnt/boot
ls /mnt/usr/lib/modules                        # la versión restaurada
sudo cp /mnt/usr/lib/modules/<version>/vmlinuz /mnt/boot/vmlinuz-linux
sudo arch-chroot /mnt mkinitcpio -P
sudo umount -R /mnt
```

Estos pasos no tocan nada dentro de `@home`.

## Referencia de la línea de comandos

Todo esto funciona sin abrir el Centro de control. Los comandos de solo
lectura no piden contraseña; los que cambian algo la piden una vez con el
aviso normal del sistema.

- Listar puntos de restauración, del más nuevo al más viejo:
  `horneroctl recovery list`. Sumá `--all` para incluir las instantáneas
  horarias del timeline, o `--json` para una salida legible por máquinas.
- Previsualizar una vuelta atrás sin cambiar nada:
  `horneroctl recovery rollback <n> --dry-run`.
- Volver atrás el sistema, los ajustes de Hornero y la paleta Chromatic:
  `horneroctl recovery rollback <n> --yes`.
- Volver atrás solo el sistema:
  `horneroctl recovery rollback <n> --yes --system-only`.
- Volver atrás solo los ajustes de Hornero y la paleta:
  `horneroctl recovery rollback config_<stamp> --yes`.
- Actualizar sin punto de restauración:
  `horneroctl package upgrade --no-snapshot --yes`.
- Chequear si la vuelta atrás está lista: `horneroctl recovery doctor`.

`<n>` es el número de una instantánea del sistema, normalmente la
instantánea *pre* de una actualización. `config_<stamp>` es un punto de
restauración solo de ajustes, como lo muestra `recovery list`.
`--system-only` conserva tus ajustes de Hornero y tu paleta Chromatic
actuales.

## Ajustes

Centro de control → Updates & backups tiene tres opciones. Se guardan en
tu configuración de la shell.

- **Snapshot before upgrade**
  (`services.rollback.snapshotBeforeUpgrade`, por defecto **activado**).
  Desactivado actualiza sin punto de restauración, como `--no-snapshot`.
- **Restore desktop with system**
  (`services.rollback.restoreDesktopWithSystem`, por defecto
  **activado**). Desactivado vuelve atrás solo el sistema y conserva tus
  ajustes de Hornero y tu paleta actuales, como `--system-only`.
- **Show timeline snapshots**
  (`services.rollback.showTimelineSnapshots`, por defecto
  **desactivado**). Activado también lista las instantáneas automáticas
  horarias, como `--all`.

## Cuánto espacio usan los puntos de restauración

La retención tiene un límite, así que las instantáneas no llenan el
disco:

- instantáneas de actualizaciones y paquetes: se conservan las **10**
  más nuevas;
- instantáneas marcadas como importantes (actualizaciones de HorneroOS e
  instantáneas de seguridad "Before rollback"): las **5** más nuevas;
- instantáneas del timeline: **5** horarias y **7** diarias.

Las instantáneas Btrfs comparten los datos que no cambiaron, así que cada
una ocupa solo el espacio de lo que cambió desde entonces.

## Instalaciones sin Btrfs

La vuelta atrás del sistema necesita Btrfs. Sobre ext4 u otro sistema de
archivos, HorneroOS lo dice claramente en el Centro de control y en
`horneroctl recovery doctor` en vez de disimularlo. Igual podés volver
atrás tus **ajustes de Hornero y tu paleta Chromatic**: las
actualizaciones los siguen guardando y el historial los lista como puntos
de restauración solo de ajustes.

HorneroOS no convierte una instalación existente a Btrfs ni le agrega el
esquema de instantáneas. Para tener vuelta atrás del sistema, reinstalá
sobre Btrfs.

## Instalaciones con systemd-boot

El menú de arranque "HorneroOS snapshots" es una función de GRUB. Las
instalaciones que usan systemd-boot no tienen entradas de arranque de
instantáneas. Volver atrás desde un sistema que está andando (Centro de
control o `horneroctl recovery rollback`) funciona igual; si el sistema
no arranca para nada,
[usá la ISO Live](#volver-atrás-desde-la-iso-live).

## Estado de validación

<!-- VALIDATION-STATUS: filled in by the rollback PR author after the VM proof -->
Esta función es nueva en esta preview; mirá el escenario de QA enlazado
para ver qué se probó en una máquina virtual.

Los escenarios de QA viven en
[HorneroOS/qa `scenarios/recovery`](https://github.com/HorneroOS/qa/tree/main/scenarios/recovery)
(en inglés). La vuelta atrás del sistema no se validó en hardware físico,
y el [procedimiento manual desde la ISO Live](#volver-atrás-desde-la-iso-live)
no forma parte de la prueba en máquina virtual.

## Relacionado

- [Mapa del Centro de control](control-center.md)
- [horneroctl](../../desktop/horneroctl.md) (en inglés)
- [Hornero Chromatic](chromatic.md)
- [Solución de problemas](../troubleshooting/README.md)
