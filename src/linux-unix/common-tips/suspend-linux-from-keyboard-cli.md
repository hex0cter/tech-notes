
date: None  
author(s): None  

# [Suspend Linux from Keyboard/CLI - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/suspend-linux-from-keyboard-cli)

Suspend from CLI:

dbus-send --system --print-reply --dest=org.freedesktop.UPower /org/freedesktop/UPower org.freedesktop.UPower.Suspend

Suspend from keyboard.

You can set from power manager, or create a keyboard shortcut in Settings -> Keyboard --> Application shortcut. The key should be XF86PowerOff.  
  
---

