# Lock screen and login

The lock screen and login screen run at different points in a session.
Hyprlock locks an active Hyprland session. SDDM and Hornero Greeter display
the login screen before a session starts.

## Lock the session

Press **Super + L** to request a lock from Hornero Shell. Hypridle handles
idle timers in the configured session and may request a lock before display
power or sleep actions. The host must have the corresponding Hyprland tools
and system services installed.

![The locked session screen: a large clock and date over a dark
background, a password field in a small panel, and a notifications
card that stays unreadable until unlock.](https://www.horneroos.com/captures/cap-lock-01.png)

*The session lock screen (Hyprlock) on the maintainer's machine —
their username is the one shown. This is the lock screen, not the
login greeter. Capture, 19 November 2026.*

If the screen does not lock, check the Shell and Hyprland session first:

```sh
horneroctl doctor
horneroctl shell logs --lines 100
```

Do not run a second locker in parallel with the active session locker.

![Settings, Lock screen page with switches for hiding notifications
while locked, recolouring the logo, fingerprint unlock with an attempt
count, the brand hairline, the 12-hour clock and the lock panel
width.](https://www.horneroos.com/captures/cap-cc-12.png)

*Settings → Lock Screen: privacy, fingerprint and appearance of the
next lock. Running-desktop capture from the maintainer's machine,
19 November 2026.*

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

See [release status](https://horneroos.com/releases),
[installation status](https://horneroos.com/install), and the
[greeter repository](https://github.com/HorneroOS/greeter) before installing
or upgrading login components.
