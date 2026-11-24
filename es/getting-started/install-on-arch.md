# Instalar HorneroOS sobre un Arch Linux existente

Esta guía instala el escritorio HorneroOS como paquetes sobre un
sistema Arch Linux que ya usás. Nada se reinstala, ningún disco se
toca y ningún archivo que ya sea tuyo se sobrescribe. Para una
instalación desde cero con provisión por edición, usá la ruta de
la ISO en [Primeros pasos](README.md).

## Qué obtenés y qué no

Obtenés el escritorio empaquetado: Hornero Shell, los defaults con
curaduría, el tema de greeter si lo pedís, y `horneroctl`. Llegan
también los modos de experiencia. Las aplicaciones de cada edición
no: el stack creativo de Studio, Steam y el resto de Gaming se
instalan con pacman/yay como en cualquier Arch, y cambiar de modo
no las instala por vos. La ISO sigue siendo el único camino que
provisiona una edición entera de una vez.

Las derivadas de Arch (CachyOS, EndeavourOS y otras) usan los
mismos paquetes, pero no están verificadas oficialmente; tratá
ese camino como experimental.

## Requisitos

Obligatorios:

- Arch Linux x86_64 completamente actualizado (`pacman -Syu`).
- `git` y `base-devel` para compilar paquetes del AUR, y un
  ayudante de AUR como yay (abajo).
- Para la experiencia completa, una sesión Wayland con Hyprland.
  La variante de solo la shell también lo necesita. Si todavía no
  tenés compositor, el paso de paquetes lo instala.

Recomendados: PipeWire + WirePlumber, y un respaldo de tu
configuración actual. El paso de configuración inicial nunca
sobrescribe tus archivos, pero un respaldo sigue saliendo gratis:

```sh
tar -czf ~/hornero-pre-adopt-$(date +%F).tar.gz \
  ~/.config/hypr ~/.config/ghostty ~/.config/environment.d 2>/dev/null
```

Los drivers de GPU quedan a tu cargo, igual que en Arch puro:
seguí la wiki de Arch para tu hardware (en NVIDIA, el driver
propietario y su modeset no los instala HorneroOS en este camino).

## 1. Instalar yay (si no tenés ayudante de AUR)

El AUR lo mantiene la comunidad: leé cada PKGBUILD antes de
compilar, y nunca corras `makepkg` como root.

```sh
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

## 2. Instalar los paquetes

`hornero-shell` trae como dependencias `hornero-config` (los
defaults) y `horneroctl-bin` (la CLI firmada). El segundo grupo es
el soporte de sesión; salteá lo que ya tengas.

```sh
yay -Syu hornero-shell
yay -S --needed hyprland xdg-desktop-portal-hyprland \
  xdg-desktop-portal-gtk kitty dex hypridle cliphist wl-clipboard
```

El greeter es opcional y solo si ya usás SDDM: instala el tema sin
cambiar tu display manager ni activarlo por vos.

```sh
yay -S hornero-greeter
```

## 3. Sembrar tu configuración de usuario (solo lo que falta)

Tu cuenta es anterior a los paquetes, así que el esqueleto de
fábrica en `/etc/skel` nunca te llegó. El sembrado empaquetado
copia solo lo que te falta —los módulos de Hyprland, la terminal,
el entorno de sesión y los symlinks a los helpers empaquetados— y
te muestra la lista exacta antes de tocar nada:

```sh
/usr/share/hornero/seed-user.sh --dest "$HOME" --dry-run
/usr/share/hornero/seed-user.sh --dest "$HOME"
horneroctl doctor
```

En releases actuales de `horneroctl` el mismo backend también
responde a `horneroctl config materialize --dest "$HOME"`. El
sembrado es idempotente: correrlo de nuevo tras una actualización
de paquete solo agrega archivos nuevos. Se niega a destinos de
sistema y a raíces que sean symlinks.

Lo que el sembrado nunca hace:

- Nunca sobrescribe un archivo existente. Tu propio
  `hyprland.lua`, la configuración de tu terminal y tu shell de
  login le ganan a cualquier default de fábrica.
- Nunca deshabilita otro escritorio, barra o daemon de
  notificaciones. Si uno ya arranca automático, van a convivir
  hasta que decidas.
- Nunca cambia tu display manager, bootloader ni particiones.

Si tu entrada de Hyprland es la de fábrica (sembrada arriba o de
una cuenta creada tras instalar los paquetes),
`horneroctl config refresh-hypr` mantiene su lista de módulos al
día de forma aditiva; tus overrides en `hyprland.lua.d/*-user.lua`
siguen siendo tuyos.

## 4. Arrancar el escritorio

No hay una sesión nueva para elegir: HorneroOS vive dentro de
Hyprland.

- **Sin configuración propia de Hyprland:** entrá a la sesión
  Hyprland desde tu display manager de siempre (o arrancá
  `Hyprland` desde una TTY). Los defaults sembrados/de fábrica
  arrancan la shell solos.
- **Con configuración propia de Hyprland:** tu entrada sigue al
  mando. Para probar solo la shell dentro de tu sesión actual,
  ejecutá `horneroctl shell start --yes`. Para adoptar la entrada
  de fábrica, mové tu `hyprland.lua` a un lado, sembrá de nuevo y
  llevá tus personalizaciones a `hyprland.lua.d/*-user.lua`.
- **Con otro escritorio instalado:** no hay nada que hacer. KDE,
  GNOME u otra sesión quedan instalados y elegibles en tu
  display manager; HorneroOS no reemplaza ninguno.

## 5. Hacelo tuyo

Abrí el Centro de control para layouts, temas, Hornero Chromatic,
modos de experiencia y extensiones PluginKit del catálogo. Los
compañeros se instalan desde el mismo catálogo como paquetes de
datos. Después seguí con [Primeros pasos después de
instalar](../applications/post-install-first-steps.md).

## Actualizar

Actualizar es el `yay -Syu` de siempre. Si querés, tomá antes un
snapshot de settings de Hornero:

```sh
horneroctl config snapshot create --yes
yay -Syu
```

El escritorio por paquetes puede ir más adelante que la ISO
publicada; es lo esperado. Seguí las notas de release para los
cambios por versión.

## Volver atrás y desinstalar

Desinstalar es quitar paquetes: tu configuración y tus datos
quedan donde estaban, y tu sesión anterior sigue arrancando como
siempre.

```sh
yay -Rns hornero-shell hornero-config horneroctl-bin
```

Los únicos archivos que creó el sembrado son los que listó al
correr; borrarlos es opcional y seguro si nunca los editaste. Tus
archivos propios nunca se tocaron, así que no hay nada que
restaurar.

## Problemas frecuentes

- **La shell no arranca con tu sesión:** tu entrada de Hyprland es
  tuya y no la autostartea. Arrancala una vez con
  `horneroctl shell start --yes` para confirmar que funciona, y
  después adoptá la entrada de fábrica (paso 3) o agregá ese
  comando a tu propio autostart.
- **`horneroctl doctor` reporta herramientas faltantes:** instalá
  el paquete nombrado y volvé a correrlo; el doctor distingue
  requisitos duros de herramientas creativas opcionales.
- **Dos daemons de notificaciones o barras a la vez:** es lo
  esperado cuando un componente de otro escritorio también
  arranca automático junto a Hornero Shell. Desactivá el autostart
  del que no quieras; HorneroOS no mata procesos ajenos por vos.
- **Cualquier otra cosa:** mirá
  [Problemas por síntoma](../troubleshooting/by-symptom.md).
