
date: None  
author(s): None  

# [vbox 4.0 gives VERR_SUPLIB_OWNER_NOT_ROOT - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/ubuntu/vbox-4-0-gives-verr_suplib_owner_not_root)

daniel@daniel-laptop:/opt/VirtualBox$ ls -ld /usr/lib

drwxr-xr-x 246 daniel daniel 69632 2011-07-24 14:46 /usr/lib

daniel@daniel-laptop:/opt/VirtualBox$ sudo chown root /usr/lib/

daniel@daniel-laptop:/opt/VirtualBox$ ls -ld /usr/lib

drwxr-xr-x 246 root daniel 69632 2011-07-24 14:46 /usr/lib

Then it works.

<http://ubuntuforums.org/showthread.php?t=1695134>  
  
---

