# Desktop experience reference study

> Checked against the public project sources on 2026-10-14. This is a
> product-engineering study, not a feature scorecard or a claim that the
> projects have the same audience. Recheck linked sources before using this
> page to make a release decision.

HorneroOS has its own product history, design language, and operating-system
boundaries. This study records useful patterns from Caelestia, Ryoku, and
Omarchy, then states which ideas fit HorneroOS and which do not. The goal is to
improve the product without copying another project's structure or identity.

## Current HorneroOS position

HorneroOS is an Arch-based operating-system family in development. Desktop is
Wayland-first; Hyprland is its default validated compositor, while Niri remains
experimental until its broader session matrix passes. The current product
website says no installable ISO is published. Server, Agents, and Studio remain
planned editions. These maturity boundaries are part of product quality and
must stay visible in docs and marketing.

The desktop already has a composed identity: a Quickshell-based UI, an
`horneroctl` system interface, shared theme and wallpaper data, real
Argentina-related photographic assets with provenance, and palette adapters
for Kitty, Alacritty, Ghostty, btop, and Cava. Hornero Config derives native
formats for all five applications from the active wallpaper scheme. The
terminal emulators are curated integrations; btop and Cava remain optional
applications. See the [palette renderers](https://github.com/HorneroOS/config/blob/main/lib/hornero/terminal_themes.py),
[appearance application path](https://github.com/HorneroOS/config/blob/main/lib/hornero/apply-appearance.sh),
and [integration tests](https://github.com/HorneroOS/config/blob/main/tests/test_apply_official.sh).
The responsibilities are intentionally split between `shell`, `hornero`,
`config`, `docs`, and `website`; see the [repository map](../architecture/README.md)
and [design language](design-language.md).

## What the references do well

### [Caelestia](https://github.com/caelestia-dots/shell)

**Pattern.** The shell and its CLI are separate projects. The shell documents
its IPC, while the CLI owns operations such as scheme, wallpaper, recording,
screenshots, and updates. Shell settings are explicit JSON, with per-monitor
overrides and a Home Manager integration.

**Transfer.** Keep UI presentation separate from stable operating-system
commands. Make shell controls, CLI commands, and docs describe the same state
transitions. Keep machine-specific settings out of packaged defaults.

**Keep distinct.** Caelestia's shell is explicitly Hyprland-oriented.
HorneroOS's desktop identity is Wayland-first, and compositor-specific
operations must remain behind capability-aware adapters.

### [Ryoku](https://github.com/Ryoku-dev/ryoku)

**Pattern.** The repository presents the system definition, desktop, installer,
and release tooling as one product. It describes Hyprland and Niri sessions,
signed package delivery, update snapshots, and boot-time rollback. Its docs
explain the intended audience and system boundaries directly.

**Transfer.** Treat installation, update, and recovery as product experiences,
not package-list chores. A future supported Hornero release needs a verifiable
artifact chain and a documented recovery path. Keep the Niri maturity label
tied to real session acceptance.

**Keep distinct.** HorneroOS has established repository ownership boundaries
and work on a provisional installer with a separate long-term owner. Do not
collapse repositories or take over installer architecture to imitate Ryoku.

### [Omarchy](https://github.com/omacom/omarchy)

**Pattern.** Themes are data packages. Color definitions feed generated
application configuration, and a theme can include wallpapers, preview images,
lock imagery, icon choices, keyboard color, and a light-mode marker. Its CLI
and menu expose direct, scriptable theme operations.

**Transfer.** Continue moving theme support toward generated adapters from one
reviewed palette, with visual previews and explicit light/dark metadata. Keep
the theme picker, command line, and documentation in agreement.

**Keep distinct.** Omarchy's templates can produce executable configuration
for applications. HorneroOS must keep its own licensing, trust review, and
generated-file boundaries. A theme or extension must not become an implicit
code-execution permission.

## Product decisions for HorneroOS

### Keep product ownership explicit

The current multi-repository model is useful when each contract has one owner:

- `shell` owns the desktop presentation and interactive session.
- `hornero` owns the stable CLI and operating-system operations.
- `config` owns packaged defaults, themes, wallpapers, and application
  materialization.
- `docs` owns user and contributor guidance.
- `website` publishes reviewed, pinned product data and real captures.

Do not duplicate package, theme, edition, or compositor truth to make a page or
installer easier to implement. Extend the existing machine-readable contracts
instead.

### Make integration depth a first-class feature

Theme quality is not the number of palettes. It is the number of applications
that adopt a selected palette correctly, the fidelity of light and dark
variants, and whether applying or reverting a theme restores a coherent
desktop. Hornero Config currently renders one wallpaper-derived scheme into
native Kitty, Alacritty, Ghostty, btop, and Cava files. Add another adapter
only when its format is generated from the shared palette and the result has
tests. This keeps app-specific colors from drifting into separate hand-edited
copies.

### Treat reliability as part of the desktop experience

The visual shell is only one part of a dependable workstation. Product work
must also cover upgrade integrity, recovery, clear failure messages, and safe
first boot. Signed repositories, snapshots, and boot rollback are useful
reference patterns from Ryoku, but each needs an explicit HorneroOS threat and
maintenance model before adoption.

### Support compositors by evidence

Hyprland remains the validated default. Niri is experimental until graphics,
workspace and window state, portals, lock behavior, multi-monitor, and
capture-related workflows pass the QA matrix. Do not describe a generic
Wayland abstraction as complete while essential actions still rely on one
compositor. Labwc remains a future backend until it has a real adapter and
acceptance coverage.

### Keep the website tied to the running product

The website's Buenos Aires cyberpunk palette and Argentina photography give
HorneroOS a recognizable identity. Keep product shots real, captions
provenance-backed, and edition maturity accurate. Reference projects can
inform interaction and release engineering, but their screenshots, names, and
visual systems do not belong in HorneroOS product media.

## Source notes

The statements above are based on the projects' own current documentation and
source trees:

- [Caelestia shell README](https://github.com/caelestia-dots/shell#readme)
  and [Caelestia CLI](https://github.com/caelestia-dots/cli).
- [Ryoku README](https://github.com/Ryoku-dev/ryoku#readme),
  [vision](https://github.com/Ryoku-dev/ryoku-docs/blob/main/docs/vision.mdx),
  [installation map](https://github.com/Ryoku-dev/ryoku/blob/main/installation/README.md),
  and [package delivery](https://github.com/Ryoku-dev/ryoku/blob/main/release/packages/README.md).
- [Omarchy theming](https://github.com/omacom/omarchy/blob/quattro/docs/theming.md)
  and [CLI](https://github.com/omacom/omarchy/blob/quattro/manual/14-omarchy-cli.md).
- HorneroOS's [edition status](https://horneroos.com/editions),
  [installation status](https://horneroos.com/install),
  [terminal integrations](https://horneroos.com/terminals), and
  [architecture docs](../architecture/README.md).

## Review cadence

Update this study when a referenced project changes a product boundary that
affects HorneroOS decisions, or when HorneroOS ships a capability that changes
the comparison. Record repository evidence and test results with the change.
Do not turn star counts, release frequency, or screenshot volume into quality
claims.
