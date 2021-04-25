
date: None  
author(s): None  

# [Suspend Linux from command line - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/suspend-linux-from-command-line)

  

    
    
    dbus-send --system --print-reply --dest="org.freedesktop.UPower"  /org/freedesktop/UPower  org.freedesktop.UPower.Suspend
    
    
    dbus-send --system --print-reply --dest="org.freedesktop.UPower"  /org/freedesktop/UPower  org.freedesktop.UPower.Hibernate
    
    
      
      
  
---

