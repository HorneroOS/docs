# Experience modes architecture

This page explains how experience modes are built and who owns each piece.
For what they do for a person, read [Experience modes](../desktop/experience-modes.md).
The design authority is [RFC 0001](../development/rfc-0001-hornero-signal.md)
section 5a and [Signal Visual Language](../development/signal-visual-language.md)
section 13. The code-level contract lives in the Shell repository
([`docs/EXPERIENCE.md`](https://github.com/HorneroOS/shell/blob/main/docs/EXPERIENCE.md)
and [`docs/IPC.md`](https://github.com/HorneroOS/shell/blob/main/docs/IPC.md));
this page does not repeat it.

> **Development.** This describes the Shell `main` branch (November 2026).
> The model, the deck solver and the Experience page are covered by
> headless tests that run in CI. None of it has been validated on a virtual
> machine image or a physical desktop yet. `horneroctl` has no mode
> command group yet; the RFC plans one, and until it exists the shell's own
> interface is the supported way to change modes.

## Four axes, four owners

A mode is one of four independent axes. No axis is a separate shell.

| Axis | Owner | Notes |
| --- | --- | --- |
| Edition | [hornero](https://github.com/HorneroOS/hornero) | Installed capabilities and packages |
| Experience mode | [shell](https://github.com/HorneroOS/shell) | `services/Experience.qml` and `services/experience.js` |
| Layout preset | [shell](https://github.com/HorneroOS/shell) (catalogue), [config](https://github.com/HorneroOS/config) (factory default) | Bar composition |
| Theme | [config](https://github.com/HorneroOS/config) (themes), [hornero](https://github.com/HorneroOS/hornero) (apply) | Signal roles |

The shell keeps the composition rule: a mode may enable a capability only if
the edition provides it, and a missing capability is reported as unavailable
instead of being faked.

## Layers inside the shell

- **Pure model**, `services/experience.js`: profiles, field validation,
  guardrails, state parsing, preset migration and the automatic-switch
  decision. It runs under Node in tests and touches nothing.
- **Service**, `services/Experience.qml`: the only QML consumer. It
  persists state, exposes effective fields to the rest of the shell and
  publishes the IPC target `experience`.
- **Deck model**, `services/deck.js`: the pure layout solver for the Signal
  instrument deck.
- **Pane**, `modules/controlcenter/experience/ExperiencePane.qml`: Settings
  → Experience.
- **Consumers**: the bar, motion, notifications, the desktop layer and
  PluginKit read effective fields and never read raw profiles.

### Profiles and effective fields

A profile is declarative data: a flat map of dotted fields such as `motion`,
`density`, `glow`, `scanlines`, `telemetry.rateHz`, `desktopWidgets`,
`notifications.hold`, `layout.preset`, `layout.apply`, `power.suggest` and
`hooks.*`. Each field has a validator. The effective profile is computed in a
fixed order:

1. the factory profile for the mode;
2. valid user overrides from `shell.json`, key `experience.modes.<mode>`;
3. the locked guardrails (glow and scanlines off in Focus and Gaming, motion
   off in Gaming), which ignore overrides.

Overrides equal to the factory value, unknown keys and invalid values are
dropped when the file is read. A preset id removed by the layout audit is
migrated once on read, so a stale `layout.preset` never points at nothing.
Consumers see motion forced to `off` by reduced-motion settings and glow
gated by theme polarity, high contrast and motion level; the mode cannot
override those accessibility rules.

### State and persistence

- Active mode, previous mode, source (user, auto, cli, reset, migration)
  and the auto flag: `$XDG_STATE_HOME/hornero/experience.json`.
- Per-mode overrides: `shell.json`, `experience.modes`.
- Signal deck overrides (hidden instruments, geometry per mode and
  display): `shell.json`, `experience.deck`.
- Automatic switching and toasts: `shell.json`, `experience.auto` and
  `experience.toasts`.

The session state file is separate from `shell.json` on purpose: switching a
mode is a runtime act, not a configuration edit, and it must not rewrite your
bars.

### Switching, reverting and resetting

- `set`, `toggle` and `revert` go through one transition function in the
  model. Every transition records its source, so the shell can tell an
  explicit choice from an automatic one.
- **Revert** returns to the previous mode. **Reset** selects Everyday and
  asks `horneroctl shell preset apply cockpit --yes` and the theme pipeline
  for the Signal Night theme. Reset keeps per-mode customisations; clearing
  them is a separate per-mode action that also clears that mode's deck.
- Applying a mode's preferred layout is an explicit act or a per-mode
  opt-in, because a preset rewrites the bar configuration.
- Edition hooks are best effort and reversible. Studio's audio hint records
  the previous profile and restores it when the mode is left; Gaming's
  compositor tuning is gated by the compositor capability table.

### Automatic switching

The decision function takes the state, the focused window's application id,
its fullscreen flag and a pattern list (defaults cover Steam, Gamescope and
Windows executables). It returns `enter`, `leave` or nothing. It never
overrides an explicit choice: it only leaves a mode that it entered itself.
It is off by default and reads nothing else about the session.

## The Signal instrument deck

Signal's desktop layer uses `desktopWidgets: instruments`. The deck is
PluginKit desktop widgets, not a second widget engine:

- `services/deck.js` solves placement per display in logical pixels inside
  the area the desktop layer already insets for bars, keeping the desktop
  clock's box reserved. Two flank rails, an open centre, priority drop
  instead of overlap.
- The six instruments (System Insight, Network Scope, Audio Deck, Calendar,
  Agenda, Moon Phase) come from the first-party
  [plugins](https://github.com/HorneroOS/plugins) catalogue and load only
  when the installed payload is trusted. The deck never writes extension
  lifecycle state.
- Glow comes from one shell-wide budget (`acquireGlow`): three items in
  total, shared by native instruments and extension traces, with extensions
  never taking the last slot.
- Leaving the mode fades the deck layer out before the widgets unload. In
  Focus and Gaming no widget is instantiated, so every provider lease is
  released and nothing polls for the desktop.

The shared telemetry providers follow the mode's `telemetry.rateHz`
(`Theme.telemetryIntervalMs` for extensions); see
[extension providers](../development/extensions.md#shared-data-providers).

## What is validated, and where

| Piece | Evidence | Where it ran |
| --- | --- | --- |
| Profiles, guardrails, state | Node unit tests | CI, headless |
| Deck layout | Solver tests, a diagram | CI, headless |
| Experience page and search | Offscreen QML tests | CI, offscreen |
| Per-mode idle cost | `scripts/perf-signal-deck.sh` | Not yet run |
| Visual result of each mode | QA virtual machine capture | Not yet run |
| Real-host behaviour | Host validation with a person | Not yet run |

The deck layout figures (1366×768 shows four instruments, a 3440-pixel
ultrawide shows six) come from the solver tests and a layout diagram, not
from a render.

Evidence is only recorded as validated for the place it was produced. The
[RFC 0001 implementation status](../development/rfc-0001-hornero-signal.md#implementation-status)
table tracks the overall picture.
