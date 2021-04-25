
date: None  
author(s): None  

# [Linux Serial Console HOWTO - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/linux-serial-console-howto)

<http://www.vanemery.com/Linux/Serial/serial-console.html>

On my STB simply uncomment the line below in /etc/inittab:

s0:23:respawn:/sbin/agetty -L 115200 ttyS0 vt100

Or on Ubuntu Karmic and newer:

1) Create a file called /etc/init/ttyS0.conf containing the following:
    
    
    # ttyS0 - getty
    #
    # This service maintains a getty on ttyS0 from the point the system is
    # started until it is shut down again.
    
    start on stopped rc or RUNLEVEL=[12345]
    stop on runlevel [!12345]
    
    respawn
    exec /sbin/getty -L 115200 ttyS0 vt102

2) Ask upstart to start the getty


sudo start ttyS0

This preserves during reboot.

<https://help.ubuntu.com/community/SerialConsoleHowto>  
  
---

