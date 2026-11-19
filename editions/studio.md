# Studio: make something real

Studio extends Desktop with creative-production specializations (audio and
music, video, streaming, graphics, photography, 3D, game development, maker
CAD), a Studio experience mode, Studio diagnostics and a reversible
PipeWire Low Latency profile.

**Maturity: Preview.** Package selection and diagnostics exist; no
application workflow is certified on physical hardware, and hardware QA is
blocked on approved audio fixtures.

## What is real today

- **Selection**: What it does: Records specializations and applications;
  installs nothing; Command: `horneroctl studio selection set --specialization
  audio-music-production --application ardour`
- **Doctor**: What it does: Selection validity, PipeWire/WirePlumber, PipeWire
  runtime, xruns, JACK bridge, RealtimeKit, profile state; Command:
  `horneroctl studio doctor`
- **Low Latency profile**: What it does: One user drop-in plus live PipeWire
  clock values (quantum 128, min 64, max 256 at 48 kHz); exact revert;
  Command: `horneroctl studio audio apply --yes` / `revert`
- **Instrumentation**: What it does: Live quantum/rate, xruns and DSP load as
  `pw-top` reports them; Command: `horneroctl studio audio status`
- **Temporary Performance**: What it does: power-profiles-daemon switch with
  exact restore; Command: `horneroctl studio mode performance --yes`
- **Render jobs**: What it does: Allow-listed ffmpeg and Blender jobs, never
  overwriting output; Command: `horneroctl studio jobs submit ...`
- **Experience mode**: What it does: Stable canvas, no glow, popups held under
  fullscreen; a deliberate switch into Studio (you, or `horneroctl mode set
  studio`) applies the Low Latency profile and leaving Studio reverts it;
  automatic switches, reset and shell start never apply it. The Experience
  pane shows the real status (quantum, xruns, DSP load) or "unavailable";
  Command: `horneroctl mode set studio`

Low Latency values are a **proposal**, not measured support for your
interface. A quantum is a scheduling period, not round-trip latency. If you
hear crackles or `studio audio status` counts xruns, run
`horneroctl studio audio revert`. Apply and revert never restart services,
need no root, never change realtime privileges, kernel, IRQ or governors,
and refuse to overwrite a personal file of the same name.
See [Studio audio](../applications/studio-audio.md).

![Krita and Kdenlive open side by side. Krita shows a blank unsaved
canvas with its brush presets; Kdenlive shows an empty project with no
media imported and an empty timeline.](https://www.horneroos.com/captures/cap-studio-03.png)

*Creative applications installed and open — with blank, unsaved
projects. Presence is not a certified workflow; see "Not validated"
below. Running-desktop capture from the maintainer's machine,
19 November 2026.*

### Workflow: low-latency monitoring on a USB interface

1. `horneroctl studio doctor` (warnings are honest: unavailable stays
   unavailable).
2. `horneroctl studio audio apply --dry-run`, then `--yes`.
3. Start your DAW (Ardour, REAPER, Guitarix through `pipewire-jack`/`pw-jack`)
   and play.
4. `horneroctl studio audio status`: look at xruns and DSP load.
5. `horneroctl studio audio revert` when done or on any dropout.

## Verified

- **apply / dry-run / revert / foreign-file refusal / no-PipeWire states,
  pw-top parsing**: Where: unit tests with fake `pw-metadata`/`pw-top` (CI)
- **`studio doctor` and `pw-metadata`/`pw-top` output format on a real
  PipeWire 1.6 host (read-only)**: Where: host, read-only; nothing applied
- **Mode intent is Balanced by default and Low Latency refuses without
  `--yes`**: Where: QA VM scenario `studio/audio-mode-opt-in`
- **apply, revert and refusal to touch a personal file against a live
  PipeWire (quantum 1024/1024/2048 to 128/64/256 and back exactly)**: Where:
  QA VM scenarios `studio/audio-apply-live`, `studio/audio-revert-live`,
  `studio/audio-foreign-file-live` (no audio hardware in the guest)
- **Mode hook decision table (apply only on deliberate switch)**: Where:
  offscreen node tests, CI
- **Studio preset and experience profile**: Where: CI + offscreen

## Not validated

- `studio audio apply` on a real host with a real interface: only run on a
  disposable VM PipeWire with no audio hardware (Dummy driver).
- Any real interface (a Focusrite Scarlett 2i2 was visible in ALSA on the
  inspected host; no latency, xrun-free operation or loopback measurement
  was done).
- REAPER, Ardour, Guitarix, OBS, Blender, Kdenlive, Carla and qpwgraph
  were found installed on the inspected host but **not launched or
  validated** by Hornero; no workflow in them is certified.
- Windows VST bridging (yabridge), plugin licensing, MIDI hardware.
- Capture/encode acceleration, OBS scene and virtual-camera workflows.
- RT scheduling: RealtimeKit presence is reported; whether a stream really
  got realtime priority is not checked.
