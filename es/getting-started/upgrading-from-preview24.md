# Actualizar una instalación preview24 existente

> Traducción al español rioplatense de la
> [versión en inglés](../../getting-started/upgrading-from-preview24.md), que es
> la canónica.

Esta guía migra un sistema instalado desde **HorneroOS v0.2.0-preview24** a la
composición de paquetes publicada en **v0.2.0-preview28**, sin reinstalar el
sistema operativo.

Se validó de punta a punta en una máquina virtual UEFI descartable (Studio —
Hyprland, Btrfs cifrado con LUKS, sin swap): los archivos de usuario, un perfil
de OBS y una línea personalizada en `.zshrc` sobrevivieron a la actualización y
al reinicio, y `horneroctl studio doctor` pasó todos los chequeos después.

> `horneroctl package upgrade` solo corre `pacman -Syu`. **No** realiza esta
> migración: no repara la configuración de repositorios de preview24, no
> actualiza paquetes del AUR, no instala paquetes de fábrica agregados después
> de preview24 (zsh, nano) ni cambia tu shell de login. Seguí en cambio los
> pasos de abajo.

## Antes de empezar

- Hacé un respaldo de todo lo que no te puedas permitir perder. Este
  procedimiento no tiene mecanismo de snapshots ni vuelta atrás; recuperarse de
  una actualización de sistema fallida usa herramientas estándar de Arch (caché
  de pacman, `downgrade`, chroot desde un medio vivo).
- Leé cada paso primero. El paso 1 es obligatorio en preview24: su configuración
  del gestor de paquetes está rota y `pacman -Syu` falla hasta repararla.

## 1. Repará la configuración de repositorios de pacman (bug de preview24)

Las instalaciones de preview24 vienen con dos defectos:

- La sección `[multilib]` de `/etc/pacman.conf` no tiene línea `Include`.
- `/etc/pacman.d/mirrorlist` no contiene ninguna línea `Server` activa.

Juntos provocan
`error: failed to synchronize all databases (no servers configured for repository)`.

Repará ambos y después verificá que cada repositorio habilitado tenga
servidores:

```bash
sudo sed -i '/^\[multilib\]/a Include = /etc/pacman.d/mirrorlist' \
  /etc/pacman.conf
sudo sed -i \
  '1i Server = https://geo.mirror.pkgbuild.com/$repo/os/$arch' \
  /etc/pacman.d/mirrorlist
grep -A1 '^\[multilib\]' /etc/pacman.conf
grep -c '^Server' /etc/pacman.d/mirrorlist
```

Resultado esperado: la línea `Include` aparece bajo `[multilib]` y el conteo de
mirrors es al menos 1 (agregá más mirrors si preferís).

## 2. Actualizá los paquetes de Arch

```bash
sudo pacman -Syu
```

No uses un `pacman -Sy` pelado seguido de instalar paquetes sueltos; eso deja el
sistema en un estado de actualización parcial.

## 3. Instalá los paquetes de fábrica agregados después de preview24

Preview28 hace de zsh la shell de login de fábrica para usuarios nuevos y trae
nano como editor por defecto. Las instalaciones existentes no reciben ninguno
automáticamente:

```bash
sudo pacman -S --needed zsh nano base-devel
```

`base-devel` solo hace falta para el paso siguiente (compilar el paquete del
AUR); saltealo si no querés herramientas de compilación instaladas.

## 4. Actualizá los paquetes de HorneroOS en el AUR

Componentes de HorneroOS como `hornero-config` se distribuyen por el AUR y
`pacman -Syu` no los toca. No hay un ayudante de AUR integrado; compilá el
paquete a mano:

```bash
git clone https://aur.archlinux.org/hornero-config.git
cd hornero-config
makepkg -si
pacman -Q hornero-config   # se espera 0.3.14-1 o más nuevo
```

Repetí la actualización equivalente para cualquier otro paquete de HorneroOS del
AUR que tengas instalado (por ejemplo `horneroctl-bin`).

## 5. Adoptá el editor por defecto de fábrica (usuarios existentes)

El valor por defecto `EDITOR=nano` / `VISUAL=nano` viene en
`/etc/skel/.config/environment.d/10-hornero-editor.conf`, que solo aplica a
usuarios creados de cero. Adoptalo para tu cuenta actual sin sobrescribir nada:

```bash
mkdir -p ~/.config/environment.d
cp -n /etc/skel/.config/environment.d/10-hornero-editor.conf \
  ~/.config/environment.d/
```

Cerrá sesión y volvé a entrar para que las variables surtan efecto. El archivo
de fábrica `/etc/skel/.zshrc` no se copia a propósito sobre tu `~/.zshrc`;
fusioná manualmente lo que quieras conservar de él.

## 6. Opcionalmente cambiá tu shell de login a zsh

Los usuarios existentes nunca se cambian automáticamente. Si querés la shell de
fábrica de preview28:

```bash
chsh -s /usr/bin/zsh
```

Cerrá sesión, volvé a entrar y confirmá con `echo $SHELL`.

## 7. Verificá

```bash
horneroctl studio doctor        # sistemas Studio; todos los chequeos en verde
systemctl --user status pipewire wireplumber
pacman -Q hornero-config zsh nano
```

Reiniciá una vez y confirmá que la máquina todavía desbloquea (LUKS), llega al
greeter e inicia sesión normalmente. Ninguno de los pasos anteriores toca tus
archivos, perfiles de OBS ni configuración personal.

## Limitaciones conocidas

- **La identidad del SO no cambia.** `/etc/os-release` mantiene `ID=arch` en los
  sistemas migrados. La identidad `ID=horneroos` la escribe el instalador al
  momento de instalar (preview28 y posteriores) y no se propaga con
  actualizaciones de paquetes. Las herramientas que detectan HorneroOS por
  os-release (por ejemplo `osRelease.id` de chezmoi) no van a reconocer un
  sistema preview24 migrado; usá el override documentado `HORNERO_NATIVE=1`
  donde esté soportado.
- **Sin reconciliación de ediciones.** Si una release futura cambia la
  composición de una edición, los sistemas ya instalados no ganan ni pierden
  paquetes de edición automáticamente. Instalalos o quitalos de forma explícita.
- **Sin vuelta atrás.** Todavía no existe una vuelta atrás del sistema HorneroOS
  en ningún tipo de instalación. Las instalaciones Btrfs limpias en previews
  posteriores ganan un diseño de almacén de snapshots, y herramientas de
  snapshots solo con una capacidad opt-in que viene apagada por defecto;
  ninguna de las dos cosas es una vuelta atrás, y un sistema preview24 migrado
  no se convierte. Mirá [Actualizaciones y recuperación][upd].
- **Los controladores gráficos quedan fuera de alcance.** Los sistemas NVIDIA y
  con GPU híbrida conservan su stack de controladores existente; esta guía se
  validó solo sobre gráficos de VM, no en hardware con GPU física.

[upd]: ../desktop/updates-and-rollback.md
