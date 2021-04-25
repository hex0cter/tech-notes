
date: None  
author(s): None  

# [Change splash screen of Ubuntu Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/ubuntu/change-splash-screen-of-ubuntu-linux)

The instructions below are tested on Ubuntu 9.10.

1\. How to change the splash screen of Gnome?

Replace the file **/usr/share/images/xsplash/bg_2560x1600.jpg** with another one of the same size.

2\. How to change the splash screen of grub2?

Copy an image file of the size specified in **/etc/default/grub to /usr/share/images/desktop-base/moreblue-orbit-grub.png** , then run **sudo update-grub** to reflect the changes.  
  
---

