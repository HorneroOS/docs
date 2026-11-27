# Studio: ruteo en vivo para micrófono, guitarra, DAW, Discord y OBS

Una guía práctica y 100% reversible en HorneroOS Studio para mezclar un
micrófono en vivo, una guitarra eléctrica pasando por un DAW (como REAPER
sobre `pipewire-jack`) y audio opcional del navegador hacia Discord y OBS
— sin acoples ni cambios permanentes en el sistema.

Todo lo que configurás acá vive bajo `~/.config/` y usa primitivas
estándar de PipeWire y WirePlumber. Esta guía no asume ningún modelo de
hardware específico ni hace afirmaciones de soporte validado en QA: una
interfaz de audio USB multientrada y un DAW propietario como REAPER
(bajo el EULA de Cockos; mirá la
[matriz de aplicaciones de Studio](studio.md)) son elecciones opt-in
instaladas por vos.

## Panorama general y flujo de señal

La regla central es aislar por bus: tus auriculares, tu envío a Discord y
tu mezcla para OBS salen por pares distintos del DAW, mientras que la
salida de Discord va directo a tus auriculares y nunca vuelve a entrar al
DAW ni al micrófono virtual de Discord.

```text
  [Mic (In 1)] ──────┐
                     ▼
  [Guitarra (In 2)] ─┼─► [REAPER] ─► out1-2 ─► Auriculares
                     ▲            ├─► out3-4 ─► REAPER Lesson Mic ─► Discord
  [Browser Backing] ─┘ (in3-4)    └─► out5-6 ─► REAPER Program ────► OBS

  Discord Out ─► [Discord Call sink] ─► Solo auriculares (sin retorno)
```

Como la salida de Discord (`Discord Call`) solo alimenta tu dispositivo
de salida por defecto (auriculares) y la entrada de `REAPER Lesson Mic`
nunca se autoconecta, la llamada queda estructuralmente libre de acoples.

## Paso 1 — Línea base y requisitos previos

Arrancá siempre en el modo **Balanced** de Hornero Studio antes de tocar
tamaños de buffer, como explican [Audio en Studio](studio-audio.md) y
[Studio: audio de baja latencia](studio-low-latency.md):

```sh
horneroctl studio doctor
horneroctl studio selection show
```

Confirmá que tu host tenga instalados el stack de audio y las
herramientas de usuario:

- Servicios base de sesión: `pipewire`, `pipewire-pulse`,
  `pipewire-jack` y `wireplumber`
  (`systemctl --user status pipewire pipewire-pulse wireplumber`).
- Utilidades de ruteo y mezcla: `qpwgraph` (patchbay) y `pavucontrol`
  (mezclador por flujo de PulseAudio/PipeWire).
- DAW y plugins opcionales: `reaper` (opt-in propietario) y paquetes LV2
  como `lsp-plugins`, `calf` o `gxplugins.lv2`.

Si tu interfaz funciona limpia en Balanced, usalo como base antes de
sumar la regla de latencia por aplicación de más abajo.

## Paso 2 — Endpoints virtuales reversibles en PipeWire

Creá los directorios drop-in de usuario si todavía no existen:

```sh
mkdir -p ~/.config/pipewire/pipewire.conf.d ~/.config/pipewire/jack.conf.d
```

### 1. Buses de estudio (`60-reaper-music-studio.conf`)

Escribí `~/.config/pipewire/pipewire.conf.d/60-reaper-music-studio.conf`
para crear tres endpoints virtuales permanentes:

- `REAPER Lesson Mic` (fuente `reaper_lesson_mic`) para la entrada de
  Discord.
- `REAPER Program` (fuente `reaper_program`) para capturar en OBS Studio.
- `Discord Call` (sink `discord_call`) para mandar la salida de Discord
  solo a tus auriculares.

Con `priority.session = 0` evitás que estos nodos pasen a ser tu
micrófono o salida por defecto; `node.autoconnect = false` en las
entradas de bus asegura que solo `qpwgraph` los cablee; y poner
`audio.position = [ FL FR ]` de ambos lados garantiza que cada fuente
virtual exponga puertos estéreo.

```conf
# ~/.config/pipewire/pipewire.conf.d/60-reaper-music-studio.conf
context.modules = [
  { name = libpipewire-module-loopback
    args = {
      node.description = "REAPER Lesson Mic"
      capture.props = {
        node.name           = "reaper_lesson.input"
        node.description    = "REAPER Lesson Bus input"
        node.autoconnect    = false
        node.dont-reconnect = true
        stream.dont-remix   = true
        audio.position      = [ FL FR ]
      }
      playback.props = {
        node.name        = "reaper_lesson_mic"
        node.description = "REAPER Lesson Mic"
        media.class      = "Audio/Source"
        audio.position   = [ FL FR ]
        priority.session = 0
        priority.driver  = 0
      }
    }
  }
  { name = libpipewire-module-loopback
    args = {
      node.description = "REAPER Program"
      capture.props = {
        node.name           = "reaper_program.input"
        node.description    = "REAPER Program input"
        node.autoconnect    = false
        node.dont-reconnect = true
        stream.dont-remix   = true
        audio.position      = [ FL FR ]
      }
      playback.props = {
        node.name        = "reaper_program"
        node.description = "REAPER Program"
        media.class      = "Audio/Source"
        audio.position   = [ FL FR ]
        priority.session = 0
        priority.driver  = 0
      }
    }
  }
  { name = libpipewire-module-loopback
    args = {
      node.description = "Discord Call"
      capture.props = {
        node.name        = "discord_call"
        node.description = "Discord Call"
        media.class      = "Audio/Sink"
        audio.position   = [ FL FR ]
        priority.session = 0
        priority.driver  = 0
      }
      playback.props = {
        node.name        = "discord_call.output"
        node.description = "Discord Call to headphones"
        audio.position   = [ FL FR ]
      }
    }
  }
]
```

### 2. Sink opcional para pista del navegador (`65-browser-backing.conf`)

Escribí `~/.config/pipewire/pipewire.conf.d/65-browser-backing.conf`
para que el audio del navegador solo entre al DAW cuando movés un flujo
hacia `Browser Backing`, sin duplicarse hacia tus parlantes:

```conf
# ~/.config/pipewire/pipewire.conf.d/65-browser-backing.conf
context.modules = [
  { name = libpipewire-module-loopback
    args = {
      node.description = "Browser Backing"
      capture.props = {
        node.name        = "browser_backing"
        node.description = "Browser Backing"
        media.class      = "Audio/Sink"
        audio.position   = [ FL FR ]
        priority.session = 0
        priority.driver  = 0
      }
      playback.props = {
        node.name           = "browser_backing.output"
        node.description    = "Browser Backing output"
        node.autoconnect    = false
        node.dont-reconnect = true
        stream.dont-remix   = true
        audio.position      = [ FL FR ]
      }
    }
  }
]
```

### 3. Período de scheduling acotado al DAW (`60-reaper-low-latency.conf`)

En lugar de pisar el reloj global de PipeWire, acotá un período de 256
cuadros únicamente para REAPER en
`~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf`:

```conf
# ~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf
jack.rules = [
  { matches = [ { application.process.binary = "reaper" } ]
    actions = { update-props = { node.latency = 256/48000 } }
  }
]
```

Acordate: el quantum (`256/48000`) es un período de planificación, **no**
latencia física medida de ida y vuelta. Mientras REAPER corre, PipeWire
planifica el grafo activo a 256 cuadros; cuando cerrás REAPER, el grafo
vuelve solo a tu línea base Balanced.

Aplicá los tres drop-ins sin reiniciar la máquina:

```sh
systemctl --user restart pipewire pipewire-pulse wireplumber
```

## Paso 3 — Interfaz y configuración del DAW (REAPER 4-in / 6-out)

### Reglas de la interfaz de audio

- **Entrada 1 (Micrófono):** activá `48V` (phantom power) **solo** si
  usás un micrófono condenser; dejalo apagado para micrófonos dinámicos.
- **Entrada 2 (Guitarra DI):** activá el selector `INST` (Hi-Z) para no
  atenuar la señal directa del instrumento.
- **Direct Monitor OFF:** apagá el monitoreo directo por hardware para
  escuchar tu tono procesado desde el DAW sin duplicar la señal seca.
- **No conectes puertos loopback del hardware:** si tu interfaz expone
  canales virtuales de loopback (como `AUX2` o `AUX3`), dejalos sin
  conectar.

### REAPER vía `pipewire-jack`

Antes de tocar `~/.config/REAPER/reaper.ini`, guardate un respaldo para
que volver atrás sea trivial:

```sh
cp ~/.config/REAPER/reaper.ini ~/.config/REAPER/reaper.ini.bak
```

Configurá REAPER en modo **JACK** (`pipewire-jack`) con **4 entradas** y
**6 salidas**, y desactivá la autoconexión de JACK (`jack_options |= 2`
en `reaper.ini`, o desde las preferencias de Audio Device de REAPER)
para que `qpwgraph` sea dueño de todos los enlaces:

| Puerto de REAPER | Señal |
| --- | --- |
| `in1` | Entrada 1 de la interfaz (micrófono) |
| `in2` | Entrada 2 de la interfaz (guitarra DI) |
| `in3` / `in4` | Browser Backing estéreo (`FL` / `FR`) |
| `out1` / `out2` | Auriculares / monitores de estudio |
| `out3` / `out4` | `REAPER Lesson Bus input` (`REAPER Lesson Mic` → Discord) |
| `out5` / `out6` | `REAPER Program input` (`REAPER Program` → OBS) |

Chequeos prácticos de pistas y efectos dentro de REAPER:

- **Separar el DI de guitarra:** sacale el envío a Master a la pista DI
  cruda y ruteala únicamente hacia tu pista de ampli/tono, así la señal
  seca no se cuela junto al simulador.
- **Estado de FX en la pista de tono:** verificá que la pista activa de
  guitarra tenga los **FX encendidos** (online y sin bypass global).
- **Polaridad `BYPASS` en LV2:** algunos pedales LV2 (por ejemplo
  Guitarix `GxSD1`) exponen su parámetro `BYPASS` como `lv2:enabled`,
  donde `1` significa pedal **encendido** y `0` apagado. Confirmalo de
  oído si un efecto parece no actuar.
- **Pista de respaldo del navegador:** asignale la entrada estéreo
  `Input 3–4`, activá el monitoreo de entrada y elegí **Record: disable
  (input monitoring only)** para escucharla y enviarla a tus buses sin
  grabar clips por accidente.

## Paso 4 — Cableado persistente con `qpwgraph`

Abrí REAPER (para que aparezcan sus 4 entradas y 6 salidas JACK) y abrí
`qpwgraph`. Hacé estos **10 enlaces** una sola vez:

| Puerto origen | Puerto destino | Función |
| --- | --- | --- |
| Interfaz `capture_FL` (ch 1) | `REAPER:in1` | Micrófono en vivo |
| Interfaz `capture_FR` (ch 2) | `REAPER:in2` | Guitarra DI |
| `browser_backing.output:output_FL` | `REAPER:in3` | Pista navegador L |
| `browser_backing.output:output_FR` | `REAPER:in4` | Pista navegador R |
| `REAPER:out1` | Interfaz `playback_FL` | Auriculares L |
| `REAPER:out2` | Interfaz `playback_FR` | Auriculares R |
| `REAPER:out3` | `reaper_lesson.input:input_FL` | Bus Discord L |
| `REAPER:out4` | `reaper_lesson.input:input_FR` | Bus Discord R |
| `REAPER:out5` | `reaper_program.input:input_FL` | Bus OBS L |
| `REAPER:out6` | `reaper_program.input:input_FR` | Bus OBS R |

Guardá el patchbay en `~/.config/qpwgraph/music-studio.qpwgraph` y
dejá marcado **Activated** en `qpwgraph` para que restaure esos 10
enlaces automáticamente cada vez que REAPER y los endpoints estén
activos.

Verificá los enlaces activos y la salud de la sesión:

```sh
pw-link -l
horneroctl studio doctor
```

## Paso 5 — Discord, OBS y ruteo de pista del navegador

### Ajustes de Voz y Video en Discord

- **Dispositivo de entrada:** `REAPER Lesson Mic`
- **Dispositivo de salida:** `Discord Call`
- **Sensibilidad de entrada:** desactivá la detección automática y
  bajá el umbral manual al mínimo (`-100 dB`) para que la cola de las
  notas de guitarra no se corte.
- **Procesamiento de audio:** desactivá **Supresión de ruido** (Krisp),
  **Cancelación de eco** y **Control automático de ganancia**, porque
  tratan el sustain de la guitarra y las pistas de acompañamiento como
  ruido.

### Captura en OBS Studio

Agregá una fuente **Captura de entrada de audio** apuntando a
`REAPER Program` para grabar o transmitir tu mezcla completa. Si también
querés capturar la voz remota de Discord, sumá una captura de salida (o
monitor) sobre `Discord Call`.

### Mandar audio del navegador a `Browser Backing`

Iniciá la reproducción en tu navegador (Zen Browser, Firefox o
Chromium) y elegí una de estas dos formas:

- Abrí `pavucontrol`, entrá a la pestaña **Reproducción** y cambiá la
  salida del navegador a **Browser Backing**; o
- Movelo desde la terminal con `pactl`:

```sh
pactl list short sink-inputs
pactl move-sink-input <ID> browser_backing
```

Cuando termines, devolvé el flujo a tus auriculares normales desde
`pavucontrol` o con `pactl move-sink-input <ID> <DEFAULT_SINK>`.

### Solución rápida de problemas frecuentes

- **Discord se queda mudo después de abrir `pavucontrol`:** fijate en la
  pestaña Reproducción que `WEBRTC VoiceEngine` no haya quedado en `0%`
  o silenciado por error. Restablecelo desde la terminal si hace falta:

  ```sh
  pactl list sink-inputs
  pactl set-sink-input-volume <ID> 100%
  ```

- **Clics, cortes o xruns a 256 cuadros:** editá
  `~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf` y subí
  `256/48000` a `512/48000`, o borrá ese archivo para quedarte en
  Balanced. Volvé a correr `horneroctl studio doctor` para confirmar que
  los xruns dejen de subir.

## Paso 6 — Rollback completo (100% reversible)

Podés desactivar cada capa por separado, sin permisos de root y sin
reiniciar.

### 1. Apagar solo la pista del navegador

- En `pavucontrol` (pestaña **Reproducción**), devolvé el flujo del
  navegador a tu salida de auriculares normal, o muteá la pista en
  REAPER.

### 2. Desactivar el ruteo de estudio temporalmente

- Cerrá REAPER y `qpwgraph`.
- En **Voz y Video** de Discord, volvé a elegir tu micrófono y tus
  auriculares habituales.
- Como los tres endpoints virtuales tienen `priority.session = 0`,
  quedan inactivos y no interfieren con el audio normal del escritorio.

### 3. Limpieza total

Borrá los tres drop-ins de PipeWire y el patchbay de `qpwgraph`,
restaurá el respaldo de `reaper.ini` si lo modificaste y reiniciá los
servicios de audio del usuario:

```sh
rm -f ~/.config/pipewire/pipewire.conf.d/60-reaper-music-studio.conf \
  ~/.config/pipewire/pipewire.conf.d/65-browser-backing.conf \
  ~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf \
  ~/.config/qpwgraph/music-studio.qpwgraph
mv -f ~/.config/REAPER/reaper.ini.bak ~/.config/REAPER/reaper.ini
systemctl --user restart pipewire pipewire-pulse wireplumber
horneroctl studio doctor
```

(Si no creaste `~/.config/REAPER/reaper.ini.bak`, salteá la línea de
`mv`.) Al reiniciar los servicios de usuario, el grafo vuelve al estado
previo exacto de Hornero Studio.
