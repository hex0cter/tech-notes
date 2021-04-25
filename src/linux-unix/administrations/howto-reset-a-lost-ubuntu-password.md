
date: None  
author(s): None  

# [HOWTO – reset a lost Ubuntu password - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/howto-reset-a-lost-ubuntu-password)

<http://makezine.com/2008/09/03/howto-reset-a-lost-ubuntu-pass/>

  * By [jstriegel](http://makezine.com/author/jstriegel/)
  * Posted 2008/09/03 @ 10:37 pm
  * Category [Electronics](http://makezine.com/category/electronics/)
  * Comments [17](http://makezine.com/2008/09/03/howto-reset-a-lost-ubuntu-pass/#comments)



I loaded one of my test Ubuntu virtual machines today (one that I hadn’t used for a month) and, surprise, I had forgotten the password. This sort of thing happens from time to time, and if you’re new to Linux, it can be a little disconcerting.

Losing your root password isn’t the end of the world, though. You’ll just need to reboot into single user mode to reset it. Here’s how to do it on a typical Ubuntu machine with the GRUB bootloader:

 **Boot Linux into single-user mode**

  1. Reboot the machine.
  2. Press the ESC key while GRUB is loading to enter the menu.
  3. If there is a ‘recovery mode’ option, select it and press ‘b’ to boot into single user mode.
  4. Otherwise, the default boot configuration should be selected. Press ‘e’ to edit it.
  5. Highlight the line that begins with ‘kernel’. Press ‘e’ again to edit this line.
  6. At the end of the line, add an additional parameter: ‘single’. Hit return to make the change and press ‘b’ to boot.



 **Change the admin password**  
The system should load into single user mode and you’ll be left at the command line automatically logged in as root. Type ‘passwd’ to change the root password or ‘passwd someuser’ to change the password for your “someuser” admin account.

 **Reboot**  
Once your done, give the three finger salute, or enter ‘reboot’ to restart into your machine’s normal configuration.

That’s all there is to it. Now just make sure to write your password down on a post-it and shove it somewhere safe like under your keyboard. ![:\)](http://s0.wp.com/wp-includes/images/smilies/icon_smile.gif?m=1129645325g)  
  
---

