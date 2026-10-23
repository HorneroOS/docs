# Release readiness checklist

**Status: NOT READY for a public launch.** HorneroOS remains a development
preview. A gate is PASS only when the evidence below exists for the exact
candidate composition; source tests and maintainer-host checks do not prove
installed-system acceptance.

Last reviewed: 2026-10-23.

Current candidate: [`hornero-0.2.0-preview20`][candidate], selected by
[`manifests/candidate`][candidate-pointer]. It pins Shell
`2fcc59de53fa7761b6958fc87e65123a7296af6d` and Config
`f95b1f51aefc4e42f642a3fc84759822c6c0f74d`. The composition workflow passed
at [run 39695291293][composition-run]. That validates composition, not an ISO
or installed system.

[candidate]: https://github.com/HorneroOS/hornero/blob/main/manifests/v0.2.0-preview20.yaml
[candidate-pointer]: https://github.com/HorneroOS/hornero/blob/main/manifests/candidate
[composition-run]: https://github.com/HorneroOS/hornero/actions/runs/39695291293

## Gates

- **ISO installs on clean hardware/VM — BLOCKED.** Panda Foss owns the
  official installer and has not provided install-to-first-boot acceptance.
  Installer [issue #11](https://github.com/HorneroOS/installer/issues/11) is
  still open. A fresh unsigned provisional image built from installer main
  booted to the live desktop in disposable UEFI and legacy-BIOS VMs. Initial
  runs stopped at the network/DNS preflight. A follow-up UEFI run with working
  rootless VM networking resolved the Arch mirror, but Calamares could not
  start because it requires Qt 6.12 while the live image has Qt 6.11.2. No
  target was installed. The builder must be synchronized to the locked Arch
  snapshot before producing another image. The tested ISO used installer
  revision `78a292ec00c7eee989c68b40054580dff805270f`, product revision
  `7471351cbe26e2a8754fd1bd9c5f4a2b984115ad`, and Calamares 3.4.3. Its SHA-256
  is `fde2e6f54f33c341afa6fa87a26cff86740f58e48d8b3ea949cafff35281a2a1`.
  It remains unsigned. See the runtime evidence and the pending builder fix
  in [issue #11](https://github.com/HorneroOS/installer/issues/11) and
  [installer#17](https://github.com/HorneroOS/installer/pull/17).
  QA [issue #19](https://github.com/HorneroOS/qa/issues/19) tracks the full
  install scenarios. This image is not a release artifact.
- **Boot to desktop after installation — BLOCKED.** No passing QA run exists
  for preview20 installed from an ISO in both UEFI and legacy BIOS. The
  existing `smoke/desktop-ready` scenario checks a prepared QA image; it does
  not prove a completed installation.
- **Compositor support matrix — FAIL.** Hyprland is the validated default.
  Niri remains experimental and has no candidate-release parity acceptance.
- **Package integrity — FAIL.**
  [hornero#180](https://github.com/HorneroOS/hornero/issues/180) remains open.
  Signing workflow engineering landed in
  [hornero#275](https://github.com/HorneroOS/hornero/pull/275), and its CI
  smoke uses an ephemeral key. That does not prove that a published asset was
  signed with the production release key. No release public key or production
  signing secret is provisioned, and no official signed release has been
  verified. AUR checksums alone do not establish maintainer authenticity.
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
  index are not complete. Do not represent the official-catalogue PASS as
  community-registry acceptance.
- **Lock/session safety — FAIL.** The Shell refuses its stop/restart actions
  while locked, but recovery after a Shell crash while locked remains open in
  [shell#257](https://github.com/HorneroOS/shell/issues/257). The lock surface
  also lacks a real screen-reader acceptance pass; see the accessibility gate.
- **Accessibility audit — FAIL.** Static checks cover the inventoried
  controls and some AT-SPI journeys. The real session-lock surface, a
  screen-reader task-completion pass, and runtime exposure for collapsed
  delegates remain unverified. Track
  [shell#221](https://github.com/HorneroOS/shell/issues/221) and the
  [2026-10-21 shell accessibility inventory](https://github.com/HorneroOS/shell/blob/main/docs/a11y-audit-2026-10-21.md).
  Draft [shell#310](https://github.com/HorneroOS/shell/pull/310) adds a
  persisted shell high-contrast palette; all current CI checks pass, but the
  PR remains draft until rendered review and the Orca task pass are recorded.
  Greeter [#37](https://github.com/HorneroOS/greeter/pull/37) also has green
  CI but still needs graphical and Qt Virtual Keyboard acceptance.
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
  governance pin. The latest installer main checks
  [39988724178](https://github.com/HorneroOS/installer/actions/runs/39988724178)
  and [39988724180](https://github.com/HorneroOS/installer/actions/runs/39988724180)
  passed. This says nothing about ISO installation acceptance.
- **QA acceptance — FAIL.** The preview20 checklist still has unchecked
  exact-pin VM and Hornero QA gates. See the
  [candidate checklist](https://github.com/HorneroOS/hornero/blob/main/releases/v0.2.0-preview20-checklist.md),
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
run_id="$(date +%Y%m%d-%H%M%S)"
sudo env VJOBS=2 ./scripts/build-iso.sh \
  --work "/mnt/build/hornero-work-${run_id}" \
  --output "/mnt/build/hornero-output-${run_id}"
```

In `HorneroOS/qa`:

```sh
uv run hornero-qa list
uv run hornero-qa run smoke/desktop-ready
uv run hornero-qa inspect <run-id>
```

The current scenario validates a ready image. QA#19 must add and accept the
install-to-first-boot matrix before this proves an installed ISO.

To reproduce the latest live-image runtime check in a disposable guest, use
working DNS and run:

```sh
getent ahostsv4 archive.archlinux.org
curl -I --connect-timeout 6 archive.archlinux.org
pacman -Q qt6-base calamares
calamares
```

The 2026-10-23 test resolved the mirror to `49.12.124.107` and received HTTP
301. The packages reported `qt6-base 6.11.2-3` and `calamares 3.4.3-1`; the
last command reported that the Calamares binary requires `Qt_6.12`, which the
live Qt library does not provide. This reproduces the blocker. It is not an
installation acceptance pass.

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

The first command uses a throwaway key. The second is the release check; it
currently lacks a committed public key until hornero#180 lands.

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
preview20 pins and attach their evidence. The Hornero script requires KVM and
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
