# Updates and system rollback

HorneroOS can take your whole system back to how it was before an update.
Before every update it saves a **restore point**; if the update leaves you
with a broken app, a desktop that will not start, or simply a change you
do not like, you pick that restore point and go back to it in one step.

> **Preview.** System rollback is new in this preview. Read
> [Validation status](#validation-status) before you rely on it.

## What a restore point is

A restore point bundles three things that are restored together:

- **The system**: a Btrfs snapshot of the operating system root, which
  holds the installed packages, their files and system settings under
  `/etc`.
- **Your Hornero settings**: the shell configuration (layout, bars,
  appearance and the rest of the Control Center choices).
- **Your Chromatic palette**: the [Hornero Chromatic](chromatic.md) state
  and the files Chromatic generated for your apps.

You do not have to restore the parts one by one. Choosing a restore point
returns all three to the same moment, unless you ask for the system only.

Some things are **never rolled back**, so a rollback cannot lose your work:

- your files in `/home` (documents, downloads, projects, app data);
- system logs in `/var/log`;
- the package cache in `/var/cache` (so packages do not need to be
  downloaded again).

## It is on by default on new Btrfs installs

A fresh Desktop, Studio or Gaming installation on **Btrfs** sets this up
for you: snapshot tools (snapper, snap-pac and grub-btrfs), a separate
snapshot store at `/.snapshots`, a "HorneroOS snapshots" boot menu, and
permission for desktop users in the `wheel` group to list restore points
without typing a password.

Existing installations are **not** converted. If you installed an earlier
preview, or installed on ext4, read
[Installs without Btrfs](#installs-without-btrfs).

Check what your system supports at any time:

```sh
horneroctl recovery doctor
```

On a ready system every check is green and the backend is `snapper`.

## How updates create restore points

When you update from Control Center or run `horneroctl package upgrade
--yes`, HorneroOS:

1. saves your Hornero settings and Chromatic palette;
2. asks once for your password, then takes a system snapshot labelled
   **HorneroOS update** (the *pre* snapshot);
3. runs the full system upgrade (`pacman -Syu`);
4. takes a second snapshot after the upgrade (the *post* snapshot). If the
   upgrade failed, it is labelled **HorneroOS update (failed, exit N)** so
   you can see which update went wrong.

The pre and post snapshots are kept as a pair and linked to the settings
saved in step 1. That pair is what you see as one entry in the update
history. Package installs made outside HorneroOS (for example a plain
`sudo pacman -S`) also get a smaller snapshot pair from snap-pac.

To update without a restore point, turn off
[Snapshot before upgrade](#settings) or run:

```sh
horneroctl package upgrade --no-snapshot --yes
```

## Roll back from Control Center

Open **Control Center → Updates & backups → Update history & rollback**
(or run `horneroctl config gui --pane updates`). The list shows restore
points, newest first, with their date, label and what they contain
(system, Hornero settings, Chromatic palette).

Rolling back has a deliberate two-step guard, because there is no
one-click undo:

1. Select a restore point and choose **Roll back**. Nothing changes yet.
   A panel explains exactly what will happen: the date you return to,
   what goes back to that state, what is kept, and whether a reboot is
   needed.
2. If that is what you want, confirm with **Roll back and reboot later**.

For a restore point that includes the system:

- The new state takes effect **after you reboot**. Keep working, save
  your files, and restart when you are ready.
- Before anything changes, HorneroOS takes one more snapshot named
  **Before rollback to #n** (n is the restore point number). It also
  keeps the root you are leaving as a subvolume named
  `@.pre-rollback-<time>`. Those two are your manual undo: if the older
  state turns out to be worse, roll back to the "Before rollback"
  snapshot the same way.
- Your Hornero settings and Chromatic palette return to the saved state
  right away; a safety copy of the current settings is saved first.

A restore point that holds only Hornero settings and the Chromatic palette
is applied immediately and does not need a reboot.

## When the desktop will not start

If an update leaves you without a working desktop, start an older system
state from the boot menu, then make it permanent:

1. Restart the computer. In the GRUB menu open **HorneroOS snapshots** and
   choose the snapshot from before the update (labelled
   **HorneroOS update**, with its date).
2. The system starts from that snapshot. This is a temporary start:
   changes you make to the system while running it are discarded at the
   next reboot. Your `/home` files are the normal, current ones.
3. Log in, open a terminal and find the number of the restore point:

   ```sh
   horneroctl recovery list
   ```

4. Make it permanent, then reboot normally:

   ```sh
   horneroctl recovery rollback 42 --dry-run
   horneroctl recovery rollback 42 --yes
   ```

   Replace `42` with your restore point number. The dry run shows the same
   explanation as the Control Center panel without changing anything.

If the disk is encrypted with LUKS, starting a snapshot still asks for
your passphrase. A snapshot never skips the encryption.

## Kernel updates

The Linux kernel and its startup image live on the boot partition, outside
the system snapshots. When you roll back across an update that changed the
kernel, HorneroOS copies the kernel stored in the snapshot back to the
boot partition and rebuilds the startup image, so the restored system
starts with the kernel that matches it.

Starting a snapshot from the **HorneroOS snapshots** menu is different: it
uses the kernel that is on the boot partition now. If the update that
broke things also replaced the kernel, an older snapshot started that way
may not find matching kernel modules and can fail to start. In that case
roll back from the Live ISO as described below.

## Roll back from the Live ISO

Use this only when no installed system state starts (for example on a
systemd-boot install, or after a kernel update as described above). It is
the same subvolume swap that `horneroctl recovery rollback` performs, done
by hand. Boot the HorneroOS Live ISO, open a terminal and replace the
device names with yours (`lsblk -f` lists them):

```sh
sudo cryptsetup open /dev/nvme0n1p2 root      # LUKS installs only
sudo mount -o subvolid=5 /dev/mapper/root /mnt  # or the Btrfs partition
ls /mnt/@snapshots                             # find the number, e.g. 42
sudo mv /mnt/@ /mnt/@.pre-rollback-manual
sudo btrfs subvolume snapshot /mnt/@snapshots/42/snapshot /mnt/@
sudo umount /mnt
```

If the update had changed the kernel, also put the matching kernel back
on the boot partition before rebooting (here the boot partition is
`/dev/nvme0n1p1` and the kernel package is `linux`; use yours):

```sh
sudo mount -o subvol=@ /dev/mapper/root /mnt
sudo mount /dev/nvme0n1p1 /mnt/boot
ls /mnt/usr/lib/modules                        # the restored version
sudo cp /mnt/usr/lib/modules/<version>/vmlinuz /mnt/boot/vmlinuz-linux
sudo arch-chroot /mnt mkinitcpio -P
sudo umount -R /mnt
```

Nothing under `@home` is touched by these steps.

## Command-line reference

All of these work without opening Control Center. Read-only commands do
not ask for a password; changing commands ask once through the normal
system prompt.

- List restore points, newest first: `horneroctl recovery list`. Add
  `--all` to include the hourly timeline snapshots, or `--json` for
  machine-readable output.
- Preview a rollback without changing anything:
  `horneroctl recovery rollback <n> --dry-run`.
- Roll back the system, Hornero settings and Chromatic palette:
  `horneroctl recovery rollback <n> --yes`.
- Roll back the system only:
  `horneroctl recovery rollback <n> --yes --system-only`.
- Roll back Hornero settings and the palette only:
  `horneroctl recovery rollback config_<stamp> --yes`.
- Update without a restore point:
  `horneroctl package upgrade --no-snapshot --yes`.
- Check rollback readiness: `horneroctl recovery doctor`.

`<n>` is a system snapshot number, usually the *pre* snapshot of an update.
`config_<stamp>` is a settings-only restore point, as shown by
`recovery list`. `--system-only` keeps your current Hornero settings and
Chromatic palette.

## Settings

Control Center → Updates & backups has three options. They are stored in
your shell configuration.

- **Snapshot before upgrade** (`services.rollback.snapshotBeforeUpgrade`,
  default **on**). Off updates without a restore point, like
  `--no-snapshot`.
- **Restore desktop with system**
  (`services.rollback.restoreDesktopWithSystem`, default **on**). Off
  rolls back only the system and keeps your current Hornero settings and
  palette, like `--system-only`.
- **Show timeline snapshots** (`services.rollback.showTimelineSnapshots`,
  default **off**). On also lists the hourly automatic snapshots, like
  `--all`.

## How much space restore points use

Retention is bounded, so snapshots do not fill the disk:

- update and package snapshots: the newest **10** are kept;
- snapshots marked important (HorneroOS updates and "Before rollback"
  safety snapshots): the newest **5**;
- timeline snapshots: **5** hourly and **7** daily.

Btrfs snapshots share unchanged data, so each one uses only the space of
what changed since.

## Installs without Btrfs

System rollback needs Btrfs. On ext4 or another filesystem, HorneroOS
says so plainly in Control Center and in `horneroctl recovery doctor`
instead of pretending. You can still roll back your **Hornero settings
and Chromatic palette**: updates keep saving those, and the history lists
them as settings-only restore points.

HorneroOS does not convert an existing installation to Btrfs or add the
snapshot layout to it. To get system rollback, reinstall on Btrfs.

## systemd-boot installs

The "HorneroOS snapshots" boot menu is a GRUB feature. Installs that use
systemd-boot have no snapshot boot entries. Rolling back from a running
system (Control Center or `horneroctl recovery rollback`) still works; if
the system cannot start at all, [use the Live ISO](#roll-back-from-the-live-iso).

## Validation status

<!-- VALIDATION-STATUS: filled in by the rollback PR author after the VM proof -->
This feature is new in this preview; see the linked QA scenario for what
has been proven in a virtual machine.

The QA scenarios live in
[HorneroOS/qa `scenarios/recovery`](https://github.com/HorneroOS/qa/tree/main/scenarios/recovery).
System rollback has not been validated on physical hardware, and the
manual [Live ISO procedure](#roll-back-from-the-live-iso) is not part of
the virtual-machine proof.

## Related

- [Control Center map](control-center.md)
- [horneroctl](horneroctl.md)
- [Hornero Chromatic](chromatic.md)
- [Troubleshooting](../troubleshooting/README.md)
