
date: None  
author(s): None  

# [repair grub with live cd - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/repair-grub-with-live-cd)

http://askubuntu.com/questions/110722/windows-xp-no-longer-boots

  


Using your Ubuntu Live CD boot into the system. Once running, open a terminal and type or copy and paste this:
    
    
    sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update
    

then
    
    
    sudo apt-get install -y boot-repair && boot-repair
    

you will download a repair tool

![enter image description here](http://i.stack.imgur.com/jkB9O.png)

To use the tool launch Boot-Repair from either :

the dash (Unity) System->Administration->Boot-Repair menu (Gnome)

by typing 'boot-repair' in a terminal

Then try "Recommended repair" button. When repair is finished, reboot and check if you recovered access to your OSs.

use this for reference <https://help.ubuntu.com/community/Boot-Repair>  
  
---

