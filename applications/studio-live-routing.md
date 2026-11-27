# Studio: live routing for mic, guitar, DAW, Discord, and OBS

> [!TIP]
> **Fast-track:** You can also enable these virtual routing kits in 1 click
> via `Control Center → Studio` or `horneroctl studio routing enable` (e.g.
> `live-call`, `browser-backing`, `reaper-low-latency`), route streams
> directly from `Control Center → Audio`, and save the entire setup as a
> switchable workspace profile via `Control Center → Profiles` or `horneroctl
> profile capture`! See [Profiles and
> snapshots](../desktop/profiles-snapshots.md).

A practical, 100%-reversible setup on HorneroOS Studio to mix a live
microphone, an electric guitar through a DAW (such as REAPER over
`pipewire-jack`), and optional browser backing audio into Discord and
OBS — without echo loops or permanent system edits.

Everything in this guide lives under `~/.config/` and uses standard
PipeWire and WirePlumber primitives. It assumes no specific hardware
model and makes no QA support claims: a multi-input USB audio interface
and a proprietary DAW such as REAPER (under Cockos's EULA; see the
[Studio application matrix](studio.md)) are user-installed opt-ins.

## Overview and signal flow

The core rule is isolation by bus: your headphones, your Discord feed,
and your OBS program feed each get their own DAW output pair, while
Discord's playback goes straight to your headphones and never re-enters
the DAW or your outbound Discord mic bus.

```text
  [Mic (In 1)] ──────┐
                     ▼
  [Guitar DI (In 2)] ┼─► [REAPER] ─► out1-2 ─► Headphones
                     ▲            ├─► out3-4 ─► REAPER Lesson Mic ─► Discord
  [Browser Backing] ─┘ (in3-4)    └─► out5-6 ─► REAPER Program ────► OBS

  Discord Out ─► [Discord Call sink] ─► Headphones only (no loopback)
```

Because Discord's output (`Discord Call`) only feeds your default
output device (headphones) and the `REAPER Lesson Mic` input never
auto-connects, the call is structurally feedback-free.

## Step 1 — Baseline and prerequisites

Start on Hornero Studio's **Balanced** mode before tuning any buffer
size, as described in [Studio audio](studio-audio.md) and
[Studio: low-latency audio](studio-low-latency.md):

```sh
horneroctl studio doctor
horneroctl studio selection show
```

Confirm that your host has the audio stack and user tools installed:

- Core session services: `pipewire`, `pipewire-pulse`, `pipewire-jack`,
  and `wireplumber` (`systemctl --user status pipewire pipewire-pulse
wireplumber`).
- Routing and mixer utilities: `qpwgraph` (patchbay) and `pavucontrol`
  (per-stream PulseAudio/PipeWire mixer).
- Optional DAW and plugins: `reaper` (proprietary opt-in) and LV2
  plugin packs such as `lsp-plugins`, `calf`, or `gxplugins.lv2`.

If your interface works cleanly on Balanced, keep that as your baseline
before adding the per-app JACK latency rule below.

## Step 2 — Reversible PipeWire virtual endpoints

Create the user drop-in directories if they do not exist yet:

```sh
mkdir -p ~/.config/pipewire/pipewire.conf.d ~/.config/pipewire/jack.conf.d
```

### 1. Studio buses (`60-reaper-music-studio.conf`)

Write `~/.config/pipewire/pipewire.conf.d/60-reaper-music-studio.conf`
to create three permanent virtual endpoints:

- `REAPER Lesson Mic` (`reaper_lesson_mic` source) for Discord input.
- `REAPER Program` (`reaper_program` source) for OBS Studio.
- `Discord Call` (`discord_call` sink) for Discord output to headphones.

Setting `priority.session = 0` prevents these endpoints from ever
becoming your default mic or speakers, `node.autoconnect = false` on
the bus inputs ensures only `qpwgraph` wires them, and placing
`audio.position = [ FL FR ]` on both sides ensures each virtual source
exposes stereo ports.

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

### 2. Optional browser backing sink (`65-browser-backing.conf`)

Write `~/.config/pipewire/pipewire.conf.d/65-browser-backing.conf` so
browser audio only enters your DAW when you move a browser stream into
`Browser Backing`, and never doubles straight into your speakers:

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

### 3. Scoped DAW scheduling period (`60-reaper-low-latency.conf`)

Instead of overriding PipeWire's global clock, scope a 256-frame
scheduling period exclusively to REAPER via
`~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf`:

```conf
# ~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf
jack.rules = [
  { matches = [ { application.process.binary = "reaper" } ]
    actions = { update-props = { node.latency = 256/48000 } }
  }
]
```

Remember: quantum (`256/48000`) is a scheduling period, **not** measured
round-trip latency. While REAPER is running, PipeWire schedules the
active graph at 256 frames; when REAPER closes, the graph returns to
your Balanced baseline automatically.

Apply the three drop-ins without rebooting:

```sh
systemctl --user restart pipewire pipewire-pulse wireplumber
```

## Step 3 — Interface and DAW setup (REAPER 4-in / 6-out)

### Audio interface rules

- **Input 1 (Mic):** keep `48V` phantom power enabled **only** for a
  condenser microphone; leave it off for dynamic microphones.
- **Input 2 (Guitar DI):** engage the `INST` (Hi-Z) switch so the
  instrument signal is not loaded down.
- **Direct Monitor OFF:** turn hardware direct monitoring off so you
  monitor your processed tone through the DAW rather than hearing a
  doubled dry signal.
- **Ignore hardware loopback ports:** if your interface exposes virtual
  loopback channels (such as `AUX2` or `AUX3`), leave them disconnected.

### REAPER via `pipewire-jack`

Before editing `~/.config/REAPER/reaper.ini`, save a backup so full
rollback stays effortless:

```sh
cp ~/.config/REAPER/reaper.ini ~/.config/REAPER/reaper.ini.bak
```

Configure REAPER for **JACK** (`pipewire-jack`) with **4 inputs** and
**6 outputs**, and disable JACK auto-connect (`jack_options |= 2` in
`reaper.ini`, or uncheck auto-connect in REAPER's Audio Device settings)
so `qpwgraph` owns every link:

| REAPER port | Signal |
| --- | --- |
| `in1` | Interface Input 1 (mic) |
| `in2` | Interface Input 2 (guitar DI) |
| `in3` / `in4` | Browser Backing stereo (`FL` / `FR`) |
| `out1` / `out2` | Headphones / studio monitors |
| `out3` / `out4` | `REAPER Lesson Bus input` (`REAPER Lesson Mic` → Discord) |
| `out5` / `out6` | `REAPER Program input` (`REAPER Program` → OBS) |

Practical track and FX checks inside REAPER:

- **Guitar DI separation:** keep the raw DI track unrouted from Master
  (turn off its Master send) and route it only to your amp-sim/tone
  track, so dry DI never bleeds alongside the processed guitar.
- **Tone track FX state:** confirm the active guitar tone track has
  **FX enabled** (online and not globally bypassed).
- **LV2 `BYPASS` polarity:** some LV2 plugins (for example Guitarix
  `GxSD1`) map their `BYPASS` parameter to `lv2:enabled`, where `1`
  means the pedal is **active** and `0` means bypassed. Verify with your
  ears if an effect sounds off.
- **Browser backing track mode:** assign stereo `Input 3–4`, enable
  input monitoring, and set **Record: disable (input monitoring only)**
  so backing audio passes to your headphones and buses without recording
  clips by mistake.

## Step 4 — Persistent wiring with `qpwgraph`

Launch REAPER (so its 4 input and 6 output JACK ports exist) and open
`qpwgraph`. Make these **10 links** once:

| Source port | Destination port | Purpose |
| --- | --- | --- |
| Interface `capture_FL` (ch 1) | `REAPER:in1` | Live mic |
| Interface `capture_FR` (ch 2) | `REAPER:in2` | Guitar DI |
| `browser_backing.output:output_FL` | `REAPER:in3` | Backing left |
| `browser_backing.output:output_FR` | `REAPER:in4` | Backing right |
| `REAPER:out1` | Interface `playback_FL` | Headphones left |
| `REAPER:out2` | Interface `playback_FR` | Headphones right |
| `REAPER:out3` | `reaper_lesson.input:input_FL` | Discord bus left |
| `REAPER:out4` | `reaper_lesson.input:input_FR` | Discord bus right |
| `REAPER:out5` | `reaper_program.input:input_FL` | OBS bus left |
| `REAPER:out6` | `reaper_program.input:input_FR` | OBS bus right |

Save the patchbay to `~/.config/qpwgraph/music-studio.qpwgraph` and click
**Activated** in `qpwgraph` so it restores these 10 links automatically
whenever REAPER and the virtual endpoints are running.

Verify the active links and session health:

```sh
pw-link -l
horneroctl studio doctor
```

## Step 5 — Discord, OBS, and browser backing routing

### Discord Voice & Video settings

- **Input Device:** `REAPER Lesson Mic`
- **Output Device:** `Discord Call`
- **Input Sensitivity:** disable automatic sensitivity and drag the
  manual threshold to the minimum (`-100 dB`) so quiet guitar decay is
  never chopped off.
- **Audio processing:** disable **Noise Suppression** (Krisp), **Echo
  Cancellation**, and **Automatic Gain Control**, which treat electric
  guitar sustain and backing music as noise.

### OBS Studio capture

Add an **Audio Input Capture** source pointing to `REAPER Program` to
record or stream your full mixed lesson/performance. If you also want to
capture the remote voice from Discord, add an **Audio Output Capture**
(or monitor capture) for `Discord Call`.

### Routing browser audio into `Browser Backing`

Start playback in your browser (Zen Browser, Firefox, or Chromium), then
either:

- Open `pavucontrol`, go to the **Playback** tab, and switch the
  browser stream's output device to **Browser Backing**; or
- Move it from a terminal with `pactl`:

```sh
pactl list short sink-inputs
pactl move-sink-input <ID> browser_backing
```

When you finish, move the stream back to your normal headphones sink in
`pavucontrol` or with `pactl move-sink-input <ID> <DEFAULT_SINK>`.

### Troubleshooting quick-wins

- **Discord goes silent after opening `pavucontrol`:** check that
  `WEBRTC VoiceEngine` was not muted or dragged to `0%` in the Playback
  tab. Restore it from the terminal if needed:

  ```sh
  pactl list sink-inputs
  pactl set-sink-input-volume <ID> 100%
  ```

- **Clicks, dropouts, or xruns at 256 frames:** edit
  `~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf` and change
  `256/48000` to `512/48000`, or delete that file to stay on Balanced.
  Check `horneroctl studio doctor` again to confirm xruns stop climbing.

## Step 6 — Complete rollback (100% reversible)

You can back out any layer independently, with zero root privileges and
no reboot.

### 1. Disable browser backing only

- In `pavucontrol` (**Playback** tab), move the browser stream back to
  your normal headphones output, or mute the backing track in REAPER.

### 2. Disable studio routing temporarily

- Close REAPER and `qpwgraph`.
- In Discord **Voice & Video**, switch Input and Output back to your
  regular microphone and headphones.
- Because `priority.session = 0` on all three virtual endpoints, they sit
  idle and do not affect normal desktop audio.

### 3. Full clean removal

Remove the three PipeWire drop-ins and the `qpwgraph` patchbay, restore
your `reaper.ini` backup if you edited it, and restart the user audio
services:

```sh
rm -f ~/.config/pipewire/pipewire.conf.d/60-reaper-music-studio.conf \
  ~/.config/pipewire/pipewire.conf.d/65-browser-backing.conf \
  ~/.config/pipewire/jack.conf.d/60-reaper-low-latency.conf \
  ~/.config/qpwgraph/music-studio.qpwgraph
mv -f ~/.config/REAPER/reaper.ini.bak ~/.config/REAPER/reaper.ini
systemctl --user restart pipewire pipewire-pulse wireplumber
horneroctl studio doctor
```

(If you did not create `~/.config/REAPER/reaper.ini.bak`, skip the `mv`
line.) After restarting the user services, your audio graph returns
exactly to its prior Hornero Studio state.
