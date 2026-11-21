# Studio: hacé algo real

Studio extiende Desktop con especializaciones de producción creativa (audio
y música, video, streaming, gráficos, fotografía, 3D, desarrollo de juegos,
CAD), un modo de experiencia Studio, diagnósticos y un perfil PipeWire de
baja latencia reversible.

**Madurez: Supported.** Existen la selección de paquetes y los diagnósticos;
ningún flujo de aplicación está certificado en hardware físico y el QA de
hardware está bloqueado por falta de fixtures de audio aprobados.

## Qué es real hoy

- **Selección**: Qué hace: Registra especializaciones y aplicaciones; no
  instala nada; Comando: `horneroctl studio selection set --specialization
  audio-music-production --application ardour`
- **Doctor**: Qué hace: Selección, PipeWire/WirePlumber, runtime de PipeWire,
  xruns, puente JACK, RealtimeKit, estado del perfil; Comando: `horneroctl
  studio doctor`
- **Perfil Low Latency**: Qué hace: Un drop-in de usuario más valores de reloj
  en vivo (quantum 128, mín 64, máx 256 a 48 kHz); reversión exacta; Comando:
  `horneroctl studio audio apply --yes` / `revert`
- **Instrumentación**: Qué hace: Quantum/tasa, xruns y carga DSP según
  `pw-top`; Comando: `horneroctl studio audio status`
- **Rendimiento temporal**: Qué hace: Cambio vía power-profiles-daemon con
  restauración exacta; Comando: `horneroctl studio mode performance --yes`
- **Trabajos de render**: Qué hace: Trabajos ffmpeg y Blender en lista
  permitida, sin sobrescribir; Comando: `horneroctl studio jobs submit ...`
- **Modo de experiencia**: Qué hace: Lienzo estable, sin brillo, avisos
  retenidos en pantalla completa; Comando: `horneroctl mode set studio`

Los valores de Low Latency son una **propuesta**, no soporte medido para tu
interfaz. El quantum es un período de planificación, no latencia de ida y
vuelta. Si oís chasquidos o `studio audio status` cuenta xruns, ejecutá
`horneroctl studio audio revert`. Aplicar y revertir no reinician servicios,
no piden root, no tocan privilegios de tiempo real, kernel, IRQ ni
governors, y se niegan a pisar un archivo personal con el mismo nombre.

![Krita y Kdenlive abiertos uno al lado del otro. Krita muestra un
lienzo en blanco sin guardar, con sus presets de pinceles; Kdenlive
muestra un proyecto vacío, sin medios importados y con la línea de
tiempo vacía.](https://www.horneroos.com/captures/cap-studio-03.png)

*Aplicaciones creativas instaladas y abiertas, con proyectos en blanco
y sin guardar. Estar presentes no certifica ningún flujo; mirá "No
validado" más abajo. Captura real del escritorio en el equipo del
maintainer, 19 de noviembre de 2026.*

### Flujo: monitoreo de baja latencia con una interfaz USB

1. `horneroctl studio doctor` (las advertencias son honestas: lo no
   disponible se informa como no disponible).
2. `horneroctl studio audio apply --dry-run` y luego `--yes`.
3. Abrí tu DAW (Ardour, REAPER, Guitarix vía `pipewire-jack`/`pw-jack`) y
   tocá.
4. `horneroctl studio audio status`: mirá xruns y carga DSP.
5. `horneroctl studio audio revert` al terminar o ante cualquier corte.

## Verificado

- **apply / dry-run / revert / rechazo de archivo ajeno / estados sin
  PipeWire, parseo de pw-top**: Dónde: pruebas unitarias con
  `pw-metadata`/`pw-top` falsos (CI)
- **`studio doctor` y formato de salida de `pw-metadata`/`pw-top` en un equipo
  real con PipeWire 1.6 (solo lectura)**: Dónde: equipo real, solo lectura; no
  se aplicó nada
- **El modo es Balanced por defecto y Low Latency se rechaza sin `--yes`**:
  Dónde: escenario de VM `studio/audio-mode-opt-in`
- **apply, revert y rechazo de tocar un archivo personal contra un PipeWire
  vivo (quantum 1024/1024/2048 a 128/64/256 y de vuelta exacto)**: Dónde:
  escenarios de VM `studio/audio-apply-live`, `studio/audio-revert-live`,
  `studio/audio-foreign-file-live` (sin hardware de audio en la VM)
- **Tabla de decisión del hook (aplica solo con un cambio deliberado)**:
  Dónde: pruebas node offscreen, CI
- **Preset Studio y perfil de experiencia**: Dónde: CI + offscreen

## No validado

- `studio audio apply` en un equipo real con una interfaz real: solo se
  ejecutó contra el PipeWire de una VM descartable sin hardware de audio
  (driver Dummy).
- Ninguna interfaz real (en el equipo inspeccionado se vio una Focusrite
  Scarlett 2i2 en ALSA; no se midió latencia, operación sin xruns ni
  loopback).
- REAPER, Ardour, Guitarix, OBS, Blender, Kdenlive, Carla y qpwgraph
  estaban instalados en el equipo inspeccionado pero Hornero **no los
  lanzó ni validó**; ningún flujo en ellos está certificado.
- Puente de VST de Windows (yabridge), licencias de plugins, hardware MIDI.
- Aceleración de captura/codificación, escenas de OBS y cámara virtual.
- Planificación en tiempo real: se informa la presencia de RealtimeKit; no
  se comprueba si un stream obtuvo prioridad RT.
