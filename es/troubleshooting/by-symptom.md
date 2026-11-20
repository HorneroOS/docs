# Solución de problemas por síntoma

Empezá por lo que ves, corré el chequeo de solo lectura de ese
síntoma y guardá la salida. No empieces por una solución: anotá
primero el error exacto y los pasos que lo reproducen.

```sh
horneroctl doctor
```

![Una terminal con la salida de doctor: catorce chequeos con marcas
OK, sesión Wayland, terminal elegida, rutas de configuración del
shell y temas Qt, terminando con "all 14 checks
passed".](https://www.horneroos.com/captures/cap-term-04.png)

*Salida de ejemplo de `doctor` en la máquina del mantenedor — las
rutas son su home; las tuyas van a diferir. Captura,
19 de noviembre de 2026.*

## La máquina no arranca

1. Arrancá una vez el [kernel de respaldo](../desktop/kernel-and-fallback.md)
   desde las opciones avanzadas de GRUB.
2. Si ningún kernel arranca, arrancá la ISO live y no toques la
   máquina hasta tener el log del arranque que falló.
3. Anotá si falla antes del menú, al desbloquear el disco o
   después del login: cada caso tiene otro dueño.

No hay rollback de sistema al que agarrarte; mirá
[Actualizaciones y recuperación](../desktop/updates-and-rollback.md)
para el procedimiento Btrfs manual y su límite de mismo kernel.

## Sin red

```sh
horneroctl hardware network status
horneroctl doctor
```

Si el adaptador ni aparece en el sistema, juntá `lspci -nnk`,
`lsusb` y sus líneas de kernel. Un adaptador ausente está por
debajo del escritorio. Mirá [Red y Bluetooth](README.md#network-and-bluetooth).

## Sin audio

```sh
horneroctl studio doctor
horneroctl studio selection show
systemctl --user status pipewire wireplumber
```

Confirmá primero el dispositivo correcto en Settings → Sound.
Si activaste un drop-in Studio de baja latencia, quitalo y
reiniciá los servicios como en
[Audio Studio](../../applications/studio-audio.md#recovery) antes de
cambiar otra cosa.

## El shell no levanta o un panel de Settings sale vacío

```sh
horneroctl shell status --json
horneroctl shell logs --lines 120
horneroctl config validate
```

Guardá el primer error de import o carga QML del log. No
reinicies la sesión gráfica en loop ni borres ajustes de usuario
para que un panel cargue. Mirá
[El shell falta](README.md#the-shell-is-missing-or-not-responding).

## Un juego no arranca

Corré `horneroctl gaming doctor` y cambiá una opción de
lanzamiento por vez como en
[Gaming: Proton, GameMode, Gamescope y MangoHud](../applications/gaming-proton-gamemode.md).
Guardá el log Proton de Steam para ese juego.

## Juntar logs para un reporte

```sh
journalctl -b -1 --no-pager
journalctl -b -k -p warning --no-pager
horneroctl doctor
```

`-b -1` es el arranque anterior, el que falló. Quitá usuarios,
hostnames, seriales, identificadores de red y líneas personales
antes de compartir, y seguí
[cómo reportar un bug](../development/README.md#reportá-un-bug).
