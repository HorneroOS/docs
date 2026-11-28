# Hornero Apps

Hornero Apps gives you one place to discover, inspect, install, update, and
launch software across Arch Linux repositories, Flathub, AppImages, official
vendor channels, and isolated Web Apps without needing to memorize package
formats.

It combines the Quickshell Hornero Apps interface, Launcher integration,
Hornero Welcome workstation profiles, and the `horneroctl store` command-line
engine backed by a signed declarative catalog (`catalog/apps.v1.json`).

> **System boundary and rollback:** Hornero Apps does **not** create system
> snapshots or provide universal OS rollback today. Native Arch installs and
> upgrades remain one-way operations on disk; see
> [Updates and recovery](updates-and-rollback.md) before modifying system
> packages.

## Discovery across formats

Instead of switching between `pacman`, `flatpak`, browser bookmarks, and
downloaded binaries, search by application name or workflow category:

- **Native Arch (`core`, `extra`, `multilib`):** Fast host binaries installed
  through `pacman` and Polkit (`pkexec`), enforcing full-system sync (`-Syu`)
  so partial upgrades never break shared libraries.
- **Flatpak and Flathub:** Sandboxed desktop applications with AppStream
  descriptions and explicit verification status.
- **Official vendor channels:** Signed vendor repositories (such as OpenAI's
  Arch repo for ChatGPT Desktop), vendor OCI Flatpak repos (such as ArtCraft),
  and vendor-signed tarballs or installers.
- **AppImage:** User-space portable executables stored in `~/Applications`,
  verified by SHA-256 when pinned, and integrated via Gear Lever
  (`it.mijorus.gearlever`).
- **Web Apps:** Dedicated browser app windows (`hornero-webapp-<id>.desktop`)
  with isolated per-app browser profiles so cookies and permissions stay
  separated.
- **Opt-in AUR:** Disabled by default. Community `PKGBUILD` recipes require
  explicit opt-in, manual `PKGBUILD` review, and non-root `makepkg` builds.

Snap (`snapd`) is disabled by default and excluded from standard discovery.

## Provenance badges and honest limits

Every entry in Hornero Apps displays a provenance badge so you know who built
and signed the package before installing it.

| UI badge | Catalog provenance | Meaning |
| --- | --- | --- |
| **Official** | `arch_official` | Arch `core`, `extra`, or `multilib` |
| **Official** | `hornero_official` | Built in `HorneroOS` repos |
| **Official** | `vendor_official_repo` | Signed vendor repo or OCI channel |
| **Official** | `vendor_official_binary` | Vendor-signed tarball or AppImage |
| **Verified** | `flathub_verified` | Flathub `verified == true` build |
| **Community** | `flathub_community` | Unverified community Flathub build |
| **Community** | `community_package` | Community AUR `PKGBUILD` recipe |
| **Web App** | `official_web_app` | Isolated `webapp.v` browser profile |

Hornero Apps also distinguishes **AppImages** and **native packages** (which
run unsandboxed with normal user permissions) from **Flatpak** apps (which run
in a portal-mediated sandbox).

### Honest compatibility notes

Package availability does not mean universal feature parity on Arch Linux:

- **ChatGPT Desktop:** OpenAI provides an official Linux preview/beta with a
  signed Arch Linux bootstrap repository (`[openai-chatgpt]`, package
  `chatgpt-bin`, signing key `3BFA0E4AE8B8CC16A2D9BA684A3B4A566C4660E4`,
  `x86_64` and `aarch64`). Because it is preview software using an external
  vendor repo, it is marked `installable_with_limitations`.
- **Claude Desktop:** Anthropic's official Linux beta supports Ubuntu 22.04+
  and Debian 12+ (`x64`/`arm64`) only. There is **no** official Arch package.
  On HorneroOS, the official vendor paths are **Claude Code CLI**
  (`claude-code`) or **`https://claude.ai`** (`official_web_app`). The AUR
  `claude-desktop` recipe is a `community_package` repackaging the `.deb`
  (and Cowork requires KVM plus 8+ GiB RAM).
- **Google Antigravity:** Ships five official surfaces: Antigravity App,
  Antigravity IDE, Antigravity CLI (`agy`), IDE extensions (VS Code and
  JetBrains), and Python SDK (`google-antigravity`). Official Linux App and
  IDE builds ship as `.tar.gz` archives; community AUR desktop packages can
  lag upstream releases.
- **ArtCraft Launcher and Studio:** Not listed on Flathub. Upstream ships an
  official signed Arch `.pkg.tar.zst`, an official OCI Flatpak repository
  (`getartcraft.com/artcraft-oci.flatpakrepo`), and an AppImage. It remains an
  experimental manual opt-in; see [ArtCraft Launcher](../applications/studio-artcraft.md).
- **Gaming anti-cheat:** Kernel-level anti-cheat is unsupported on Linux.
  Easy Anti-Cheat and BattlEye work only when the game publisher enables
  Proton support; see [Gaming applications](../applications/gaming.md).
- **No universal rollback:** Removing a Flatpak or WebApp is clean in user
  space, while native `pacman` transactions modify the host root without a
  system restore point.

## Using Hornero Apps

### Hornero Apps UI and Launcher search

Open the graphical store from the Launcher or directly from a terminal:

```sh
horneroctl store gui
```

Inside the Launcher (**Ctrl + Space**), typing an application name searches
installed desktop entries first and surfaces installable matches from the
Hornero Apps catalog underneath with their provenance badge. Queued GUI
installations and updates can be inspected with `horneroctl store queue`.

### Hornero Welcome workstation profiles

During first setup or when provisioning a new discipline, Hornero Welcome and
`horneroctl store profiles` group applications into curated workstation
profiles (such as Everyday, Developer, Creative Studio, Gaming, and AI
Workstation). Inspect a profile before installing anything:

```sh
horneroctl store profiles
horneroctl store profile-show ai-workstation --json
```

Profiles preview every package, source, and license first and never install
proprietary or AUR entries without explicit confirmation.

### AppImage import and Gear Lever

Import a vendor AppImage into `~/Applications`, verify its SHA-256 digest
when known, and create an XDG desktop entry:

```sh
horneroctl store appimage list
horneroctl store appimage add ./MyApp.AppImage --sha256 <hex> --yes
```

Hornero Apps detects FUSE readiness (`fuse2`/`fuse3`) and pairs with Gear
Lever (`it.mijorus.gearlever`) when installed so AppImages keep clean icons
and update metadata. Remember that AppImages are **not** sandboxed.

### Web Apps with isolated profiles

Create or manage standalone web apps backed by `hornero_core/webapp.v`:

```sh
horneroctl store webapp list
horneroctl store webapp add claude-web \
  --name "Claude" --url "https://claude.ai" --yes
```

Each WebApp receives a sanitized `hornero-webapp-<id>.desktop` file and an
isolated browser `--user-data-dir`, keeping site storage and login cookies
away from your primary browser session.

### Flatpak permissions and Flatseal

Inspect Flatpak permissions for an installed sandboxed app or launch Flatseal
focused on its app ID:

```sh
horneroctl store permissions ai.jan.Jan
```

Prefer granting narrow portal permissions (documents, Wayland, audio) rather
than blanket `--filesystem=host` access.

## CLI reference (`horneroctl store`)

All read-only commands support `--json`. Mutating commands accept `--dry-run`
to preview changes and `--yes` to confirm execution.

```sh
# Catalog discovery and inspection
horneroctl store search "obsidian"
horneroctl store list --category "Creative Studio"
horneroctl store show md.obsidian.Obsidian --json
horneroctl store categories
horneroctl store collections
horneroctl store profiles
horneroctl store profile-show creative-studio

# Local state, lifecycle, and launching
horneroctl store installed
horneroctl store install md.obsidian.Obsidian --dry-run
horneroctl store install md.obsidian.Obsidian --yes
horneroctl store update --dry-run
horneroctl store remove md.obsidian.Obsidian --yes
horneroctl store launch md.obsidian.Obsidian

# Sources, formats, queue, UI, and diagnostics
horneroctl store sources
horneroctl store permissions ai.jan.Jan
horneroctl store appimage list
horneroctl store webapp list
horneroctl store queue
horneroctl store gui
horneroctl store doctor
```

## Enterprise and team provisioning

Teams managing shared workstations can enforce trust boundaries, reproduce
software stacks declaratively, and audit every install decision.

### Software trust policies (`horneroctl store policy`)

Restrict which provenance tiers and package sources may be installed on a
machine:

```sh
# Inspect active policy
horneroctl store policy show --json

# Allow only Official and Verified Flathub entries
horneroctl store policy set --mode verified-only --yes

# Restrict to OSI/FSF-approved open-source licenses
horneroctl store policy set --mode open-source-only --yes

# Allow explicit sources only (blocks AUR and unverified Flathub)
horneroctl store policy set \
  --allowed-sources arch_official,hornero_official,flathub_verified --yes
```

Policy enforcement runs inside `horneroctl store` before any transaction
starts and also blocks AI assistants from proposing disallowed sources.

### Declarative manifests (`horneroctl store manifest`)

Export an existing workstation's app selection and apply it across new
machines cleanly:

```sh
# Export current store-managed apps and policy to a manifest
horneroctl store manifest export ./team-workstation.json --yes

# Preview what a manifest would install on another host
horneroctl store manifest apply ./team-workstation.json --dry-run

# Import and apply with explicit confirmation
horneroctl store manifest import ./team-workstation.json --yes
horneroctl store manifest apply ./team-workstation.json --yes
```

### Audit log (`audit.jsonl`)

Every store mutation (`install`, `remove`, `update`, `policy`, `manifest`,
`sources`) appends a structured JSON record to the user XDG state directory
(`~/.local/state/hornero/store/audit.jsonl`) containing the timestamp, action,
app ID, resolved source, provenance tier, policy decision, and outcome.

## Catalog contribution and governance

Applications in Hornero Apps live in `catalog/apps.v1.json`. Contributors add
or update entries through pull requests rather than ad-hoc edits.

### Submission rules

1. **Verified identifiers only:** Include exact Arch repo package names,
   Flathub app IDs, official vendor release URLs, or official web app URLs.
2. **Accurate provenance and status:** Match the 8-tier provenance taxonomy
   and mark preview, experimental, or distro-limited apps honestly with
   `installable_with_limitations`, `community_maintained`, or
   `guided_setup_required`.
3. **License and trademark compliance:** Record the exact SPDX or proprietary
   license identifier. Never add mirror links for proprietary binaries or
   include third-party Chaotic-AUR packages as `arch_official`.
4. **Automated CI validation:** Every catalog PR runs schema validation,
   live checks against Arch package indexes, Flathub API v2 (`verified`
   status), and AUR RPC v5, plus trademark/license checks before maintainers
   sign the published catalog release with `minisign`.

## Related guides

- [ADR: Hornero Apps architecture](../architecture/adr-hornero-apps.md)
- [Hornero Apps threat model](../architecture/hornero-apps-threat-model.md)
- [`horneroctl` CLI overview](horneroctl.md)
- [Security and privacy](../security/README.md)
- [Updates and recovery](updates-and-rollback.md)
