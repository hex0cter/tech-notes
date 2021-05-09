# Change splash screen of Ubuntu Linux

The instructions below are tested on Ubuntu 9.10.

1. How to change the splash screen of Gnome?

Replace the file **/usr/share/images/xsplash/bg_2560x1600.jpg** with another one of the same size.

Run sudo xsplash to preview the changes. Find details at: <http://www.ghacks.net/2010/01/06/change-your-ubuntu-splash-screen-background/>

2. How to change the splash screen of grub2?

Copy an image file of the size specified in **/etc/default/grub to /usr/share/images/desktop-base/moreblue-orbit-grub.png** , then run **sudo update-grub** to reflect the changes.
