# Kernel and fallback boot

HorneroOS does not ship a custom kernel. An installed system runs
the kernel packages from its Arch base, and HorneroOS does not
enable kernel, scheduler, governor or memory tweaks by default.
This guide covers which kernel you are running and how to boot the
other installed kernel when an update leaves the machine unstable.

## See what is running and what is installed

```sh
uname -r
pacman -Q | grep -E '^(linux|linux-lts|linux-zen) '
```

`uname -r` is the running kernel. A package listed by `pacman -Q`
is installed; it is bootable only if a boot entry exists for it.
HorneroOS maintains no kernel manager and no Hornero-specific
kernel choice screen.

## Keep a fallback kernel before you need it

A spare kernel only helps if it is installed and has a boot entry
before the update that breaks the main one. If you choose to keep
a long-term-support kernel alongside the main one, install it with
your normal package workflow, confirm a new entry appears in the
boot menu, and test-boot it once while the system is healthy.

Do not remove the running kernel, and do not treat a fallback as a
system rollback: it changes only the kernel you boot, not the
packages, configuration or files an upgrade already wrote. System
rollback does not exist today; see
[Updates and recovery: no system rollback yet](updates-and-rollback.md).

## Boot the other kernel from GRUB

1. Reboot and hold or tap the key your firmware needs to show the
   GRUB menu if it does not appear.
2. Open the advanced options entry for HorneroOS.
3. Select the entry naming the fallback kernel and boot it.
4. Confirm you landed on it:

   ```sh
   uname -r
   horneroctl doctor
   ```

Booting a fallback is a diagnostic step. If the machine is stable
on the fallback, keep using it, save the doctor output, and report
the failure with both kernel versions. If both kernels fail, the
problem is below or beyond the kernel choice; see
[Troubleshooting by symptom](../troubleshooting/by-symptom.md).

## After a kernel update

- Reboot promptly when an update replaces the kernel; the running
  kernel and its modules can otherwise disagree.
- Graphics modules built per kernel (for example NVIDIA through
  DKMS) must build for the new kernel before you rely on that
  session. A black screen after a kernel update is a graphics
  symptom first; see [Hybrid graphics and NVIDIA](../hardware/hybrid-graphics-nvidia.md).
- GRUB snapshot entries are not recovery: booting a read-only
  snapshot is a recorded failure, not a fallback path. The manual
  Btrfs limits in [Updates and recovery](updates-and-rollback.md)
  apply, including same-kernel only.

This procedure is ordinary GRUB operation on an installed system.
It has not been separately qualified per machine; test your
fallback once while healthy rather than discovering its menu in an
emergency.
