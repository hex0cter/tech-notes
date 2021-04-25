
date: None  
author(s): None  

# [Access Windows shared folder from Ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/access-windows-shared-folder-from-ubuntu)

  1. install smbfs
    1. `$sudo apt-get install smbfs`
  2. use ‘mount’ to mount the file share
    1. for mount you need to create a local folder that will be the mount point for example create a folder test under /media
    2. then mount the share using
      1. `$sudo mount -t smbfs -o username=myusername //192.168.0.10/sharename /media/test`
      2. myusername – is a valid username on the windows machine
      3. the ip address is the ip of the windows machine
      4. sharename is the name given to the share on the windows machine
      5. This will prompt you for the passwor d- the password for myusername on the windows machine
      6. on successful password you will be able to see the contents of the sharedfolder under /media/test
      7. Note: if you this is the first time you are using sudo in this shell session or if sudo has timed out there will be two password prompts first for the sudo next for the share mount. you could avoid this by doing `$sudo -v` before doing the sudo mount
  3. to umount



<http://mytechnotes.wordpress.com/2007/05/21/windows-shared-folder-from-ubuntu/>  
  
---

