# RFC 0003 — PluginKit contribution surfaces

- **Status** — Proposed (2026-11-17)
- **Implementation** — Partial. Section 12 states, per contribution point,
  what is merged, what is in review and what is not started. Nothing here is
  claimed as shipped unless Section 12 says so.
- **Amends** — [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md) §5b
  (PluginKit 3: surfaces, shared providers). Everything else stands.
- **Scope** — Shell (PluginKit, `Plugins` service, hosts, Control Center ›
  Extensions, `scripts/validate_plugin.py`, manifest schema), plugins
  (validator mirror, catalogue generator), horneroctl (no change: it
  delegates manifest validation to the Shell's validator)
- **Tracking** — [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)
  (mission), requirement K1/K2 in the mission matrix

## 1. Problem

PluginKit 3 (apiLevel 3) lets one package render on six places: bar item,
dashboard card, desktop widget, background, launcher provider and a custom
settings tab. That is a good start and it is not a platform:

1. A widget is **one instance per plugin**. Two clocks, two network scopes or
   two note cards with different settings are impossible, because geometry,
   anchor, settings and the load state are all keyed by the plugin id.
2. Settings are five scalar types. There is no colour, no list or
   multi-select, no multi-line text, no path, no grouping, no step or unit,
   and no way to see the effect of a change before leaving the pane.
3. An extension cannot add a Control Center panel, a quick-setting tile, a
   named action that a launcher row, a key binding or a script can invoke, a
   notification source or a lock-screen element. Those features are either
   hard-coded in the Shell or impossible.
4. There is no versioning story smaller than a schemaVersion break: adding a
   field today means old validators and hosts reject the package for an
   "unknown field", which is correct but gives the author nothing to target.

The product goal (user brief, 2026-11-17) is one of the most extensible Linux
desktops: a lean core and stable, reusable extension APIs rather than
hard-coded features, with everything customisable from Control Center
(AGENT-RULES §6).

## 2. Principles

1. **Contribute, don't patch.** An extension adds to a named surface through a
   typed contract. It never edits Shell files, never reaches Shell internals,
   and never needs a Shell release to appear.
2. **Declarative first, code second.** Whatever the Shell can show without
   running extension code (names, glyphs, settings, previews, action lists,
   tile metadata) is declared in `manifest.json`, validated statically and
   rendered without instantiating the package. Code is loaded lazily, per
   surface, only when that surface is on screen or invoked.
3. **One settings model.** Every surface of one instance reads the same typed
   settings; Control Center renders them; the user can reset any of them.
4. **Failure stays local.** A failed surface marks that surface of that
   instance failed. It never blocks the host, another instance, another
   extension or the recovery UI.
5. **Honest security.** QML runs in-process as the user and is not sandboxed
   (`docs/PLUGINS.md` › Trust boundary). This RFC does not pretend otherwise.
   It adds *consent and visibility* (what an extension contributes is listed
   and individually switchable) and *containment* (budgets, isolation of
   failure, safe mode); it adds no new way to run code outside the existing
   contract and no new privilege.
6. **Additive.** Nothing in apiLevel 3 changes meaning. A package that uses
   none of the new features is byte-for-byte unaffected.

## 3. Versioning and back-compatibility

- `schemaVersion` stays **3**. It versions the manifest *structure* (and
  Signal), and breaking it is reserved for a rewrite like the Material to
  Signal move.
- `PluginKitInfo.apiLevel` becomes **4** ("Platform"): the capability level of
  the installed kit. It is the single number the host compares.
- A new optional manifest field **`pluginKit`** (integer, default `3`) is the
  minimum apiLevel the package needs. The validator derives the level a
  manifest actually requires from the features it uses (Section 4 and 5) and
  rejects a manifest that uses a level-4 feature while declaring `pluginKit`
  below 4 or omitting it. Authors cannot under-declare.
- Host: `Plugins.requiredKitLevel` stays the floor for hosting anything (3).
  A package whose `pluginKit` exceeds the resolved `PluginKitInfo.apiLevel` is
  refused with the existing plain "update the hornero-shell package" message,
  as a per-package state (`failed`), not a global kit block.
- Old Shells (apiLevel 3) reject a manifest containing `pluginKit` as an
  unknown top-level field (existing "unknown fields are rejected" rule). That
  is the intended failure: the package is not installable where it cannot
  run, and `horneroctl` reports it through the Shell validator it already
  delegates to. The catalogue records the level per package so the registry
  can hide what a given Shell cannot run.
- Deprecation: a contribution point or field is marked deprecated for at least
  one apiLevel before removal; the validator warns, the host keeps working.
  No removal is planned.

## 4. The contribution-point matrix

"Surface" is where it appears; "Contract" is what the extension provides;
"Loaded" is when its code runs. Level is the apiLevel that introduced it.

- **1. `bar` (bar item)** — Surface: Bar island; Contract: `surfaces.bar`
  Item; host context; optional `section`; Loaded: Always while enabled;
  Multi-instance: Per screen (existing); Level: 3; Status: Shipped
- **2. Popover / popup** — Surface: Anchored to the bar item or widget;
  Contract: `UiPopover` / `UiTooltip` from the bar or desktop surface; not a
  surface of its own; Loaded: With its host surface; Multi-instance: Follows
  host; Level: 3; Status: Shipped
- **3. `desktop` (desktop widget)** — Surface: Desktop layer; Contract:
  `surfaces.desktop` Item, geometry hints; Loaded: While enabled and mode
  allows; Multi-instance: **Yes** (instances); Level: 3, instances 4; Status:
  Instances: this RFC
- **4. `dashboard` card** — Surface: Dashboard › Extensions; Contract:
  `surfaces.dashboard` Item, `size`, `category`; Loaded: While the dashboard
  is open; Multi-instance: Yes (instances); Level: 3, instances 4; Status:
  Instances: follow-up
- **5. `settings` section** — Surface: Control Center › Extensions; Contract:
  Generated from the typed schema; optional custom `surfaces.settings` Item;
  Loaded: While the section is expanded; Multi-instance: Per instance; Level:
  3; Status: Shipped; schema v2 level 4
- **6. `launcher` provider** — Surface: Launcher; Contract: `query` / `result`
  contract; Loaded: Hidden, while enabled; Multi-instance: No; Level: 3;
  Status: Shipped
- **7. `contributes.commands`** — Surface: Launcher rows, IPC, key bindings,
  scripts; Contract: Declared `{id, title, glyph, keywords}` plus a
  `surfaces.commands` handler `run(actionId, args)`; Loaded: Handler loaded on
  first invocation; Multi-instance: No; Level: 4; Status: This RFC
- **8. `contributes.quickSettings`** — Surface: Utilities quick toggles,
  Control Center overview; Contract: Declared tile `{id, title, glyph, kind}`
  plus a `surfaces.quickSetting` Item exposing `checked`/`state` and
  `toggle()`; Loaded: While the tile is placed; Multi-instance: No; Level: 4;
  Status: This RFC
- **9. `contributes.panels`** — Surface: Control Center nav (Extensions
  group); Contract: Declared `{id, title, glyph}` plus a `surfaces.panel`
  Item; Loaded: Only while the panel is open; Multi-instance: Per instance;
  Level: 4; Status: This RFC
- **10. Notification source** — Surface: Notification centre; Contract: A
  source id and a typed `post({summary, body, glyph, urgency, actions})`
  through PluginKit; grouped and DND-aware by the host; Loaded: Background;
  Multi-instance: No; Level: 5; Status: Designed, not started
- **11. Session / lock-screen slot** — Surface: Lock, greeter-adjacent
  surfaces; Contract: Read-only, declarative card (`UiMetric` subset) rendered
  by the host, never extension code on the lock surface; Loaded: Never on
  lock; Multi-instance: No; Level: 5; Status: Designed, not started; see 7.5
- **12. Hooks** — Surface: Shell events (mode change, lock, wake, workspace);
  Contract: Declared subscriptions delivered to `surfaces.background` as
  signals on a `Hooks` facade; Loaded: Background; Multi-instance: No; Level:
  5; Status: Designed, not started
- **13. Theme templates** — Surface: horneroctl theme apply; Contract:
  `theme.templates` (existing); Loaded: CLI only; Multi-instance: No; Level:
  3; Status: Shipped
- **14. `dashboardTab` page (shell#709)** — Surface: Dashboard top-level tab;
  Contract: `contributes.dashboardTabs` `{id, title, glyph}` plus a
  `surfaces.dashboardTab` Item; stable key `<pluginId>:<tabId>`, lazy
  failure-isolated Loader, `qs ipc call drawers dashboardTab <key>` deep
  link; Loaded: While the tab (or a neighbour) is selected; Multi-instance:
  No (max 2 pages per package); Level: 5; Status: Shipped (shell#710);
  first consumer `hornero-ai-usage` Agents page

Rationale for the order. Rows 3 and 5 (instances and the settings schema) are
the multiplier: every other contribution is more useful once an extension can
be configured per instance with real controls. Rows 7 to 9 are the three
smallest contracts that remove hard-coded features. Rows 10 to 12 need a
security review of their own and are deliberately not bundled.

### 4.1 Declared metadata: `contributes`

Row 7 to 9 contributions are declared in one optional manifest object so the
Shell, Control Center, the launcher and the catalogue can list them without
running code:

```json
"pluginKit": 4,
"contributes": {
  "actions": [
    { "id": "startFocus", "title": "Start focus session", "glyph": "player-play",
      "keywords": ["pomodoro", "timer"] }
  ],
  "quickSettings": [
    { "id": "focus", "title": "Focus timer", "glyph": "hourglass",
      "kind": "toggle" }
  ],
  "panels": [
    { "id": "stats", "title": "Focus statistics", "glyph": "chart-bar" }
  ]
},
"surfaces": {
  "actions":      { "entrypoint": "Actions.qml" },
  "quickSetting": { "entrypoint": "Tile.qml" },
  "panel":        { "entrypoint": "Panel.qml" }
}
```

Rules: ids match `^[a-z][a-zA-Z0-9]{0,31}$`, are unique per kind, at most 16
actions, 4 tiles and 4 panels per package; `title` at most 48 characters;
`glyph` must be a Hornero Glyph name (checked against the shipped name table);
every kind that is declared requires its surface entrypoint and vice versa.
All strings are plain text; none is interpreted as markup or a command.

### 4.2 Actions (launcher, IPC, key bindings)

- The registry lives in the `Plugins` service and is built from the
  *manifests only*: listing actions never runs extension code.
- Launcher: prefix `>` lists actions of enabled, installed extensions
  (title, glyph, extension name, fuzzy match on title and keywords).
  Activating one calls the handler.
- IPC: `qs ipc call plugincommands list` (JSON), `qs ipc call plugincommands run
  <pluginId> <commandId> [args]` (returns `ok`, or a one-line error). This is
  the stable surface for key binds (`bind = SUPER, F9, exec, qs ipc call
  plugins action hornero-pomodoro startFocus`) and scripts. The Shell does not
  write key bindings itself: the user owns the binding, Control Center shows
  the exact command to copy.
- Handler contract: `surfaces.commands` entrypoint is an `Item` with
  `function run(actionId: string, args: string): string` returning an empty
  string on success or a short error. The host loads the handler on first
  invocation and keeps it for the session, in its own asynchronous Loader. A
  throwing or slow handler affects only that call (the host reports the
  error as a toast and a diagnostic).
- Arguments are one plain string, at most 512 characters, never interpreted
  by the host.

### 4.3 Quick-setting tiles

- A tile is a small `Item` exposing `bool checked`, `string subtitle`,
  `bool busy` and `function toggle()`. The host draws the tile frame (same
  geometry and state layer as the built-in toggles); the extension owns only
  the state it reports and what `toggle()` does. This keeps one look and
  makes the tile accessible by construction (host-provided role and name).
- Placement is the user's: tiles from extensions appear in a picker in
  Control Center › Utilities and are **off by default**.

### 4.4 Control Center panels

- A panel is an `Item` shown inside Control Center under an "Extensions"
  group of the navigation rail, titled and glyphed from the manifest. It is
  loaded only while open and unloaded on leave, so it costs nothing when
  unused.
- A panel gets the standard host context (`hostSurface: "panel"`) and may
  use `Settings`, the data facades and the Ui kit. It cannot navigate or
  change other panes.

### 4.5 Session / lock-screen slots (design only)

Extension code is never instantiated on the lock surface: the lock screen is
a security boundary and one failing or hung plugin must not be able to affect
unlocking. A lock-screen contribution is therefore a **declared card** the
host renders (a title, a glyph, up to three metrics bound to a shared
provider domain), with no extension code on the lock surface. This is
Section 12 row 11.

## 5. Typed settings schema v2 (apiLevel 4)

The closed type set grows; the existing five types and their rules are
unchanged. New types and fields require `pluginKit: 4`.

- **`colour`** — Value: `#RRGGBB` or `#RRGGBBAA` string; Constraints: `alpha`
  (bool, default false); Generated control: Swatch with hex field and the
  Signal palette as presets
- **`list`** — Value: array of strings; Constraints: `options` (required, 1–32
  unique strings), `minItems`, `maxItems`; Generated control: Toggle group
  (multi-select), order preserved as declared
- **`text`** — Value: string, may contain newlines; Constraints: `minLength`,
  `maxLength` (≤ 4096), `rows` (1–12); Generated control: Multi-line text area
- **`path`** — Value: string; Constraints: `kind`: `file` or `directory`;
  `mustExist` (bool) is a UI hint only; Generated control: Text field with a
  Browse button; see 5.1

Fields available on **every** type (display only, never change validation):

- `title`: label shown instead of the key (≤ 48 characters).
- `group`: section heading the control is placed under (≤ 32 characters);
  groups render in first-declared order, ungrouped settings first.
- `unit`: a short suffix (`px`, `%`, `s`, `°C`, ≤ 8 characters) for numbers.
- `step` (`integer`/`number`): increment for the spin box and slider.
- `visibleWhen`: `{ "key": "<other setting>", "equals": <value> }`. The
  control is shown only when the referenced setting equals the value; the
  validator rejects unknown keys, self-references and cycles. It is UI only:
  a hidden setting keeps its value and remains readable by the extension.

### 5.1 `path` is a string, not a capability

A `path` setting stores a string the **Shell never opens**. Browsing uses the
Control Center file dialog, which is user-initiated. What extension code does
with the string is covered by the trust boundary (it runs as the user, and
`capabilities.processCommands` / the broker remain the disclosure and
enforcement points). Consequences encoded in the validator and the host:

- the validator requires a `path` default to be empty or a safe relative path
  (no leading `/`, no `~`, no `..`), so a package cannot ship a default
  pointing at `~/.ssh` or `/etc`;
- a `path` setting forces the extension card to show a "reads a path you
  choose" line in the permissions summary;
- stored values are re-validated on every read like any other setting.

### 5.2 Live preview

Control Center › Extensions shows, above the generated controls, a **preview
frame**: the extension's own surface (desktop widget, bar item or dashboard
card, in that order of preference) instantiated at its manifest size in a
host-owned frame, bound to the instance being edited. Because settings flow
through the shared `Settings` storage, every control change is visible
immediately, with no extension code written for it. The preview obeys the same
rules as the real surface (own asynchronous Loader, failure shown inline,
no preview in safe mode) and is only instantiated while the section is
expanded.

## 6. Per-instance configuration (apiLevel 4)

- An **instance** is one placed copy of a plugin's `desktop` widget (first
  step) or `dashboard` card (follow-up). The plugin always has an implicit
  *primary* instance with the empty instance id, which is exactly today's
  widget; nothing changes for users who add no instance.
- Extra instances are stored as `plugins.instances = { "<pluginId>": [
  { "id": "a1b2", "label": "Home" } ] }`. Instance ids match `^[a-z0-9]{1,8}$`
  and are generated by the Shell. At most 8 extra instances per plugin.
- The **instance key** is `<pluginId>` for the primary and
  `<pluginId>#<instanceId>` for the rest. Every per-instance record uses the
  key: `plugins.settings[key]`, `plugins.desktopWidgets[screen][key]`,
  `plugins.desktopWidgetSlots[screen][key]`. The primary key is the plugin id,
  so **no stored data is migrated**.
- A new instance can start from defaults or **duplicate** another instance's
  settings. Removing an instance deletes its settings, geometry and slot.
  Removing or disabling the plugin hides the instances without deleting them;
  uninstalling removes them (the lifecycle cleanup already used for settings).
- Plugin side: the host injects `hostInstanceId` (string, empty for the
  primary) with the other host-context properties, and `Settings` has a new
  `instanceId` property. An extension opts in with two lines:
  `property string hostInstanceId: ""` on its root and
  `Settings { pluginId: "..."; instanceId: root.hostInstanceId }`.
  Extensions that do not opt in still render once per instance but share the
  primary's settings; the Control Center says so ("This extension does not
  support separate settings per instance").
- Load state, diagnostics and the performance budget stay **per plugin**
  (the Loader failure of one instance marks the plugin, the error names the
  instance), because that is what `horneroctl` and safe mode act on.
- The Signal deck (`experience.deck`) is curated and keeps one instance per
  deck widget; instances apply to the user's own desktop widgets.

## 7. Capability and permission model

What exists today and stays: `capabilities.processCommands`, `networkHosts`
and `providers` are **review disclosures**, not enforcement; `capabilities
.actions` is checked by the horneroctl broker at call time; trust (payload
hash, receipt) and enable are explicit user steps in Control Center or the
CLI.

What this RFC adds, none of it a sandbox:

1. **Contribution consent.** Enabling an extension does not place it
   everywhere. Panels appear in the Extensions group (visible, removable by
   disabling), tiles are off until the user adds them, actions are listed but
   only run on a user gesture or an explicit IPC/key-binding call, and
   instances exist only when the user adds them. The enable dialog lists
   every contribution the package declares, so the user consents to the whole
   surface area at once.
2. **Disclosed data and system touchpoints.** `path` settings and each
   `contributes` kind are summarised on the extension card next to the
   existing disclosures.
3. **Containment.** Each surface of each instance has its own asynchronous
   Loader; failures are per surface; the existing load-time and churn budgets
   (`slow-load`, `load-churn`) apply per surface and are advisory; safe mode
   still instantiates nothing; handlers run on a user gesture only.
4. **No new code path.** Hosts load only manifest-listed `.qml` entrypoints
   through the same Loader and the same import allowlist. There is no
   `eval`, no new process API, no host-callable shell escape. The validator's
   static rules (imports, `Process`, shell metacharacters, glyph names) apply
   to every new entrypoint.
5. **Honest limits.** A hostile extension that you enabled can still do
   anything the user can. Out-of-process isolation (a per-extension
   Quickshell instance or a restricted subprocess with a typed bridge) is the
   real fix and is a separate RFC; the contribution contracts above are
   deliberately typed (scalar properties, `run(actionId, args)`) so that
   moving them behind such a bridge later does not change extension code.

## 8. Lifecycle

`discover → validate → (trust) → enable → surface activation → run → update
→ disable → remove`, driven by `horneroctl` (lifecycle owner) and the
`Plugins` service (state). Surface activation is lazy per row of Section 4:
background while enabled; bar, desktop and dashboard while their host is
shown; panel while open; handler on first invocation; tile while placed;
preview while the section is expanded. Updates apply without a shell restart
(entrypoint URLs carry the package version, existing behaviour); instances and
their settings survive updates and are re-validated against the new
declaration on read (migration rule of shell#374).

## 9. Error containment

- Manifest or settings declaration invalid: the package is refused with an
  actionable message by the validator (CLI) and, if one slips through, by the
  runtime normalisers, which drop the malformed declaration instead of
  failing the plugin.
- Loader failure: `Plugins.markFailed(id, detail, surface)` names the
  surface (extended with the instance key in the detail), bounded and
  redacted, visible in Control Center and `qs ipc call plugins status`.
- Action handler failure: toast plus diagnostic `action-failed`, never an
  unhandled exception in the launcher or IPC.
- A kit older than a package needs: that package `failed` with the update
  message; others are unaffected.

## 10. Hard-coded features to extract

Shell core stays lean only if first-party features use the same contracts.
Candidates, in the order they become safe (each is behaviour-preserving and
each needs the contribution point it names):

1. **Quick toggles registry** (`modules/utilities/cards/Toggles.qml`). The
   Shell's own toggles (Wi-Fi, Bluetooth, microphone, gaming, DND, VPN) become
   registered *internal* tiles read from the same registry that extension
   tiles use; the row renders the registry. No behaviour change, and the
   extension contract gets a real first consumer. Needs row 8.
2. **Dashboard Weather card** (`modules/dashboard/dash/Weather.qml`,
   `modules/dashboard/weather`). `hornero-weather` already ships in the
   catalogue and `Weather` is a PluginKit facade, so the card duplicates a
   first-party extension. Make it a default-enabled first-party extension
   with the Shell card kept only as the fallback when the extension is
   removed. Needs row 4 instances only if the user wants two locations.
3. **Idle inhibit and recording shortcuts** (`utilities/cards/IdleInhibit.qml`,
   `Record.qml`): actions plus tiles over existing Shell services. Needs rows
   7 and 8 and a typed facade for the two services.
4. **Calculator and similar launcher providers** are already extensions and
   are the reference for row 6.

Extraction happens only when the replacement is demonstrably identical in the
QA VM; until then the built-in stays. Section 12 records what was done.

## 10a. Catalogue API wishes, prioritised

The catalogue audit (plugins#80, #81) lists API gaps that block shipped or
planned extensions. Priority is by how many extensions each unblocks, and
whether it is a small additive change at level 4.

- **1. Per-instance configuration** — Plan: Section 6; Level: 4; Status: In
  review (shell#603)
- **2. Hidden state storage (timers persisting deadlines must not show in
  generated settings)** — Plan: Display field `hidden: true` on any setting:
  stored, validated and readable like any other, never rendered nor counted by
  Reset all; or a separate `Storage` facade if hidden state must survive
  Reset; Level: 4; Status: Next small PR
- **3. `string-list` and `path` setting types** — Plan: `path` shipped in
  settings v2; free-form `strings` (list of up to 32 strings of at most 128
  chars, text rows) added beside `list` (which is a multi-select over declared
  options); Level: 4; Status: `path` in review (shell#602); `strings` next
- **4. `experience` capability instead of spawning horneroctl** — Plan: A
  typed `Experience` facade (read mode; `set(mode)` on a user gesture) over
  the existing service, declared in `capabilities.providers`; Level: 5;
  Status: Designed
- **5. Process failure signal (a missing executable never reports exit)** —
  Plan: The host owns a `Run` facade: argv from `processCommands` only,
  `started`/`failed(reason)`/`finished(code)` signals, a timeout, one place
  for the not-found case; Level: 5; Status: Designed; needs a security review
  as it is the only new process API
- **6. Launcher surface host** — Plan: Already hosted (`PluginLauncherHost`,
  shell#250 closed); `commands` (shell#605) adds action rows; Level: 3/4;
  Status: Shipped
- **7. Desktop-widget content and scroll contract** — Plan: Host-provided
  `UiScrollArea` in PluginKit and a documented rule that content past the
  frame scrolls instead of clipping; Level: 4; Status: Next small PR
- **8. Real-shell screenshots in marketplace metadata** — Plan: Existing
  `marketplace.screenshots`; the QA VM capture tool should write them; Level:
  -; Status: Tooling, plugins repo
- **9. Providers: `Power.devices`, calendar, clipboard (consent-gated), game
  library, frame time** — Plan: One shared-provider domain each (RFC 0001
  section 5b); clipboard and library need an explicit per-extension consent
  step, not a manifest declaration alone; Level: 5; Status: Designed;
  `Power.devices` first (no consent needed)

The ones that unblock shipped extensions (1, 2, 3, 7) are level 4 and
additive; 4, 5 and 9 introduce new capabilities and ship as level 5 each with
their own review.

## 11. Alternatives considered

- **Break to schemaVersion 4.** Rejected: nothing structural breaks, a break
  would re-port all 36 catalogue extensions for no gain, and `pluginKit` gives
  the same refusal behaviour with an additive field.
- **Free-form settings UI per extension.** Rejected: it is what the custom
  `settings` surface already allows; the point is that typed schema gives
  consistent, validated, searchable, previewable, resettable controls.
- **Host-visible code in manifests (eval, expressions).** Rejected for
  security; `visibleWhen` is data, not code.
- **Per-instance by copying the package.** Rejected: it forks updates and
  load state; instances are configuration of one installed package.

## 12. Rollout and status

- **This RFC** — Repo: docs; Status: Proposed (docs#130)
- **`pluginKit` field, apiLevel 4, validator, schema; settings schema v2 and
  live preview** — Repo: shell; Status: In review: shell#602 (CI green)
- **Per-instance desktop widgets** — Repo: shell; Status: Draft: shell#603
  (stacked on #602)
- **Commands (launcher, IPC)** — Repo: shell; Status: Draft: shell#605
  (stacked on #603)
- **Validator, schema and catalogue mirror** — Repo: plugins; Status: In
  review: plugins#82
- **Quick-setting tiles, Control Center panels** — Repo: shell; Status: Not
  started
- **Hidden settings, `strings`, scroll area (Section 10a 2, 3, 7)** — Repo:
  shell; Status: Not started
- **Notification source, lock-screen card, hooks, new providers** — Repo:
  shell; Status: Designed here, not started
- **Extractions (Section 10)** — Repo: shell, plugins; Status: Not started
- **Dashboard pages (row 14, apiLevel 5)** — Repo: shell, plugins; Status:
  Shipped: shell#710 (contract) + plugins Agent Deck (first consumer)
- **Spanish handbook page** — Repo: docs; Status: Not started

The PR numbers and the exact state are recorded in the tracking issue and in
`docs/PLUGINS.md` of the Shell, which is the contract; this RFC is the design.
