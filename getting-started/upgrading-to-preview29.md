# Upgrading an existing installation to preview29

This addendum moves a system that already followed
[Upgrading an existing preview24 installation](upgrading-from-preview24.md)
(or was installed from preview25–preview28) to the package composition
shipped in **v0.2.0-preview29**, without reinstalling.

Preview29 changes no edition composition. The delta is package-level:

- `horneroctl-bin` `0.2.0_preview37-1`: `horneroctl gaming doctor`
  diagnoses NVIDIA module/kernel coherence (`nvidia-open`, `-lts` and
  `-dkms` variants) and reports it as one check.
- `hornero-config` `0.3.15-1`: the Hyprland environment no longer
  forces `LIBVA_DRIVER_NAME=nvidia`; VA-API auto-selects the driver
  for the GPU that is actually present.

## Steps

1. Upgrade Arch packages (full upgrade, never a partial one):

   ```bash
   sudo pacman -Syu
   ```

2. Update the HorneroOS AUR packages. AUR packages are **not** updated
   by `pacman -Syu` or by `horneroctl package upgrade`; rebuild them
   with your AUR helper or manually, for example:

   ```bash
   git clone https://aur.archlinux.org/horneroctl-bin.git
   cd horneroctl-bin
   # horneroctl-bin verifies its signed binary against the HorneroOS
   # release key (fingerprint
   # FCFBEE43925AB5429362278AE59EAB44AA2498DC, pinned in validpgpkeys).
   # The key ships with the package; import it once so makepkg can
   # verify. AUR helpers (yay/paru) can also fetch it automatically
   # from public keyservers. Never build with signature checks off.
   gpg --import keys/pgp/*.asc
   gpg --list-keys FCFBEE43925AB5429362278AE59EAB44AA2498DC
   makepkg -si
   cd ..
   git clone https://aur.archlinux.org/hornero-config.git
   cd hornero-config && makepkg -si
   pacman -Q horneroctl-bin hornero-config
   # expect horneroctl-bin 0.2.0_preview37-1, hornero-config 0.3.15-1
   ```

   If the build stops with
   `gpg: keyserver receive failed: No data` or
   `FAILED (unknown public key …)`, the import step above was skipped
   in a keyring that does not have the key yet; run it and rebuild.
   Do not work around it by disabling PGP verification.

3. Log out and back in so the session picks up the new Hyprland
   environment (the VA-API change is session-scoped).

4. Verify:

   ```bash
   horneroctl version            # horneroctl-v0.2.0-preview37
   horneroctl gaming doctor      # Gaming systems; gpu-driver-coherence included
   horneroctl studio doctor      # Studio systems; expect all checks passed
   ```

## Notes for dotfiles users (chezmoi)

Native HorneroOS detection reads `ID=horneroos` from `/etc/os-release`.
Installations migrated from preview24 keep `ID=arch` (see the known
limitations of the preview24 guide), so they are not detected as
native. Where a chezmoi template supports it, preview the migration
with the explicit override and review the diff before applying
anything:

```bash
HORNERO_NATIVE=1 chezmoi diff
```

Do not run a destructive `chezmoi apply` as part of this upgrade;
personal configuration, OBS profiles and user data are not touched by
the package steps above.

## Known limitations

The limitations of the preview24 guide still apply: no edition
reconciliation, no snapshot/rollback integration, and graphics driver
stacks are unchanged by this addendum. `gpu-driver-coherence` only
*reports* a driver/kernel mismatch; it never installs or removes
driver packages.
