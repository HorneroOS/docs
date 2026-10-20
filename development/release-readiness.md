# Release readiness checklist

**Status: NOT READY for a public launch.** HorneroOS is a development
preview that runs on the maintainers' machines. This checklist is
the single gate list for calling anything a release; an item is PASS
only with linked evidence, never by intention.

Last reviewed: 2026-10-20.

| Gate | Status | Evidence / exact check |
| --- | --- | --- |
| ISO installs on clean hardware/VM | BLOCKED | Installer owned by Panda Foss; no install-to-first-boot evidence yet. HorneroOS/installer#11, #14 |
| Boot to desktop (first boot) | BLOCKED | Depends on the installer gate above; QA scenarios exist in HorneroOS/qa but no passing run against a release ISO |
| Compositor support matrix | FAIL | Hyprland supported; Niri experimental and not validated at parity. Do not advertise parity |
| Package integrity | FAIL | horneroctl release binaries unsigned (HorneroOS/hornero#180); AUR publishes checksums from CI, no signature verification in install flows |
| Safe updates + rollback | FAIL | Snapshot/rollback backend is a spike (hornero#179); update lanes issue open (hornero#178, #62) |
| Hermes Companion functional | PASS | Loopback gateway, manual approvals, Hornero skill, Javi chat with sessions/attachments/voice path/activity trace; verified live on the dev host (docs `development/hermes-assistant-architecture.md`). Packaging for end users still open (hornero#174) |
| Plugin lifecycle | PASS | horneroctl validate/install/list/enable/disable/remove with receipts + pinned revisions; shell runtime slices merged |
| Extensions marketplace | PASS | HorneroOS/plugins (catalogue + SHA-256 + CI), `horneroctl plugin catalog`, Control Center browse/install (HorneroOS/hornero#214, HorneroOS/shell#268). Community listings not yet open (shell#251) |
| Lock/session safety | PASS | `horneroctl shell stop/restart` refuses while locked (shell IPC probe); incident recorded in `development/incident-2026-10-20-session-lock-crash.md`; spontaneous-crash resilience open (shell#257) |
| Accessibility audit | FAIL | Accessible-name audit incomplete (shell#221); Control Center panes keyboard-verified only in part |
| Performance baseline | FAIL | No published numbers; shell#47/#228 open. No performance claims until measured |
| Documentation | PASS | Canonical docs in this repo; website generated catalogue only via pinned `data:bump`/`data:sync` |
| QA acceptance | FAIL | HorneroOS/qa acceptance suite not green against a candidate composition; preview20 remains unpublished candidate |

## Rules

- Never publish an ISO, screenshot, benchmark or compatibility claim
  whose gate is not PASS with evidence.
- Installer gates move only with Panda Foss's acceptance; HorneroOS
  does not self-certify the installer.
- Update this file in the same PR that changes a gate's evidence.
