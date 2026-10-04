# Media and audio

The Shell provides controls around host audio devices and media players. It
does not replace the audio server or the player that owns the music or video.

## Audio devices

The Audio page in Control Center selects the host's output and input
devices. Volume keys change the default output, the microphone key toggles
the default input, and the Shell shows short-lived volume feedback. A mixer
such as `pavucontrol` can expose per-application streams and device routing;
it is an optional host application, not installed by `hornero-config`.

PipeWire and WirePlumber are common Arch audio components, but their exact
installation and service state belong to the host setup. Check the current
Control Center state before changing services. See the
[Arch Wiki PipeWire guide](https://wiki.archlinux.org/title/PipeWire) and
[pavucontrol](https://freedesktop.org/software/pulseaudio/pavucontrol/).

## Media players

The Shell watches MPRIS-compatible players and presents the active player's
metadata and transport controls. Media keys use `playerctl` in the curated
Hyprland config. The player itself is chosen by the user; mpv is an optional
playback tool in the personal dotfiles setup, not a required Hornero
dependency.

Opening an audio or video file uses the host's MIME association. This is
separate from the player currently selected for the Shell's media controls.
See [Default applications](default-apps.md) to change file associations.

## Visualizer

Cava is an optional package with a Hornero Config file. The Shell's desktop
visualizer is disabled by default. Enabling that visualizer requires a
working audio source and the configured audio integration; Cava's existence
alone does not start it.

Troubleshooting:

- If the volume OSD moves but sound does not change, verify the host audio
  service and the selected output device.
- If media controls show no player, start a player that supports MPRIS.
- If media keys do nothing, check whether `playerctl` is installed and the
  active player accepts MPRIS commands.

Upstream: [MPRIS](https://specifications.freedesktop.org/mpris-spec/latest/),
[playerctl](https://github.com/altdesktop/playerctl),
[mpv manual](https://mpv.io/manual/stable/),
[Cava](https://github.com/karlstav/cava).
