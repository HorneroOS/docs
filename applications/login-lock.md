# Lock screen and login

The lock screen and login screen run at different points in a session.
Hyprlock locks an active Hyprland session. SDDM and Hornero Greeter display
the login screen before a session starts.

## Lock the session

Press **Super + L** to request a lock from Hornero Shell. Hypridle handles
idle timers in the configured session and may request a lock before display
power or sleep actions. The host must have the corresponding Hyprland tools
and system services installed.

If the screen does not lock, check the Shell and Hyprland session first:

```sh
horneroctl doctor
horneroctl shell logs --lines 100
```

Do not run a second locker in parallel with the active session locker.

## Hornero Greeter

Hornero Greeter is an optional SDDM theme package maintained in
[HorneroOS/greeter](https://github.com/HorneroOS/greeter). SDDM owns the
login service and selects its theme through the system SDDM configuration.
The current Hornero release profiles do not install or configure SDDM as an
end-user installer would.

Greeter packaging, Qt runtime requirements, assets, and release instructions
belong to that repository. After changing a greeter package or SDDM theme,
inspect its documented preview path and package files before relying on the
next login. Do not restart SDDM from a running desktop just to test a theme.

See [release status](https://horneroos.org/releases),
[installation status](https://horneroos.org/install), and the
[greeter repository](https://github.com/HorneroOS/greeter) before installing
or upgrading login components.
