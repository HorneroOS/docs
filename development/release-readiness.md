# Release readiness checklist

**Status: NOT READY for a public launch.** HorneroOS is a
development preview that runs on the maintainers' machines. This
checklist is the single gate list for calling anything a release;
an item is PASS only with linked evidence, never by intention.

Last reviewed: 2026-10-21.

## Gates

- **ISO installs on clean hardware/VM — BLOCKED.**
  Installer owned by Panda Foss; no install-to-first-boot
  evidence yet. HorneroOS/installer#11, HorneroOS/installer#14.
- **Boot to desktop (first boot) — BLOCKED.**
  Depends on the installer gate; QA scenarios exist in
  HorneroOS/qa but no passing run against a release ISO.
- **Compositor support matrix — FAIL.**
  Hyprland supported; Niri experimental and not validated at
  parity. Do not advertise parity.
- **Package integrity — FAIL.**
  horneroctl release binaries unsigned (HorneroOS/hornero#180);
  AUR publishes CI checksums, no signature verification in
  install flows.
- **Safe updates + rollback — FAIL.**
  Update status lanes shipped read-only
  (HorneroOS/hornero#216: Hornero-owned vs system vs held,
  surfaced in the Control Center Updates pane); snapshot and
  rollback backend is still a spike (HorneroOS/hornero#179),
  mutating lanes open (HorneroOS/hornero#62). No rollback is
  advertised anywhere until a backend contract passes.
- **Hermes Companion functional — PASS.**
  Loopback gateway, manual approvals, Hornero skill, Javi chat
  with sessions, attachments, voice path and activity trace;
  verified live on the dev host. End-user packaging still open
  (HorneroOS/hornero#174).
- **Plugin lifecycle — PASS.**
  horneroctl validate/install/list/enable/disable/remove with
  receipts and pinned revisions; shell runtime loads enabled
  plugins after the PluginHost delegate fix
  (HorneroOS/shell#269: delegates under an Item root). Live
  evidence: three official plugins loaded (two bar, one
  dashboard) via `qs ipc call plugins status`.
- **Extensions marketplace — PASS.**
  HorneroOS/plugins catalogue (SHA-256 + CI), catalogue commands
  in horneroctl, Control Center browse/install
  (HorneroOS/hornero#214, HorneroOS/shell#268). Community
  listings not yet open (HorneroOS/shell#251).
- **Lock/session safety — PASS.**
  Shell stop/restart refuses while locked (shell IPC probe);
  incident in `incident-2026-10-20-session-lock-crash.md`;
  spontaneous-crash resilience open (HorneroOS/shell#257).
- **Accessibility audit — FAIL.**
  Accessible-name audit incomplete (HorneroOS/shell#221).
  Static slices landed: lock controls (shell#276), launcher
  rows (shell#277), dashboard cards (shell#278), shared
  controls (shell#279); inventory in shell
  `docs/a11y-audit-2026-10-21.md`. AT-SPI runtime passes now
  exist for the bar, dashboard, Control Center, launcher rows
  (shell#290; the earlier gap was a stale deployed checkout,
  not shell code) and lock content (shell#291, inert-Pam
  harness). The static inventory is now covered for the
  inventoried surfaces (Appearance rows shell#295, shared
  controls and Welcome cards shell#296, pane list rows
  shell#297). Still FAIL: the real session-lock surface, any
  screen-reader task-completion pass, and runtime exposure
  checks for collapsed-section delegates.
- **Performance baseline — FAIL.**
  Steady-state numbers published (shell
  `docs/perf-baselines/2026-10-21.md`, HorneroOS/shell#270).
  Development-host measurements now exist for full-shell cold
  start (≈1.7 s to the bar in AT-SPI, shell#292) and frame-cost
  bounds for the launcher (60 Hz vsync, shell#293) and
  dashboard (118/120 slots, shell#294) and Control Center
  initial render (169/180 slots, shell#298) and lock content
  (171/180 slots, shell#299). Still FAIL: no disposable-QA-
  harness run and no performance claims are made
  from development-host numbers (HorneroOS/shell#47, #228).
- **Documentation — PASS.**
  Canonical docs in this repo; website catalogue only via the
  pinned data pipeline.
- **QA acceptance — FAIL.**
  HorneroOS/qa suite not green against a candidate composition;
  preview20 remains an unpublished candidate.

## Rules

- Never publish an ISO, screenshot, benchmark or compatibility
  claim whose gate is not PASS with evidence.
- Installer gates move only with Panda Foss's acceptance;
  HorneroOS does not self-certify the installer.
- Update this file in the same PR that changes a gate's
  evidence.
