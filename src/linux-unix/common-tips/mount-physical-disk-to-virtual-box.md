
date: None  
author(s): None  

# [Mount physical disk to virtual box - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/mount-physical-disk-to-virtual-box)

Connect the disk onto the host, assuming /dev/sdb, run the following command:

  


sudo VBoxManage internalcommands createrawvmdk -filename /home/daniel/VMs/Raw/sdb.vmdk -rawdisk /dev/sdb 

create a vm with that file attached as the disk. Install it.  
  
---

