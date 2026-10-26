# Studio hardware and performance boundaries

What HorneroOS Studio does and does not claim about creative
hardware today, and the boundaries every Studio workflow respects.
Studio is a **Preview** edition: there is no Hornero-tested
hardware list, no certified interface, GPU, tablet, or control
surface yet. Support claims arrive only with HorneroOS/qa
acceptance evidence.

## The honest support picture

| Area | Today | Evidence needed |
| --- | --- | --- |
| Audio interfaces | PipeWire defaults | QA loopback fixtures |
| GPUs | Upstream Arch drivers | QA capability matrix |
| Displays | Per-output Shell | QA display fixtures |
| Tablets/MIDI/surfaces | Upstream stack | QA device scenarios |
| Storage | Policy thresholds | CLI path validation |

Area notes:

- **Audio:** no Hornero-measured latency or XRUN claims yet.
- **GPUs:** no render/encode certification yet.
- **Displays:** the Studio preset ships no geometry.
- **Tablets/MIDI/surfaces:** kernel, libinput, and PipeWire
  behaviour as shipped upstream.

If a device works, it works because of the upstream stack. That is
worth using — it is just not a Hornero support promise.

## Performance boundaries Studio never crosses

- No RT kernel is installed or required.
- No IRQ threading, CPU governor, GPU clock, or I/O scheduler tuning.
- Temporary Performance mode only reuses power-profiles-daemon and
  restores the previous profile; it writes no governor values.
- Low Latency quantum values are proposals to try per interface,
  never a latency guarantee (quantum is a scheduling period, not
  round-trip latency).
- Benchmarks, thermal claims, and render-time comparisons are QA
  evidence or they are not claims at all.

## Creator workflows, as they stand

- **Audio/music:** Balanced PipeWire with WirePlumber routing;
  Ardour/Guitarix/Carla/Audacity from the catalogue, REAPER only by
  explicit proprietary opt-in, yabridge for your own Windows VSTs.
- **Video/streaming:** OBS Studio and Kdenlive via PipeWire capture
  on the compositor you already run; GPU encode depends entirely on
  your upstream driver stack.
- **Design/photo/3D:** Krita, GIMP, Inkscape, darktable, RawTherapee,
  Blender, FreeCAD, and Godot as ordinary Arch applications with
  Hornero defaults around them — no forked builds.
- **Selection and state:** Settings → Studio or
  `horneroctl studio selection` records intent; `horneroctl studio
  doctor` reports selection and audio-stack health read-only.

## Before you buy or blame hardware

1. Run `horneroctl doctor` and `horneroctl studio doctor`.
2. Check the upstream view (`lspci -nnk`, `wpctl status`,
   `pw-top` while audio runs) before changing any setting.
3. Stay on Balanced audio unless you measured a reason not to;
   change one variable at a time and keep the delete-to-restore
   path from the [Studio audio guide](../applications/studio-audio.md).

See also the [Studio application matrix](../applications/studio.md)
and [getting started](../applications/studio-getting-started.md).
