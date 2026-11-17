# Popups, focus and motion

How menus, panels and tooltips open, where they appear, how they close, and
how the desktop moves — or stops moving — when you ask it to.

> **Development.** The interaction contract below is on the `main` branch of
> Shell since November 2026. Preview ISOs up to and including
> v0.2.0-preview32 behave differently. The placement solver, the motion
> levels and the Escape cascade are covered by Shell's automated tests (run
> headless and offscreen). Popup geometry, motion timing and the Niri
> keyboard behaviour have not yet been validated in a virtual machine or on
> a physical desktop.

## Where popups appear

Every popout, tray menu, tooltip and extension popover is placed by one
shared rule, so no layout, bar style or extension invents its own:

- **Away from the bar that owns it.** A top bar opens downward, a bottom bar
  upward, a left rail to the right and a right rail to the left.
- **Attached to its trigger.** A popout from an attached bar sits flush on
  the bar's inner edge. Floating, island, inset, dock and Cockpit Clear bars
  leave a small gap. A thin amber line, as wide as the trigger, runs along
  the edge facing it so you can see where the popup came from, even with
  motion off.
- **Always on screen.** It is centred on its trigger, then kept inside the
  usable area of the display, clear of every bar and an 8 px margin. If it
  does not fit it flips to the other side once; if neither side fits it
  takes the largest size that does and scrolls.
- **Following its trigger.** If the bar reorders or a monitor changes, an
  open popup follows. Each display of a mixed-scale setup is solved the same
  way.

With Cockpit's two bars, popups from the top rail open down and never reach
the bottom strip; popups from the strip open up and stop below the top rail.
Popups from Cockpit Clear are opaque cards, since there is no bar slab to
attach to.

## Opening and closing

- **Hover.** Resting on a bar item for about a tenth of a second opens its
  popup; moving to the next item morphs the popup there instead of closing
  and reopening. Hover popups never take keyboard focus.
- **Click or keyboard.** Clicking an item, or pressing Enter or Space on it,
  opens the popup with focus inside. It stays open when the pointer leaves.
- **Leaving.** Moving off both the item and the popup starts a short grace
  period (about a quarter of a second) before it closes; coming back cancels
  it. The gap between a floating bar and its card does not count as
  leaving.
- **Tooltips.** Short hints appear on hover **and** on keyboard focus after
  the same delay, and never hold anything you need to read or press.
- **Dashboard and utilities** open when the pointer touches their screen
  edge and close when it leaves. They do not take keyboard focus from other
  apps on hover. Opening them from a shortcut does take focus.

### Escape

Every transient surface closes from the keyboard, and **one Escape closes
exactly one surface**, innermost first:

1. Unsaved inner state: a workspace rename cancels, an armed power action
   disarms, a Wi-Fi password page steps back to the network list.
2. The popup that holds the keyboard closes and focus returns to the item
   that opened it.
3. Then the topmost open drawer: layout picker, session menu, launcher,
   dashboard, sidebar or utilities.

The on-screen display and toasts expire on their own timers; they never
take focus. The lock screen ignores Escape, because it has to authenticate.

On Niri, a click outside an open drawer closes it and is consumed by the
dismissal: click the window underneath again to use it.

### Find a setting

**Ctrl + ,** opens a search over every Settings page and common control (try
*reduce motion*, *wallpaper* or *fonts*). Escape clears the query, then
closes search, then closes Settings. The [Control Center
map](control-center.md) lists the pages.

## Motion levels

The shell animates popups, panels and some indicators with one shared set of
timings. Four levels control how much:

| Level | Used by | What you see |
| --- | --- | --- |
| Full | Signal mode | The richest effects |
| Standard | Everyday, Studio | Popups grow from the trigger |
| Reduced | Focus | Appear in place, tiny slide and fade |
| Off | Gaming, reduce motion | Instant, fades up to 90 ms |

With **Full** and **Standard** everything described below is on. **Reduced**
drops the growing and the staggering. **Off** shows every change at once;
only quick fades remain, so a change is never invisible.

How the standard level feels: a popup grows from its trigger over about a
third of a second, its rows scan in with a short stagger (at most eight
rows), switching between neighbouring items morphs the popup rather than
closing and reopening it, and closing is a quick fade. Nothing blinks or
pulses while idle.

### Turn motion down

- **Settings → Accessibility → Reduce motion** (the same switch is under
  **Appearance → Animations**) forces the level to Off in every experience
  mode.
- The desktop-wide GNOME setting `org.gnome.desktop.interface
  enable-animations` is followed too.
- **Settings → Accessibility → Animation speed** stretches or shrinks every
  duration without changing the level.
- An [Experience mode](experience-modes.md) sets the starting level, but
  accessibility settings always win.

## Learn more

- [Interaction contract for extension authors](../development/interaction-contract.md)
  — the placement and motion rules a surface must follow.
- [Shell interaction reference](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md)
  — the full per-surface dismissal table and focus-grab details.
- [Hornero Signal](hornero-signal.md) — the visual language, including
  accessibility.
