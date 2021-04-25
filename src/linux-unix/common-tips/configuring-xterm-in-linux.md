
date: None  
author(s): None  

# [Configuring Xterm In Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/configuring-xterm-in-linux)

  * User config files
    * ~/.Xdefaults
    * ~/.Xresources
  * Global Various Files



  * *visualBell: BOOLEAN

    Changes [system beep](http://how-to.wikia.com/index.php?title=Compuer_system_beep&action=edit&redlink=1) to make the windows background flicker
  * XTerm*saveLines: INTEGER

    The number of lines that do not clear the screen after the program exits
  * XTerm*background: COLOR

    The color of the background
  * XTerm*foreground: COLOR

    Color of highlighted text
  * XTerm*pointerColor: COLOR
    * Color of the mouse pointer when it's in front on the xterm window
  * XTerm*pointerColorBackground: white

    Border color around the mouse pointer
  * XTerm*cursorColor: COLOR

    Color of cursor
  * XTerm*pointerShape: SHAPE

    Sets [mouse](http://how-to.wikia.com/index.php?title=Computer_mouse&action=edit&redlink=1) pointer's appearance when over the xterm window
    Options: XTerm, left_ptr, bogosity, ...
  * XTerm*font: FONT

    Sets the font
    Example: -adobe-courier-medium-r-normal*14-140-75-75-m-90*



  
XTerm*internalBorder: INTEGER XTerm*loginShell: BOOLEAN XTerm*scrollBar: BOOLEAN XTerm*scrollKey: BOOLEAN

## [[edit](http://how-to.wikia.com/index.php?title=How_to_configure_xterm&action=edit§ion=3)]Other

  * [All configuration parameters](http://how-to.wikia.com/wiki/Howto_configure_xterm/All_configs)


  * XTerm*VT100*titeInhibit: true
  * XTerm*alwaysHighlight: yes
  * XTerm*marginBell: yes
  * xterm*iconPixmap: /usr/share/pixmaps/gnome-gemvt.xbm
  * xterm*iconMask: /usr/share/pixmaps/gnome-gemvt-mask.xbm
  * XTerm*iconName: terminal
  * Mwm*xterm*iconImage: /home/a/a1111aa/xterm.icon
  * XTerm*loginShell: true
  * XTerm*scrollColor: black
  * XTerm*allowSendEvents: True
  * XTerm*sessionMgt: false
  * XTerm*eightBitInput: false
  * XTerm*metaSendsEscape: true
  * XTerm*internalBorder: 10
  * XTerm*highlightSelection: true
  * XTerm*VT100*colorBDMode: on
  * XTerm*VT100*colorBD: blue
  * XTerm.VT100.eightBitOutput: true
  * XTerm.VT100.titeInhibit: false
  * XTerm*color0: black
  * XTerm*color1: red3
  * XTerm*color2: green3
  * XTerm*color3: yellow3
  * XTerm*color4: DodgerBlue1
  * XTerm*color5: magenta3
  * XTerm*color6: cyan3
  * XTerm*color7: gray90
  * XTerm*color8: gray50
  * XTerm*color9: red
  * XTerm*color10: green
  * XTerm*color11: yellow
  * XTerm*color12: blue
  * XTerm*color13: magenta
  * XTerm*color14: cyan
  * XTerm*color15: white
  * XTerm*colorUL: yellow
  * XTerm*colorBD: white
  * XTerm*mainMenu*backgroundPixmap: gradient:vertical?dimension=400&start=gray10&end=gray40
  * XTerm*mainMenu*foreground: white
  * XTerm*vtMenu*backgroundPixmap: gradient:vertical?dimension=550&start=gray10&end=gray40
  * XTerm*vtMenu*foreground: white
  * XTerm*fontMenu*backgroundPixmap: gradient:vertical?dimension=300&start=gray10&end=gray40
  * XTerm*fontMenu*foreground: white
  * XTerm*tekMenu*backgroundPixmap: gradient:vertical?dimension=300&start=gray10&end=gray40
  * XTerm*tekMenu*foreground: white
  * XTerm*rightScrollBar: true
  * XTerm*VT100*colorBDMode: on
  * XTerm*VT100*colorBD: purple


  * ! Colour for underline attribute
    * XTerm*VT100*colorULMode: on
    * XTerm*VT100*underLine: on
    * XTerm*VT100*colorUL: red


  * ! Turn on colour mode in your xterms
    * XTerm.VT100*dynamicColors: On



<http://how-to.wikia.com/wiki/How_to_configure_xterm>

<http://linuxhelp.blogspot.com/2005/10/configuring-xterm-in-linux.html>  
  
---

