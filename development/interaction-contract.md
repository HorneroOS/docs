# Interaction contract for extension authors

Extensions share the shell's popups, tooltips, focus rules and motion. This
page is the author-facing summary of the rule set; the implementation and
the full tables live in the Shell repository
([`docs/INTERACTION.md`][interaction] and [`docs/PLUGINS.md`][plugins]).
The design authority is [RFC 0001](rfc-0001-hornero-signal.md) section 4
(anchored surfaces) and section 3.6 (motion), and
[Signal Visual Language](signal-visual-language.md) sections 7 and 11. For
what a person experiences, see
[Popups, focus and motion](../desktop/popups-and-motion.md).

> **Development.** This describes Shell `main` since November 2026 and the
> PluginKit 3 module it ships. The placement solver, the PluginKit copy of
> it, the Escape cascade and the motion levels are covered by Shell's
> headless and offscreen tests. Nothing here has been validated in a
> virtual machine or on a physical desktop yet.

## The one rule

**An extension never positions, sizes against the screen, or animates its
own popup.** It names a trigger; the host places and animates the surface.
Do not compute screen coordinates, create your own window, or add your own
open and close animations to a popover or tooltip.

## Use the host components

- **A rich panel from a bar indicator:** `UiPopover { target: indicator }`.
  Do not build a panel `Item` and anchor it by hand.
- **A hint on hover or focus:** `tooltipText` on `UiButton`, `UiToggle`,
  `UiSlider` or `UiActionRow`, or `UiTooltip { target; text }`. Do not show
  a custom floating label.
- **A transient message:** `Notifications.toast(summary, body, glyph)`. Do
  not draw your own toast.

In a bar, the popover content is handed to the shell's own popout. It opens
on hover after the dwell delay, grows from the trigger, morphs when the
pointer moves to a neighbouring trigger, honours the close grace and closes
with the same fade as native popouts. On the dashboard or the desktop the
popover places itself with `Placement.js`, a verbatim copy of the shell's
solver inside `Hornero.PluginKit`.

The stable popover and tooltip API is `target`, `text`, `delay`, `timeout`,
`preferredSide`, `accessibleName`, `contentPadding`, `initialFocusItem`,
`open()`, `close()`, `toggle()`, `dismiss()`, `actualSide` and
`placementFor(...)`.

### Placement you can rely on

- `preferredSide: "auto"` (the default) opens away from the owning bar: down
  from a top bar, up from a bottom bar, inward from a rail. A trigger outside
  a bar prefers the free vertical half.
- An explicit side flips once if it would clip. The panel stays inside the
  screen minus an 8 px gutter and follows its trigger across moves, resizes
  and scale changes.
- Surfaces opened from Cockpit Clear bars are opaque cards; do not assume a
  bar slab behind your content.
- Give the popover a bounded size. When no side fits, the host shrinks it to
  the largest size that does and scrolls the page, so content must tolerate
  a smaller box and never rely on a fixed height.

## Keyboard and focus

- Hover popovers never take focus. Click and keyboard opens move focus into
  the panel (`initialFocusItem`, otherwise the first focusable control) and
  return it to the trigger on close.
- **Escape closes your popover first**, before anything underneath, and is
  consumed there. One Escape closes one surface. Handle Escape for inner
  state of your own (a rename field, a confirm step) before letting it fall
  through.
- Set `accessibleName` on the popover and on its trigger. A tooltip is also
  exposed as the trigger's accessible description, so never put essential
  information, or anything interactive, only in a tooltip.
- Every action reachable by pointer must be reachable by keyboard; focus
  rings show only when the last input was the keyboard (`Theme.keyboardFocus`).
- Desktop widgets live below windows and never take keyboard focus from
  applications.

## Motion and reduced motion

Read motion from `Theme`; do not hard-code durations.

- `Theme.duration(name)`: `quick` 90, `short` 160, `medium` 240, `long`
  360, `scan` 480, `settleFast` 220 and `settle` 320 ms, plus `fade` for
  opacity.
- `Theme.anim.curves.<name>`: `standard`, `enter`, `exit`, `sweep`,
  `settle` and `settleFast`.
- `Theme.motionLevel`: `full`, `standard`, `reduced` or `off`.
- `Theme.reducedMotion`: true when the person asked for less motion; it
  forces `off`.

Rules that review checks:

- Use `settle` curves to move position, size or shape only, never opacity
  or colour.
- At level `off` durations are 0, except `fade`, which is capped at 90 ms;
  at `reduced` there is no morph and no stagger. Your own transitions must
  collapse the same way, so check `Theme.motionLevel` or use
  `Theme.duration(...)`, which already does.
- Nothing blinks, pulses or animates while idle. An indeterminate
  `UiProgress` is static.
- Luminous accents (`glow`) are never drawn by hand. Instrument components
  apply it, and only while `Theme.glowEnabled` holds, which is true only in
  the Signal experience with a dark theme, no high contrast and motion
  allowed. Without a lease on the shell-wide glow budget a trace renders the
  same line without the halo.
- Polling follows the experience: read `Theme.telemetryIntervalMs` or use
  the shared providers rather than your own timers. In Gaming and Focus the
  desktop layer instantiates no widget at all, so a desktop widget must
  release everything when destroyed. See
  [Extensions](extensions.md#shared-data-providers).

## Checklist

- [ ] Popups use `UiPopover` or `UiTooltip`; no manual coordinates.
- [ ] The content works in a smaller box than designed.
- [ ] Escape closes the popover and focus returns to the trigger.
- [ ] `accessibleName` is set on trigger and popover; nothing essential is
  tooltip-only.
- [ ] Transitions use `Theme.duration(...)` and collapse at `off`.
- [ ] No idle animation and no hand-drawn glow.
- [ ] Verified at motion levels `standard` and `off`, and with the keyboard
  only. Record where it was verified (offscreen, virtual machine or host).

[interaction]: https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md
[plugins]: https://github.com/HorneroOS/shell/blob/main/docs/PLUGINS.md
