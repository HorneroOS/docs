# Solución de problemas

Empezá con diagnósticos de solo lectura. Registrá el error exacto y los
pasos que lo reproducen antes de cambiar configuración o reinstalar
paquetes.

```sh
horneroctl doctor
horneroctl config validate
horneroctl shell status --json
horneroctl appearance doctor
```

## La shell no está o no responde

Chequeá si Quickshell es alcanzable y después leé su log reciente:

```sh
horneroctl shell status --json
horneroctl shell logs --lines 120
```

Si el log reporta un módulo o plugin QML faltante, registrá las versiones
de los paquetes y el primer error de import/carga. No reinicies la sesión
gráfica una y otra vez. Ver las
[notas de troubleshooting de la Shell](https://github.com/HorneroOS/shell/blob/main/README.md#troubleshooting)
y [reportá un problema reproducible](../development/README.md#reportá-un-bug).

## Ajustes o un panel se ve vacío

Validá la configuración materializada, leé el log de la Shell y volvé a
abrir el panel específico desde el Centro de control. Incluí el nombre
del panel y si se abrió desde la barra lateral o un deep link. Evitá
borrar ajustes de usuario:

```sh
horneroctl config validate
horneroctl shell logs --lines 120
horneroctl config gui --pane appearance
```

Si otro panel anda pero uno está en blanco, reportalo como un fallo de
carga de panel.

## El tema y el fondo no coinciden

Leé el estado en vivo antes de aplicar otro aspecto:

```sh
horneroctl appearance status --json
horneroctl appearance theme get
horneroctl appearance gtk current
horneroctl appearance gtk current-icon
horneroctl wallpaper current
horneroctl appearance doctor
```

Una imagen nombrada por un manifiesto de tema puede no estar instalada
localmente. Elegí un fondo local y revisá los temas GTK y de íconos
instalados antes de tratar una dependencia externa como un fallo de la
shell. Ver [Apariencia](../../desktop/appearance.md) y
[Fondos](../../desktop/wallpapers.md).

## Red y Bluetooth

Chequeá que el adaptador sea visible para el sistema operativo y después
abrí el panel correspondiente del Centro de control. Un adaptador
faltante está por debajo de la capa de la shell; reuní `lspci -nnk`,
`lsusb` y las líneas relevantes del log del kernel antes de reportarlo.
Estos comandos solo inspeccionan dispositivos.

## Pantalla y gráficos

Chequeá la lista de monitores y el driver del kernel cargado:

```sh
hyprctl monitors -j
lspci -nnk
journalctl -b -k -p warning
```

Para NVIDIA o gráficos híbridos, seguí la
[guía de hardware](../hardware/README.md#nvidia-y-gráficos-híbridos)
específica de tu dispositivo. Una pantalla negra o una sesión que falla
antes de que arranque la shell no es un problema del Centro de control.

## Pantalla de login

Para un fallo de la pantalla de login de SDDM, reuní el paquete instalado
y el tema seleccionado junto con el log del arranque actual:

```sh
pacman -Q sddm hornero-greeter
journalctl -b -u sddm --no-pager
```

El [repositorio del greeter de Hornero](https://github.com/HorneroOS/greeter)
es dueño del contrato de tema y empaquetado. No reinicies SDDM durante
una sesión gráfica solo para probar un tema.

## Fallos de instalación

Si la ISO Preview no arranca, el instalador Calamares falla, o el primer
arranque de esa ISO no llega a un login, reportalo en el
[selector de issues de HorneroOS/installer](https://github.com/HorneroOS/installer/issues/new/choose)
con el nombre de la ISO, tu firmware (UEFI o BIOS), si el disco está
cifrado y el paso donde falló. Los fallos posteriores a ese primer
arranque (greeter, shell, hardware de escritorio, aplicaciones)
pertenecen a los trackers de los componentes dueños de abajo, no al
repositorio del instalador.

## Incluí esto en un reporte de bug

- Repositorio y versión del componente relevantes.
- Qué esperabas y qué pasó.
- La secuencia de acciones repetible más chica.
- Las primeras líneas de error relevantes, sin identificadores personales.
- Una captura solo cuando no contiene ventanas privadas ni notificaciones.

Ver [cómo reportar un bug](../development/README.md#reportá-un-bug) para
los links de issues de cada repositorio y la información a incluir.

## El instalador no ve el disco NVMe interno (Intel VMD/RST)

En algunas laptops Intel (por ejemplo modelos ASUS ROG) el firmware
expone el SSD NVMe a través de Intel VMD/RST ("PCIE RST Controlled
Disk"). Con VMD activado, el sistema Live puede no mostrar ningún disco
interno. Es un problema de visibilidad de la controladora, no un disco
faltante o dañado:

1. **No** borres particiones ni reformatees nada para "arreglarlo".
2. Reiniciá al setup del firmware y cambiá la controladora de
   almacenamiento de RST/VMD al modo NVMe/AHCI estándar, si tu firmware
   lo ofrece.
3. Arrancá de nuevo la ISO Live de HorneroOS y confirmá que el disco
   aparezca en la lista de discos del instalador antes de seguir.

Advertencias: cambiar el modo de la controladora puede dejar sin arrancar
una instalación de Windows existente hasta que su driver de
almacenamiento esté preparado, y puede afectar la recuperación de
BitLocker (tené la clave de recuperación a mano). HorneroOS nunca cambia
ajustes de firmware por vos. No se afirma compatibilidad con discos
gestionados por VMD; el camino de controladora estándar de arriba es el
probado. Notá también que un disco faltante no prueba que el SSD esté
sano: si el disco sigue invisible también en modo de controladora
estándar, sospechá un problema de hardware o de conexión y frená antes de
instalar en otro lado.

## Swap cifrado y el error de initramfs `openswap`

Las builds viejas del instalador podían generar una configuración de
`mkinitcpio` con un hook `openswap` (más entradas `encrypt` duplicadas)
para LUKS + swap cifrado separado, fallando con `ERROR: Hook 'openswap'
cannot be found`. HorneroOS no incluye ningún hook `openswap`, así que
ese esquema nunca podía producir un initramfs arrancable. Por eso los
instaladores actuales ofrecen solo `No Swap` (`userSwapChoices:
[ none ]`): un límite fail-closed, no una afirmación de que el swap
cifrado esté soportado. Si necesitás swap, agregá un swapfile sobre la
raíz Btrfs instalada (ya cifrada) después de la instalación en vez de
reactivar la opción de partición.

## Copy-to-RAM y el `base.sqfs` faltante

Con mucha RAM, Archiso podía copiar el sistema Live a la RAM y desmontar
el payload de instalación, tras lo cual Calamares fallaba con `The source
filesystem "/run/archiso/bootmnt/hornero/x86_64/base.sqfs" does not
exist`. Las ISOs actuales desactivan el copy-to-RAM automático y
verifican el payload antes de cualquier cambio de disco. Si te pasa en
una ISO vieja, arrancá con `copytoram=n` como workaround y preferí una
ISO actual.
