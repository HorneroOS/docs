# Matriz competitiva de capacidades

> Traducción al español rioplatense de la
> [versión en inglés](../../development/competitive-capability-matrix.md), que
> es la canónica.

Comparación respaldada por evidencia de HorneroOS frente a las referencias
open-source más sólidas de escritorios Arch/Wayland. Este documento guía las
prioridades de ingeniería; no es texto de marketing. Una capacidad solo está
"validada" cuando una persona usuaria puede descubrirla, configurarla, usarla y
recuperarse de ella — nunca simplemente porque exista código.

Estados de madurez: **Validated** · **Partial** · **Experimental** ·
**Planned** · **Absent**.

## Referencias upstream estudiadas

Estudiadas desde el código fuente en un espacio de trabajo aislado de
investigación (nunca en commits de producto, nunca instaladas en un host).
Revisiones fijadas:

| Proyecto | Revisión | Estudiado por |
| --- | --- | --- |
| Omarchy | `81fd2d23ca6e` | Cohesión, cambio de tema, migraciones |
| Ryoku | `98a0368253d9` | Filosofía del instalador, Rashin |
| DankMaterialShell | `d6a362d6b36b` | Cargador de plugins, servicios en Go |
| Noctalia Shell (v4) | `3aab45a2f34f` | Configurabilidad, API de plugins |
| Hermes Agent | `f14699a13798` | API del gateway, runs, aprobaciones |

URLs completas: `github.com/omacom/omarchy`, `github.com/Ryoku-dev/ryoku`,
`github.com/AvengeMedia/DankMaterialShell`, `github.com/kozer/noctalia-shell`
(el repositorio canónico ahora es `noctalia-dev/noctalia`),
`github.com/NousResearch/hermes-agent` (MIT). Clase de atribución para cada
fila anterior: *estudiado para inspiración*. Cualquier reutilización futura de
código requiere verificación de licencia y atribución en el repositorio dueño.

## Resumen de la matriz

| Capacidad | Estado HorneroOS | Dueño |
| --- | --- | --- |
| Runtime de plugins/extensiones | Partial | shell + hornero |
| Companion / asistente de IA | Experimental | shell + hornero |
| Transporte Hermes | Experimental | hornero |
| Herramientas de agente read-only | Partial (sólido) | hornero |
| Proveedores del lanzador | Partial | shell |
| Profundidad del Centro de control | Partial | shell |
| Sistema de temas | Validated (núcleo) | config + hornero |
| Actualizaciones y recuperación | Partial | hornero + installer |
| Instalador y primer arranque | Experimental | installer |
| Hardware y rendimiento | Partial | hornero + qa |
| Perfiles opcionales | Planned | hornero + config |
| Incorporación (onboarding) | Partial | shell |
| Capacidades solo en dotfiles | Partial | config + shell |

## Evidencia por capacidad

### Runtime de plugins/extensiones

- DMS: `PluginService.qml` más registros en Go; QML en proceso con privilegios
  completos de usuario, API experimental, sin firma.
- Noctalia v4: `pluginApi` inyectado más puntos de entrada.
- HorneroOS: contrato y validador estático (`shell/docs/PLUGINS.md`,
  `shell/scripts/validate_plugin.py`, esquema v1, imports permitidos,
  coincidencia exacta de archivos). El ciclo de vida está implementado:
  `horneroctl plugin enable|disable` es dueño del estado del recibo (las
  instalaciones limpias arrancan deshabilitadas; habilitar revalida y falla
  cerrado). `services/Plugins.qml` descubre plugins habilitados y
  `modules/plugins/PluginHost.qml` carga cada punto de entrada en su propio
  loader con aislamiento de fallos por plugin. El campo `placement` del
  manifiesto renderiza plugins de barra en el grupo final de la barra
  (`background` queda sin interfaz gráfica) y plugins de dashboard como
  tarjetas en la pestaña Extensions del dashboard. El panel Extensions del
  Centro de control lista el estado instalado y puede habilitar/deshabilitar
  invocando los comandos exactos de ciclo de vida de `horneroctl`
  (`horneroctl` sigue siendo el único escritor de recibos; habilitar pide una
  confirmación en línea que espeja el gate `--yes` de la CLI). La ubicación
  `desktop` renderiza widgets en la capa de fondo (pila fija abajo a la
  derecha; ubicación y persistencia todavía no son configurables). Todavía no
  están hechos la firma ni un registro comunitario. El QML habilitado corre con
  los permisos de quien inició sesión; no está en sandbox.

### Companion / asistente de IA

- Ryoku Rashin (`docs/rashin.md` en Ryoku): opcional, apagado por defecto,
  daemon en loopback, bóveda generada de conocimiento del sistema, instalación
  de Hermes en un clic; sin UX nativa de chat en la shell.
- HorneroOS: estados de Companion, apariencias, IPC y estados reservados del
  asistente (`listening/thinking/acting/success/warning/error`) están vivos.
  `horneroctl assistant` (`status`, `enable`, `disable`, `tools`, `ask`, `stop`,
  `approve`, `clarify`, `events`)
  habla con Hermes; `AssistantBridge.qml` enruta `ask` del IPC de Companion
  solo por esa CLI, muestra aprobaciones pendientes en el globo y nunca las
  auto-responde; el lanzador ofrece una entrada de prompt `>ai`. Apagado por
  defecto; herramientas de solo lectura corte 1. `assistant ask` y
  `assistant events` aceptan `--stream` (solo salida humana): los deltas SSE
  se imprimen en vivo a medida que llegan (parser incremental sobre el
  callback de progreso HTTP; las rutas con buffer y `--json` no cambian). Un
  panel nativo de chat muestra la conversación con botones de aprobación; la
  aceptación con Hermes real pasó localmente el 2026-10-19 (proveedor real,
  aprobaciones aprobar/denegar ejecutadas, uso de herramientas guiado por
  skill — ver el doc de arquitectura). Quedan la aceptación gráfica de
  Companion y el ciclo de vida administrado de Hermes.

### Transporte Hermes

- `gateway/platforms/api_server.py` de Hermes: `127.0.0.1:8642`, clave
  Bearer, `POST /v1/runs`, eventos SSE, `/stop`, `/approval`, `/clarify`,
  `GET /v1/capabilities`, claves de idempotencia. Solo sesiones propiedad de la
  API.
- HorneroOS: implementado en `hornero_core/assistant.v` — endpoint loopback,
  archivo local de clave Bearer (`0600`), runs + consumo SSE, detención,
  respuestas de aprobación/aclaración, lector `events` para solicitudes
  pendientes y sonda de capacidades en `assistant status`. No hay semver de
  gateway para fijar, así que `status` negocia el protocolo (plataforma más
  los cinco flags de funcionalidad que llama el cliente) contra el commit
  estudiado de Hermes `f14699a13798…` y falla cerrado cuando es incompatible.
  Mirá [Arquitectura del asistente Hermes](hermes-assistant-architecture.md).

### Herramientas de agente de solo lectura

- El sustrato de HorneroOS es sólido: consultas de solo lectura de `horneroctl`
  con una envoltura `--json` uniforme — info del sistema, apariencia,
  consultas de tema y GTK, chequeo de actualizaciones de paquetes, hardware,
  Hyprland, shell, energía, fondo de pantalla, bienvenida.

### Lanzador, Centro de control, temas

- El lanzador existe; los proveedores definidos por plugins están bloqueados en
  el runtime de plugins.
- Centro de control: 17 paneles (red, bluetooth, VPN, apariencia, barra de
  tareas, layout, lanzador, dashboard, companion, audio, notificaciones, OSD,
  sistema, actualizaciones, terminal, energía, extensiones). Las brechas se
  siguen por panel, no con UI ficticia.
- Temas: núcleo validado. Packs maduros, esquema de tokens, enlace de GTK,
  íconos y fondo de pantalla, aplicación por CLI, 12 Hornero Originals
  regionales. Falta adoptar el intercambio atómico por etapas de Omarchy con
  token de generación (`omarchy-theme-set`).

### Actualizaciones, recuperación, instalador

- Omarchy: archivos marcadores de migración y snapshot antes de actualizar.
- HorneroOS tiene actualizaciones para paquetes y componentes. No hay una
  historia probada de snapshots/vuelta atrás del SO; un respaldo de chezmoi es
  solo de configuración y no debe venderse como vuelta atrás del SO.
- Instalador: Calamares provisional; la ISO Preview firmada v0.2.0-preview22
  está publicada y pasó la matriz de instalación en VM (hardware físico sin
  validar). El issue 11 de `installer` sigue la aceptación restante de
  instalación. Los gates oficiales (issue 12) todavía no están acordados con
  el dueño del instalador. (Una revisión anterior de esta matriz registró una
  guarda de disco del builder que bloqueaba una recompilación; esa compilación
  ya se completó.)

### Hardware, perfiles, incorporación, dotfiles

- Existen consultas de hardware; existen líneas base medidas de la shell
  (issue 47 de `shell`). Todavía no hay matriz de detección nivel CachyOS.
- Los perfiles (developer/gaming/creator/agentic) deben montarse sobre el
  modelo canónico de ediciones con dependencias exactas, huella,
  comportamiento al desinstalar y aceptación. No son ediciones publicadas.
- Existen el módulo Welcome más `horneroctl welcome status`; la configuración
  de Hermes se suma a la incorporación solo como paso opcional y salteable.
- Dotfiles: la migración a Lua de Hyprland está preparada e inerte (issue 179
  de `dotfiles`, 2 de 9 pasos); los flujos de tmux/yazi están marcados como
  adoptar-copia, todavía sin generalizar. Las preferencias personales quedan
  como personales.

## Copiar, adaptar, evitar

- **Copiar (ideas, no ABI)**: disciplina de manifiesto, semver y lockfile
  para plugins (DMS/Noctalia); cambio atómico de tema con token de generación
  (Omarchy); marcadores de migración y snapshot antes de actualizar (Omarchy);
  conocimiento del sistema generado y acotado para agentes (Rashin), producido
  por consultas de `horneroctl` en lugar de un segundo indexador donde sea
  posible.
- **Adaptar**: la postura apagada por defecto y solo local de Rashin, pero con
  transporte autenticado y una UX nativa de chat en Companion en lugar de un
  dashboard web.
- **Evitar**: QML de terceros en proceso presentado como en sandbox; daemons
  locales sin autenticación; instalaciones de agentes con `curl | bash`; IA
  como dependencia obligatoria; afirmar validación de ISO a partir de una
  compilación sola.

## Orden de prioridad (según dependencias)

1. Desbloquear la aceptación de instalador/primer arranque (issues 11 y 12 de
   `installer`, liderado por su dueño).
2. Ciclo de vida del runtime de plugins sobre el contrato de manifiesto
   existente, con etiquetas honestas de confianza: el QML confiable corre con
   privilegios de usuario; sin afirmaciones falsas de sandbox.
3. Corte vertical del asistente Hermes, según el doc de arquitectura.
4. Brechas de ajustes y lanzador cerradas por panel, paridad GUI/CLI.
5. Diseño de actualización/snapshot/recuperación con gates de rendimiento
   medidos.

## Brechas de evidencia conocidas

- Noctalia v5 (`noctalia-dev/noctalia`) todavía no estudiado.
- Repositorio del registro comunitario de DMS no clonado; las afirmaciones
  sobre el registro se apoyan solo en el árbol de DMS.
- Escenarios gráficos de QA auditados, no ejecutados, en esta pasada.
- Estudio a nivel de código fuente de CachyOS y Garuda todavía pendiente.
