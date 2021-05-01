# fluxbox thunar icons missing

> Gtk-CRITICAL **: IA__gtk_drag_source_set_icon_name: assertion `icon_name != NULL' failed

Answer: Add
```
gtk-icon-theme-name = "elementary-xfce-dark"
```
to `~/.gtkrc-2.0`.
