
date: None  
author(s): None  

# [how to mount Linux LVM ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-mount-linux-lvm-ubuntu)

http://www.linuxquestions.org/questions/fedora-35/how-can-i-mount-lvm-partition-in-ubuntu-569507/  

    
    
    sudo su
    apt-get install lvm2
    modprobe dm-mod
    vgchange -a y  
  
---

