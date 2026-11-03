# Quality assurance and release engineering

This page is the technical home for how HorneroOS is tested, signed and
released. Product pages describe what HorneroOS does; this page explains how
we know it works, and where the evidence for every claim lives.

It deliberately records no per-release gate status. Status belongs to the
per-release checklists in
[HorneroOS/hornero/releases](https://github.com/HorneroOS/hornero/tree/main/releases),
which are written once per release and never edited afterwards.

## Evidence classes

Every acceptance claim in HorneroOS carries one of four labels. They are not
interchangeable:

- `AUTOMATED-VERIFIED`: a deterministic check or graphical scenario
  executed and recorded the result.
- `SCREENSHOT-VERIFIED`: a human or reviewer inspected a real capture
  of the running system.
- `USER-VERIFIED`: the maintainer reports it working on real hardware
  in daily use.
- `NOT SPECIFICALLY TESTED`: nobody has evidence either way. It is
  never presented as working.

A virtual-machine result is never physical-hardware evidence, and a
screenshot alone never makes a scenario pass: the deterministic runner is
the authority, captures are supporting evidence.

## How graphical acceptance works

[HorneroOS/qa](https://github.com/HorneroOS/qa) boots the exact pinned
shell, config and `horneroctl` revisions — or the exact published ISO — in
disposable QEMU/KVM virtual machines, drives them with synthetic input, and
records an evidence bundle per run: scenario result, screenshots, hashes
and the pinned product revisions.

- Scenario model and failure taxonomy:
  [qa/docs/ARCHITECTURE.md](https://github.com/HorneroOS/qa/blob/main/docs/ARCHITECTURE.md)
- Generated scenario ledger:
  [qa/docs/SCENARIO-MATRIX.md](https://github.com/HorneroOS/qa/blob/main/docs/SCENARIO-MATRIX.md)
- Edition gates that fail closed and never change product maturity by
  themselves:
  [STUDIO-ACCEPTANCE.md](https://github.com/HorneroOS/qa/blob/main/docs/STUDIO-ACCEPTANCE.md),
  [GAMING-ACCEPTANCE.md](https://github.com/HorneroOS/qa/blob/main/docs/GAMING-ACCEPTANCE.md),
  [BLUETOOTH-ACCEPTANCE.md](https://github.com/HorneroOS/qa/blob/main/docs/BLUETOOTH-ACCEPTANCE.md)
- Physical-workstation parity record:
  [qa/docs/PELICANO-PARITY.md](https://github.com/HorneroOS/qa/blob/main/docs/PELICANO-PARITY.md)

Destructive installation tests only ever run against disposable virtual
disks. Physical-hardware checks happen after release, on real machines, and
are recorded with the evidence class that actually applies.

## Release engineering

A HorneroOS release is a composition, not a snapshot of whatever was
installed on a workstation:

1. Each release is described by an immutable manifest in
   [HorneroOS/hornero](https://github.com/HorneroOS/hornero) (`manifests/`),
   resolved from the canonical edition catalogue. Tagged manifests are
   never edited; a new composition means a new release.
2. The five validation gates (manifest checks, pin checks, test suites,
   documentation lint and the executable composition gate) must pass before
   tagging. The process is documented in
   [hornero/docs/RELEASE_PROCESS.md](https://github.com/HorneroOS/hornero/blob/main/docs/RELEASE_PROCESS.md).
3. Packages are built in order — `horneroctl`, config, shell, installer —
   and the ISO is built in a disposable build environment, never on a
   developer workstation's disks.
4. The exact final ISO is installed in disposable VMs (Desktop, Studio and
   Gaming) and exercised at first boot before anything is published.
5. Artifacts are signed with the HorneroOS release key
   `FCFBEE43925AB5429362278AE59EAB44AA2498DC`. Key distribution and the
   human signing step are documented in
   [hornero/docs/RELEASE_SIGNING.md](https://github.com/HorneroOS/hornero/blob/main/docs/RELEASE_SIGNING.md);
   the public key ships in the repository at
   `packaging/keys/hornero-release.pub.asc`, so verification never depends
   on a keyserver.
6. Each release publishes its ISO, SHA-256 checksum, detached signature and
   a checklist recording what passed, what carries forward and what remains
   untested. The derived index is
   [releases/LEDGER.md](https://github.com/HorneroOS/hornero/blob/main/releases/LEDGER.md).

## Verify a download yourself

The [install page](https://www.horneroos.com/install) prints the commands
next to the download. In short: check the SHA-256 against the published
`.sha256`, import the public key from the repository, verify the detached
`.sig`, and confirm the fingerprint above. A tampered copy must fail
verification — that negative case is part of every release checklist.

## Reproduce the tests

Contributors can run the same evidence pipeline locally:

- Per-change, risk-matched checks: see [Testing](testing.md).
- Graphical scenarios: clone
  [HorneroOS/qa](https://github.com/HorneroOS/qa) and follow its README
  quick start (`doctor`, `list`, `run`, `inspect`, `studio-gate`).
  Graphical lanes need a host with KVM; they do not run on standard
  GitHub-hosted runners.
- Website and documentation integrity: the website build runs
  release-truth, data-sync, i18n-parity and internal-link checks, so public
  copy cannot silently drift from the canonical release data.
