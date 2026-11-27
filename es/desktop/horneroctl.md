# `horneroctl`

`horneroctl` es la interfaz de línea de comandos de Hornero para capacidades
del sistema, ajustes del escritorio, diagnósticos y scripts. Usala cuando
quieras comandos repetibles o necesites inspeccionar el estado sin abrir una
página de Ajustes.

Empezá con la ayuda del comando que necesitás:

```sh
horneroctl --help
horneroctl appearance --help
horneroctl appearance theme --help
```

Usá `--json` para salida legible por máquina. Los comandos de solo lectura no
necesitan confirmación. Para un cambio, inspeccioná el dry run y después pasá
`--yes`:

```sh
horneroctl shell preset apply cockpit --dry-run
horneroctl shell preset apply cockpit --yes
```

## Grupos de comandos

`horneroctl` organiza sus subcomandos en 27 grupos de nivel superior:

- `agent` — gestionar agentes locales de código con IA, valores por defecto,
  configuración, ejecuciones en sandbox y uso (`horneroctl agent list`).
- `appearance` — temas, paletas Chromatic, sincronización GTK/Qt, modo noche y
  colores (`horneroctl appearance status --json`).
- `apps` — lanzador de aplicaciones, switcher, observador `git-status`,
  toggles, rendimiento y entradas XDG de WebApp/TUI
  (`horneroctl apps toggle launcher`).
- `assistant` — gateway opcional del asistente Hermes, sesiones, herramientas,
  política ABAC, workspaces y prompts (`horneroctl assistant status`).
- `backup` — crear, listar, restaurar y programar copias de seguridad de
  usuario (`horneroctl backup list`).
- `bluetooth` — diagnósticos, estado, dispositivos, energía y reinicio del
  servicio Bluetooth (`horneroctl bluetooth doctor`).
- `capture` — capturas de pantalla, grabación de pantalla y portapapeles
  (`horneroctl capture status`).
- `completion` — generar scripts de autocompletado para `bash`, `fish` y `zsh`
  (`horneroctl completion bash`).
- `config` — GUI del Centro de control, rutas, validación, snapshots y
  aplicaciones por defecto (`horneroctl config validate`).
- `doctor` — correr chequeos de salud del sistema y la sesión
  (`horneroctl doctor`).
- `gaming` — diagnósticos de la edición Gaming, opciones de lanzamiento y
  selecciones (`horneroctl gaming doctor`).
- `github` — actividad de GitHub de solo lectura, bandeja, estado,
  estadísticas y exportación vía `gh` (`horneroctl github status`).
- `hardware` — controles de batería, brillo, teclado, micrófono, red,
  Bluetooth y diagnóstico redacted `rollcall`
  (`horneroctl hardware battery status`).
- `help` — mostrar la ayuda de la CLI para cualquier grupo de comandos
  (`horneroctl help`).
- `hypr` — animaciones, cursor, entrada, layouts, monitores y plugins de
  Hyprland (`horneroctl hypr monitors list`).
- `lock` — control y estado de la pantalla de bloqueo
  (`horneroctl lock status`).
- `mode` — cambiar o inspeccionar modos de experiencia del escritorio
  (`horneroctl mode list`).
- `package` — consultar actualizaciones de repositorios/AUR, dependencias y
  actualizaciones del sistema (`horneroctl package check`).
- `plugin` — explorar catálogos de PluginKit, instalar, validar, confiar,
  activar/desactivar, correr acciones tipadas o generar plantillas de plugins
  (`horneroctl plugin catalog`).
- `power` — bloquear, cerrar sesión, suspender, reiniciar, apagar y estado de
  energía (`horneroctl power status`).
- `recovery` — diagnósticos de solo lectura de snapshots y preparación de
  recuperación (`horneroctl recovery doctor`).
- `shell` — iniciar, detener, reiniciar, leer logs, IPC y presets de barras
  (`horneroctl shell status`).
- `studio` — perfiles de audio de Studio, trabajos de render, modos, apps y
  diagnósticos (`horneroctl studio doctor`).
- `system` — perfil de edición instalada e información del compositor activo
  (`horneroctl system info`).
- `version` — imprimir la versión de `horneroctl` (`horneroctl version`).
- `wallpaper` — inspeccionar o cambiar el fondo de pantalla activo
  (`horneroctl wallpaper current`).
- `welcome` — abrir, restablecer o configurar el Centro de bienvenida al
  iniciar sesión (`horneroctl welcome status`).

Corré `horneroctl <grupo> --help` para inspeccionar cada subcomando y flag de
un grupo.

## Abrir una página de Ajustes

La CLI puede abrir el Centro de control directamente en un panel:

```sh
horneroctl config gui
horneroctl config gui --pane appearance
horneroctl config gui --pane network
```

Los IDs de panel salen del
[registro de paneles](https://github.com/HorneroOS/shell/blob/main/modules/controlcenter/PaneRegistry.qml)
de la Shell; los ejemplos de arriba usan `appearance` y `network`. Si un
destino no puede abrirse, corré el comando de la CLI correspondiente directo;
mirá `horneroctl <comando> --help`.

## Comandos útiles

| Necesidad | Comando |
| --- | --- |
| Chequear el entorno de ejecución | `horneroctl doctor` |
| Ver rutas resueltas de configuración y estado | `horneroctl config paths` |
| Validar la configuración de la shell | `horneroctl config validate` |
| Ver el tema y la apariencia activos | `horneroctl appearance status --json` |
| Chequear la consistencia del tema | `horneroctl appearance doctor` |
| Listar los temas instalados | `horneroctl appearance theme list` |
| Ver el fondo de pantalla actual | `horneroctl wallpaper current` |
| Listar presets de la shell | `horneroctl shell preset list --full` |
| Leer logs de la Shell | `horneroctl shell logs --lines 100` |
| Leer los atajos de teclado actuales | `horneroctl hardware keyboard keys` |

![Una terminal mostrando la salida de doctor: catorce chequeos listados con
marcas OK, cubriendo la sesión Wayland, la terminal elegida, las rutas de
configuración de la shell y los temas Qt, terminando con "all 14 checks
passed".](https://www.horneroos.com/captures/cap-term-04.png)

*Ejemplo de salida de `doctor` en el equipo del maintainer — las rutas
mostradas son del directorio home de esa máquina; las tuyas van a diferir.
Captura, 19 de noviembre de 2026.*

## Buscar actualizaciones

Los chequeos de actualizaciones conscientes de AUR informan los paquetes de
repositorios mediante `checkupdates` y los paquetes de AUR mediante `yay -Qua`
o `paru -Qua` cuando uno de esos helpers está instalado. Estos chequeos solo
consultan el estado de paquetes; no instalan ni actualizan nada. La consulta de
AUR tiene un límite de 30 segundos.

```sh
horneroctl package check
horneroctl package updates --json
horneroctl package check --dry-run
```

`package check` lista cada origen por separado. `package updates` incluye un
`count` combinado, además de `repository_count`, `aur_count` y `aur_status` en
la salida JSON. Si no hay `yay` ni `paru` disponibles, los resultados de
repositorios siguen estando disponibles y el carril de AUR queda marcado
explícitamente como no verificado. Un dry run muestra qué comandos se correrían
sin invocar ninguna consulta. Una actualización completa del sistema es una
operación separada y explícita: `horneroctl package upgrade`.

## Información de edición y compositor

`horneroctl system info` informa la composición instalada por separado del
compositor activo en la sesión actual:

```sh
horneroctl system info
horneroctl system info --json
```

El comando lee el registro de perfil instalado por una composición de
HorneroOS. Informa la edición, los conjuntos de paquetes, el compositor
configurado, la madurez y la revisión fuente, junto con el compositor detectado
en la sesión en curso. No infiere una edición a partir de los paquetes que
estén instalados. Los sistemas sin registro de perfil se informan como
**unrecorded**.

## Actualizaciones y preparación de recuperación

Hoy no hay vuelta atrás del sistema en HorneroOS, y ningún comando crea ni
restaura un snapshot del sistema operativo. `horneroctl package upgrade --yes`
hace una actualización completa del sistema sin paso de snapshot. El único
subcomando de recuperación es de solo lectura:

```sh
horneroctl recovery doctor
horneroctl recovery doctor --json
```

Inspecciona el backend de snapshots incluido (actualmente `none`), el sistema
de archivos raíz, el almacén `/.snapshots`, `snapper` y sus timers. Estar
preparado no prueba que una restauración funcione. Mirá
[Actualizaciones y recuperación: todavía no hay vuelta atrás del sistema](updates-and-rollback.md).

## Recuperación de configuración

`horneroctl config snapshot list` muestra los snapshots guardados. Creá o
restaurá un snapshot solo después de revisar su dry run y elegir el destino
buscado. `horneroctl config show <clave>` lee un valor materializado;
`config paths` muestra qué archivos están activos. Un snapshot de configuración
archiva solo ajustes de Hornero; nunca es un snapshot del sistema ni una vuelta
atrás del SO.

La CLI no reescribe datos de otro producto ni de un espacio de rutas retirado.
Para recuperar una configuración rota de Hornero, inspeccioná
`horneroctl config paths`, usá un snapshot revisado o restablecé el archivo de
usuario específico descripto en la página de ajustes correspondiente.

## Asistente y agentes

El asistente opcional de IA Hermes (`assistant`) viene desactivado por defecto
y nunca es obligatorio. Cuando se activa, habla con el gateway local de Hermes
en `http://127.0.0.1:8642` usando una clave Bearer local de usuario con
permisos `0600`. Nada se autoaprueba y nada corre como root:

```sh
horneroctl assistant status
horneroctl assistant health
horneroctl assistant enable --dry-run
horneroctl assistant gateway status
horneroctl assistant tools --json
horneroctl assistant policy
horneroctl assistant ask "what updates are available?" --mode ask
```

Usá `horneroctl assistant shell-proposal --command "<cmd>"` para clasificar el
riesgo de un comando sin ejecutar nada, o
`horneroctl assistant delegate <agent-id> --workspace <dir> "<task>"` para una
propuesta de derivación en modo dry run.

`horneroctl agent` es un registro declarativo de CLIs locales de agentes de
código (`javi-hermes`, `codex`, `claude-code`, `muse`, `cursor`, `opencode`,
`veasel`). Los comandos de inspección son de solo lectura, nunca se leen los
contenidos de credenciales y `agent launch` solo imprime una propuesta dry run
sin ejecutar ningún agente.

Para ejecutar un agente registrado de forma directa, usá `horneroctl agent run
<id> --sandbox`: se niega a correr sin sandbox y lanza la CLI dentro de una
jaula de workspace con `bubblewrap`, reemplazando `$HOME` con `tmpfs`,
enmascarando directorios sensibles de credenciales y navegadores, montando en
lectura/escritura solo `--workspace <dir>` (por defecto el directorio actual) y
el directorio de configuración propio del agente, y sin interpolación de shell
ni flags de autoaprobación. Pasá `--no-net` para aislar la red,
`--allow-git-auth` para montar credenciales de git/SSH en solo lectura
(manteniendo GPG y AWS enmascarados), `--dry-run` para ver el argv exacto de
`bwrap` y `-- <args>...` para reenviar flags textuales. Mirá
[Confinamiento de agentes de IA](../security/README.md#confinamiento-de-agentes-de-ia-bubblewrap):

```sh
horneroctl agent list
horneroctl agent status codex --json
horneroctl agent doctor
horneroctl agent usage --json
horneroctl agent default show
horneroctl agent launch codex
horneroctl agent run codex --sandbox --dry-run
horneroctl agent run claude-code --sandbox --no-net --dry-run
horneroctl agent run opencode --sandbox -- --help
horneroctl agent config status
```

## Plugins, GitHub y Chromatic

`horneroctl plugin` gestiona paquetes estáticos de extensiones de Quickshell
con recibos de propiedad bajo el estado XDG. Los plugins recién instalados
arrancan desactivados, los plugins no oficiales requieren `trust` explícito
para el hash actual de su payload antes de activarse, y el QML de Quickshell no
corre en sandbox:

```sh
horneroctl plugin catalog
horneroctl plugin community list --json
horneroctl plugin list --json
horneroctl plugin validate ./my-plugin
horneroctl plugin install-local ./my-plugin --dry-run
horneroctl plugin trust example-clock --dry-run
horneroctl plugin enable example-clock --dry-run
horneroctl plugin action list
```

`horneroctl github` expone actividad de desarrollo en GitHub de solo lectura
(Dev Pulse) mediante la CLI oficial `gh`. `gh` es dueña de la autenticación,
ningún token se registra ni se guarda en caché, y no se modifica nada en
GitHub:

```sh
horneroctl github status
horneroctl github stats --days 30 --json
horneroctl github inbox --json
horneroctl github refresh --json
horneroctl github export --format markdown --output report.md --public-only
```

`horneroctl appearance chromatic` maneja Hornero Chromatic para generar paletas
Signal verificadas por contraste a partir del fondo de pantalla, una imagen o
colores semilla, con reversión transaccional:

```sh
horneroctl appearance chromatic status
horneroctl appearance chromatic preview --seed "#D98A3A"
horneroctl appearance chromatic apply --dry-run
horneroctl appearance chromatic rollback --yes
horneroctl appearance chromatic off --yes
```

## Studio, hardware rollcall y lanzadores WebApp/TUI

`horneroctl studio` ofrece diagnósticos de solo lectura, registro de intención
de cargas de trabajo (nunca instala paquetes), drop-ins reversibles de PipeWire
en Baja Latencia, modos temporales de perfil de energía y trabajos de render
tipados con adaptadores en lista blanca:

```sh
horneroctl studio doctor
horneroctl studio selection show --json
horneroctl studio audio status
horneroctl studio mode show
horneroctl studio jobs list
horneroctl studio app show artcraft-launcher --json
```

`horneroctl hardware rollcall` arma un reporte de diagnóstico de hardware de
solo lectura con redacción automática sobre diez categorías (`wifi`,
`bluetooth`, `audio-output`, `audio-input`, `panel`, `backlight`, `touchpad`,
`graphics`, `battery`, `services`), ocultando direcciones MAC e identificadores
etiquetados antes de compartir:

```sh
horneroctl hardware rollcall --list
horneroctl hardware rollcall --markdown
horneroctl hardware rollcall wifi graphics --json
```

`horneroctl apps webapp` y `horneroctl apps tui` gestionan entradas `.desktop`
XDG propiedad de Hornero (`hornero-webapp-<id>.desktop` y
`hornero-tui-<id>.desktop`) bajo `$XDG_DATA_HOME/applications` (usando por
defecto `chromium --app=<url>` para webapps y `kitty` para apps TUI):

```sh
horneroctl apps webapp list
horneroctl apps webapp add github --name GitHub --url https://github.com
horneroctl apps webapp remove github
horneroctl apps tui list
horneroctl apps tui add lazygit --name Lazygit --command lazygit
horneroctl apps tui remove lazygit
```

## Scripts

Preferí salida estructurada y chequeos explícitos antes que parsear texto de
pantalla:

```sh
horneroctl appearance status --json
horneroctl shell preset current --json
```

Tratá un código de salida distinto de cero como falla. La CLI verifica el
estado en vivo en cambios de apariencia de varias partes; una aplicación
parcial se informa como error para que un script pueda frenar y recuperarse. El
[repositorio HorneroOS/hornero](https://github.com/HorneroOS/hornero) es
dueño de la implementación de los comandos y de los contratos detallados.
