# Hornero Welcome

Hornero Welcome is your starting deck for HorneroOS and your permanent guide to
what the desktop can do. It guides new users through a calm first-run setup,
turns into an everyday discovery hub once you finish, and surfaces concise
release highlights after an upgrade without replaying first-run screens.

> **Development.** The `horneroctl welcome` CLI and the initial Welcome
> window are already on `main`, while the **Signal Flight** 3-mode redesign
> (`First Flight`, `Explore Hornero`, and `What's New`) is tracked across
> `HorneroOS/shell#751` and `HorneroOS/hornero#506`. Current ISOs up to
> `v0.2.0-preview32` ship the earlier 11-page Welcome window.

## Three modes, one window

| Mode | When it opens | Purpose |
| --- | --- | --- |
| **First Flight** | First login (`showOnLogin`) | 9-scene guided setup |
| **Explore Hornero** | Returning manual opens | Search features and keys |
| **What's New** | Upgraded (`showOnLogin` on) | Release highlights |

Open Welcome anytime from the Launcher (**Ctrl + Space**), **Settings**, or a
terminal:

```sh
horneroctl welcome open
horneroctl welcome status
horneroctl welcome set-show-on-login false --yes
```

To replay the guided tour later, run `horneroctl welcome reset --yes`. Every
mutating command accepts `--dry-run` before `--yes`.

## First Flight: guided arrival

Instead of a dense checklist, **First Flight** opens in a calm `1080×680`
window with a minimal top mode bar and a compact bottom flight rail. You can
toggle **Show on login**, click **Skip tour** at any moment, or move step by
step through nine focused scenes:

1. **Arrival:** Reads your active edition and compositor (`Hyprland` or
   `Niri`) over verified Argentine artwork with an attributed photographer
   credit.
2. **Make It Yours:** Try themes, wallpapers, Chromatic accents, and bar
   layouts with instant reversible previews.
3. **Workstation Builder:** Pick an Experience Mode and explore workstation
   software profiles.
4. **Meet Javi:** Customize Javi's visual sidekick skin and review how the
   optional local AI assistant stays off until you enable it.
5. **Move & Fly:** Practice four real desktop actions using your actual live
   keybindings.
6. **Extensions & Ecosystem:** Browse curated PluginKit v3 extensions and
   review their privilege and Safe Mode boundaries.
7. **Create · Build · Play:** Inspect real readiness for Studio Audio,
   Developer/Agent tools, and Gaming.
8. **Trust, Diagnostics & Recovery:** Check `horneroctl doctor` health and the
   boundary between config snapshots and OS Btrfs recovery probes.
9. **Ready to Fly:** Review your locked choices and jump straight into the
   Launcher or **Explore Hornero**.

## Make It Yours: reversible live previews

Scene 2 lets you experiment with your desktop look without risking a broken
configuration:

- **Polarity and themes:** Switch live between **Signal Day** (white ceramic),
  **Signal Night** (blue-hour graphite), **Signal High Contrast**, and
  Argentine Originals (`jacaranda`, `glaciar`, `ceibo`).
- **Verified Argentine wallpapers:** Welcome showcases only the 2 MIT
  procedural Signal SVGs and 3 verified CC BY 2.0 Argentine photographs (Luis
  Argerich's *Buenos Aires after dark*, RAYANDBEE's *Beagle Channel*, and
  Kevin Jones's *Quebrada del Condorito*) with visible photographer credits. See
  [Wallpapers](wallpapers.md).
- **Hornero Chromatic v3:** Preview wallpaper-harmonized accents (`Balanced`,
  `Vibrant`, or `Muted`) while keeping ceramic or graphite surfaces clean. See
  [Hornero Chromatic](chromatic.md).
- **Bar layouts:** Switch between `Cockpit`, `Hornero Left`, `Islands`, and
  `Dock Bottom` on a live miniature desktop stage. See [Layouts](layouts.md).

Theme, Chromatic, and wallpaper previews run in memory first. When a layout
preview writes to disk, Welcome snapshots your baseline in
`$XDG_STATE_HOME/hornero/welcome-preview-tx.json` and shows a non-blocking
**Previewing live** bar with **Revert** and **Apply & Keep**. Pressing
**Escape** or closing the window cancels unapplied previews; if the shell ever
crashes mid-preview, the next login restores your baseline automatically.

## Build your workstation

### Experience Modes

Scene 3 pairs an asymmetric selector for all five [Experience
modes](experience-modes.md) (**Everyday**, **Focus**, **Signal**, **Studio**,
and **Gaming**) with a live spec readout showing Motion Level, Telemetry Rate,
Glow Budget, Popup Hold, and honest hardware/compositor readiness (such as
whether PipeWire Studio Audio or Hyprland tuning is available on your host).

### Curated software profiles via Hornero Apps

Software installation in Welcome is powered by [Hornero Apps](hornero-apps.md)
and its signed declarative catalog (`catalog/apps.v1.json`) rather than ad-hoc
scripts. Individual users and organizations can inspect workstation profiles
and trust policies before installing anything:

```sh
horneroctl store profiles
horneroctl store profile-show ai-workstation --json
horneroctl store policy show --json
```

Every package displays its provenance badge (**Official**, **Verified**,
**Community**, or **Web App**) and license. Proprietary tools and opt-in AUR
builds never install silently, and teams can lock allowed sources with
`horneroctl store policy` or reproduce fleets with `horneroctl store manifest`
(all mutations are recorded in `~/.local/state/hornero/store/audit.jsonl`).

### Workloads and honest edition limits

Scene 7 (`Create · Build · Play`) adapts to what is actually installed on your
machine:

- **Create (Studio):** Shows live PipeWire Studio Audio readiness and routing
  kits (`live-call`, `browser-backing`, `reaper-low-latency`).
- **Build (Dev & Agents):** Launches your configured terminal, Yazi file
  browser, and the **Agent Center** (`ControlCenter("agents")`) to inspect
  local coding agents and usage telemetry. (The dedicated `Agents` edition
  remains **Planned**.)
- **Play (Gaming):** Surfaces fullscreen GameMode readiness (`gamescope` and
  `mangohud`).
- **Compositors and planned editions:** Hyprland is the validated default;
  [Niri](compositors.md) is **Experimental** and hides Hyprland-only items.
  `Labwc` and `Server` are **Planned** and omitted from Welcome.

## Meet Javi & Companion

Scene 4 separates Javi's two distinct roles clearly so you always know what
runs locally:

- **Javi Companion (Visual Sidekick):** An expressive desktop sprite with eight
  skins (`default`, `argentina`, `gaucho`, `blue-gold`, `nocturnal`,
  `retro-terminal`, `mono`, and `red`) and live preview poses (`Greet`,
  `Think`, `Work`, `Sleep`) that react to battery, builds, and Experience Modes.
- **Javi AI / Hermes Assistant (Optional, Local-only):** Off by default and
  never auto-started by Welcome. When enabled separately, it streams local
  commands via `horneroctl`, strips secret-looking attachments (`.env` files
  and private keys) before sending prompts, and requires an explicit
  **Approval** gate before changing anything on your system.

Hornero Welcome requires **zero accounts**, **zero cloud sign-in**, and sends
**zero telemetry**.

## Interactive tutorials (`Move & Fly`)

Scene 5 teaches core navigation without fake timer checkmarks. It reads your
**active keybindings** live (so custom remaps appear accurately, or shows
`Unbound — use action button or Bar` when a shortcut is unbound) and marks
each mission complete only when the real shell or compositor event fires:

1. **Summon Launcher:** Open the Launcher via your live keybinding or
   **Try Launcher**.
2. **Peek Dashboard:** Toggle the Dashboard drawer.
3. **Switch Workspace:** Move to another workspace on `Hyprland` or `Niri`.
4. **Open Settings:** Launch Control Center while Welcome stays open in the
   background so you can see the checkmark land.

On Hyprland, a bonus **Toggle Scratchpad** hint appears; on Niri it stays
hidden automatically. You can always click **Continue** at your own pace.

## Explore Hornero: your permanent discovery hub

After finishing `First Flight`, opening Welcome manually lands in **Explore
Hornero**:

- **Unified instant search:** Filter across Hornero features, Control Center
  settings pages, and your live keybindings in one place.
- **Categorized feature guide:** Jump directly to safe destinations across
  Navigate & Shell, Appearance & Chromatic, Javi & AI, Workloads & Editions,
  and Safety & Recovery.
- **Searchable Shortcuts reference:** Inspect live bindings anytime alongside
  the [Shortcuts](shortcuts.md) guide.
- **Extensions and Trust ledger:** Browse curated [Extensions](extensions.md)
  with an explicit reminder that Quickshell plugins run unsandboxed with your
  user privileges (`HORNERO_SAFE_MODE=1` disables all plugins for recovery),
  plus a clear Trust & Recovery ledger distinguishing supported **Hornero
  Config Snapshots** from read-only **OS Btrfs Recovery** readiness probes (see
  [Updates and recovery](updates-and-rollback.md)).

## What's New and upgrade behavior

Returning users who update HorneroOS are **never** forced back through
`First Flight`. Welcome decouples first-run completion (`firstRunCompleted`)
from release tracking (`lastSeenReleaseVersion`):

- If you disabled auto-launch (`showOnLogin: false`), Welcome **never**
  auto-opens on login—even after major upgrades.
- If you kept auto-launch enabled and already completed `First Flight`, an
  upgrade opens directly into **What's New** once per release with curated
  highlights and direct links to new settings.

## Accessibility and power efficiency

Hornero Welcome follows the [Hornero Signal](hornero-signal.md) and
[Popups, focus and motion](popups-and-motion.md) contracts:

- **Full keyboard operation:** Every scene, tab, swatch, and tutorial action
  works from the keyboard with a `2 px` celeste (`Signal.palette.focus`) focus
  ring and predictable **Escape** handling.
- **AT-SPI semantics and text scaling:** Controls expose explicit accessible
  names and state, and respect **Settings → Accessibility → Text size**.
- **Contrast modes:** Signal Day (`>= 5.27:1` weakest text), Signal Night, and
  **Signal High Contrast** (`hornero-signal-contrast`) work across every scene,
  with directional scrims preserving legibility over Scene 1 photography.
- **Reduced motion and zero idle wakeups:** Under **Reduce motion** (or
  `org.gnome.desktop.interface enable-animations = false`), transitions cap at
  `<= 90 ms` crossfades, Javi holds still on frame `0` (`holdStill`),
  `HorneroSprite` stops its blink timer, and ambient animations pause whenever
  Welcome is hidden or minimized.

## Related guides

- [ADR: Hornero Welcome architecture](../architecture/adr-hornero-welcome.md)
- [Hornero Signal](hornero-signal.md) · [Themes and appearance](appearance.md)
- [Hornero Chromatic](chromatic.md) · [Wallpapers](wallpapers.md)
- [Hornero Apps](hornero-apps.md) · [Experience modes](experience-modes.md)
- [Shortcuts](shortcuts.md) · [Extensions](extensions.md)
- [Updates and recovery](updates-and-rollback.md) · [`horneroctl`](horneroctl.md)
