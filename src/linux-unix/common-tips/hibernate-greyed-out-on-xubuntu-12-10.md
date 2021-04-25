
date: None  
author(s): None  

# [hibernate greyed out on xubuntu 12.10 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/hibernate-greyed-out-on-xubuntu-12-10)

<http://askubuntu.com/questions/94754/how-to-enable-hibernation>
    
    
    udo nano /etc/polkit-1/localauthority/50-local.d/com.ubuntu.enable-hibernate.pkla
    

Fill it with this:
    
    
    [Re-enable hibernate by default]
    Identity=unix-user:*
    Action=org.freedesktop.upower.hibernate
    ResultActive=yes

Some users will then need to run `sudo update-grub` to get the hibernate option to be available in the power menu...  
  
---

