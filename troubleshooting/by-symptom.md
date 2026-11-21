# Troubleshooting by symptom

Start from what you see, run the read-only check for that symptom,
and keep the output. Do not start from a fix: record the exact
error and the steps that reproduce it first.

```sh
horneroctl doctor
```

![A terminal showing doctor output: fourteen checks listed with OK
marks, covering the Wayland session, the selected terminal, the shell
configuration paths and the Qt themes, ending with "all 14 checks
passed".](https://www.horneroos.com/captures/cap-term-04.png)

*Example `doctor` output on the maintainer's machine — the paths
shown are that machine's home directory; yours will differ. Capture,
19 November 2026.*

## The machine does not boot

1. Boot the [fallback kernel](../desktop/kernel-and-fallback.md)
   from the GRUB advanced options once.
2. If neither kernel boots, boot the live ISO and keep the machine
   unchanged until you have the failing boot's log.
3. Note whether the failure is before the boot menu, at disk
   unlock, or after login: each is a different owner.

There is no system rollback to reach for; see
[Updates and recovery](../desktop/updates-and-rollback.md) for the
manual Btrfs procedure and its same-kernel limits.

## No network

```sh
horneroctl hardware network status
horneroctl doctor
```

If the adapter itself is missing from the system, collect
`lspci -nnk` and `lsusb` and the kernel log lines for it. A missing
adapter is below the desktop layer. See
[Network and Bluetooth](README.md#network-and-bluetooth).

## No audio

```sh
horneroctl studio doctor
horneroctl studio selection show
systemctl --user status pipewire wireplumber
```

Confirm the right output device in Settings → Sound first. If you
enabled a Studio low-latency drop-in, remove it and restart the
user services as in [Studio audio](../applications/studio-audio.md#recovery)
before changing anything else.

## The shell does not start or a Settings pane is empty

```sh
horneroctl shell status --json
horneroctl shell logs --lines 120
horneroctl config validate
```

Keep the first QML import or load error from the log. Do not
repeatedly restart the graphical session, and do not delete user
settings to make a pane load. See
[The shell is missing](README.md#the-shell-is-missing-or-not-responding).

## A game does not start

Run `horneroctl gaming doctor`, then change one launch option at a
time as in
[Gaming: Proton, GameMode, Gamescope and MangoHud](../applications/gaming-proton-gamemode.md).
Keep Steam's Proton log for that game.

## Gather logs for a report

```sh
journalctl -b -1 --no-pager
journalctl -b -k -p warning --no-pager
horneroctl doctor
```

`-b -1` is the previous boot, the one that failed. Remove
usernames, hostnames, serial numbers, network identifiers and
unrelated personal lines before sharing anything publicly, then
follow [how to report a bug](../development/README.md#report-a-bug).
