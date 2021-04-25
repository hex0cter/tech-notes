
date: None  
author(s): None  

# [Gnome panel font color - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/gnome/gnome-panel-font-color)

In ~/.gtkrc-2.0 insert this line

`include "/home/<user_name>/.gnome2/panel-fontrc"`

then create the file panel-fontrc in .gnome2, which consists of the following lines:

`style "my_color"`  
`{`  
`fg[NORMAL] = "#4353b6"`  
`}`  
`widget "*PanelWidget*" style "my_color"`  
`widget "*PanelApplet*" style "my_color"`

and that's it. All you have to do is choose the color and do a killall gnome-panel. The second "widget" line affects only the applets and the first one does the rest.To chose the color you can use the color select dialog in GIMP or, even better, use this:

<http://gcolor2.sourceforge.net/>

  
it allows you to pick colors from anywhare in the gnome desktop. It compiled smothly in Hoary.

<http://ubuntuforums.org/showthread.php?t=47776>  
  
---

