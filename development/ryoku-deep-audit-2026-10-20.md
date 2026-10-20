# Spike: How does Ryoku's desktop experience compare to HorneroOS, and where must Hornero be decisively better?

**Owner:** HorneroOS maintainers (AI-assisted audit)
**Timebox:** 2026-10-20 session
**Status:** Complete

## Purpose

Ryoku (github.com/Ryoku-dev/ryoku, audited at HEAD 98a0368) is the
closest open-source reference for an AI-native, Quickshell-based
Linux desktop with a Hub settings surface, a federated launcher, and
the Rashin/Hermes companion. This spike answers: which of its
strengths does HorneroOS already match or beat, which are real gaps,
and what is the implementation strategy for closing them without
copying its architecture wholesale.

## Approach

- Multi-agent read-only audit of the Ryoku tree (launcher/bar,
  widgets/plugins/themes, DevEx/installer, Hub schema) against the
  HorneroOS shell/hornero trees, with every claim tied to inspected
  files (see References).
- Gap reconciliation against the live GitHub backlog
  (HorneroOS/shell, HorneroOS/hornero), creating only issues that did
  not exist.
- Implementation in dependency order: real backends first
  (horneroctl), then Control Center panes, each live-verified on the
  development host.

## Findings

1. **Chat/AI.** Ryoku's Needle/PanelChat streams inline answers and
   has session lists and model pickers; Rashin copies a static
   system-knowledge vault (408 schema rows) into agent context.
   Hornero already beats this on truthfulness (live
   `horneroctl assistant tools --json` catalogue, authenticated
   loopback transport, never-auto-approved actions) and now on
   parity basics (streaming NDJSON, attachments, voice path,
   persistent history). Sessions/model UI is tracked in
   hornero#189; the knowledge-vault pattern is answered by generated
   snapshots (hornero#191, slice 1 shipped) instead of hand copies.
2. **Launcher.** Ryoku federates 12 providers behind a prefix
   dispatcher. Hornero had apps + calc/scheme/theme prefixes and a
   fire-and-forget `>ai`. Shipped since: `>win` window provider
   (shell#252) and `>file` bounded file provider (shell#253, no
   indexing daemon by design). Remaining: inline streamed AI and
   plugin-defined providers (shell#250).
3. **Settings depth (Hub).** Ryoku's Hub exposes deep per-area
   surfaces (windows, keybinds, capture). Hornero's Control Center
   reached 24 real panes in this pass — Displays (#249), Input
   (#249), Windows geometry with a new horneroctl writer (#196 +
   #254), Night Light (#259) — each bound to confirmed CLI backends,
   never decorative toggles. Remaining: focus/float rules (#235),
   keybinds pane on the Lua-aware read model (#236 + hornero#176,
   parser shipped in hornero PR#202), capture/performance (#237).
4. **Widgets/plugins/themes.** Ryoku ships 7 desktop widgets, a
   plugin kit with discovery, and a signed package repo; its docs
   claim 57 themes while the audited tree lists 10 static +
   dynamic — an unresolved docs/code drift worth not repeating.
   Hornero has PluginKit + lifecycle (shell#222, partial) but no
   plugin signing/provenance or registry design (shell#251), and
   widget placement/persistence is partial in #222.
5. **DevEx/installer.** Ryoku is a monorepo with signed repo/ISO
   and a dry-run matrix; Hornero's installer is Calamares-provisional
   (Panda Foss-owned), no install-to-first-boot evidence yet — the
   honest readiness gap, tracked in HorneroOS/installer, not closable
   from the shell.
6. **Safety lesson (own finding).** Restarting Quickshell while the
   in-shell session lock is engaged orphaned the compositor lock and
   forced a reboot (shell#255, closed): horneroctl now refuses
   stop/restart while locked, probing the shell IPC because logind
   LockedHint stays "no" under the shell lock on Hyprland.

## Recommendation

Keep Hornero's architecture (single shell process, horneroctl-owned
backends, live tool catalogue over copied vaults) and close the
remaining Ryoku-parity gaps in this order:

1. hornero#189 sessions/model backend contract, then panel pickers.
2. shell#250 inline streamed AI in the launcher.
3. shell#236 keybinds pane on the hornero#176 read model.
4. shell#222/#251 plugin placement, signing and provenance.
5. shell#237 capture/performance with measured numbers only.

## Tradeoffs

- Bounded on-demand file search (no daemon) trades instant results
  for privacy and zero idle cost; revisit only with user-visible
  indexing controls.
- Generated knowledge snapshots trade a small regeneration step for
  never-stale agent context; preferable to Rashin-style static
  vaults.
- Refusing shell restarts while locked trades convenience for a
  session that cannot lose its lock surface; unlock-first is the
  correct UX.

## Open questions

- Ryoku's 57-vs-10 theme drift: stale docs or an external theme
  store not in the audited tree (unresolved upstream).
- Lock resilience if the shell process crashes while locked
  (shell#257): dedicated lock process vs supervised relock —
  needs a prototype, not yet scheduled.
- Hermes end-user setup packaging (hornero#191 slice 2, gated on
  hornero#174 lifecycle decisions).

## References

- Ryoku: https://github.com/Ryoku-dev/ryoku (HEAD 98a0368)
- HorneroOS/shell issues #220–#260, HorneroOS/hornero #176, #189–#202
- `development/competitive-capability-matrix.md`,
  `development/hermes-assistant-architecture.md`,
  `development/backlog-audit-2026-10-19.md` (this repo)
- HorneroOS/shell `docs/LOCKING.md`, `docs/NOTIFICATIONS.md`
