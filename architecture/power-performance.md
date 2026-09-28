# Power and performance

How the desktop *feels*: how fast it gets to first frame after login,
how quiet it idles, and whether interactions stay smooth while the
shell is doing real work.

## One rule

A performance change lands with a number or it does not land. Measure,
change, measure again; keep the change only if the number moved. Close
tickets with measurements, not theories.

## The baseline (cheapest item, do it first)

On a clean reference session, record:

- login to first painted shell surface
- per-surface frame cost while idling, while animating, while playing audio
- resident memory of every QML process and daemon at login
- idle CPU and power draw

How with what exists today: `systemd-analyze` for the boot chain,
`horneroctl shell logs` for shell-side timings, and the native
`horneroctl apps performance` suite (`startup`, `memory`, `benchmark`,
`report`, `mode`). What is missing is the committed reference run: the
`performance report` output recorded on reference hardware and checked
in where reviewers can see it — that table is the deliverable, not a
one-off measurement.

Done means: one committed script, baseline recorded on reference
hardware, numbers visible in the repo (not in someone's notes).

## Budgets to defend

- Cold login-to-first-surface: must not regress without a number
  justifying it.
- Idle cost: no always-on analyzers, pollers, or animations when the
  desktop is at rest; expensive work pays on first use, not at login.
- Update cost: `horneroctl` operations stay off the frame path; heavy
  reconciliation (doctor, snapshots) never blocks login.

## Where the costs live

- QML parse/compile at login, per surface (shell, hub-style surfaces,
  lockscreen each pay it).
- Eager singletons that initialize before anything is visible.
- Wallpaper analysis and palette generation on the login path.

The implementing work lands in [HorneroOS/shell][shell] and
[HorneroOS/hornero][hornero]; this page owns the numbers.

[shell]: https://github.com/HorneroOS/shell
[hornero]: https://github.com/HorneroOS/hornero
