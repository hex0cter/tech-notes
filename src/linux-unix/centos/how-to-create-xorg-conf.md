
date: None  
author(s): None  

# [How to create xorg.conf - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/centos/how-to-create-xorg-conf)

  


http://fedoraproject.org/wiki/How_to_create_xorg.conf

You can create a basic `xorg.conf` using the X executable itself. As root run:
    
    
    Xorg :1 -configure
    

This will create the file `/root/xorg.conf.new`, which you can then copy to `/etc/X11/xorg.conf`:
    
    
    cp /root/xorg.conf.new /etc/X11/xorg.conf
    

and edit according to your needs.  
  
---

