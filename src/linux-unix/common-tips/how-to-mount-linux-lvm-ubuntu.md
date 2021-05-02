# [how to mount Linux LVM ubuntu](http://www.linuxquestions.org/questions/fedora-35/how-can-i-mount-lvm-partition-in-ubuntu-569507/)


```
    sudo su
    apt-get install lvm2
    modprobe dm-mod
    vgchange -a y
```
