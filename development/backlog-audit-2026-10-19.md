# Backlog audit — 2026-10-19

Status: completed audit; issue filing and reconciliation executed
the same day. This report is a summary and index. Issue status
lives on GitHub, not here; the roadmap remains
[hornero#154](https://github.com/HorneroOS/hornero/issues/154).

## Method

- Source-level inspection of every HorneroOS repository plus the
  personal dotfiles repo (entrypoints, modules, tests, CI,
  packaging), at the HEADs below.
- Live GitHub reconciliation: all open issues and PRs fetched
  (28 open issues, 1 open PR at audit start), known issues read
  with comments, recently merged PRs cross-checked against code.
- Upstream study: previously cloned references (Omarchy, Ryoku,
  DankMaterialShell, Noctalia, Hermes Agent at pinned commits)
  plus documentation-level survey of KDE/GNOME/COSMIC, Fedora
  Atomic, NixOS and chezmoi for the capability matrix.
  Documentation-level comparisons are marked as such in the
  issues that rely on them; nothing was cloned or executed from
  upstream installers.
- Independent review pass over every filed issue: ownership,
  template shape, canonical labels (`governance/labels.yml`),
  duplicates, testable acceptance criteria.

## Repository state at audit

| Repo | HEAD | Open issues (before → after) |
| --- | --- | --- |
| HorneroOS/hornero | `63d2752` | 2 → 15 |
| HorneroOS/shell | `2c78e9f` | 3 → 12 |
| HorneroOS/config | `76a552f` | 0 → 3 |
| HorneroOS/installer | `d310242` | 3 → 4 |
| HorneroOS/greeter | `179a99b` | 0 → 1 |
| HorneroOS/qa | `a5e7381` | 0 → 4 |
| HorneroOS/docs | `1f0ca9f` | 0 → 1 (+this report) |
| HorneroOS/website | `fe8c7a0` | 0 → 2 |
| HorneroOS/.github | `74d2143` | 1 → 3 |
| ulises-jeremias/dotfiles | `c156a606` | 19 → 19 (comments only) |

## Top verified findings

1. **Hermes approvals are broken on the wire** (hornero#168):
   the client sends a `decision` key; the pinned upstream
   gateway reads `choice`. Proven from both codebases; no live
   gateway call was performed.
2. **Assistant hardening gaps** filed at requirement level
   (hornero#169 endpoint host validation, #170 CSPRNG key,
   #172 HTTP/SSE bounds, #173 Idempotency-Key). No exploit
   detail is published; `area:security` guidance was followed.
3. **No mock-Hermes contract tests exist** (hornero#171), which
   is how finding 1 shipped. horneroctl CI also runs its tests
   non-blocking today (residual risk noted in the issue).
4. **Installer acceptance is implemented-not-validated**:
   installer#11's fix merged (PR #13) but install-to-first-boot
   has never executed; QA scenarios filed as qa#19.
5. **Preview19 VM smoke/QA evidence is stale** (last bundle
   preview13): qa#16–#18.
6. **Hyprland Lua migration is staged, not active** in dotfiles
   (legacy entrypoint live); product consumers tracked in
   hornero#176/#177 and config#88.
7. **Desktop completeness gaps with no prior issues**:
   Displays, Accessibility, Input panes (shell#220/#221/#226),
   greeter accessibility (greeter#36), PluginKit contract break
   (shell#222 — the validator allows an import the runtime
   cannot satisfy).
8. **Update/rollback remains honestly unimplemented** (#62);
   children filed: hornero#178 (status lane), #179 (snapshot
   spike with VM proof).

## Reconciliation of existing issues

| Issue | Classification | Action |
| --- | --- | --- |
| hornero#154 | partially-completed epic | labels + child index comment |
| hornero#62 | partially-completed | labels + children #178/#179 |
| shell#24 | blocked (upstream) | labels incl. `status:blocked` + evidence |
| shell#47 | implemented-not-validated | labels + remainder shell#228 |
| shell#77 | underspecified | labels + decision request comment |
| installer#11 | implemented-not-validated | staleness comment (PR 13 merged) |
| installer#12 | accurate | left as-is (owner gates) |
| installer#3 | accurate | split note (hornero#180); ISO slice stays |
| .github#9 | blocked (human action) | `status:blocked` + verification issue #2 |
| dotfiles#179/#181–#188 | partially-completed | comment with product-side links |
| dotfiles#170–#178 | maintainer decision pending | re-scope suggestion comment |
| dotfiles#187/#200 | possible duplicates | consolidation comment on #200 |
| dotfiles#201 | superseded path | pointer comment to config#89 |

No issue was closed by the audit: closures require executed
validation evidence, which a research pass does not produce.

## New issues filed (36)

Filed with the organization issue forms (headings, title
prefixes, exactly one `type:*`, at most one `area:*`, priority
per taxonomy) and linked to #154 where applicable:

- hornero: #168–#180 (Hermes correctness/security/tests,
  lifecycle, audit log, Lua consumers, update lane, signing)
- shell: #220–#228 (panes, PluginKit, Companion cancel,
  notifications, night light, IA ADR, perf remainder)
- config: #87 (GTK drift guard), #88 (Lua port), #89 (theme pack)
- greeter: #36 (accessibility)
- qa: #16–#19 (smoke evidence, cadence, scenario matrix,
  installer scenarios)
- docs: #45 (handbook coverage)
- website: #126 (a11y gate), #127 (data-bump CI)
- .github: #19 (contributor onboarding), #20 (AUR verification)
- installer: #14 (label-sync pin)

Duplicates avoided by design: roughly ten audit candidates were
amendments to existing issues (#154, #62, #24, #47, #77, #11,
installer#3, .github#9, dotfiles Lua epic) and were filed as comments/labels
instead of new issues; ISO signing stayed inside installer#3.

## Security handling

Two hardening topics are tracked only at requirement level in
public issues (no bypass forms, payloads, or entropy analysis).
Key-custody work remains in the pre-existing public issues
(.github#9, installer#3, hornero#180) with human actions called
out. Nothing sensitive was posted.

## Unresolved / not covered

- No live VM, graphical session, or real Hermes gateway run was
  performed; graphical and real-Hermes acceptance remain open
  (qa#16–#19, hornero#171).
- GNOME/KDE/COSMIC comparisons are documentation-level and must
  be re-verified before implementing shell#220/#221.
- Unaudited in depth: greeter PAM/session internals, installer
  Calamares privilege model, non-assistant horneroctl surface,
  lock-screen auth internals, printer/user-account panes,
  NVIDIA/hybrid-GPU acceptance. Candidates were filed only
  where evidence existed.
- Whether #154 children should become GitHub sub-issues is a
  maintainer governance choice; links were used instead.

## Suggested sequence

1. M0: hornero#168 + #171 (approval correctness with tests),
   qa#16 (preview19 evidence), installer#11 execution (qa#19).
2. M1: shell#227 (IA ADR) → #220/#221/#226; greeter#36.
3. M2: shell#222 (PluginKit + placement persistence).
4. M3: hornero#174 (lifecycle), #175, shell#223 (real cancel).
5. M0/M4 in parallel: #62 children (#178 → #179), signing
   (#180, installer#3, .github#9 → #20).
