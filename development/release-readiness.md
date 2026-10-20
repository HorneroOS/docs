# Release readiness checklist

**Status: NOT READY for a public launch.** HorneroOS is a
development preview that runs on the maintainers' machines. This
checklist is the single gate list for calling anything a release;
an item is PASS only with linked evidence, never by intention.

Last reviewed: 2026-10-20.

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
  Snapshot/rollback backend is a spike (HorneroOS/hornero#179);
  update lanes open (HorneroOS/hornero#178, #62).
- **Hermes Companion functional — PASS.**
  Loopback gateway, manual approvals, Hornero skill, Javi chat
  with sessions, attachments, voice path and activity trace;
  verified live on the dev host. End-user packaging still open
  (HorneroOS/hornero#174).
- **Plugin lifecycle — PASS.**
  horneroctl validate/install/list/enable/disable/remove with
  receipts and pinned revisions; shell runtime slices merged.
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
- **Performance baseline — FAIL.**
  No published numbers; HorneroOS/shell#47, #228 open. No
  performance claims until measured.
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
