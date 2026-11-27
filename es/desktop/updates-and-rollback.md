# Actualizaciones y recuperación: todavía no hay vuelta atrás del sistema

**HorneroOS hoy no tiene vuelta atrás del sistema.** Ningún comando
de `horneroctl`, ningún botón del Centro de control y ningún flujo de
actualización crea o restaura una instantánea del sistema operativo,
y actualizar no guarda antes un punto de restauración del sistema.
Todas las builds actuales informan su backend de instantáneas como
`none`.

Esta página separa lo que sí existe de lo que no, para que una
actualización nunca se apoye en una red de seguridad que no está. El
contrato vinculante es
[`docs/SNAPSHOT_BACKEND_CONTRACT.md`](https://github.com/HorneroOS/hornero/blob/main/docs/SNAPSHOT_BACKEND_CONTRACT.md)
en HorneroOS/hornero (issue HorneroOS/hornero#179), en inglés:
ninguna superficie de HorneroOS puede anunciar una vuelta atrás del
sistema hasta que su prueba de seis pasos en máquina virtual pase
completa. No pasó. Mirá
[Estado de validación](#estado-de-validación).

En particular, hoy no existe nada de lo siguiente, digan lo que digan
borradores o capturas viejas:

- un subcomando recovery list o recovery rollback (el único
  subcomando de recovery es el doctor de solo lectura de abajo);
- puntos de restauración que junten el sistema, los ajustes de
  Hornero y la paleta Chromatic en un solo paso para deshacer;
- un par de instantáneas del sistema pre/post tomado por una
  actualización de HorneroOS;
- ajustes de vuelta atrás en el Centro de control
  (`services.rollback.*`);
- una forma probada de arrancar una instantánea desde el menú de
  GRUB y seguir usándola, o de volver atrás por encima de una
  actualización del kernel.

## Chequeá la preparación para recuperación

Existe un diagnóstico de solo lectura:

```sh
horneroctl recovery doctor
horneroctl recovery doctor --json
```

Son seis chequeos y no cambia nada: el backend de instantáneas que
viene en la build, el tipo de sistema de archivos de la raíz, el
almacén de nivel superior `/.snapshots`, el binario de snapper,
`/etc/snapper/configs/root` y las unidades de temporizador de
timeline/limpieza de snapper. Esperá que hoy informe chequeos
fallidos: el chequeo del backend falla mientras el backend sea
`none`, y el comando nunca termina bien anunciando que la
recuperación está lista.

Leé la salida literalmente. Una raíz Btrfs, un almacén montado, un
snapper instalado o un temporizador presente son *plomería de
preparación*, no prueba de que restaurar funcione. El propio doctor
lo dice, y nunca lista una instantánea como restaurable.

## Qué sí existe hoy

### Actualizaciones

Chequear es de solo lectura; actualizar es una actualización
completa del sistema Arch:

```sh
horneroctl package check
horneroctl package upgrade --dry-run
horneroctl package upgrade --yes
```

La actualización corre `pkexec pacman -Syu`. No se limita a paquetes
de Hornero, no retiene ni excluye el kernel, no crea ninguna
instantánea del sistema y no promete ninguna vuelta atrás. No hay
ninguna opción para saltearse una instantánea, porque no hay ningún
paso de instantánea que saltear. Revisá primero la lista de
pendientes y tratá cada actualización como la operación sin vuelta
que hoy es.

### Centro de control: Updates & backups

Centro de control → Updates (id del panel `updates`; abrilo con
`horneroctl config gui --pane updates`) lleva el encabezado "Updates
& backups", en inglés como aparece en pantalla. Muestra las
actualizaciones del sistema pendientes, ofrece la misma
actualización completa detrás de una confirmación de dos clics y
avisa cuando hace falta reiniciar para terminar una actualización
(nunca reinicia nada por su cuenta).

Su panel Dependencies & recovery se guía por el backend que informa
la CLI. Mientras ese backend sea `none`, dice claramente que la
vuelta atrás de actualizaciones no está disponible y que no hay
ningún backend de instantáneas registrado para el sistema. El resto
del panel es ayuda a nivel configuración, descrita a continuación:
copias de seguridad, restaurar una instantánea de configuración por
id, una tarjeta para listar y crear instantáneas de configuración,
un chequeo de dependencias y una receta de programación de copias
que se imprime y nunca se instala por vos.

![Ajustes, página Updates & backups. La zona de actualizaciones del
sistema todavía está consultando, la de copias de seguridad informa
que no hay ninguna guardada y abajo están las acciones de restauración
de instantáneas de configuración y de
dependencias.](https://www.horneroos.com/captures/cap-cc-10.png)

*Ajustes → Updates en un equipo sin copias de seguridad todavía. Nada
de esta página es una vuelta atrás del sistema, como explica esta
guía. Captura real del escritorio en el equipo del maintainer,
19 de noviembre de 2026.*

### Instantáneas de configuración

Las instantáneas de configuración son archivos de ajustes. No son
instantáneas del sistema, y la palabra "snapshot" en `horneroctl`
significa esto y solo esto:

```sh
horneroctl config snapshot list
horneroctl config snapshot create --dry-run
horneroctl config snapshot create --yes
horneroctl config snapshot restore config_20260101_020000 --dry-run
horneroctl config snapshot restore config_20260101_020000 --yes
```

Reemplazá el id de ejemplo por uno de la lista. Una instantánea
guarda las raíces de configuración de Hornero más el inventario de
paquetes y metadatos del host en el directorio de datos del usuario
(`hornero/snapshots` en los datos XDG, o `HORNERO_SNAPSHOTS_DIR`).
Al restaurar, primero crea una instantánea de seguridad de la
configuración actual y después restaura el archivo elegido. No toca
`/`, los archivos de paquetes instalados, las entradas de arranque,
las bases de datos ni el estado del kernel, y no puede recuperar una
transacción de paquetes fallida ni un sistema que no arranca.

### Copias de seguridad de la configuración

Las copias archivan el directorio de configuración de Hornero en un
tarball con fecha y lo restauran de vuelta:

```sh
horneroctl backup list
horneroctl backup create --dry-run
horneroctl backup create --yes
horneroctl backup restore <id> --dry-run
horneroctl backup schedule
```

Reemplazá `<id>` por un archivo de la lista; restaurar también
necesita `--yes` después de su dry run. Los archivos viven en el
estado XDG (`hornero/backups`, o `HORNERO_BACKUP_DIR`). El comando de
programación solo imprime una receta de cron/systemd para copiar;
`horneroctl` nunca instala un temporizador. Igual que las
instantáneas de configuración, una copia restaura solo la
configuración de Hornero, nunca el sistema operativo.

### Instantáneas de Chromatic

[Hornero Chromatic](chromatic.md) lleva su propio historial
transaccional: cada aplicación guarda el contenido anterior de los
archivos que va a escribir y lo restaura si la aplicación falla.
También podés volver atrás vos:

```sh
horneroctl appearance chromatic history
horneroctl appearance chromatic rollback --dry-run
horneroctl appearance chromatic rollback --steps 2 --yes
horneroctl appearance chromatic off --yes
```

El historial lista las diez instantáneas más nuevas; la vuelta atrás
restaura el estado de esa cantidad de aplicaciones hacia atrás (por
defecto, una). Esto cubre la paleta y los archivos que Chromatic
generó. No tiene relación con las actualizaciones del sistema.

### El esquema Btrfs de las instalaciones nuevas

Las instalaciones nuevas sobre Btrfs crean un subvolumen de nivel
superior `/@snapshots` montado en `/.snapshots`, fuera del subvolumen
raíz, para que las instantáneas de la raíz no aniden instantáneas de
instantáneas. El esquema también mantiene `/home`, `/var/cache` y
`/var/log` en sus propios subvolúmenes (`/@home`, `/@cache` y
`/@log`). Las instalaciones existentes no se migran a este esquema.
El esquema es un lugar donde un backend futuro podría escribir; por
sí solo no instala ninguna herramienta de instantáneas ni habilita
ninguna vuelta atrás.

### La capacidad optativa de instantáneas

El catálogo de ediciones tiene una capacidad optativa `snapshots`
(Desktop, Studio y Gaming) que está **apagada por defecto para todas
las ediciones**. Solo cuando se la elige, una instalación gana
snapper, snap-pac, grub-btrfs e inotify-tools, más los temporizadores
de timeline/limpieza de snapper y el demonio de grub-btrfs. Elegirla
no cambia el backend informado: `horneroctl` sigue informando `none`.

Cuando esa capacidad llegó a un destino Btrfs que tiene el almacén
`/.snapshots`, el instalador siembra una configuración de fábrica
`/etc/snapper/configs/root` y la registra, sin sobrescribir una
configuración del administrador que ya exista. Cualquier otro caso es
un no-op. La retención de fábrica tiene límites:

- instantáneas numeradas: se conservan las 10 más nuevas, y las
  5 más nuevas de las marcadas como importantes;
- instantáneas del timeline: 5 horarias y 7 diarias, ninguna
  semanal, mensual ni anual;
- una antigüedad mínima de 30 minutos antes de la limpieza, un
  límite de espacio del 50% y un límite de espacio libre del 20%.

Con esa pila efectivamente instalada y configurada, snap-pac puede
tomar pares pre/post de snapper alrededor de transacciones de
pacman; eso es snapper y snap-pac funcionando como herramientas
upstream, probado en una instalación candidata en máquina virtual
(paso 2 de abajo), no una función de puntos de restauración de
HorneroOS. Sigue sin haber ningún comando de Hornero para enumerarlas
como destinos de recuperación ni para restaurar una.

El alcance importa si las instantáneas existen: la configuración de
fábrica cubre solo el subvolumen raíz y nunca home. Como `/home`,
`/var/cache` y `/var/log` son subvolúmenes separados, quedan fuera de
una instantánea de la raíz, pero todo lo demás bajo la raíz no —
incluidos el estado de aplicaciones y bases de datos en `/var/lib` y
los ajustes en `/etc`. Reemplazar la raíz también revierte esas
rutas. Un límite por cantidad tampoco garantiza espacio libre: las
instantáneas retenidas mantienen vivos datos borrados o cambiados,
así que vigilá el espacio en disco en vez de confiar en la cantidad.

## El procedimiento manual de reemplazo de @ y sus límites

El contrato registra exactamente un mecanismo de restauración con
evidencia aprobada: el **reemplazo de @** — renombrar el subvolumen
raíz y poner en su lugar una instantánea escribible de una
instantánea de snapper existente — hecho desde un sistema en
funcionamiento en la VM de la prueba y descrito por el contrato como
el mismo intercambio desde un medio live, **dentro de una misma
versión del kernel**. Es un procedimiento manual de administración con
herramientas de Btrfs, no una función de HorneroOS: ningún comando de
Hornero lo hace, lo chequea ni lo deshace por vos.

No lo intentes salvo que se cumpla todo esto:

- la raíz es Btrfs con el almacén `/@snapshots` y existe una
  instantánea en la que confiás en `@snapshots/<n>/snapshot`;
- la instantánea se tomó con la versión del kernel que todavía está
  en la partición del sistema EFI — si la actualización de la que
  escapás cambió el kernel, pará acá (mirá el límite del kernel más
  abajo);
- copiaste afuera todo lo que está bajo la raíz y no debe revertir,
  en particular el estado actual en `/var/lib`, y aceptás que todo en
  la raíz vuelve al momento de la instantánea.

Desde un medio ISO Live, en una terminal, reemplazando los nombres de
dispositivo por los tuyos (`lsblk -f` los lista) y `<n>` por el número
de la instantánea:

```sh
sudo cryptsetup open /dev/nvme0n1p2 root
sudo mount -o subvolid=5 /dev/mapper/root /mnt
ls /mnt/@snapshots/<n>/snapshot
ls /mnt/@snapshots/<n>/snapshot/usr/lib/modules
ls /mnt/@/usr/lib/modules
sudo mv /mnt/@ /mnt/@.pre-rollback-manual
sudo btrfs subvolume snapshot /mnt/@snapshots/<n>/snapshot /mnt/@
ls /mnt/@
sudo umount /mnt
```

La primera línea es solo para instalaciones con LUKS; en una
instalación sin cifrado montá directamente la partición Btrfs.
Verificá que la instantánea existe *antes* del renombre; si el comando
de instantánea falla después (número equivocado, falta de espacio),
volvé a poner la raíz original enseguida con
`sudo mv /mnt/@.pre-rollback-manual /mnt/@` antes de desmontar o
reiniciar. Conservar la original renombrada también es el deshacer
manual: intercambiála de vuelta de la misma manera. Nada de estos
pasos toca `@home`, y no restauran tus ajustes de Hornero ni tu paleta
Chromatic — esos viven en tu configuración dentro de home, conservan
sus valores actuales y pueden volver atrás por separado con las
herramientas de configuración y de Chromatic de arriba, si querés.

Sus límites registrados son parte del procedimiento, no letra chica:

- **Solo con el mismo kernel.** El kernel y el initramfs viven en la
  partición del sistema EFI, fuera de las instantáneas de la raíz.
  Restaurar una raíz tomada antes de una actualización del kernel
  arranca el kernel nuevo contra el `/usr/lib/modules` viejo y falla;
  la prueba observó exactamente ese desajuste. Con este esquema no es
  posible ninguna afirmación de vuelta atrás por encima de una
  actualización del kernel, y esta página deliberadamente no da
  ninguna variante que copie el kernel.
- **Arrancar desde GRUB no es recuperación probada.** En la prueba, el
  menú de instantáneas de GRUB se mostró, pero arrancar una instantánea
  de snapper de solo lectura terminaba en modo de emergencia: la
  instantánea es de solo lectura y su fstab monta `/` como el
  subvolumen raíz, así que los sistemas de archivos locales fallan.
  Nunca trates el menú de arranque solo como una vía de recuperación.
- **La retención/GC no está probada.** La prueba habilitó los
  temporizadores pero no observó ninguna corrida de recolección de
  basura, así que la retención acotada a los límites de fábrica y la
  supervivencia bajo GC de la instantánea desde la que se arrancó no
  están probadas.
- **Sin prueba en hardware físico.** La evidencia es una corrida en
  una VM QEMU desechable sobre una ISO candidata (UEFI, Btrfs, sin
  cifrado); los pasos y los fallos están listados en Estado
  de validación.

## Según el tipo de instalación

- **Btrfs nueva**: recibe el esquema con el almacén `/@snapshots`.
  Sin herramienta de instantáneas salvo que se haya elegido la
  capacidad optativa; en ningún caso hay vuelta atrás del sistema de
  HorneroOS.
- **Instalación existente o migrada**: no se convierte: no se agrega
  ningún almacén y ningún esquema se migra automáticamente. Un
  sistema migrado desde preview24 queda en este grupo.
- **ext4 u otro no-Btrfs**: el backend Btrfs del contrato no está
  soportado, y el doctor de recuperación y el panel Updates lo dicen
  claramente. Solo aplican las herramientas de configuración y
  Chromatic de arriba. HorneroOS no convierte el sistema de archivos.
- **GRUB (UEFI o BIOS heredado)**: las entradas de grub-btrfs solo
  pueden existir con la capacidad optativa, y arrancar una de solo
  lectura es un fallo registrado, no recuperación.
- **systemd-boot (solo UEFI)**: no hay entradas de instantáneas de
  GRUB. Las vías de arranque de instantáneas de GRUB y de systemd-boot
  son implementaciones separadas en el contrato, y ninguna de las dos
  se entrega. El intercambio manual de arriba no usa un menú de
  arranque, pero sus límites de mismo kernel y GC sin probar aplican
  igual.
- **LUKS**: una instantánea nunca se saltea el cifrado: las vías de
  arranque igual deben exigir el desbloqueo y el procedimiento manual
  empieza abriendo el dispositivo LUKS. La VM de la prueba no estaba
  cifrada, así que acá no se afirma ninguna restauración con LUKS como
  probada.

## Si una actualización rompió algo hoy

Sé honesta u honesto con las opciones que realmente existen:

1. Si solo salieron mal los ajustes de Hornero o los colores,
   restaurá una instantánea de configuración o una copia, o hacé
   volver atrás Chromatic, con los comandos de arriba. Previsualizá
   primero con un dry run.
2. Corré `horneroctl recovery doctor` y guardá su salida para un
   reporte de bug; registra exactamente qué piezas de preparación
   tiene tu instalación. No va a arreglar nada.
3. Si se rompió el sistema mismo, HorneroOS no ofrece ninguna vuelta
   atrás del sistema soportada en la que apoyarte. El reemplazo
   manual de @ de arriba es el único mecanismo con evidencia en el
   contrato, solo dentro de una misma versión del kernel y solo si
   ya existe una instantánea de snapper adecuada. Todo lo demás —
   bajar versiones de paquetes, reparar por chroot, reinstalar — es
   administración común de un sistema Arch, fuera de cualquier
   garantía de HorneroOS.
4. Antes de la próxima actualización, guardá al menos lo que
   HorneroOS sí puede guardar: una instantánea de configuración y una
   copia protegen tus ajustes de Hornero aunque no puedan proteger el
   sistema.

## Estado de validación

La prueba en VM desechable del contrato (ISO candidata, 2026-11-03)
está registrada paso a paso en HorneroOS/hornero. En resumen:

1. Instalar desde el esquema aceptado; primer arranque — **PASS**,
   después de corregir dos defectos del instalador que la prueba
   encontró.
2. Crear una instantánea / par de transacción — **PASS**: creación
   manual y un par pre/post de snap-pac alrededor de una
   actualización completa real.
3. Romper el sistema con una actualización mala — ejecutado solo
   como una mutación marcadora más una actualización completa, no
   como un estado de paquetes deliberadamente roto.
4. Arrancar el estado anterior desde el menú de arranque — **FAIL**:
   el arranque de la instantánea de solo lectura termina en modo de
   emergencia.
5. Restaurar y coincidir con el punto de la instantánea — **PASS**
   por reemplazo de @ dentro de un mismo kernel; **FAIL** a través
   de un cambio de kernel.
6. Ejercitar GC hasta el límite de retención — **NOT TESTED**:
   temporizadores habilitados, ninguna corrida de GC observada.

Hasta que los seis pasos pasen y queden registrados, la puerta de
actualizaciones/vuelta atrás de la preparación de releases se
mantiene en FAIL y esta documentación sigue diciendo que no hay
vuelta atrás del sistema de HorneroOS. Un futuro comando de
restauración de Hornero deberá envolver el flujo de reemplazo de @
con confirmación explícita; hasta que exista y esté probado, esta
página no va a describir ninguno.

## Relacionado

- [Mapa del Centro de control](control-center.md)
- [horneroctl](horneroctl.md)
- [Hornero Chromatic](chromatic.md)
- [Solución de problemas](../troubleshooting/README.md)
- [Contrato del backend de instantáneas](https://github.com/HorneroOS/hornero/blob/main/docs/SNAPSHOT_BACKEND_CONTRACT.md)
  y [límites de actualización y recuperación](https://github.com/HorneroOS/hornero/blob/main/docs/UPDATE_RECOVERY.md)
  en HorneroOS/hornero (en inglés)
