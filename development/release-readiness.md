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
  still open. QA [issue #19](https://github.com/HorneroOS/qa/issues/19) tracks
  the install scenarios. No HorneroOS ISO is an installable release artifact.
- **Boot to desktop after installation — BLOCKED.** No passing QA run exists
  for preview20 installed from an ISO in both UEFI and legacy BIOS. The
  existing `smoke/desktop-ready` scenario checks a prepared QA image; it does
  not prove a completed installation.
- **Compositor support matrix — FAIL.** Hyprland is the validated default.
  Niri remains experimental and has no candidate-release parity acceptance.
- **Package integrity — FAIL.**
  [hornero#180](https://github.com/HorneroOS/hornero/issues/180) remains open.
  AUR checksums do not verify a maintainer signature. The CI "Release signing
  smoke" uses an ephemeral key and does not prove that a published asset was
  signed with the release key.
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
  does not claim a clean-install or release-image test.
- **Plugin lifecycle — PASS for the tested official plugins.** The CLI
  validates, installs inert data, lists, enables, disables and removes
  plugins. The Shell host fix is in
  [shell#269](https://github.com/HorneroOS/shell/pull/269). Runtime evidence
  recorded three official plugins loaded through `qs ipc call plugins status`.
- **Official extensions catalogue — PASS.** The pinned
  [HorneroOS/plugins](https://github.com/HorneroOS/plugins) catalogue and
  verified installation are in
  [hornero#214](https://github.com/HorneroOS/hornero/pull/214) and
  [shell#268](https://github.com/HorneroOS/shell/pull/268). Community
  listings are not available; their trust and signing design remains open in
  [shell#251](https://github.com/HorneroOS/shell/issues/251).
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
- **Performance baseline — FAIL.** Development-host cold-start and per-surface
  numbers are published in the
  [2026-10-21 shell report](https://github.com/HorneroOS/shell/blob/main/docs/perf-baselines/2026-10-21-cold-start.md).
  They have not been reproduced by the disposable QA harness; no performance
  claim is approved. Track
  [shell#47](https://github.com/HorneroOS/shell/issues/47) and
  [shell#228](https://github.com/HorneroOS/shell/issues/228).
- **Documentation — PASS.** HorneroOS/docs owns canonical technical content;
  the website renders a reviewed pinned commit.
- **Repository governance CI — FAIL.** Installer issue
  [#14](https://github.com/HorneroOS/installer/issues/14) tracks its stale
  label-sync engine pin. The latest main-branch label-sync run
  [39226059114](https://github.com/HorneroOS/installer/actions/runs/39226059114)
  failed. This is a governance failure, separate from installer acceptance.
- **QA acceptance — FAIL.** The preview20 checklist still has unchecked
  exact-pin VM and Hornero QA gates. See the
  [candidate checklist](https://github.com/HorneroOS/hornero/blob/main/releases/v0.2.0-preview20-checklist.md),
  QA issues [#16](https://github.com/HorneroOS/qa/issues/16),
  [#18](https://github.com/HorneroOS/qa/issues/18), and
  [#19](https://github.com/HorneroOS/qa/issues/19). The latest successful
  QA test workflow run is [38537311408](https://github.com/HorneroOS/qa/actions/runs/38537311408),
  from 2026-10-14; it is not evidence for preview20.

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

In `HorneroOS/installer`, `./scripts/build-iso.sh` is run only in the dedicated
disposable Arch VM and with Panda Foss's acceptance process. Do not run this on
the maintainer host.

In `HorneroOS/qa`:

```sh
uv run hornero-qa list
uv run hornero-qa run smoke/desktop-ready
uv run hornero-qa inspect <run-id>
```

The current scenario validates a ready image. QA#19 must add and accept the
install-to-first-boot matrix before this proves an installed ISO.

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
uv run pytest tests/test_a11y_names.py tests/test_lock_a11y.py \
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
preview20 pins and attach their evidence. A prior or mutable-main run does not
count.

## Rules

- Never publish an ISO, screenshot, benchmark or compatibility claim unless
  its gate is PASS with linked evidence for the current candidate.
- Installer gates move only with Panda Foss's acceptance. HorneroOS does not
  self-certify the installer.
- Keep PASS claims scoped to what the command proves. A smoke test, source
  test, development-host observation or green composition CI is not a
  substitute for an installed release-ISO acceptance run.
- Update this file in the same PR that changes a gate's status or evidence.
