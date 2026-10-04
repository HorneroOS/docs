# Hardware

Hornero is built on Arch Linux and Hyprland. Device support therefore depends
on the kernel, firmware, drivers, and device configuration on the machine;
there is not yet a Hornero installer that selects and configures a hardware
profile for you.

## Start with a read-only check

The Control Center exposes common network, Bluetooth, audio, brightness,
battery, and microphone controls. The CLI can report several of those states:

```sh
horneroctl doctor
horneroctl hardware network status
horneroctl hardware brightness status
horneroctl hardware battery status
horneroctl hardware mic status
```

For graphics or display detection, collect the kernel's device/driver view
and the compositor's monitor list:

```sh
lspci -nnk
hyprctl monitors -j
journalctl -b -k -p warning
```

These commands inspect state. They do not install drivers or change your
boot configuration.

## NVIDIA and hybrid graphics

Driver and PRIME setup depends on the GPU generation, kernel package, laptop
firmware, and which ports are wired to which GPU. Do not copy a command from a
personal machine guide without checking those facts on your own hardware.

Use the current [ArchWiki NVIDIA guide](https://wiki.archlinux.org/title/NVIDIA)
for driver choices and [PRIME](https://wiki.archlinux.org/title/PRIME) for
hybrid rendering. Follow the guidance that matches your installed kernel and
distribution state. Hornero does not currently maintain a separate NVIDIA
driver installer or a universal hybrid-GPU profile.

For a report, include the GPU models, kernel and driver package, whether the
issue occurs before or after login, and the relevant error lines. Remove
usernames, hostnames, serial numbers, network identifiers, and unrelated
personal log content before sharing logs publicly.
See [how to report a bug](../development/README.md#report-a-bug).

## More device guides

- [Network](../troubleshooting/README.md#network-and-bluetooth)
- [Display and graphics](../troubleshooting/README.md#display-and-graphics)
- [Shell and Settings diagnostics](../troubleshooting/README.md)

Historical setup notes in the former dotfiles wiki describe one workstation.
Their GPU models, module options, package choices, and monitor wiring are not
Hornero defaults.
