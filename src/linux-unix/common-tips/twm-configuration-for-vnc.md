# TWM configuration for VNC


TWM manual:

<http://www.x.org/archive/X11R6.8.2/doc/twm.1.html>


TWM Configuration examples ($HOME/~.twmrc):

<http://xwinman.org/vtwm.php>


VNC configuration example:

```
#!/bin/sh

xrdb $HOME/.Xresources
xsetroot -solid grey
xterm -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
twm &
```
