# Extensions: PluginKit 3 authoring guide

**Development.** Hornero Shell extensions are QML packages the shell
discovers, loads in their own `Loader`, and renders on the bar, the
dashboard, the launcher, the desktop or in Settings. Since November 2026 on
the `main` branches of Shell and Plugins they are written against
**PluginKit 3**, the Hornero Signal extension contract. This page is the
handbook entry point for authors: it states what shipped, what changed from
Extensions 2.0, and what has not been verified on a live desktop. It is not
the API reference.

The implementation owns the contract, and this page links to it rather
than copying it:

- Shell contract, manifest, PluginKit, and validators:
  [`HorneroOS/shell` `docs/PLUGINS.md`][shell-plugins], the
  [manifest JSON schema][shell-schema], and the shell checker at
  `scripts/validate_plugin.py` in that repository.
- First-party catalogue workflow and quality gate:
  [`HorneroOS/plugins` `docs/DEVELOPING.md`][plugins-developing],
  [`docs/CONTRIBUTING.md`][plugins-contributing], and
  [`docs/SECURITY.md`][plugins-security].
- Design authority: [RFC 0001](rfc-0001-hornero-signal.md) and
  [Signal Visual Language](signal-visual-language.md). Popup, focus and
  motion rules are in the [interaction contract](interaction-contract.md).
- Command-line lifecycle: the CLI's own help for the plugin command
  family. The handbook page for those commands is tracked separately
  in [HorneroOS/docs#45][docs-45]; until it lands, treat CLI help as
  authoritative and this page as a summary.

Where a linked guide and this page disagree, the shell contract wins
for manifest and PluginKit behavior, and CLI help wins for command
syntax.

> **Breaking change.** PluginKit 3 removes the Material-era API outright.
> The shipped shell loads only manifests with `"schemaVersion": 3` and
> refuses `1` and `2` with a pointer to the migration steps. There is no
> compatibility layer. Packages written for Extensions 2.0 need the
> mechanical port described in [Migrating from PluginKit 1 and 2](#migrating-from-pluginkit-1-and-2).

## Read the trust model first

Extension QML runs **in-process inside Quickshell with the logged-in
user's permissions. It is not sandboxed.** No manifest field changes
that:

- `capabilities` (`processCommands`, `networkHosts`, `providers`,
  `settings`, and the broker `actions` list below) are review
  disclosures shown before consent. They are not an operating-system
  permission grant and the shell does not enforce them against running
  QML.
- The static validators reject malformed packages and a conservative
  set of suspicious patterns. Passing validation is not a security
  certification, and textual checks can be evaded by dynamic code.
- The PluginKit `Settings` component selects a settings namespace by
  `pluginId`. That ID is not proof of the caller's identity and does
  not isolate one extension from another.
- Installing a package copies inert data. Enabling is a separate,
  explicit consent action, and enabling revalidates the installed
  payload. Read the source before you enable a community extension.
- Never ship credentials, privileged helpers, compiled binaries, or
  personal configuration in an extension package.

One real boundary does exist, and it is narrow: calls made **through
the CLI's typed capability broker** (the plugin action commands in
CLI help) run only when the package is receipt-owned, enabled, and
trusted, when the action is declared in `capabilities.actions`, and
when the CLI's ABAC policy allows it. Mutating broker calls also
need explicit confirmation and every broker run decision is
audit-logged. The broker governs only calls made through it. It does
not sandbox, observe, or restrict the extension's own QML.

## What shipped, and what did not

| Area | State |
| --- | --- |
| Manifest `schemaVersion` 3 | The only version the host loads |
| `background`, `bar`, `dashboard`, `desktop` | Hosted |
| `launcher` and `settings` surfaces | Hosted |
| Generated settings UI | Hosted in Control Center |
| Desktop widgets (free placement) | Hosted; edit mode, per display |
| Signal instrument deck | Six first-party widgets in Signal mode |
| Shared providers and `Telemetry` | Hosted, one source per domain |
| Screenshots, installed package | Shown, no plugin code runs |
| Screenshots, not yet installed | Caption only, no local image |
| Marketplace `compatibility` | Review metadata, gates nothing |
| Community catalogue pane | Read-only; lifecycle stays in CLI |
| Community registry product key | Not shipped; fails closed |
| Per-user per-surface toggles | Not part of the contract yet |

The official catalogue has **36 extensions, all ported to PluginKit 3**
(see [The official catalogue](#the-official-catalogue)).

### Not yet verified on a live desktop

The contracts below are covered by unit, host, schema, and offscreen
QML tests in the shell, CLI, and plugins repositories. That is not
the same as graphical acceptance, and this page does not claim it:

- No PluginKit 3 extension has been validated in the QA virtual machine
  or on a physical desktop yet. The port of the 36 catalogue extensions,
  the instrument widgets and the Signal deck are checked by validators,
  schema tests and offscreen QML, not by a captured render.
- Host-context layout across bar edges, displays, and output scales
  is contract-tested, not yet verified in a live multi-monitor
  compositor session.
- Keyboard behavior is driven by an offscreen QML probe. Live
  compositor focus grabs and screen-reader (AT-SPI) announcements
  still need a running session to verify.
- The shared-provider idle-cost argument is static analysis pinned
  by tests, not a host power or wakeup measurement; the same is true
  of the per-mode idle cost of the deck.
- The first-party quality audit (see
  [Quality gate](#quality-gate)) currently classifies **every**
  catalogue extension as `needs-upgrade`. The audit is static; a merged
  PluginKit 3 port is shipped code, not a premium-ready or graphically
  accepted claim.

## Package shape

One directory per extension, containing exactly `manifest.json`
plus every file listed in the manifest `files` array:

- the declared QML `entrypoint` (and one entrypoint per additional
  surface),
- `README.md` and `LICENSE` for anything you distribute,
- translation catalogs and preview images, when declared.

Paths are package-relative and may not escape the package.
Symlinks, compiled binaries or bytecode, setuid/setgid bits,
world-writable files, and executable files are rejected. The
extension import surface is intentionally narrow: Qt Quick and
Quickshell public modules plus `Hornero.PluginKit`. Imports from
Hornero's internal implementation are rejected.

## Manifest v3

`"schemaVersion": 3` is the only accepted value. It keeps the identity,
`surfaces`, `capabilities`, `translations` and `marketplace` shapes that
manifest v2 introduced and adds the Signal rules around them: the data
domains you read are declared in `capabilities.providers`, icons are
Hornero Glyph names, and colours come from `Theme.palette`. Unknown fields,
unknown surface names, and unknown schema versions are rejected. The
canonical field-by-field reference is the [shell contract][shell-plugins]
and the [JSON schema][shell-schema]; the summary below is orientation.

- Required identity: `id`, `name`, `version`, `description`,
  `author`, `license`, top-level `entrypoint`, and `files`.
- `placement` picks the primary surface: `background` (headless,
  the default), `bar`, `dashboard`, or `desktop`.
- `surfaces` maps additional surface names to their own
  `entrypoint`, with an optional manifest-default `enabled` flag
  (default `true`), so one package can render in several places.
  Re-declaring the primary surface is allowed only with the same
  entrypoint as the top-level pair.
- The `dashboard` surface may add a `size` hint (`compact`,
  `standard`, or `wide`) and a short `category` grouping label.
  Both are hints; the user's persisted dashboard arrangement wins.
- The `desktop` surface may add geometry hints: `width`, `height`,
  `minWidth`, `minHeight` (80 to 1600 logical pixels), `resizable` and
  `anchor` (one of nine start positions).
- `capabilities` discloses `processCommands` (exact executable
  basenames), `networkHosts`, `providers`, typed `settings`, and the
  optional broker `actions` list. Under-declaring a process, host or
  provider your code actually uses is a review failure.
- Optional `translations` and `marketplace` blocks are covered
  below.

### Surface types

| Surface | Where it renders |
| --- | --- |
| `bar` | The bar end group; open richer panels with `UiPopover` |
| `dashboard` | A card in the dashboard Extensions tab |
| `desktop` | A desktop widget on each display |
| `background` | Headless; declare it only where it is justified |
| `launcher` | A hidden query and result entry in the launcher |
| `settings` | A custom tab in Control Center, beside the generated UI |

The launcher contract is a root `Item` with a settable string `query` and a
read-only `result` of the form `{ ok, text }`. The prefix is the plugin id
without a leading `hornero-`, and activating a result copies its text. The
`settings` surface sits next to the generated settings UI, which already
renders `capabilities.settings` without it. Both run in-process with the
same trust as every other surface.

### Host context and responsive layout

The same extension must render in a horizontal bar, a vertical
rail, a dashboard card, and a desktop widget. Declare any of the host
context properties on your entrypoint root item — orientation,
edge, surface, available width and height, compact flag, and screen
name — and the host keeps them bound to the real surface. Declaring
none changes nothing. Give the properties defaults that match your
current layout, honour the available-size caps instead of hardcoding
sizes, and let the PluginKit stack layout component stack controls on
narrow or vertical surfaces. Exact property names, types, and
per-surface caps are in the [shell contract][shell-plugins].

## The Signal Theme

`Theme` carries exactly the shell's Signal tokens, under the same names the
shell uses. Never hardcode a colour, font, size or duration.

- **Colour roles**, `Theme.palette.<role>`: surfaces `ground`, `sunken`,
  `base`, `panel`, `raised`, `lifted`; text `ink`, `inkMuted`, `inkFaint`;
  lines `rule`, `ruleStrong`, `focus`; accents `signal` (amber), `cue`
  (celeste), `phosphor` (green) and `alert` (red), each with its `on…` and
  `…Well` companions; plus `inverse`, `scrim`, `shadow` and `glow`.
- **Type**, `Theme.font.family.sans`, `.mono` and `.display` (IBM Plex Sans,
  Mono and Sans Condensed), and `Theme.font.size.<small…display>`.
- **Shape and rhythm**: `Theme.rounding.small`, `.normal`, `.large`;
  `Theme.spacing.*`; `Theme.padding.*`.
- **Motion**: `Theme.duration(name)`, `Theme.anim.curves.*`,
  `Theme.motionLevel` and `Theme.reducedMotion`; see the
  [interaction contract](interaction-contract.md).
- **State**: `Theme.light`, `Theme.highContrast`, `Theme.experience`
  (the active [experience mode](../desktop/experience-modes.md)),
  `Theme.glowEnabled`, `Theme.scanlines`, `Theme.telemetryIntervalMs` and
  `Theme.keyboardFocus`.

The language is deliberate. `signal` means *live, active or primary* and
`cue` means *focus, selection or information*. Numbers use tabular figures.
Panels are `panel` with a 1 px `rule` border and a small radius, never pills
or glass. `inkFaint` is decorative only. Nothing blinks or pulses, and glow
is never drawn by hand: instrument components apply it, only while
`Theme.glowEnabled` holds.

### Hornero Glyphs

Icons are **Hornero Glyph names**: the curated Tabler outline subset bundled
with the shell, kebab-case, for example `wifi`, `clock`, `calculator`,
`wave-sine` or `player-play`. They are used by `UiIcon { name }`,
`glyph` on buttons, rows, chips, cards and detail rows, a launcher
provider's `icon`, and the third argument of `Notifications.toast()`.
Glyphs are outline-only, so there is no fill axis; show state with colour or
an on-air chip. The validator checks names against the vendored list
(`schema/hornero-glyphs.names` in the plugins repository) and rejects
unknown and Material-style names before install. At runtime an unknown name
renders nothing. Ask for a missing glyph in a Shell issue rather than
shipping an icon font.

## PluginKit at a glance

The shell package installs the stable `Hornero.PluginKit` QML
module so extensions never import shell internals:

```qml
import QtQuick
import Hornero.PluginKit
```

- **Your own state:** `Settings` (typed values declared in the
  manifest), `Translations` (your package catalogs), and `Desktop`
  (read-only widget state).
- **Look and feedback:** `Theme` (above) and `Notifications.toast()` for a
  bounded in-shell toast. A toast is not a persistent desktop
  notification.
- **Data facades:** `System`, `Network`, `Media`, `Weather`, `Time`,
  `Power`, `Audio` and `Workspaces`, plus the shared history `Telemetry`
  for instruments. They are read-only except media transport, audio
  volume and mute, and workspace focus, which belong in user-initiated
  handlers only. There is no process or shell execution in PluginKit,
  and no AI quota is exposed: never display an assumed quota value as
  known.
- **UI primitives:** text, eyebrow, icon, card, well, button, toggle,
  slider, metric, detail row, action row, chip, progress, state
  placeholder, tooltip, popover and the adaptive stack, plus the
  instrument components `UiSegmentMeter`, `UiMeterRow`, `UiSparkline`,
  `UiScope` and `UiPartition`. They use `Theme` tokens, declare accessible
  names and show visible focus.

Exact properties and methods live in the
[shell contract][shell-plugins]. Build against that page and the
installed module, not against this summary.

### Providers and permissions

Facades are presentation over shared, single-instance **providers**: one
shell-owned source per domain, so many extensions reading the same domain
never duplicate its timers, file reads, or child processes. Two rules:

- **Declare what you read.** List every domain in
  `capabilities.providers` (`system`, `network`, `spectrum`, `weather`,
  `media`, `time`, `power`, `audio`, `workspaces`). The validator rejects a
  facade or subscription whose domain the manifest does not declare. Like
  every capability this is disclosure for review, not enforcement.
- **Lease polling domains.** `system` and `network` are the polling
  domains; `spectrum` is a stream. Hold a `Subscription { domain: "…" }`
  while your surface is loaded. Each polling domain owns one timer gated on
  a reference count, so ten subscribers cost one. The cadence follows the
  active experience (1 Hz, 2 Hz in Signal). In Focus and Gaming the desktop
  layer loads no widget, so every lease is released.

`weather` is cached (one shared fetch per location, hourly); `media`,
`time`, `power`, `audio` and `workspaces` are event-driven. Values are never
invented: a missing sensor reports an availability flag of false
(`System.cpuTempAvailable`, `Power.hasBattery`, …), and you render
"unavailable", never zero. With no lease, polling stops and reads return
last-known values. Prefer a facade signal or `Subscription` over your own
sub-second timer.

### Desktop widgets and the Signal deck

A `desktop` surface is a widget on each display's desktop layer. The host
owns the **module**: `panel` fill, 1 px `rule` border, shadow and an
eyebrow header (`02 · SYSTEM INSIGHT`). Your root item may declare
`widgetTitle` and `widgetContext` for that header, and draws only its
content in the host box (`hostAvailableWidth` by `hostAvailableHeight`).
Inside a widget, `UiCard` draws no second frame.

People move and resize widgets in edit mode (`qs ipc call plugins
editDesktop`), snapped to an 8 px grid and stored per display. Plugin code
can read geometry through `Desktop` but has no setter. Widgets live below
windows and never take keyboard focus from applications.

What the desktop layer holds depends on the
[experience mode](../desktop/experience-modes.md). Everyday and Studio show
the widgets the person enabled; Signal shows the curated six-instrument
**deck** (System Insight, Network Scope, Audio Deck, Calendar, Agenda and
Moon Phase), loaded from installed first-party packages whose payload is
trusted, without enabling them in Extensions; Focus and Gaming load none.
Build instruments from `Telemetry` windows and `UiScope`, `UiSparkline`
and `UiSegmentMeter`, and let the host apply glow: traces borrow from one
shell-wide budget of three items.

## Settings schema

Declare settings once, under `capabilities.settings`, keyed by
camelCase IDs. Each declaration is a `type` plus a `default`, with
an optional user-facing `description` and the constraints for its
type:

| Type | Constraints | Generated control |
| --- | --- | --- |
| `boolean` | — | Switch |
| `integer` | `minimum`, `maximum` | Spin box (+ slider if bounded) |
| `number` | `minimum`, `maximum` | Spin box (+ slider if bounded) |
| `string` | `minLength`, `maxLength` | Text field |
| `enum` | `options` (required) | One toggle button per option |

The type set is closed. There is deliberately no path type:
settings are plain shell-owned values, never filesystem paths the
shell opens. Control Center generates one validated,
keyboard-accessible field per declared setting, with per-field
reset and a confirmed reset-all, reading and writing the same
storage as the PluginKit `Settings` component. Declare settings
and stop there; you do not need settings code. A custom `settings`
surface is optional and appears next to the generated UI.

Updates never rewrite stored values. A stored value is re-validated
against the current declaration on every read: one that still
satisfies its declaration keeps working, and anything else (a
changed type, a removed enum option, a tightened range) reads as
the declared default instead of being coerced or crashing.
Renaming a key creates a new setting with its own default.

## Translations

A package ships its own translations as plain JSON catalogs, with
no build step. Declare the source locale (the language written in
your QML), the locales you ship, and optionally a directory
(default `translations`). Each catalog is a flat
`<directory>/<locale>.json` object mapping source strings to
translations, and every catalog must be listed in `files`.

Read strings through PluginKit `Translations`, keep whole sentences
as single translatable units with `%1`-style placeholders, and
format dates and numbers through its locale-aware formatters.
Resolution follows the shell (system) locale, tries the full tag
then its language, and otherwise falls back to the source strings.
A missing or malformed catalog degrades to source text; it never
fails the extension. Two rules surprise authors coming from shell
code:

- Do not use `qsTr()` in extension QML. The shell installs no Qt
  translator for extensions, so it would never translate; the
  validator rejects it. Compiled `.qm` catalogs are rejected too.
- A declared locale must be complete for literal strings: every
  literal passed to the translation call needs a non-empty entry
  with the same placeholders in every declared catalog. Design for
  text expansion instead of fixed widths; the organization-wide
  baseline is [English-first](i18n.md).

## Accessibility and keyboard contract

Extension UI follows the same rules as native shell UI. Using the
PluginKit controls gets the contract for free; hand-rolled
interactive items must provide it themselves. The popup, Escape and
motion rules are in the [interaction contract](interaction-contract.md).

- Every interactive control exposes an accessible name and role.
  Give icon-only or ambiguous controls an explicit name, and always
  name a slider after what it adjusts.
- Tab order is declaration order, one tab stop per control, and
  disabled controls are not tab stops. Enter, Return, and Space
  activate; slider arrows, page keys, Home, and End follow the kit
  behavior.
- Escape dismisses the innermost transient first: tooltip, then
  popover, then the surface underneath. Closing a popover returns
  focus to its trigger; never leave focus on a hidden item.
- Focus must be visible. Use the kit controls or draw an equally
  visible indication with `Theme.palette.focus`; hover styling alone
  is not focus.
- Reduced motion and high contrast are inherited from the host.
  Route your own animation durations through `Theme.duration(...)`.
- A mouse-only click with no keyboard path is a contract
  violation. The shell validator prints an accessibility warning
  for mouse-only actions, and reviewers treat new warnings as
  blocking.

## Marketplace metadata

An optional `marketplace` block lets Control Center describe a package
without executing its code: static `screenshots` (plain `.png`, `.jpg`,
`.jpeg`, or `.webp` images shipped in `files`, with accessible `alt` text), a
`compatibility` shell-version range, a newest-first `changelog`, and a
`deprecation` notice with an optional replacement ID. The detail view also
explains the declared capabilities in plain language next to the raw
declarations, and the Extensions pane shows compatibility and maturity
chips.

Honest limits matter when you write this metadata:

- A not-yet-installed catalogue entry has no local payload, so its
  screenshots appear as captions only. Images render after the
  package is installed.
- `compatibility` is shown to users; it does not stop an
  out-of-range package from loading.
- Deprecation warns and stops offering new installs of that
  catalogue entry. It never disables or removes an installed copy,
  and rollback stays on the existing verified CLI contract, not on
  this metadata.
- Screenshots must be real captures of the running shell.
  Generated art must be labelled artwork, never presented as a
  capture.

## Lifecycle

The CLI owns install, update, trust, enable, disable, and remove.
The shell discovers packages the CLI reports as installed and
enabled, and Control Center is a narrower surface: it can trust
and enable with explicit confirmation, while install, update, and
remove remain CLI actions. Read exact flags from CLI help; the
handbook command page is tracked in [HorneroOS/docs#45][docs-45].
The stable shape every author and user can rely on is:

1. **Scaffold** outside the catalogue with `horneroctl plugin new`, or
   copy the starter template in the plugins repository for a
   first-party submission. Check the scaffold against the current
   schema version before you start.
2. **Validate** the package directory statically before anything
   installs it (see [Validate and test](#validate-and-test)).
3. **Install** copies inert package data only. Nothing loads and
   nothing runs (`horneroctl plugin install-local` for a local
   directory, `horneroctl plugin catalog` for the official catalogue).
4. **Trust** records explicit trust for the current payload where
   reviewed provenance does not already apply. A payload change
   invalidates recorded trust, and consent is required again.
5. **Enable** (`horneroctl plugin enable`) revalidates the installed
   payload first; on failure the extension stays disabled. Only enabled
   extensions load.
6. **Load** instantiates each enabled surface in its own `Loader`,
   so one failure is confined to that extension. Load state,
   diagnostics, and a per-extension reload are visible in Control
   Center and through the shell's plugin status IPC.
7. **Disable** unloads the extension and releases its provider
   leases. **Remove** deletes the receipt-owned package. Catalogue
   update keeps the previous payload so the CLI rollback path can
   restore it.

The official catalogue is browsed and installed through the CLI catalogue
commands, with the payload SHA-256 and pinned revision verified from the
plugins repository catalogue before anything is copied. The community
listing is read-only: the shell displays entries only after the CLI
verifies the detached registry signature, it fails closed when the key,
signature, index, or verification tool is unavailable, and a verified
signature proves publication by that registry, not that HorneroOS reviewed
the code. The community pane does not install, update, enable, or roll
back entries.

One operational warning from the shell contract: merged shell
changes reach a live session only through the packaged shell. A
git checkout is not what a running session executes unless
Quickshell was started with that config explicitly, so check which
config your session runs before blaming an extension for stale
host behavior.

## The official catalogue

The `HorneroOS/plugins` catalogue lists **36 official extensions**, every
one a PluginKit 3 package with trust `official` (reviewed by HorneroOS
maintainers, pinned by commit and SHA-256, still unsandboxed). By primary
surface:

- **Desktop widgets (6):** Agenda, Audio Deck, Calendar, Moon Phase,
  Network Scope, System Insight. These six form the Signal deck. Calendar
  and Agenda show date facts and the month; they have no event data
  because PluginKit has no calendar source, and say so.
- **Bar (18):** Base Converter, Battery, Calculator, Color Converter, Date
  Calculator, Countdown, Dual Clock, JSON Tools, Metronome, Microphone,
  Now Playing, Pomodoro, Stopwatch, Studio Audio, Text Tools, Unit
  Converter, Uptime and Volume.
- **Dashboard (12):** AI Usage, Disk Usage, Focus Card, Network Monitor,
  Quick Notes, Quiet Notes, Studio Jobs, Sun Card, System Health, System
  Monitor, Weather and World Clock.

Several packages add a second surface (for example a dashboard card or a
launcher entry for the converters and calculators). Use
`horneroctl plugin catalog --json` for the live list, with each entry's id,
version, category, declared capabilities and payload hash. The catalogue
index is generated and never edited by hand.

## Performance expectations and safe mode

Performance budgets are advisory diagnostics, never enforcement:
in-process QML cannot be preempted, so exceeding a budget is
flagged, not punished.

- A load that takes over 2000 ms from discovery or reload to
  loaded/failed is flagged as a slow load.
- Five or more load attempts within 60 seconds are flagged as
  load churn.
- The validator warns (never fails) on a literal `Timer` interval
  below 1000 ms, because extension-internal timers are not
  observable at runtime. Sub-second polling is your smell to fix.
- Load failures and reloads are kept in a bounded diagnostics log
  with credential-looking values redacted before they are stored
  or shown. Diagnostics never need to carry secrets.

Author to the budget anyway: subscribe to shared providers instead
of rolling your own polling, keep entrypoints small, and let
dashboard cards load asynchronously. When an extension makes the
shell unusable, safe mode is the recovery path: started with safe
mode on, the shell parses no extension manifest and instantiates
no extension QML, so the (core shell) Extensions pane stays
reachable to disable the broken package. Safe mode itself never
enables, disables, or removes anything, and it does not sandbox a
plugin that is running normally.

## Worked example: a two-surface clock

This complete package is a manifest v3 clock: a primary `bar` surface
that drops its weekday on compact surfaces, a `dashboard` card over the
shared `system` provider, one typed setting rendered by the generated
settings UI, and a Spanish catalog. It declares no process, network, or
broker capability. It is modelled on the shell's reference packages
(`examples/plugins/example-clock` and `examples/plugins/example-multi-surface`
in the shell repository). The shell validator passed on this exact file set
at Shell commit `8cab8d0`; that is a static pass, not a render.

### `manifest.json`

```json
{
  "schemaVersion": 3,
  "id": "example-worked-clock",
  "name": "Example Worked Clock",
  "version": "1.0.0",
  "description": "PluginKit 3 example: bar clock plus dashboard card.",
  "author": "Example Author",
  "license": "MIT",
  "entrypoint": "Main.qml",
  "placement": "bar",
  "surfaces": {
    "dashboard": {
      "entrypoint": "Dashboard.qml",
      "size": "standard",
      "category": "Examples"
    }
  },
  "translations": {
    "sourceLocale": "en",
    "locales": ["es"],
    "directory": "translations"
  },
  "files": [
    "Main.qml",
    "Dashboard.qml",
    "README.md",
    "LICENSE",
    "translations/es.json"
  ],
  "capabilities": {
    "processCommands": [],
    "networkHosts": [],
    "providers": ["time", "system"],
    "settings": {
      "twentyFourHour": {
        "type": "boolean",
        "default": true,
        "description": "Show the time in 24-hour format instead of 12-hour AM/PM."
      }
    }
  }
}
```

### `Main.qml` (primary bar surface)

```qml
import QtQuick
import Hornero.PluginKit

Item {
    id: root

    // Host context: declaring a property opts in to the host
    // keeping it bound to the real surface.
    property bool hostCompact: false

    implicitWidth: label.implicitWidth + Theme.spacing.small * 2
    implicitHeight: label.implicitHeight

    Settings {
        id: pluginSettings
        pluginId: "example-worked-clock"
    }

    Translations {
        id: i18n
        pluginId: "example-worked-clock"
    }

    // A real UiButton, not a mouse-only MouseArea: tab stop,
    // Enter/Space activation, visible focus and an accessible
    // description come from PluginKit. Time.date updates every
    // second, so no Timer is needed.
    UiButton {
        id: label
        anchors.centerIn: parent
        variant: "quiet"
        glyph: "clock"
        text: i18n.formatDateTime(Time.date,
            pluginSettings.value("twentyFourHour", true)
                ? (root.hostCompact ? "HH:mm" : "ddd, HH:mm")
                : (root.hostCompact ? "h:mm ap" : "ddd, h:mm ap"))
        tooltipText: i18n.tr("Clock details")
        onClicked: Notifications.toast(
            i18n.tr("Worked Example Clock"),
            i18n.tr("Today is %1").arg(
                i18n.formatDateTime(Time.date, "dddd, d MMMM")),
            "clock")
    }
}
```

### `Dashboard.qml` (dashboard surface)

```qml
import QtQuick
import Hornero.PluginKit

UiCard {
    title: i18n.tr("Worked Example")
    channel: "01 · CLOCK"

    // The lease keeps the one shared system timer live while this
    // card is loaded; it creates no timer of its own.
    Subscription { domain: "system" }

    Settings {
        id: pluginSettings
        pluginId: "example-worked-clock"
    }

    Translations {
        id: i18n
        pluginId: "example-worked-clock"
    }

    UiMetric {
        label: i18n.tr("Current time")
        value: i18n.formatDateTime(Time.date,
            pluginSettings.value("twentyFourHour", true)
                ? "HH:mm" : "h:mm ap")
    }
    UiMeterRow {
        label: i18n.tr("CPU")
        value: System.cpuPerc
        valueText: Math.round(System.cpuPerc * 100) + "%"
    }
}
```

### `translations/es.json`

Every literal string above appears once, placeholders preserved:

```json
{
  "CPU": "CPU",
  "Current time": "Hora actual",
  "Today is %1": "Hoy es %1",
  "Worked Example": "Ejemplo completo",
  "Clock details": "Detalles del reloj",
  "Worked Example Clock": "Reloj del ejemplo completo"
}
```

### `README.md` and `LICENSE`

The README says what the package does, how to validate and install
it, and repeats the trust note. Keep it honest:

```markdown
# Example Worked Clock

A PluginKit 3 example: a bar clock plus a dashboard card over the shared
`time` and `system` providers, one typed setting, and a Spanish catalog.
It starts no processes and contacts no network hosts.

Quickshell QML is not sandboxed and runs with your user permissions.
Validation is a review aid, not a security guarantee. Read the source
before enabling any extension.
```

Ship the full text of your chosen license as `LICENSE` (this
example uses MIT, matching the manifest `license` field).

### Validate the example

From a shell repository checkout, point the checker at the package
directory (see [Validate and test](#validate-and-test) for the CLI
equivalent and what a pass does and does not prove):

```sh
python3 scripts/validate_plugin.py path/to/example-worked-clock
```

Expected: a pass line for the package, with the standing notice
that validation is a static review aid and Quickshell plugins are
not sandboxed.

## Migrating from PluginKit 1 and 2

Porting is mechanical because the validator rejects every removed name
with its replacement. The full table is in the
[shell contract][shell-plugins]; the shape of it:

1. Set `"schemaVersion": 3` and declare `capabilities.providers`.
2. Colours move to roles: `Theme.primary` to `Theme.palette.signal`,
   `secondary` to `cue`, `tertiary` and `success` to `phosphor`, `error`
   to `alert`, surfaces to `base`, `panel`, `raised` and `lifted`, and
   `onSurface` to `ink`.
3. Tokens become groups: `Theme.spacing.small`, `Theme.rounding.normal`,
   `Theme.font.family.sans`, `Theme.font.size.*` and
   `Theme.duration("medium")`.
4. Icons become Hornero Glyph names: `UiIcon { icon }` to `name`,
   `iconName` to `glyph`, with no fill axis.
5. Variants: `ghost` becomes `quiet`; `tonal` and `outlined` become
   `secondary`; chip tone `primary` becomes `signal` and `error` becomes
   `alert`. There are no ripples.

## Validate and test

Run every gate that applies to where the package will live.
None of them renders your extension:

1. **Shell checker** (any package): the validator script named
   above, run against the package directory from a shell checkout.
   The CLI's plugin validation command runs the same contract and
   is the one to use on an installed system; read its exact form
   from CLI help.
2. **Plugins catalogue gate** (first-party submissions): the
   plugins repository validator checks every catalogue package,
   the provenance inventory, and the quality audit, and CI checks
   the generated catalogue is fresh and that no legacy manifest
   passes. Catalogue payloads and the generated index are committed
   in separate steps; follow [`docs/DEVELOPING.md`][plugins-developing]
   for that flow.
3. **A real shell**: install inert, enable with consent, then
   confirm the extension appears in the shell's plugin status IPC
   and exercise every surface, setting, and keyboard path by hand.
   A validator pass plus an IPC listing prove loading, not that
   the UI is correct, accessible in use, or cheap at idle.
4. **The QA virtual machine** for anything visual: the QA repository
   runs a disposable guest and records captures. Record where each
   check ran (offscreen, virtual machine or host).

Tell reviewers which of these you actually ran. "Validated" must
never be written as "tested on a desktop" when only static gates
ran.

## Quality gate

The first-party catalogue carries a maintained per-extension
quality audit in the plugins repository. Each official extension
is classified (`premium-ready`, `needs-upgrade`, `consolidated`,
or `deprecated-with-replacement`) and scored on tooltips,
accessibility, translation, settings, theme tokens, orientation,
loading/error states, performance, and screenshots. Dimensions a
script can decide are probed from the payload and the audit must
match the probe exactly, so the audit cannot over-claim or
silently go stale. `premium-ready` additionally requires a
recorded graphical review. Failing or unverified dimensions are
warnings by default and errors in the gate's strict mode.

Current state, stated plainly: all 36 catalogue extensions are
classified `needs-upgrade`, and the audit says in its own disclaimer that
it is static and not graphical acceptance. Treat "premium" in this guide
as the bar to author to — PluginKit primitives, typed settings,
translations, accessible names, Signal tokens, shared providers, honest
capability declarations — not as a status any shipped extension has been
certified with.

## Author checklist

- Manifest v3 with exact `files`, a README, and a license file; no
  binaries, symlinks, or executable bits.
- Every process, host, provider, setting, and broker action your code
  uses is declared; nothing is under-declared.
- UI built from PluginKit primitives and `Theme.palette` roles, Hornero
  Glyph names and no Material-era names, with accessible names, visible
  focus, and a keyboard path for every pointer action.
- Host context honoured; no hardcoded colors, durations, or
  surface sizes; layout survives compact and vertical surfaces.
- Popups use `UiPopover` and `UiTooltip`; motion collapses at the `off`
  level; nothing animates at idle.
- Data read through shared providers with a subscription lease;
  no sub-second timers and no per-extension polling; unavailable sensors
  shown as unavailable.
- User-visible strings through `Translations`, with a complete
  catalog for every declared locale and locale-aware formatting.
- Marketplace metadata, when present, uses real captures.
- Shell validator passes; catalogue gate passes for first-party
  submissions; live-shell and virtual-machine exercise recorded
  separately from static results.

## References

- [Shell extension contract][shell-plugins]: manifest, PluginKit,
  Theme, surfaces, settings, translations, providers, desktop widgets,
  diagnostics.
- [Manifest JSON schema][shell-schema]: the closed field contract.
- [Plugins developing guide][plugins-developing],
  [contributing guide][plugins-contributing], and
  [security model][plugins-security]: catalogue workflow,
  provenance, quality gate, and signing context.
- [Interaction contract](interaction-contract.md),
  [Signal Visual Language](signal-visual-language.md) and
  [RFC 0001](rfc-0001-hornero-signal.md) in this handbook.
- [Testing](testing.md) and [Internationalization](i18n.md) in this
  handbook.
- [HorneroOS/docs#45][docs-45]: the pending handbook page for the
  CLI plugin and assistant command families.

[shell-plugins]: https://github.com/HorneroOS/shell/blob/main/docs/PLUGINS.md
[shell-schema]: https://github.com/HorneroOS/shell/blob/main/schemas/plugin-manifest.schema.json
[plugins-developing]: https://github.com/HorneroOS/plugins/blob/main/docs/DEVELOPING.md
[plugins-contributing]: https://github.com/HorneroOS/plugins/blob/main/docs/CONTRIBUTING.md
[plugins-security]: https://github.com/HorneroOS/plugins/blob/main/docs/SECURITY.md
[docs-45]: https://github.com/HorneroOS/docs/issues/45
