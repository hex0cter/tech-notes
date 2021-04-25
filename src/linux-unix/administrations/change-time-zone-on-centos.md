
date: None  
author(s): None  

# [Change time zone on CentOS - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/change-time-zone-on-centos)

https://chrisjean.com/change-timezone-in-centos/
    
    
    sudo mv /etc/localtime /etc/localtime.bak
    
    
    sudo ln -s /usr/share/zoneinfo/ **America/Chicago** /etc/localtime  
  
---

