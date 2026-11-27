# Studio: producción creativa asistida por IA (opcional)

HorneroOS Studio incluye las aplicaciones creativas (Kdenlive, Blender, GIMP,
Krita, Inkscape, OBS Studio, REAPER, FFmpeg/MLT). Manejarlas con un agente de
IA es **opcional** y lo provee
[Agent Toolkit Creative Studio](https://github.com/ulises-jeremias/agent-toolkit/blob/main/docs/creative-studio/README.md)
(skills portables + integraciones MCP revisadas, ADR-046 allá). HorneroOS no
empaqueta un runtime de agentes, no instala servidores MCP ni modelos de IA por
defecto y nunca los requiere para una instalación exitosa de Studio.

## Qué provee HorneroOS de forma nativa

- El catálogo de aplicaciones y especializaciones de Studio (mirá
  [Aplicaciones de Studio](studio.md)); REAPER y otras apps propietarias
  quedan en opt-in explícito.
- Trabajos de render tipados: `horneroctl studio jobs` con adaptadores en
  lista blanca (`blender-render`, `ffmpeg-export`, `kdenlive-render`,
  `melt-render`). Los trabajos corren de forma síncrona tras el envío
  explícito; nunca se sobrescribe una salida existente ni se modifican los
  archivos fuente. La cancelación es una transición de estado registrada, no
  un kill de proceso.
- Diagnósticos de solo lectura: `horneroctl studio doctor` informa las
  herramientas creativas opcionales (`ffmpeg`, `ffprobe`, `melt`, `kdenlive`,
  `blender`) como `warn` cuando faltan — nunca como falla.

## Activar edición asistida por IA (ejemplo con Kdenlive)

```bash
pipx install mcp-kdenlive        # El nombre en PyPI es mcp-kdenlive
kdenlive-mcp diagnose            # debe imprimir "ready"
```

Después apuntá tu cliente de agente compatible con MCP al servidor `kdenlive`
con `KDENLIVE_MCP_ALLOWED_ROOTS` limitado únicamente al directorio de tu
proyecto (mirá `mcp/templates/kdenlive/` en Agent Toolkit). El agente edita un
proyecto `.kdenlive` real que podés seguir editando en Kdenlive; antes de cada
edición se guarda un backup con marca de tiempo.

## Seguridad y privacidad

- Los servidores MCP creativos corren de forma local sobre stdio/loopback;
  HorneroOS no sube nada para este flujo.
- Las integraciones MCP de Blender pueden ejecutar Python dentro de Blender.
  Tratalas como ejecución arbitraria de código: activalas solo de forma
  explícita, trabajá sobre copias y mantené las escrituras dentro del
  directorio de tu proyecto.
- La grabación, el streaming y el acceso al micrófono nunca se habilitan de
  forma automática. Las integraciones con OBS las tenés que iniciar vos, por
  sesión.
- Los modelos de transcripción/IA (por ejemplo Whisper) son descargas grandes
  y nunca se bajan en silencio; instalalos solo cuando lo elijas.

## Recursos

Los renders son pesados. Revisá primero `horneroctl studio doctor` y el margen
libre de disco/GPU, y acotá trabajos largos, por ejemplo con
`systemd-run --user --scope -p MemoryMax=6G -p MemorySwapMax=0 …`. La
codificación por hardware (NVENC/VAAPI) depende de tu GPU y tus drivers;
HorneroOS no la promete.

## Solución de problemas

- `kdenlive-mcp diagnose` no queda en `ready` → instalá `kdenlive mlt ffmpeg`
  desde los repositorios y volvé a correrlo.
- Trabajo en estado `failed` con salida parcial → el archivo parcial queda
  identificado como parcial, nunca como un render terminado; leé
  `horneroctl studio jobs log <id>` (se redacta al leer), corregí la causa y
  volvé a enviarlo con una ruta de salida nueva.
- Trabajo en estado `interrupted` → una corrida anterior terminó a mitad del
  render; volvé a enviarlo con tranquilidad (las salidas nunca se
  sobrescriben).

## Desactivar / desinstalar

Quitá la entrada MCP de tu cliente de agente y corré
`pipx uninstall mcp-kdenlive`. Quitá el producto
`agent-toolkit-creative-studio` de Agent Toolkit con su flujo habitual. Tus
proyectos, archivos nativos de edición y backups son datos de usuario y nunca
se borran al desinstalar.
