# Profiles & Snapshots

HorneroOS **Profiles & Snapshots** (`horneroctl profile`) provide universal,
100% user-space workspace configuration management. They are designed to be
fully reversible by construction—requiring **no root privileges**, **no custom
real-time kernel**, and **never touching private application databases**.

Whether you are switching from deep focused development to live music
production, gaming, or presenting, Profiles capture and apply your exact
environment in seconds.

---

## The 5 Composable Domains

Every HorneroOS profile encapsulates exactly 5 composable domains, allowing
you to bundle or selectively apply configuration aspects:

1. **Experience**: Visual mode, Signal theme variants, and window layout
   presets (`hypr` layouts, animation profiles).
2. **Audio & Routing**: Studio audio mode, PipeWire quantum/clock settings,
   default sink/source selections with intelligent missing-hardware warnings,
   user PipeWire/JACK drop-in symlinks, custom PipeWire links, and per-app
   stream routing rules.
3. **Power**: Active power profile (balanced, performance, power-saver) and
   idle inhibitor / keep-awake rules (`caffeine` / redshift / screen
   blanking).
4. **Extensions**: Enabled Hornero PluginKit extensions and Hyprland plugin
   states.
5. **Companion Apps**: Auto-detected user applications active during capture
   (system daemons are strictly excluded). Companion apps feature an opt-in
   launch offer when switching profiles via Quickshell UI or `horneroctl
   profile launch-apps`, never blind auto-spawning!

---

## Automatic Safety Net

HorneroOS protects your workspace with a robust multi-tier safety architecture:

- **Immutable Baseline**: The first time you capture or apply a profile,
  HorneroOS automatically records an immutable `baseline` snapshot of your
  initial system state.
- **Automatic Previous Backup**: Every single time you apply a profile or
  revert changes, the system automatically saves a `previous` snapshot
  beforehand.
- **Quickshell 15-Second Safety Bar**: When applying profiles through the
  Quickshell control center or CLI, a 15-second confirmation banner appears,
  allowing you to instantly keep or revert changes if hardware or display
  states misbehave.

---

## Quickshell UI Walkthrough

The Quickshell desktop environment integrates profiles deeply across three
main panels:

### Control Center → Profiles

- **Capture Snapshot**: Snapshot your current live workspace with a custom
  name and description.
- **Saved Profiles**: View all profiles with status badges indicating hardware
  compatibility and companion app availability.
- **Diff Preview**: Inspect configuration diffs against the live system state
  before applying.
- **15-Second Safety Banner**: Confirmation bar with automatic rollback on
  timeout if unconfirmed.
- **Companion Apps Prompt**: Opt-in dialog offering to launch missing
  companion apps.
- **Restore Baseline / Revert**: Instant 1-click restoration to your original
  `baseline` or `previous` snapshot.

### Control Center → Studio

- **Quick Profile Switch**: Rapidly toggle between studio and desktop modes.
- **1-Click Live Audio Routing Kits**: Enable pre-configured virtual routing
  kits:
  - `live-call`: Discord/Zoom zero-feedback routing with hardware loopbacks.
  - `browser-backing`: Browser media routing into DAW inputs.
  - `reaper-low-latency`: Ultra-low quantum PipeWire routing for REAPER.
- **Open qpwgraph**: Launch the visual PipeWire graph patchbay in 1 click.

### Control Center → Audio

- **Per-App Stream Sink Selector**: Route individual application streams to
  specific audio sinks without needing `pavucontrol`.
- **Zero-Volume Alert**: Automatic detection of muted or `0%` streams with a
  1-click **Restore 100%** button.

---

## Complete CLI Reference (`horneroctl profile`)

Manage your workspace snapshots directly from the terminal:

```bash
# List all profiles and baseline/previous status
horneroctl profile list --json

# Show full profile details + live hardware and app state
horneroctl profile show music-prod --json

# Capture live workspace
horneroctl profile capture music-prod \
  --name "Music Production" \
  --description "REAPER + PipeWire routing" --yes

# Compare profile against live system state
horneroctl profile diff music-prod --json

# Apply profile domains best-effort
horneroctl profile apply music-prod \
  --domains experience,audio --launch-apps --yes

# Revert to previous (default) or baseline
horneroctl profile revert --to previous --yes

# Launch missing installed companion apps detached
horneroctl profile launch-apps music-prod --yes

# Export self-contained portable JSON bundle
horneroctl profile export music-prod ./music-prod.json --portable --yes

# Import a JSON bundle
horneroctl profile import ./music-prod.json --id studio-rig --yes

# Delete a user profile (refuses baseline)
horneroctl profile delete music-prod --yes
```

---

## Reversible Studio Routing Kits (`horneroctl studio routing`)

Manage virtual audio routing drop-ins without touching your personal dotfiles:

```bash
# Show kit status, active sinks, and streams
horneroctl studio routing status --json

# Enable a virtual routing kit
horneroctl studio routing enable live-call --yes

# Disable a kit
horneroctl studio routing disable live-call --yes

# Move an active stream ID to a target sink
horneroctl studio routing move-stream 42 discord_call --yes

# Unmute stream and set volume (0..150)
horneroctl studio routing fix-volume 42 100 --yes
```

---

## Portability & Dotfiles Workflow

Profiles can be exported as standalone, portable JSON bundles using
`horneroctl profile export <id> <file> --portable`. These bundles strip local
absolute paths and machine-specific IDs, making them perfect for committing to
your dotfiles repository or sharing across different HorneroOS machines via
`horneroctl profile import <file>`.

---

## Full Rollback

If your workspace configuration ever enters an undesirable state, you can
instantly restore your pristine initial environment with:

```bash
horneroctl profile revert --to baseline --yes
```
