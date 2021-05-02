# Suspend Linux from Keyboard/CLI

Suspend from CLI:

```
dbus-send --system --print-reply --dest=org.freedesktop.UPower /org/freedesktop/UPower org.freedesktop.UPower.Suspend
```

Suspend from keyboard.

You can set from power manager, or create a keyboard shortcut in Settings -> Keyboard --> Application shortcut. The key should be XF86PowerOff.

This works for XFCE. GNOME may differ. See <https://bbs.archlinux.org/viewtopic.php?id=58273>
