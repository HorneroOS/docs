# ArtCraft Launcher (experimental)

ArtCraft Launcher is an early-alpha, experimental Studio application
from the ArtCraft project. It installs and updates the Craft
applications; which applications exist is decided by the launcher and
can change without a HorneroOS update, so HorneroOS never lists or
counts them.

## Opt-in only

The launcher is a single optional Studio application
(`artcraft-launcher`). It is never installed by choosing a Studio
specialization or a broad workload, and the HorneroOS installer never
downloads it. Recording the choice only records your intent:

```bash
horneroctl studio selection set --application artcraft-launcher
horneroctl studio app show artcraft-launcher --json
```

The second command reports whether the launcher's desktop file
(`ai.storyteller.artcraft-launcher`) is present. Its version and update
state are reported by the launcher itself.

## Install

Installation is manual and user-approved, following the English
runbook in HorneroOS/hornero (`docs/studio-artcraft.md`): download the
catalogue-pinned signed vendor Arch package, verify the pinned
release-signing fingerprint and SHA256 sums, and only then install it
with `pacman -U`. A failed verification stops the install. Do not
install releases that HorneroOS has not pinned and verified.

## Updates and drift

The launcher updates itself and its Craft applications outside the
system package repositories. HorneroOS does not pin, mirror, or roll
back those updates, so the installed version can drift from the
catalogue pin; that is expected for this experimental entry, and the
launcher is the source of truth for its own state.

## Uninstall

Remove Craft applications from inside the launcher first, then remove
the launcher package (`pacman -R ai.storyteller.artcraft-launcher`)
and delete any leftover user-local files (for example an AppImage copy
in `~/Applications` and launcher-managed data you no longer want).
Removing the Studio selection in `horneroctl` or Control Center never
uninstalls anything by itself.

## Prerequisites and troubleshooting

A native Wayland session with `xdg-desktop-portal` and the Hyprland
portal backend (plus the GTK backend for file dialogs) is required.
If an AppImage build is used instead of the package, it additionally
needs working FUSE or `APPIMAGE_EXTRACT_AND_RUN=1`. Crashes and Craft
application bugs are upstream issues: report them to the ArtCraft
project with the launcher's own logs.

## Status and trademark

HorneroOS acceptance for this entry is tracked in HorneroOS/qa#36 and
stays pending until real Studio Preview evidence exists; nothing here
is a support claim. ArtCraft, the ArtCraft name and the A mark are
trademarks of the ArtCraft Team, used only unmodified as part of the
unmodified launcher; they are not licensed under MIT or Apache-2.0.
The installer itself remains the future Panda Foss installer's
ownership boundary — Calamares is only the provisional bridge.
