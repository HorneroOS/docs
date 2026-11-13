# Extensions 2.0: authoring guide

**Development.** Hornero Shell extensions are QML packages the shell
discovers, loads in their own `Loader`, and renders on the bar, the
dashboard, or the desktop. This page is the handbook entry point for
extension authors: it states what shipped, what is declaration-only,
and what is not yet verified on a live desktop. It is not the API
reference.

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
- Command-line lifecycle: the CLI's own help for the plugin command
  family. The handbook page for those commands is tracked separately
  in [HorneroOS/docs#45][docs-45]; until it lands, treat CLI help as
  authoritative and this page as a summary.

Where a linked guide and this page disagree, the shell contract wins
for manifest and PluginKit behavior, and CLI help wins for command
syntax. The plugins repository guide predates some manifest v2
additions, so do not use it alone to decide whether a v2 field is
accepted.

## Read the trust model first

Extension QML runs **in-process inside Quickshell with the logged-in
user's permissions. It is not sandboxed.** No manifest field changes
that:

- `capabilities` (`processCommands`, `networkHosts`, `settings`, and
  the broker `actions` list below) are review disclosures shown
  before consent. They are not an operating-system permission grant
  and the shell does not enforce them against running QML.
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

Extensions 2.0 landed across the shell extension series (manifest
v2, PluginKit UI primitives, host context, typed settings,
accessibility contract, localization, shared providers, dashboard
layout, marketplace metadata, diagnostics and safe mode), the CLI
broker and manifest v2 lifecycle support, and the first-party 2.0
plugin families in the plugins catalogue. Be precise about the
edges:

| Area | State |
| --- | --- |
| `background`, `bar`, `dashboard`, `desktop` | Hosted |
| `launcher` surface | Declaration only, never loaded |
| `settings` surface (custom UI) | Declaration only, never loaded |
| Generated settings UI | Hosted in Control Center |
| Screenshots, installed package | Shown, no plugin code runs |
| Screenshots, not yet installed | Caption only, no local image |
| Marketplace `compatibility` | Review metadata, gates nothing |
| Community catalogue pane | Read-only; lifecycle stays in CLI |
| Community registry product key | Not shipped; fails closed |
| Per-user per-surface toggles | Not part of the contract yet |

Declaring a `launcher` or `settings` entrypoint today causes no code
to run. Do not document, advertise, or depend on those surfaces as
features until their hosts ship. The generated settings UI needs no
`settings` surface at all.

### Not yet verified on a live desktop

The contracts below are covered by unit, host, schema, and offscreen
QML tests in the shell, CLI, and plugins repositories. That is not
the same as graphical acceptance, and this page does not claim it:

- Host-context layout across bar edges, displays, and output scales
  is contract-tested, not yet verified in a live multi-monitor
  compositor session.
- Keyboard behavior is driven by an offscreen QML probe. Live
  compositor focus grabs and screen-reader (AT-SPI) announcements
  still need a running session to verify.
- The shared-provider idle-cost argument is static analysis pinned
  by tests, not a host power or wakeup measurement.
- The first-party quality audit (see
  [Quality gate](#quality-gate)) currently classifies every
  catalogue extension as needs-upgrade, with screenshots missing
  and orientation, loading/error states, and performance
  unverified. A merged 2.0 plugin family is shipped code, not a
  premium-ready or graphically accepted claim.

## Package shape

One directory per extension, containing exactly `manifest.json`
plus every file listed in the manifest `files` array:

- the declared QML `entrypoint` (and one entrypoint per additional
  surface in manifest v2),
- `README.md` and `LICENSE` for anything you distribute,
- translation catalogs and preview images, when declared.

Paths are package-relative and may not escape the package.
Symlinks, compiled binaries or bytecode, setuid/setgid bits,
world-writable files, and executable files are rejected. The
extension import surface is intentionally narrow: Qt Quick and
Quickshell public modules plus `Hornero.PluginKit`. Imports from
Hornero's internal implementation are rejected.

## Manifest v2

`"schemaVersion": 2` keeps every version 1 field with the same
meaning and adds one optional field, `surfaces`. Version 1 packages
keep working unchanged, and unknown fields, unknown surface names,
and unknown schema versions are rejected (only `1` and `2` exist).
The canonical field-by-field reference is the
[shell contract][shell-plugins] and the
[JSON schema][shell-schema]; the summary below is orientation.

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
- `capabilities` discloses `processCommands` (exact executable
  basenames), `networkHosts`, typed `settings`, and the optional
  broker `actions` list. Under-declaring a process or host your
  code actually uses is a review failure.
- Optional `translations` and `marketplace` blocks are covered
  below. Installing or enabling a v2 package also requires a CLI
  build that accepts schema version 2.

### Surface types

| Surface | Where it renders |
| --- | --- |
| `bar` | The bar end group; open richer panels with PluginKit `UiPopover` |
| `dashboard` | A card in the dashboard Extensions tab |
| `desktop` | A widget in one of nine named slots per display |
| `background` | Headless; declare it only where a headless part is justified |
| `launcher` | Nothing yet: declaration only, not loaded |
| `settings` | Nothing yet: declaration only, not loaded |

Desktop widget slots are chosen by the user in Control Center and
persist in the user's shell config. Plugin code can read the
current slot through PluginKit and has no setter for it. A new or
unrecognized display and malformed slot data fall back to
`bottom-right`.

### Host context and responsive layout

The same extension must render in a horizontal bar, a vertical
rail, a dashboard card, and a desktop card. Declare any of the host
context properties on your entrypoint root item — orientation,
edge, surface, available width and height, compact flag, and screen
name — and the host keeps them bound to the real surface. Declaring
none changes nothing, so older packages keep working. Give the
properties defaults that match your current layout, honour the
available-size caps instead of hardcoding sizes, and let the
PluginKit stack layout component stack controls on narrow or
vertical surfaces. Exact property names, types, and per-surface
caps are in the [shell contract][shell-plugins].

## PluginKit at a glance

The shell package installs the stable `Hornero.PluginKit` QML
module so extensions never import shell internals:

```qml
import QtQuick
import Hornero.PluginKit
```

- **Your own state:** `Settings` (typed values declared in the
  manifest), `Translations` (your package catalogs), and `Desktop`
  (the current desktop slot for a widget).
- **Look and feedback:** `Theme` semantic tokens (token names are
  the compatibility contract; never hardcode colors) and
  `Notifications.toast()` for a bounded in-shell toast. A toast is
  not a persistent desktop notification.
- **Read-only data facades:** `System`, `Network`, `Media`,
  `Weather`, `Time`, `Power`, and `Audio`. The only mutating facade
  calls are media transport and the audio volume/mute controls,
  and those belong in user-initiated handlers only. There is no
  process or shell execution in PluginKit, and no AI quota is
  exposed: never display an assumed quota value as known.
- **UI primitives:** text, card, button, toggle, slider, metric,
  chip, progress, state placeholder, tooltip, popover, and the
  adaptive stack layout. They use `Theme` tokens, declare
  accessible names, and show visible focus. Popovers and tooltips
  are host-owned: never create an independent top-level window for
  a bar panel, and never put essential information only in a
  tooltip.

Exact properties and methods live in the
[shell contract][shell-plugins]. Build against that page and the
installed module, not against this summary.

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
and stop there; you do not need settings code, and the declaration-
only `settings` surface is not how this UI is provided.

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

Shipped platform support is not a translated catalogue: first-party
extensions migrate onto this contract package by package, and the
quality audit records each package's translation state instead of
claiming blanket coverage.

## Accessibility and keyboard contract

Extension UI follows the same rules as native shell UI. Using the
PluginKit controls gets the contract for free; hand-rolled
interactive items must provide it themselves.

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
  visible indication with the theme focus token; hover styling
  alone is not focus.
- Reduced motion and high contrast are inherited from the host.
  Route your own animation durations through the theme helper and
  never hardcode colors or durations.
- A mouse-only click with no keyboard path is a contract
  violation. The shell validator prints an accessibility warning
  for mouse-only actions, and reviewers treat new warnings as
  blocking even though the warning does not fail older packages.

## Shared data providers

The seven data facades are presentation over shared,
single-instance providers: one shell-owned source per domain, so
many extensions reading the same domain never duplicate its
timers, file reads, or child processes. Declare interest with a
PluginKit subscription lease for the domain you read (`system`,
`network`, `weather`, `media`, `time`, `power`, or `audio`):

- `system` and `network` are the only polling domains. Each owns
  exactly one timer that runs at the shell's configured resource
  interval while at least one lease or shell surface references
  it, and stops at zero references. Ten subscribers cost the same
  wakeups as one.
- `weather` is cached: one shared fetch per configured location,
  refreshed hourly. `media`, `time`, `power`, and `audio` are
  event-driven and never polled.
- There is no per-extension rate or backoff to tune. A failed
  sample keeps the previous values and retries on the next shared
  tick; reading a facade without a lease returns last-known values
  (zeros before the first sample).
- Disabling or unloading an extension releases its leases, and one
  extension can never drive a shared gate negative for the others.

Prefer the declarative lease over the imperative provider calls,
and prefer a facade signal over your own sub-second timer.

## Marketplace metadata

An optional `marketplace` block (any schema version) lets Control
Center describe a package without executing its code: static
`screenshots` (plain `.png`, `.jpg`, `.jpeg`, or `.webp` images
shipped in `files`, with accessible `alt` text), a `compatibility`
shell-version range, a newest-first `changelog`, and a
`deprecation` notice with an optional replacement ID. The detail
view also explains the declared capabilities in plain language
next to the raw declarations.

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

1. **Scaffold** outside the catalogue with the CLI's plugin
   scaffolding command, or copy the starter template in the
   plugins repository for a first-party submission.
2. **Validate** the package directory statically before anything
   installs it (see [Validate and test](#validate-and-test)).
3. **Install** copies inert package data only. Nothing loads and
   nothing runs.
4. **Trust** records explicit trust for the current payload where
   reviewed provenance does not already apply. A payload change
   invalidates recorded trust, and consent is required again.
5. **Enable** revalidates the installed payload first; on failure
   the extension stays disabled. Only enabled extensions load.
6. **Load** instantiates each enabled surface in its own `Loader`,
   so one failure is confined to that extension. Load state,
   diagnostics, and a per-extension reload are visible in Control
   Center and through the shell's plugin status IPC.
7. **Disable** unloads the extension and releases its provider
   leases. **Remove** deletes the receipt-owned package. Catalogue
   update keeps the previous payload so the CLI rollback path can
   restore it.

Two catalogue flows complete the picture. The official catalogue
is browsed and installed through the CLI catalogue commands, for
example `horneroctl plugin catalog --json`, with the payload
SHA-256 and pinned revision verified from the plugins repository
catalogue before anything is copied. The community listing is
read-only: the shell displays entries only after the CLI verifies
the detached registry signature, it fails closed when the key,
signature, index, or verification tool is unavailable, and a
verified signature proves publication by that registry, not that
HorneroOS reviewed the code. The community pane does not install,
update, enable, or roll back entries.

One operational warning from the shell contract: merged shell
changes reach a live session only through the packaged shell. A
git checkout is not what a running session executes unless
Quickshell was started with that config explicitly, so check which
config your session runs before blaming an extension for stale
host behavior.

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

This complete package is a manifest v2 clock: a primary `bar`
surface that drops its weekday on compact surfaces, a `dashboard`
card over the shared `System` provider, one typed setting rendered
by the generated settings UI, and a Spanish catalog. It declares no
process, network, or broker capability. It is modelled on the
shell's reference packages (`examples/plugins/example-clock` and
`examples/plugins/example-multi-surface` in the shell repository),
and the file set below passes the shell validator as written.

### `manifest.json`

```json
{
  "schemaVersion": 2,
  "id": "example-worked-clock",
  "name": "Example Worked Clock",
  "version": "1.0.0",
  "description": "Manifest v2 example: bar clock plus dashboard card.",
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
    // keeping it bound to the real surface. The default keeps
    // the clock sensible before injection.
    property bool hostCompact: false

    implicitWidth: label.implicitWidth + Theme.spacingSmall * 2
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
    // Enter/Space activation, visible focus, and an accessible
    // description come from PluginKit. Time.date re-evaluates
    // the binding every second, so no Timer is needed.
    UiButton {
        id: label
        anchors.centerIn: parent
        variant: "ghost"
        text: i18n.formatDateTime(Time.date,
            pluginSettings.value("twentyFourHour", true)
                ? (root.hostCompact ? "HH:mm" : "ddd, HH:mm")
                : (root.hostCompact ? "h:mm ap" : "ddd, h:mm ap"))
        tooltipText: i18n.tr("Clock details")
        onClicked: Notifications.toast(
            i18n.tr("Worked Example Clock"),
            i18n.tr("Today is %1").arg(
                i18n.formatDateTime(Time.date, "dddd, d MMMM")),
            "schedule")
    }
}
```

### `Dashboard.qml` (dashboard surface)

```qml
import QtQuick
import Hornero.PluginKit

UiCard {
    // The lease keeps the one shared system timer live while
    // this card is loaded; it creates no timer of its own and
    // is released when the card unloads.
    Subscription { domain: "system" }

    Settings {
        id: pluginSettings
        pluginId: "example-worked-clock"
    }

    Translations {
        id: i18n
        pluginId: "example-worked-clock"
    }

    UiText { role: "title"; text: i18n.tr("Worked Example") }
    UiMetric {
        label: i18n.tr("Current time")
        value: i18n.formatDateTime(Time.date,
            pluginSettings.value("twentyFourHour", true)
                ? "HH:mm" : "h:mm ap")
    }
    UiMetric {
        label: i18n.tr("CPU")
        value: Math.round(System.cpuPerc * 100)
        unit: "%"
    }
    UiProgress { value: System.cpuPerc }
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

A manifest v2 example: a bar clock plus a dashboard card over the
shared PluginKit System facade, one typed setting, and a Spanish
catalog. It starts no processes and contacts no network hosts.

Quickshell QML is not sandboxed and runs with your user
permissions. Validation is a review aid, not a security guarantee.
Read the source before enabling any extension.
```

Ship the full text of your chosen license as `LICENSE` (this
example uses MIT, matching the manifest `license` field).

### Validate the example

From a shell repository checkout, point the checker at the
package directory (see [Validate and test](#validate-and-test)
for the CLI equivalent and what a pass does and does not prove):

```sh
python3 scripts/validate_plugin.py path/to/example-worked-clock
```

Expected: a pass line for the package, with the standing notice
that validation is a static review aid and Quickshell plugins are
not sandboxed.

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
   the generated catalogue is fresh. Catalogue payloads and the
   generated index are committed in separate steps; follow
   [`docs/DEVELOPING.md`][plugins-developing] for that flow.
3. **A real shell**: install inert, enable with consent, then
   confirm the extension appears in the shell's plugin status IPC
   and exercise every surface, setting, and keyboard path by hand.
   A validator pass plus an IPC listing prove loading, not that
   the UI is correct, accessible in use, or cheap at idle.

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

Current state, stated plainly: every catalogue extension is still
classified needs-upgrade, screenshots are missing across the
catalogue, and orientation, loading/error states, and performance
are unverified. Treat "premium" in this guide as the bar to author
to — PluginKit primitives, typed settings, translations,
accessible names, theme tokens, shared providers, honest
capability declarations — not as a status any shipped extension
has been certified with.

## Author checklist

- Manifest v2 (or v1 for a single surface) with exact `files`, a
  README, and a license file; no binaries, symlinks, or executable
  bits.
- Every process, host, setting, and broker action your code uses
  is declared; nothing is under-declared.
- UI built from PluginKit primitives and `Theme` tokens, with
  accessible names, visible focus, and a keyboard path for every
  pointer action.
- Host context honoured; no hardcoded colors, durations, or
  surface sizes; layout survives compact and vertical surfaces.
- Data read through shared providers with a subscription lease;
  no sub-second timers and no per-extension polling.
- User-visible strings through `Translations`, with a complete
  catalog for every declared locale and locale-aware formatting.
- Marketplace metadata, when present, uses real captures and does
  not promise behavior the hosts do not have yet (no launcher or
  custom-settings surface claims).
- Shell validator passes; catalogue gate passes for first-party
  submissions; live-shell exercise recorded separately from
  static results.

## References

- [Shell extension contract][shell-plugins]: manifest, PluginKit,
  surfaces, settings, translations, providers, diagnostics.
- [Manifest JSON schema][shell-schema]: the closed field contract.
- [Plugins developing guide][plugins-developing],
  [contributing guide][plugins-contributing], and
  [security model][plugins-security]: catalogue workflow,
  provenance, quality gate, and signing context.
- [Testing](testing.md) and
  [Internationalization](i18n.md) in this handbook.
- [HorneroOS/docs#45][docs-45]: the pending handbook page for the
  CLI plugin and assistant command families.

[shell-plugins]: https://github.com/HorneroOS/shell/blob/main/docs/PLUGINS.md
[shell-schema]: https://github.com/HorneroOS/shell/blob/main/schemas/plugin-manifest.schema.json
[plugins-developing]: https://github.com/HorneroOS/plugins/blob/main/docs/DEVELOPING.md
[plugins-contributing]: https://github.com/HorneroOS/plugins/blob/main/docs/CONTRIBUTING.md
[plugins-security]: https://github.com/HorneroOS/plugins/blob/main/docs/SECURITY.md
[docs-45]: https://github.com/HorneroOS/docs/issues/45
