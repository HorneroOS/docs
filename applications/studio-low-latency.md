# Studio: low-latency audio without the folklore

A working path through HorneroOS Studio audio: start reliable,
measure your own interface, and only then lower the quantum. This
guide extends [Studio audio](studio-audio.md); that page owns the
mode contract and recovery steps.

## Start on Balanced, every time

```sh
horneroctl studio doctor
horneroctl studio selection show
horneroctl mode set studio
```

Balanced follows your device rate and quantum and needs no tuning.
Record one clean take or playback pass on Balanced first: that is
the baseline every experiment below is compared against.

![Settings, Studio page with the Studio doctor results. Nine of ten
checks pass; the PipeWire xrun check is marked FAIL and reports xruns
counted since the audio nodes started, suggesting a larger quantum or
Balanced mode.](https://www.horneroos.com/captures/cap-cc-13.png)

*Settings → Studio runs the same doctor: honest results, including a
fail. Running-desktop capture, 19 November 2026.*

## What the modes actually change

| Mode | Use it when | What changes |
| --- | --- | --- |
| Balanced | Default, always safe | Nothing; follows device |
| Low Latency | Short monitoring paths | 128-frame quantum proposal |
| Advanced | Per-interface calibration | Your measured values |
| Temporary Performance | Long renders and exports | Temporary power profile |

PipeWire and WirePlumber run the session in every mode; switching
modes never re-prioritises Bluetooth or consumer devices, and
HorneroOS never installs a real-time kernel or retunes governors
for Studio.

## Quantum is not latency

A quantum is a scheduling period. The Low Latency proposal is 128
frames at 48 kHz; it is not a measured round-trip latency, and no
HorneroOS surface presents it as one. Only a physical loopback
measurement on your interface reports real latency. Measure yours
if the number matters to your work.

![A terminal showing studio doctor output with the Low Latency mode
recorded. Two checks are marked WARN: xruns counted since the audio
nodes started, and the low-latency profile being active, with the
command that reverts it.](https://www.horneroos.com/captures/cap-studio-04.png)

*`horneroctl studio doctor` with Low Latency recorded: the warnings
stay visible, including the xrun count. Quantum values are a
scheduling period, not measured latency. Capture from the
maintainer's machine, 19 November 2026.*

## A safe Low Latency trial

1. Follow the copy-and-restart steps in
   [Studio audio](studio-audio.md#setup) to enable Low Latency.
2. Play or record the same material as your Balanced baseline.
3. Clicks, dropouts or xruns mean your interface cannot sustain
   that quantum: go back to Balanced. That is expected behaviour,
   not a failure to tune around.
4. `rtkit` is part of the normal PipeWire session; HorneroOS does
   not ask you to replace it or to raise limits by hand.

## Routing

Route with WirePlumber-aware tools (`wpctl`, `qpwgraph`, or your
DAW's PipeWire/JACK ports). HorneroOS sets no device-specific
rules, so your routing survives device changes. Pro-audio programs
connect through `pipewire-jack`. For a full multi-bus Discord, OBS, and
browser backing walkthrough, see
[Studio: live routing](studio-live-routing.md).

## When audio breaks

Remove the copied drop-in and restart the user services, exactly
as in [Studio audio recovery](studio-audio.md#recovery), then run
`horneroctl studio doctor` again before changing anything else.
