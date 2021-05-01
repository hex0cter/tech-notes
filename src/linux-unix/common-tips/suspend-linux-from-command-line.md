# Suspend Linux from command line

```
    dbus-send --system --print-reply --dest="org.freedesktop.UPower"  /org/freedesktop/UPower  org.freedesktop.UPower.Suspend
```

```
    dbus-send --system --print-reply --dest="org.freedesktop.UPower"  /org/freedesktop/UPower  org.freedesktop.UPower.Hibernate
```
