# Release readiness checklist

**Status: Preview published; NOT READY for a stable launch.**
`v0.2.0-preview22` is published as a signed Preview ISO (Desktop and
Studio Preview). The stable-launch gates below remain open. A gate is
PASS only when the evidence below exists for the exact candidate
composition; source tests and maintainer-host checks do not prove
installed-system acceptance.

Last reviewed: 2026-10-26.

Current published release: [`hornero-0.2.0-preview22`][candidate],
selected by [`manifests/candidate`][candidate-pointer] (product
`bcc53ede593d54f6b9e7562a50cf6c620e56b275`, installer
`c8fbc359843c2249945adf0091d732c628330d8f`). Its ISO passed the
virtual-machine installation matrix on the preview21 composition
carried forward, with the cancel-cleanup scenario retested end to end;
see the [preview22 checklist](https://github.com/HorneroOS/hornero/blob/main/releases/v0.2.0-preview22-checklist.md).

[candidate]: https://github.com/HorneroOS/hornero/blob/main/manifests/v0.2.0-preview22.yaml
[candidate-pointer]: https://github.com/HorneroOS/hornero/blob/main/manifests/candidate

## Gates

- **ISO installs on clean hardware/VM — PARTIAL (VM PASS, hardware BLOCKED).**
  Panda Foss owns the official installer and its acceptance. The
  published v0.2.0-preview22 ISO (SHA-256
  `38ec76d7c9c10ea3e956b2c9f2d8d420e3d09b61899dc453a2858622d7e90bd2`)
  is signed with the HorneroOS releases key
  `FCFBEE43925AB5429362278AE59EAB44AA2498DC` and published; its Desktop
  and Studio install matrix (UEFI and legacy BIOS, encrypted and
  unencrypted) passed in disposable VMs on the preview21 composition
  carried forward. Cancellation and successful-install cleanup removed
  temporary target mounts. BIOS first login reached the installed
  desktop; UEFI reached the login screen, but authentication was not
  verified. Installed package/profile parity remains unverified. No
  physical-hardware installation has been validated. See the [R11 validation record](https://github.com/HorneroOS/installer/blob/main/docs/r11-validation.md),
  installer [issue #11](https://github.com/HorneroOS/installer/issues/11),
  and QA [issue #19](https://github.com/HorneroOS/qa/issues/19).
- **Boot to desktop after installation — BLOCKED.** Legacy BIOS reached an
  authenticated desktop on the R11 provisional ISO. UEFI authentication is
  still unverified, and QA has not produced a passing install-to-first-boot
  run against the exact preview20 candidate. The existing
  `smoke/desktop-ready` scenario checks a prepared QA image; it does not prove
  a completed installation.
- **Compositor support matrix — FAIL.** Hyprland is the validated default.
  Niri remains experimental and has no candidate-release parity acceptance.
- **Package integrity — FAIL.**
  [hornero#180](https://github.com/HorneroOS/hornero/issues/180) remains open.
  Signing workflow engineering landed in
  [hornero#275](https://github.com/HorneroOS/hornero/pull/275), and its CI
  smoke uses an ephemeral key. That does not prove that a published asset was
  signed with the production release key. No release public key or production
  signing secret is provisioned (this text predates preview22; the
  v0.2.0-preview22 ISO is signed with the HorneroOS releases key and the
  public key is committed at `packaging/keys/hornero-release.pub.asc`).
  AUR checksums alone do not establish maintainer authenticity.
- **Safe updates and system rollback — FAIL.**
  [hornero#216](https://github.com/HorneroOS/hornero/pull/216) added read-only
  ownership lanes. The rollback backend
  ([hornero#179](https://github.com/HorneroOS/hornero/issues/179)) and
  mutating update lanes
  ([hornero#62](https://github.com/HorneroOS/hornero/issues/62)) remain open.
  `horneroctl package check` is not an update transaction, and configuration
  restore is not an operating-system rollback.
- **Hermes Companion — PASS on the development host only.** The gateway and
  Javi chat were exercised with approvals, history, attachments, voice and
  activity events. The user-unit lifecycle shipped in
  [hornero#252](https://github.com/HorneroOS/hornero/pull/252); setup and
  knowledge export shipped in
  [hornero#253](https://github.com/HorneroOS/hornero/pull/253). Packaging the
  Hermes runtime for a clean install remains open in
  [hornero#191](https://github.com/HorneroOS/hornero/issues/191). This PASS
  does not claim a clean-install or release-image test. The setup/removal
  ownership fix in [hornero#278](https://github.com/HorneroOS/hornero/pull/278)
  is merged, but it is not in the preview20 candidate and no signed CLI release
  containing it is published. The dependent dotfiles migration remains in
  draft [dotfiles#383](https://github.com/ulises-jeremias/dotfiles/pull/383),
  awaiting a CLI release and an independent review.
- **Plugin lifecycle — PASS for the tested official plugins.** The CLI
  validates, installs inert data, lists, enables, disables and removes
  plugins. The Shell host fix is in
  [shell#269](https://github.com/HorneroOS/shell/pull/269). Runtime evidence
  recorded three official plugins loaded through `qs ipc call plugins status`.
- **Official extensions marketplace — PASS for the official catalogue.** The
  pinned [HorneroOS/plugins](https://github.com/HorneroOS/plugins) catalogue,
  verified CLI installation, Control Center marketplace and metadata are
  integrated in [hornero#214](https://github.com/HorneroOS/hornero/pull/214),
  [shell#268](https://github.com/HorneroOS/shell/pull/268),
  [plugins#6](https://github.com/HorneroOS/plugins/pull/6),
  [hornero#273](https://github.com/HorneroOS/hornero/pull/273), and
  [shell#309](https://github.com/HorneroOS/shell/pull/309). The marketplace is
  also live on [horneroos.com](https://www.horneroos.com/marketplace). The
  separate community-index phase remains open in
  [shell#251](https://github.com/HorneroOS/shell/issues/251): production
  registry-key custody and end-to-end consumption of a verified community
  index are not complete. Shell
  [#318](https://github.com/HorneroOS/shell/pull/318) adds verified community
  entries to Control Center. The Terminal Settings timeout is fixed in
  [shell#321](https://github.com/HorneroOS/shell/pull/321), whose checks pass.
  Hosted matrix [run 40129324336](https://github.com/HorneroOS/shell/actions/runs/40129324336)
  then exposed a separate first-login Welcome overlay: its top-level window
  covered Settings, and cursor animation made an inadequate pixel-diversity
  check accept the wrong screen. Shell #318 commit `a325e1e` closes Welcome
  before Settings navigation and verifies that the fresh VM has dismissed it
  before Settings checks. Exact-head hosted matrix
  [run 40131614836](https://github.com/HorneroOS/shell/actions/runs/40131614836)
  failed before pane capture: the qs CLI emitted a Qt locale warning before
  the valid `{"open":false,"page":"start"}` JSON, and the smoke script passed
  both lines directly to `jq`. Rebased Shell #318 commit `78877c2` extracts
  the last JSON object from IPC output and tests warning and no-JSON cases.
  Hosted matrix [run 40134380723](https://github.com/HorneroOS/shell/actions/runs/40134380723)
  was superseded after a governance check rejected its merge-commit history.
  The PR was rebased with authored commits preserved; a security review also
  reduced the VM workflow's token to contents-read, as the organization default
  was write. Exact-head matrix
  [run 40136330518](https://github.com/HorneroOS/shell/actions/runs/40136330518)
  failed at the first Terminal Settings capture: the CLI preflight passed, but
  the pane remained on its loading spinner. Shell #318 commit `b5048dd` fixed
  bounded process termination, Welcome handling when Settings allocation fails,
  VM capture environment expansion, SSH diagnostic timeouts, a QEMU socket-test
  race, and checkout credential persistence. The failed capture exposed a further
  edge case: the timer returned early when the process was no longer running,
  leaving loading stuck if no response or exit signal arrived. Commit `e59026f`
  reports a timeout in that state and signals only a live process. The focused
  pane suite (37 tests) and pre-commit pass; the full suite previously passed 641
  tests with Pillow available. Matrix
  [40138798423](https://github.com/HorneroOS/shell/actions/runs/40138798423)
  repeated the spinner after 78 seconds, despite the timeout fix in `e59026f`.
  Commit `e25ba78` binds the timeout to the loading/process state instead of
  restarting it imperatively. Build, tests, QML, lint, harness-lint, smoke-dryrun,
  governance/Danger, and CodeRabbit review are green on `e25ba78`; there are no
  unresolved review threads. Exact-head hosted matrix
  [run 40140797051](https://github.com/HorneroOS/shell/actions/runs/40140797051)
  was canceled after 25 minutes while the guest was compiling the native QML
  plugin (the last build progress was 48%). Its artifact contains no pane
  captures; `assertions.json` says `session start`, which does not match the last
  emitted build output, so the diagnosis is inconclusive. Fresh exact-head run
  [40142966617](https://github.com/HorneroOS/shell/actions/runs/40142966617)
  failed at the first Terminal Settings screenshot: the window title and
  navigation rendered, but the pane content region remained empty. Review traced
  this to the translated `ColumnLayout` in `Panes.qml` having no explicit width
  or height; implicit child sizes did not give the layout actual geometry. Shell
  #318 commit `e02b2ae` sets the stack to the viewport width and full implicit
  stack height, with a regression test. Full suite (642 tests), QML lint,
  pre-commit, CMake build, and repository hygiene scans pass on that commit.
  Exact-head matrix
  [40145172696](https://github.com/HorneroOS/shell/actions/runs/40145172696)
  demonstrated that this fix was incomplete. Visual review found its smoke
  screenshot was the desktop wallpaper empty state, Network displayed Appearance
  content under a Network title, and Bluetooth had an empty content region; the
  previous color/difference checks had accepted the first two. Commit `ddd67cf`
  replaces implicit layout sizing with a viewport-sized page stack and explicit
  per-pane positions/dimensions. Matrix
  [40147893239](https://github.com/HorneroOS/shell/actions/runs/40147893239)
  confirmed that this still did not render Terminal or Bluetooth contents.
  Run
  [40150595999](https://github.com/HorneroOS/shell/actions/runs/40150595999)
  showed that the active Terminal page and loaded item both match the viewport
  geometry and the Loader is Ready, yet the page contents are blank. Commit
  `1b917b9` adds diagnostics for TerminalPane's inner surface, Flickable, content
  layout, header, and section. Exact-head diagnostic matrix
  [40152601907](https://github.com/HorneroOS/shell/actions/runs/40152601907)
  is queued. See the
  [latest issue evidence](https://github.com/HorneroOS/shell/issues/251#issuecomment-6392198620).
  Keep merge blocked until this matrix completes successfully and all 25 screenshots
  are reviewed. Do not represent the official-catalogue PASS as community-registry
  acceptance; production key custody and end-to-end community install/update/
  rollback remain incomplete.
- **Lock/session safety — BLOCKED.** The Shell refuses its stop/restart
  actions while locked and guards detectable competing lock requests. The
  orphaned-lock failure in [shell#24](https://github.com/HorneroOS/shell/issues/24)
  remains unresolved: Quickshell v0.3.2 includes a failed-acquisition guard,
  but the exact cross-locker scenario has not been rerun with that version;
  upstream [quickshell#1054](https://github.com/quickshell-mirror/quickshell/issues/1054)
  is still open. The update and required evidence are recorded in
  [shell#24's latest comment](https://github.com/HorneroOS/shell/issues/24#issuecomment-6387620388).
  Recovery after a spontaneous Shell crash while locked remains open in
  [shell#257](https://github.com/HorneroOS/shell/issues/257). The lock surface
  also lacks a real screen-reader acceptance pass; see the accessibility gate.
- **Accessibility audit — FAIL.** Static checks cover the inventoried
  controls and some AT-SPI journeys. The real session-lock surface, a
  screen-reader task-completion pass, and runtime exposure for collapsed
  delegates remain unverified. Track
  [shell#221](https://github.com/HorneroOS/shell/issues/221) and the
  [2026-10-21 shell accessibility inventory](https://github.com/HorneroOS/shell/blob/main/docs/a11y-audit-2026-10-21.md).
  Shell [#310](https://github.com/HorneroOS/shell/pull/310) has green CI and
  visual evidence for its persisted high-contrast palette; the PR is open and
  the Orca task remains unverified. Greeter
  [#37](https://github.com/HorneroOS/greeter/pull/37) is merged with large
  text, high contrast, and optional virtual-keyboard controls. Qt 6 SDDM preview
  and AT-SPI control checks passed locally, but no screen-reader task-completion
  or candidate-image acceptance has been recorded.
- **PluginKit runtime acceptance — BLOCKED.** Shell
  [#312](https://github.com/HorneroOS/shell/pull/312) has green CI for the
  public PluginKit and desktop widget slots, but runtime loading, persistence
  across Shell restart, and display disconnect/reconnect behavior remain
  unverified. Keep the PR draft until those checks pass.
- **Performance baseline — FAIL.** Development-host cold-start and per-surface
  numbers are published in the
  [2026-10-21 shell report](https://github.com/HorneroOS/shell/blob/main/docs/perf-baselines/2026-10-21-cold-start.md).
  They have not been reproduced by the disposable QA harness; no performance
  claim is approved. Track
  [shell#47](https://github.com/HorneroOS/shell/issues/47) and
  [shell#228](https://github.com/HorneroOS/shell/issues/228).
- **Documentation and showcase — PASS for the published surfaces.**
  HorneroOS/docs owns canonical technical content; the website renders a
  reviewed pinned commit. Website PRs
  [#148](https://github.com/HorneroOS/website/pull/148) and
  [#149](https://github.com/HorneroOS/website/pull/149) publish the marketplace
  and a live workstation capture in the showroom. The capture is not
  installation, hardware-compatibility, or release evidence.
- **Repository governance CI — PASS.** Installer issue
  [#14](https://github.com/HorneroOS/installer/issues/14) is closed after
  [installer#15](https://github.com/HorneroOS/installer/pull/15) aligned the
  governance pin. Installer PR #24's evidence correction and merge to main
  passed CI in
  [run 40071650350](https://github.com/HorneroOS/installer/actions/runs/40071650350)
  and [run 40071650330](https://github.com/HorneroOS/installer/actions/runs/40071650330).
  This says nothing about ISO installation acceptance.
- **QA acceptance — FAIL.** The preview22 checklist still has unchecked
  exact-pin VM and Hornero QA gates. See the
  [candidate checklist](https://github.com/HorneroOS/hornero/blob/main/releases/v0.2.0-preview22-checklist.md),
  QA issues [#16](https://github.com/HorneroOS/qa/issues/16),
  [#18](https://github.com/HorneroOS/qa/issues/18), and
  [#19](https://github.com/HorneroOS/qa/issues/19). The latest successful fast
  QA CI run is [39957901125](https://github.com/HorneroOS/qa/actions/runs/39957901125)
  on 2026-10-23 (Ruff, Mypy, pytest, scenario matrix, Markdown lint). It tests
  repository code, not a candidate VM or installed ISO.

## Evidence commands

Run these from the named repository root. Attach the command output and a link
to the run or evidence bundle when changing a gate. Use the exact candidate
SHAs above. These commands help collect evidence; only the acceptance scope
in the gate determines PASS.

### Composition

Run in `HorneroOS/hornero`:

```sh
python3 scripts/check-manifests.py
python3 scripts/check-pins.py
python3 -m pytest tests/ -q
./scripts/compose.sh --yes
```

This validates composition. It does not build or boot an ISO.

### ISO build and installed desktop

In `HorneroOS/installer`, the following builds the provisional Calamares image
only in a dedicated disposable Arch VM, against a clean checkout, and with
Panda Foss's acceptance process. It does not replace Panda's official
installer acceptance. Do not run this on the maintainer host. Use new,
separate work and output directories for every build. Reserve 40 GiB for work
and 12 GiB for output (52 GiB if they share one filesystem):

```sh
run_dir="$(sudo mktemp -d /mnt/build/hornero-XXXXXX)"
sudo env VJOBS=2 ./scripts/build-iso.sh \
  --work "${run_dir}/work" \
  --output "${run_dir}/output"
```

In `HorneroOS/qa`:

```sh
uv run hornero-qa list
uv run hornero-qa run smoke/desktop-ready
uv run hornero-qa inspect <run-id>
```

The current scenario validates a ready image. QA#19 must add and accept the
install-to-first-boot matrix before this proves an installed ISO.

The following historical live-image runtime check was run on 2026-10-23. See
the newer [R11 validation record](https://github.com/HorneroOS/installer/blob/main/docs/r11-validation.md)
for current evidence. To reproduce the historical check in a disposable guest,
use working DNS and run:

```sh
getent ahostsv4 archive.archlinux.org
curl -I --connect-timeout 6 archive.archlinux.org
pacman -Q qt6-base calamares
calamares
```

The 2026-10-23 test resolved the mirror to `49.12.124.107` and received HTTP
301. The packages reported `qt6-base 6.11.2-3` and `calamares 3.4.3-1`; the
last command reported that the Calamares binary requires `Qt_6.12`, which the
live Qt library did not provide in that image. This records the superseded
runtime incompatibility and is not an installation acceptance pass.

### Compositors

In `HorneroOS/qa`, run both scenarios against the candidate image:

```sh
uv run hornero-qa run smoke/desktop-ready
uv run hornero-qa run compositors/niri-desktop-baseline
```

Niri remains experimental until its scenario passes on the candidate.

### Package integrity

In `HorneroOS/hornero`:

```sh
./scripts/test-signing.sh
./scripts/verify-release.sh <asset> [signature]
```

The first command uses a throwaway key. The second is the release check;
the production public key is committed at
`packaging/keys/hornero-release.pub.asc` in HorneroOS/hornero.

### Updates and rollback

Run `horneroctl package check --json` on the target system. This is read-only
status. No end-to-end system rollback command exists while hornero#179 and #62
remain open.

### Hermes

On a provisioned test system, run
`horneroctl assistant gateway status --json` and
`qs ipc call companion status`. This is development-host evidence only. Do not
put provider credentials in QA fixtures or CI logs.

### Plugin lifecycle and catalogue

In `HorneroOS/plugins`:

```sh
python3 scripts/validate_plugins.py
python3 scripts/gen_catalog.py --check
```

On the candidate image:

```sh
horneroctl plugin catalog --json
horneroctl plugin catalog install hornero-pomodoro --dry-run
qs ipc call plugins status
```

A catalogue listing or successful dry run does not prove the plugin loaded in
the release image.

### Lock and session safety

In `HorneroOS/qa`:

```sh
uv run hornero-qa run lock/lock-keyboard
uv run hornero-qa run regressions/shell-24-lock-after-hyprlock
```

The crash-recovery scenario must pass on the candidate before the gate can
pass.

### Accessibility

In `HorneroOS/shell`:

```sh
python3 -m pytest tests/test_a11y_names.py tests/test_lock_a11y.py \
  tests/test_appearance_a11y.py tests/test_shared_controls_a11y.py \
  tests/test_pane_rows_a11y.py
```

In `HorneroOS/qa`, also run `uv run hornero-qa run lock/lock-keyboard`.
Static tests and lock smoke are not the missing screen-reader
task-completion pass.

### Performance

In `HorneroOS/qa`, run `uv run hornero-qa run perf/baseline`. In
`HorneroOS/shell`, run:

```sh
./scripts/perf-baseline.sh --samples 5 --interval 1 --format json
```

The Shell command measures the development host. Only the QA image run can
support release performance claims.

### Documentation

In `HorneroOS/docs`, run `npx --yes markdownlint-cli2 '**/*.md'` and
`python3 scripts/check-horneroctl-refs.py`. Both must pass on the same docs
commit pinned by the website.

### QA and candidate release

In `HorneroOS/hornero`, run `tests/vm/smoke.sh`. In `HorneroOS/qa`, run
`uv run hornero-qa run smoke/desktop-ready`. Both runs must identify the exact
preview22 pins and attach their evidence. The Hornero script requires KVM and
a prepared base image; `VM-SMOKE-SKIP` is not a pass. Only an exact-pin
`VM-SMOKE-PASS` plus the candidate QA evidence counts. A prior or mutable-main
run does not count.

## Rules

- Never publish an ISO, screenshot, benchmark or compatibility claim unless
  its gate is PASS with linked evidence for the current candidate.
- Installer gates move only with Panda Foss's acceptance. HorneroOS does not
  self-certify the installer.
- Keep PASS claims scoped to what the command proves. A smoke test, source
  test, development-host observation or green composition CI is not a
  substitute for an installed release-ISO acceptance run.
- Update this file in the same PR that changes a gate's status or evidence.
