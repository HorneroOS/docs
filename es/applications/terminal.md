# Terminal y shell

Hornero separa la ventana de terminal, la shell interactiva adentro y las
herramientas de línea de comandos que gestionan el escritorio. Kitty es la
terminal por defecto elegida cuando está instalada; Alacritty y Ghostty son
alternativas opcionales con sus propios valores por defecto de Hornero. Las
aplicaciones de terminal son paquetes separados del host, no dependencias de
la Shell. **Super + E** abre Yazi en la terminal configurada del host, y los
lanzamientos normales de terminal siguen esa misma asociación.

## Abrir una terminal

- Presioná **Super + T** o **Super + Enter** para abrir la asociación XDG
  `TerminalEmulator` del host mediante `exo-open`.
- Abrí el Lanzador con **Ctrl + Space** y buscá una terminal instalada.
- Presioná **Super + E** para abrir Yazi en una ventana separada de la
  terminal configurada. Hornero elige Kitty por defecto; también se soportan
  Alacritty y Ghostty. Este flujo necesita la terminal elegida y Yazi.

Elegí una terminal instalada en **Ajustes → Terminal**. Hornero mantiene la
selección alineada entre el helper Xfce del host, la preferencia XDG y las
acciones de lanzamiento de la Shell. Podés inspeccionarla con
`horneroctl config default-apps list` o cambiarla desde la CLI. Previsualizá
primero el cambio:

```sh
horneroctl config default-apps set terminal ghostty --dry-run
horneroctl config default-apps set terminal ghostty --yes
```

Los destinos soportados son Kitty, Alacritty y Ghostty. El comando actualiza
`$XDG_CONFIG_HOME/xfce4/helpers.rc` del usuario y el archivo genérico
`$XDG_CONFIG_HOME/xdg-terminals.list` (o las rutas equivalentes bajo
`~/.config`), dejando intactos los valores MIME por defecto y otras entradas
de helpers. También quita una exclusión de respaldo para la terminal elegida.
Cuando está instalado, `xdg-terminal-exec` lee la lista genérica; un archivo
de preferencias específico del escritorio puede tener precedencia. Mirá
[Aplicaciones por defecto](default-apps.md) y
[atajos de teclado](../desktop/shortcuts.md).

## Kitty

Kitty es un emulador de terminal acelerado por GPU. Hornero Config provee sus
valores de sistema bajo `/etc/xdg/kitty`; tu configuración de usuario en
`~/.config/kitty/kitty.conf` puede sobrescribirlos. Los valores por defecto
incluyen la paleta Hornero Signal Night, IBM Plex Mono, espaciado de ventana,
scrollback y atajos de copiar/pegar:

| Tecla | Acción |
| --- | --- |
| `Ctrl + Shift + C` | Copiar selección |
| `Ctrl + Shift + V` | Pegar |
| `Ctrl + Shift + Page Up/Down` | Desplazar una línea |
| `Ctrl + Shift + Home/End` | Ir arriba / abajo del todo |
| `Ctrl + L` | Limpiar la pantalla visible |

> **Estado de release.** El comportamiento de paletas de abajo corresponde a
> Hornero Signal, incluido en `v0.2.0-preview42` y en `main`/AUR. Las ISO
> anteriores hasta `v0.2.0-preview32` escribían colores de terminal generados
> desde el fondo de pantalla.

Cada tema trae una paleta de Kitty como `<theme-id>.conf`, y `kitty.conf`
tiene una sola línea `include <theme-id>.conf` (el valor de fábrica es
`include hornero-signal-night.conf`). Aplicar un tema reescribe esa línea
include y recarga Kitty. Las previews anteriores incluían además un overlay
generado `~/.cache/hornero/smart-colors/colors-kitty.conf`. Signal ya no lo
usa: después de migrar a Signal, un override de usuario que todavía lo nombre
puede quitar esa línea. Dejala en una preview anterior, donde todavía lleva
los colores generados.

El [repositorio público de dotfiles](https://github.com/ulises-jeremias/dotfiles)
suma una configuración personal de Kitty con una ventana inicial de 80×24,
fuente de 12 puntos y 80% de opacidad de fondo. Son preferencias de estación
de trabajo, no un requisito de release de Hornero. Editá el `kitty.conf`
activo para personalizar Kitty. Mirá el
[manual de Kitty](https://sw.kovidgoyal.net/kitty/).

## Alacritty

Alacritty es una terminal opcional para quienes prefieren una configuración
TOML compacta. Cuando Alacritty está instalada, Hornero Config provee un
respaldo del sistema en `/etc/alacritty/alacritty.toml`. Importa la paleta
empaquetada Signal Night y después la paleta del tema aplicado, y habilita la
recarga en vivo de la configuración. Aplicar un tema escribe los colores de
ese tema en `~/.config/alacritty/hornero-colors.toml`. Si mantenés una
configuración de usuario en `~/.config/alacritty/alacritty.toml`, incluí ahí
los imports de la paleta de Hornero para mantener activos los colores del
tema.

El valor instalado por defecto usa 12 píxeles de relleno de ventana, 88% de
opacidad, 2.500 líneas de scrollback y cursor de bloque sin parpadeo. La
[referencia de configuración de Alacritty](https://alacritty.org/config-alacritty.html)
documenta los imports TOML y el resto de los ajustes.

## Ghostty

Ghostty es otra terminal opcional. Hornero Config provee un tema de respaldo
`Hornero Dynamic` bajo `/usr/share/ghostty/themes/` y siembra
`/etc/skel/.config/ghostty/config.ghostty` para cuentas recién creadas. Esa
configuración selecciona el tema de Hornero y fija 88% de opacidad de fondo.
Las cuentas existentes no se sobrescriben con el esqueleto; agregá
`theme = Hornero Dynamic` en tu propio `~/.config/ghostty/config.ghostty` para
activarlo.

Cuando se aplica un tema, Hornero escribe su paleta Signal en
`~/.config/ghostty/themes/Hornero Dynamic`, que tiene precedencia sobre el
respaldo del sistema, y le avisa a cualquier instancia activa de Ghostty que
recargue. Mantené estable el nombre del tema en tu configuración para que las
apariencias siguientes lo actualicen. Mirá la
[guía de configuración](https://ghostty.org/docs/config) y la
[guía de temas de color](https://ghostty.org/docs/features/theme) de Ghostty.

## Comportamiento compartido de apariencia

Aplicar un tema actualiza los archivos de paleta de Kitty, Alacritty y Ghostty
desde la paleta de terminal de 16 colores de ese tema. Cada emulador lee su
formato nativo. El fondo de pantalla nunca cambia los colores de la terminal.
Kitty y Alacritty caen a la paleta empaquetada Signal Night; Ghostty tiene un
respaldo estático `Hornero Dynamic`. Los archivos de nivel usuario siguen
siendo tuyos para personalizar. Para inspeccionar los colores en vivo, corré
`horneroctl appearance colors status`. Mirá
[Apariencia](../desktop/appearance.md) para los controles de temas.

## Shell y flujo de comandos

La shell configurada en tu cuenta corre adentro de la terminal. Hornero Config
no convierte a Zsh, a un prompt, a plugins de shell ni a alias en dependencias
del sistema. La configuración pública de dotfiles instala Zsh de forma
opcional y define un perfil personal en `~/.zshrc`, `~/.zsh/config.d/` y
archivos de prompt relacionados. Activa edición de línea de comandos estilo
vi, búsqueda inversa en el historial con `Ctrl + R` y carga de prompt/alias.
Esas elecciones personales no afectan el contrato CLI de Hornero.

Ese perfil también fija `$EDITOR` y `$VISUAL` a Neovim para programas de línea
de comandos. Hornero en sí no tiene un editor gráfico por defecto universal;
mirá [Aplicaciones por defecto](default-apps.md). Para correr tareas del
escritorio desde una shell, usá [`horneroctl`](../desktop/horneroctl.md) y su
salida instalada de `--help`.

## Configuración opcional de tmux

La configuración personal de estación de trabajo incluye tmux y plugins;
ninguno es requerido por Hornero. Su configuración usa `Ctrl + A` como prefijo
principal, `Ctrl + B` como prefijo alternativo, soporte de mouse, copy-mode
estilo vi y un historial largo de scrollback. La instalación de plugins
depende del checkout opcional de TPM. Mirá el
[manual de tmux](https://github.com/tmux/tmux/wiki) antes de copiar esas
preferencias a otra máquina.

## Cuando algo no abre

- Corré `horneroctl apps launch --list` para ver qué backends de lanzamiento
  están disponibles.
- Corré `horneroctl apps terminal-file --help` para inspeccionar el flujo de
  Yazi.
- Verificá que la terminal elegida esté instalada y que el helper
  `TerminalEmulator` en `~/.config/xfce4/helpers.rc` coincida con ella.
- Si los colores de una terminal quedaron viejos, volvé a aplicar la
  apariencia deseada en **Ajustes → Apariencia** y revisá
  `horneroctl appearance colors status`.
- Verificá si una configuración de nivel usuario está sobrescribiendo el
  respaldo del sistema de Hornero. Para Ghostty, confirmá que
  `theme = Hornero Dynamic` esté presente en el archivo `config.ghostty`
  activo.

Referencias útiles: [Kitty](https://sw.kovidgoyal.net/kitty/),
[Alacritty](https://alacritty.org/config-alacritty.html),
[Ghostty](https://ghostty.org/docs),
[manual de Zsh](https://zsh.sourceforge.io/Doc/Release/),
[wiki de tmux](https://github.com/tmux/tmux/wiki),
[Apariencia](../desktop/appearance.md) y
[atajos](../desktop/shortcuts.md).
