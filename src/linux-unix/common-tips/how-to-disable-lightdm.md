
date: None  
author(s): None  

# [How to disable lightdm? - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-disable-lightdm)

http://askubuntu.com/questions/139014/how-to-disable-lightdm

ightdm is starter by Upstart, not SysV Init, so update-rc.d doesn't work.

Use
    
    
     echo  "manual" | sudo tee -a /etc/init/lightdm.override  
  
---

