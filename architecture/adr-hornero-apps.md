# ADR: Hornero Apps architecture and software provenance

- **Status:** Accepted
- **Date:** 2026-11-28
- **Tracking:** `HorneroOS/docs#166`, `HorneroOS/hornero#506`

## Context

HorneroOS is an Arch-based, Wayland-first desktop operating system family
built across collaborating repositories: `HorneroOS/hornero` (`horneroctl`),
`HorneroOS/shell` (Quickshell Qt6/QML), `HorneroOS/config`, and
`HorneroOS/docs`. Users install software across multiple ecosystems: native
Arch repositories (`core`, `extra`, `multilib`), Flatpak on Flathub,
AppImages, vendor-hosted Linux channels, web applications, and opt-in AUR
builds.

Asking desktop users to remember which package format owns each app fails in
practice. On 2026-11-28, live verification against `pacman -Si`, Flathub API
v2, and AUR RPC v5 across 206 core applications and 68 AI applications showed
how fragmented Linux app availability is:

- Core catalog (206 apps): 116 `arch_official`, 137 on Flathub (only 74
  verified, 63 unverified community builds), 75 on AUR, and 12 web apps.
- AI tools, IDEs, and CLIs (68 apps): 7 `arch_official`, 7 `flathub_verified`,
  27 `vendor_official_binary`, 9 `vendor_official_repo`, 6
  `community_package`, 11 `official_web_app`, and 1 `hornero_official`.

No single format covers all of these safely. An app store for HorneroOS must
unify discovery across formats, expose honest provenance, respect Arch's
rolling upgrade invariants, and avoid reimplementing package managers.

## Options evaluated

### Software stores and management tools

| Tool | Stack / Backend | Arch safety | Verdict |
| --- | --- | --- | --- |
| Bazaar | GTK4, Flatpak | Safe (Flatpak only) | Flatpak-only UX |
| GNOME Software | GTK4, PK + Flatpak | Risky (PackageKit) | Rejected |
| KDE Discover | Qt, PK + Flatpak | Risky (PackageKit) | Rejected |
| COSMIC Store | Rust, PK + Flatpak | Risky (PackageKit) | Rejected |
| Gear Lever | GTK4, AppImage | Safe (user-space) | AppImage companion |
| Flatseal | GTK4, Flatpak | Safe (overrides) | Permission editor |
| Hornero Apps | QML + V CLI | Safe (direct pacman) | Selected |

Notes on evaluated tools:

- **Bazaar (`usebazaar.org`):** Clean Flathub store UX, but it handles only
  Flatpak and runs as a separate GTK4 window without native Arch, AppImage,
  or WebApp coverage.
- **GNOME Software, KDE Discover, COSMIC Store:** Rely on PackageKit (`PK`)
  for distro packages and introduce GNOME, KDE Frameworks, or `libcosmic`
  stacks outside Hornero Shell.
- **Gear Lever and Flatseal:** Solve single user-space jobs well and are
  reused alongside Hornero Apps for AppImage lifecycle and Flatpak
  permission overrides.

### Packaging and metadata ecosystems

| Technology | Role | Arch fit | Verdict |
| --- | --- | --- | --- |
| `pacman` / ALPM | System packages | Native, signed DBs | Core (`pkexec`) |
| PackageKit | Generic daemon | Partial-upgrade risk | Rejected |
| Flatpak + Flathub | Sandboxed GUI | Rootless + portals | Primary sandbox |
| AppStream | Catalog meta | Enriches repo/Flatpak | Reused |
| AppImage | Single binaries | No sandbox, FUSE | Gear Lever |
| AUR | `PKGBUILD` | Unreviewed, ABI drift | Opt-in only |
| Snap | `snapd` squashfs | Root daemon, AppArmor | Disabled |

### Distribution and platform patterns

| Platform | Pattern | Adopted | Not adopted |
| --- | --- | --- | --- |
| Bazzite / uBlue | Flathub + Bazaar | Verified tiers | `bootc` rollback |
| Omarchy | Arch + Hyprland | Wayland + WebApps | Static dotfiles |
| CachyOS / EOS | `pacman` + welcome | Profile bundles | GUI AUR helpers |
| Garuda | Arch + Chaotic-AUR | Fast onboarding | 3rd-party repo |
| Fedora / Mint | Verified Flatpak | Verify badges | PackageKit |
| Pop!_OS | COSMIC + Flatpak | Source selector | `.deb` paths |
| SteamOS | Immutable + Flatpak | OS/app split | A/B appliance |
| macOS App Store | Gatekeeper tiers | Trust labels | Walled garden |
| Windows Winget | `import` / `export` | JSON manifests | Unverified repo |

## Decision

HorneroOS adopts **Hybrid Native Hornero Apps**: a thin Quickshell Qt6/QML
surface driven by a typed `horneroctl store` engine in V and a canonical
declarative catalog at `catalog/apps.v1.json`.

### Three-layer architecture

1. **Quickshell Qt6/QML surface (`HorneroOS/shell`)**: Renders the Hornero
   Apps browser, Launcher catalog search (**Ctrl + Space**), and Hornero
   Welcome workstation profile picker using Hornero Signal tokens. It holds
   no package logic and delegates every query and mutation to `horneroctl store`.
2. **Typed `horneroctl store` engine (`HorneroOS/hornero`)**: Implements
   read-only inspection (`search`, `list`, `show`, `categories`, `collections`,
   `profiles`, `profile-show`, `installed`, `sources`, `doctor`) and gated
   mutations (`install`, `remove`, `update`, `launch`, `permissions`,
   `appimage`, `webapp`, `policy`, `manifest`, `queue`, `gui`). Every mutation
   supports `--dry-run` and requires `--yes` or interactive UI confirmation.
3. **Canonical declarative catalog (`catalog/apps.v1.json`)**: Stores app IDs,
   provenance, availability per source, licenses, workstation profiles, and
   compatibility notes. It aligns with `editions/catalogue.yaml` so edition
   defaults and store metadata never drift apart.

### Reused execution engines

Rather than inventing new package formats or daemons, `horneroctl store`
orchestrates mature host engines:

- **Native Arch (`pacman` via Polkit)**: Runs `pkexec pacman` directly without
  PackageKit, reusing `package_safety.v` lock and disk-space preflight
  checks. Installing native repo packages enforces a synced system (`-Syu`)
  rather than partial `-Sy pkg` installs.
- **Flatpak + Flathub + AppStream + Flatseal**: Uses user or system Flatpak
  for sandboxed GUI apps, reads AppStream metadata for rich descriptions,
  surfaces Flathub verification status, and opens or wraps Flatseal for
  permission overrides (`horneroctl store permissions`).
- **User-space AppImage + Gear Lever**: Places AppImages in `~/Applications`,
  verifies catalog SHA-256 digests when pinned, checks FUSE readiness, and
  integrates with Gear Lever (`it.mijorus.gearlever`) for desktop entries
  and updates.
- **Extended `webapp.v` for PWAs and Web Apps**: Extends
  `cli/modules/hornero_core/webapp.v` to generate isolated XDG
  `hornero-webapp-<id>.desktop` entries with dedicated browser profile
  directories (`--user-data-dir`) and validated app IDs.
- **Strictly gated opt-in AUR**: AUR installs remain disabled by default.
  Users must opt in explicitly, inspect the `PKGBUILD`, and build as an
  unprivileged user via `makepkg`.
- **Snap disabled by default**: `snapd` is not shipped, not enabled, and
  excluded from the default catalog sources.

### Why PackageKit is rejected on Arch

PackageKit maintains an asynchronous background cache and exposes generic
install verbs that encourage updating package lists and installing a single
package without upgrading the rest of the system. On a rolling release like
Arch Linux, that partial-upgrade pattern breaks shared libraries (`glibc`,
`openssl`, `icu`) and leaves the system unbootable or broken after reboot.
Calling `pacman` directly through `pkexec` preserves Arch's full-upgrade
invariant, exposes real conflict prompts, and shares the same preflight logic
already tested in `horneroctl package upgrade`.

### Why Snap is disabled by default

Snap requires a persistent root daemon (`snapd`), squashfs loop mounts, and
AppArmor confinement hooks that are not active on default Arch/HorneroOS
kernels. It also couples software discovery to a single store backend and
creates portal and font-theming duplication under Wayland compositors such as
Hyprland and Niri. Flatpak + Flathub, native Arch packages, and AppImage
cover the same desktop software with cleaner Wayland and rootless support.

### Provenance and status taxonomy

Every entry in `catalog/apps.v1.json` carries one of eight canonical
provenance values and one of eight status values.

| Provenance value | Meaning | UI badge |
| --- | --- | --- |
| `arch_official` | Arch `core`, `extra`, or `multilib` | Official |
| `hornero_official` | Built in `HorneroOS` repos | Official |
| `vendor_official_repo` | Signed vendor repo or OCI channel | Official |
| `vendor_official_binary` | Vendor-signed tarball or AppImage | Official |
| `flathub_verified` | Flathub `verified == true` build | Verified |
| `flathub_community` | Unverified community Flathub build | Community |
| `community_package` | Community AUR or 3rd-party build | Community |
| `official_web_app` | Vendor web app via `webapp.v` | Web App |

Note on AI verification records: `apps-ai-verified.json` also marks
third-party wrappers with `unofficial_wrapper` for triage. In the user-facing
store catalog, those entries are blocked by default or shown only under
community review.

Status values match the verified catalog contract:
`installable_validated`, `installable_with_limitations`,
`community_maintained`, `official_web_app`, `guided_setup_required`,
`unsupported`, `deprecated`, and `pending_verification`.

## Consequences

### Positive

- Users search and install apps by name and provenance badge instead of
  guessing whether an app lives in `extra`, Flathub, or as a web app.
- Native Arch integrity stays intact because PackageKit is never used and
  Chaotic-AUR is never enabled by default.
- Teams and enterprises can enforce `verified-only` or `open-source-only`
  policies and apply declarative manifests cleanly.
- The Quickshell store UI stays lightweight and testable because business
  logic and safety gates live in typed V code.

### Negative and honest boundaries

- Maintaining `catalog/apps.v1.json` adds curation overhead; automated CI
  checks against Arch, Flathub v2, and AUR RPC v5 must catch drift and
  stale entries.
- Hornero Apps does **not** provide universal OS or application rollback
  today (`snapshot_backend_name` is `none`; see
  [Updates and recovery](../desktop/updates-and-rollback.md)).
- Proprietary software (such as Steam, Cursor, ChatGPT Desktop, and REAPER)
  is never redistributed by HorneroOS; users install directly from upstream
  sources after explicit license opt-in.

## References

- [Hornero Apps threat model](hornero-apps-threat-model.md)
- [Hornero Apps user guide](../desktop/hornero-apps.md)
- [Editions and package composition](editions.md)
- [Updates and recovery](../desktop/updates-and-rollback.md)
- [Security and privacy](../security/README.md)
