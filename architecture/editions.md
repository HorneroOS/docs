# Editions and package composition

HorneroOS is organized as one operating-system family. Its editions share a
base and compose roles and capabilities; they are not separate distributions
with copied package scripts.

The canonical product model lives in
[`HorneroOS/hornero`'s edition catalogue](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml).
The resolver at
[`scripts/resolve-edition.py`](https://github.com/HorneroOS/hornero/blob/main/scripts/resolve-edition.py)
turns an edition and optional compositor into a deterministic Arch package
list. It does not build an image or certify the resulting system.

## Composition model

```text
Base + desktop + compositor:hyprland  → Desktop / Hyprland
Base + desktop + compositor:niri      → Desktop / Niri
Base + server                          → Server
Base + server + agent-host             → Agents
Base + desktop + studio                → Studio
```

The same model is independent of the graphical installer. The installer is
not yet a supported consumer, and HorneroOS does not currently publish
installable ISO images.

## Current maturity

- **Desktop — Preview.** Real desktop product and package composition; no
  supported installer or ISO.
- **Hyprland — Supported.** Validated default desktop session.
- **Niri — Experimental.** A single-output VM journey is verified. See
  [Wayland compositors](../desktop/compositors.md) for the gaps.
- **Server — Planned.** A headless package set is described; a bootable image
  and full remote-administration acceptance are not available.
- **Agents — Planned.** Rootless Podman and systemd Quadlet are the direction;
  Hermes provisioning, isolation, secrets, lifecycle, and recovery are not
  certified.
- **Studio — Planned.** A creative package set is described; audio, capture,
  editing, hardware acceleration, and compositor workflows are not certified.
- **Labwc — Planned.** No Hornero backend or package set is offered.

These labels describe product evidence, not whether an upstream package exists
or whether an individual component works on its own.

## Edition intent

- **Desktop** is a Wayland-first desktop powered by Hornero Shell. Hyprland is
  the default validated backend; Niri is experimental.
- **Server** is intended to be a small, remotely operable headless system. Its
  current package proposal excludes graphical Shell and compositor packages.
- **Agents** is intended to extend Server with isolated agent workloads. The
  model forbids exposing a privileged host Docker socket or baking credentials
  into images. Those are design constraints, not a claim that the workload
  runtime is ready.
- **Studio** is intended to extend Desktop with creative-production tools.
  REAPER and Windows VST integrations remain optional, licensed, and
  user-supplied; no personal license or plugin is part of HorneroOS.

## Check package composition

From a checkout of HorneroOS/hornero, inspect the exact package result without
installing anything:

```sh
python3 scripts/resolve-edition.py desktop --json
python3 scripts/resolve-edition.py desktop --compositor niri --json
python3 scripts/resolve-edition.py server --json
python3 scripts/resolve-edition.py agents --json
python3 scripts/resolve-edition.py studio --compositor hyprland --json
```

Package resolution is an architecture check. A product becomes installable
only after its services, runtime behavior, recovery, image or install path,
and acceptance evidence are implemented and tested.
