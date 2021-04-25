
date: None  
author(s): None  

# [Exclude/Hide a user from GDM Logon Window - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/exclude-hide-a-user-from-gdm-logon-window)

http://forums.fedoraforum.org/showthread.php?t=246103

vi /etc/gdm/custom.conf with the following:

Code:
    
    
    [greeter]
    Exclude=user1, user2  
  
---

