# Networking and Bluetooth

Control Center gives Hornero-native access to network and Bluetooth state,
but the host still owns the underlying services and device drivers.

## Network

The Network pane uses the host network service to show and manage available
connections. On the current Arch reference setup that service is
NetworkManager, with `nmcli` as a command-line diagnostic. Hornero Config
does not install NetworkManager as an application dependency.

If the list is empty, check that the host network service is running and
that the adapter is visible to the operating system. Avoid pasting passwords
or full connection profiles into bug reports.

## Bluetooth

The Bluetooth pane talks to BlueZ on the host. Pairing requires a working
Bluetooth adapter, the BlueZ service, and any required firmware. A missing
adapter or service is a host setup issue; reinstalling the Shell will not
create the hardware support.

Use the status shown in Control Center first. For system-level diagnostics,
consult the [Arch Wiki NetworkManager guide](https://wiki.archlinux.org/title/NetworkManager)
or [Bluetooth guide](https://wiki.archlinux.org/title/Bluetooth).

## VPN

The VPN pane manages connections already provided by the host's networking
stack and installed plugins. Hornero does not silently add a VPN provider.
Install and configure the provider you trust, then use the pane to inspect
or activate its connection.
