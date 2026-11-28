# Wayland compositors

HorneroOS Desktop is a Wayland-first desktop powered by Hornero Shell. A
compositor manages windows, workspaces, outputs, input, and the Wayland
session. Hornero Shell provides the shared bars, launcher, Dashboard, Control
Center, notifications, OSD, and other desktop surfaces.

The compositor is a backend choice, not the product identity. The available
backends have different maturity and capability boundaries:

- **Hyprland — Supported.** Default compositor for HorneroOS Desktop.
- **Niri — Supported.** Scrolling Wayland compositor option with a real
  Hornero Shell session backend; compositor-specific capability boundaries
  are documented below.
- **Labwc — Planned.** Not an install choice; no Hornero backend is implemented.

HorneroOS Desktop is a daily-driven **Supported** edition. Capability
boundaries are exposed honestly rather than faking identical Hyprland-only
features across backends.

## Hyprland

Hyprland is the default compositor and the most fully validated HorneroOS
Desktop session. Its window manager semantics, workspace behavior, multi-bar
layouts, keyboard focus, and Hyprland-specific controls are part of the
supported desktop path. The product remains Wayland-first; Hyprland is its
current backend rather than the definition of HorneroOS.

See [desktop shortcuts](shortcuts.md) and [layouts](layouts.md) for the shared
Shell workflows.

### Factory modules and user overrides

Hornero's Hyprland entrypoint (`~/.config/hypr/hyprland.lua`) separates
immutable packaged defaults from personal overrides:

- **Factory modules (`load_factory`):** modules such as `monitors.lua`,
  `autostart.lua`, `environment.lua`, `input.lua`, `gestures.lua`,
  `layout.lua`, `keybindings-overlay.lua`, `helpers.lua`, `keybindings.lua`,
  `window-rules.lua`, `animations.lua`, `smart-colors.lua`, `plugins.lua`, and
  `static.lua` load from `/etc/xdg/hypr/hyprland.lua.d/` when packaged there
  (overridable via `HORNERO_HYPR_FACTORY_DIR`), with per-file fallback to
  `~/.config/hypr/hyprland.lua.d/` for non-packaged runs. Because
  `/etc/xdg/hypr/hyprland.lua.d/` takes precedence, `pacman` upgrades reach
  existing users even when stale `/etc/skel` copies remain in `~/.config/hypr/`.
- **User override hooks (`load_user`):** `monitors-user.lua`,
  `keybindings-user.lua`, and `window-rules-user.lua` load from your local
  `~/.config/hypr/hyprland.lua.d/` first, falling back to `factory_dir` if
  absent.
- **Pinning a factory module:** to lock a local copy of a factory module,
  replace its `load_factory("...")` call with `load_user("...")` in
  `~/.config/hypr/hyprland.lua`.
- **Refreshing an older entrypoint:** `horneroctl config refresh-hypr --dry-run`
  previews missing factory module lines additively (supporting both
  `load_factory`/`load_user` and legacy `dofile` entrypoints) while preserving
  existing lines and `*-user.lua` files; `--yes` writes with a `.pre-refresh`
  backup.

## Niri

Niri is a supported scrolling Wayland compositor option in HorneroOS. HorneroOS
supplies a Niri configuration and a Shell backend that consumes Niri's event
stream for workspaces, windows, focus, and keyboard layouts. The backend uses
Niri's own window actions and screenshot picker where those differ from
Hyprland.

The current Niri configuration starts from the upstream Niri 26.04 defaults
and routes Hornero shortcuts to the Shell and `horneroctl`:

| Shortcut | Action |
| --- | --- |
| `Super+D` | Open Hornero Launcher |
| `Super+Shift+D` | Open Dashboard |
| `Super+Shift+B` | Open Layout Picker |
| `Super+X` | Open the session menu |
| `Super+,` | Open Appearance in Control Center |
| `Super+E` | Open Yazi in the configured terminal |
| `Super+V` | Open clipboard history |
| `Super+L` | Lock the session |
| `Print` | Open Niri's screenshot selection UI |
| `Ctrl+Print` | Capture the screen with Niri |
| `Alt+Print` | Capture the focused window with Niri |

The Layout Picker changes Hornero Shell surfaces and bars. It does not change
Niri's native scrolling-column layout. Niri does not expose the Shell's
Hyprland-specific special workspaces, output metadata, native window
thumbnails, workspace creation or renaming, or global shortcuts through the
Hyprland-only protocol. Hornero hides or disables controls that depend on
those capabilities instead of presenting fake parity.

### Portals and screen capture

With `hornero-config` 0.3.1 or later, the packaged Niri portal preference
selects GTK as the fallback and file chooser portal, and GNOME for
screencasting. Niri screen casting uses the compositor's native screencast
support through PipeWire. The Niri session also uses `xwayland-satellite` for
X11 applications. These are Niri session dependencies; the Hyprland package
set does not pull in the GTK or GNOME Niri portal backends.

OBS and end-to-end screen recording have not passed graphical acceptance
under Niri yet. A portal configuration file and installed packages alone do
not prove a working capture workflow.

### Verified behavior and capability boundaries

A QEMU guest running Niri 26.04 at 1280×800 has been driven with keyboard and
pointer input. The verified journey covers Shell startup, Launcher,
Dashboard, Control Center, Appearance, theme switching, Layout Picker/Hornero
Left, workspace switching, and Niri's screenshot selection.
This is a real graphical session check, not only a configuration parser test.

Several workflows still differ from Hyprland or remain uncertified under Niri:
multi-output focus and scaling, OBS/screencast through the selected portals,
GTK and Qt app theme agreement, and Hyprland-only controls (special
workspaces, fullscreen Gaming mode detection). Hyprland remains the default
when you rely on those features.

The Niri config is installed as a fallback at `/etc/niri/config.kdl` and
materialized under the user's XDG configuration directory. The package does
not overwrite an existing user config during a running session. Check the
current [release and install status](https://horneroos.com/install) before
following package-specific steps. The signed `v0.2.0-preview42` ISO installs
with the Calamares (`3.4.3`) graphical installer.

For diagnostics, `horneroctl doctor` identifies a recognized Niri session.
Use [Niri's configuration guide](https://niri-wm.github.io/niri/Configuration%3A-Introduction.html),
[key bindings](https://niri-wm.github.io/niri/Configuration%3A-Key-Bindings.html),
and [IPC reference](https://niri-wm.github.io/niri/IPC.html) for compositor
settings beyond Hornero's defaults.

## Other compositors

Labwc is planned. Hornero does not currently package or validate a Labwc
backend. The compositor boundary is capability-based: future support must use
the compositor's actual APIs and expose gaps honestly rather than copying
Hyprland assumptions into another session.
