# Incident: session-lock crash after shell restart (2026-10-20)

**Severity:** High (forced reboot, no data loss)
**Status:** Mitigated; long-term resilience tracked separately
**Tracking:** HorneroOS/shell#255 (closed), HorneroOS/shell#257 (open)

## Summary

On 2026-10-20 the development host rebooted twice after the graphical
session locked while Quickshell was stopped/restarted for deployment.
When the Quickshell process died, its `WlSessionLock` surface died with
it, Hyprland fell back to its crashed-lockscreen recovery screen, and
the only safe recovery was a reboot from a TTY. The user password was
never bypassed and no data was lost.

## Root cause analysis

- The Hornero shell owns the session lock in-process:
  `modules/lock/Lock.qml` creates a single `WlSessionLock` via
  `Lock.requestLock()` (see HorneroOS/shell `docs/LOCKING.md`).
- Stopping or restarting Quickshell therefore destroys the lock surface
  of an already-locked session. The compositor cannot re-create that
  surface from a new process, so it shows the crashed-lockscreen
  fallback and the session is unrecoverable in place.
- Contributing factor: the restart was issued during long CI waits
  while the session had idle-locked, so the lock state was not obvious
  from the operator side.
- Detection gap found during the fix: logind `LockedHint` stays `no`
  under the shell lock on Hyprland, and a running `hyprlock` process
  may not exist at all (the lock is the shell's own surface). Neither
  signal alone can be trusted to mean "not locked".

## Fix shipped

1. `horneroctl shell stop|restart` now refuses while the session is
   locked (HorneroOS/hornero PR #197). `--dry-run` stays allowed so the
   plan can be inspected.
2. The authoritative lock probe is the shell itself:
   `qs ipc call lock isLocked`, tried against the caller's
   `QS_CONFIG_PATH` first and then the resolved shell config directory
   (HorneroOS/hornero PR #199). logind `LockedHint` and a `hyprlock`
   process probe remain only as fallbacks; all probes fail open so a
   probe error never blocks an unlocked restart.
3. Live proof on the affected host: with the shell lock engaged, the
   rebuilt `horneroctl` refused `shell stop --yes` with "refusing to
   stop the shell while the session is locked" and the lock stayed
   engaged.
4. Operator rule documented in HorneroOS/shell `docs/LOCKING.md`:
   never stop/restart Quickshell while locked; unlock first. Recovery
   from an already-crashed lock is TTY-only and documented there.

## What did not work

- Trusting logind `LockedHint`: it reported `no` while the shell lock
  was visibly engaged.
- Trusting a `hyprlock` process probe: the lock belongs to the shell
  process, so no `hyprlock` process exists in this configuration.

## Remaining risk

If the shell process crashes spontaneously while locked (OOM, segfault),
the same compositor fallback can still occur; no QML or CLI change can
repair an orphaned compositor lock after the fact. HorneroOS/shell#257
tracks evaluating resilience options (for example a minimal external
lock supervisor) without weakening the lock's security model.

## Prevention checklist

- Unlock the session before any `horneroctl shell stop|restart`.
- Rely on the built-in refusal; do not add `--force`-style bypasses.
- After any shell restart on a host, confirm with
  `qs ipc call lock isLocked` and `horneroctl shell status --json`.
- Keep `MemoryMax` caps on local builds so a build cannot OOM the
  shell process while the session is locked.
