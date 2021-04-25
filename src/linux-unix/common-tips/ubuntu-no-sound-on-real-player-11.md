
date: None  
author(s): None  

# [Ubuntu: No sound on Real Player 11 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/ubuntu-no-sound-on-real-player-11)

<http://ubuntuforums.org/showthread.php?t=954664>

This may not work as expected but worth a try. I saw this solution from [_fwelland_](http://forums.fedoraforum.org/showthread.php?t=186200&page=3) on the Fedora forums.

I fix/hacked this by changing the line in the realplay script 

Code:
    
    
    sudo gedit /opt/real/RealPlayer/realplay

then on line 52 change

Code:
    
    
    $HELIX_LIBS/realplay.bin "$@"

TO

Code:
    
    
    padsp -n RealPlayer -m RealPlayerStream $HELIX_LIBS/realplay.bin "$@"  
  
---

