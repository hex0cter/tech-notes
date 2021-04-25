
date: None  
author(s): None  

# [fluxbox thunar icons missing - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/fluxbox-thunar-icons-missing)

Gtk-CRITICAL **: IA__gtk_drag_source_set_icon_name: assertion `icon_name != NULL' failed

Answer: Add 

`gtk-icon-theme-name = "elementary-xfce-dark"`

to ~/.gtkrc-2.0  
  
---

