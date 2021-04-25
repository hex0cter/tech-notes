
date: None  
author(s): None  

# [Customize color of GNOME panel - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/gnome/customize-color-of-gnome-panel)

`I created the file /home/<user>/.gtkrc-2.0 and inserted the following lines:`

`style "panel"`

`{`

` fg[NORMAL] = "#ffffff"#panel txt normal`

` fg[PRELIGHT] = "#ffffff"`

` fg[ACTIVE] = "#ffffff"`

` fg[SELECTED] = "#ffffff"`

` fg[INSENSITIVE] = "#ffffff"`

` bg[NORMAL] = "#ffffff" #Background of switcher and wl fine outline`

` bg[PRELIGHT] = "#ABDBAB"#Mouseover wl`

` bg[ACTIVE] = "#7DAD7D"#Selected wl`

` bg[SELECTED] = "#ADADAD"#Mouseover outline`

` bg[INSENSITIVE] = "#FAFF00"#??`

` base[NORMAL] = "#ffffff"#Background of things like deskbar or 'add to panel'`

` base[PRELIGHT] = "#ffffff"#fine outline on windowlist items`

` base[ACTIVE] = "#ffffff"`

` base[SELECTED] = "#ffffff"`

` base[INSENSITIVE] = "#ffffff"`

` text[NORMAL] = "#000000"`

` text[PRELIGHT] = "#000000"`

` text[ACTIVE] = "#000000"`

` text[SELECTED] = "#ffffff"`

` #text[INSENSITIVE] = "#8A857C"`

`}`

`widget "*PanelWidget*" style "panel"`

`widget "*PanelApplet*" style "panel"`

`class "*Panel*" style "panel"`

`widget_class "*Mail*" style "panel"`

`class "*notif*" style "panel"`

<http://ubuntuforums.org/showthread.php?t=351517>

