
date: None  
author(s): None  

# [How to mount remote directory under Linux? - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/linuxmount)

1\. mount remote partition (windows share) :

mount -t cifs //150.236.226.**/download -o username=*******,password=*******,domain=*** /mnt/ntserver

**Note: No slash ("/") should be added into the end of remote directory. E.g.,**

cnshexiahan:~ # mount -t cifs //150.236.226.103/LAISHARE **/** -o username=eyanlai,password="**********",domain=eapac /mnt/remoteretrying with upper case share namemount error 6 = No such device or addressRefer to the mount.cifs(8) manual page (e.g.man mount.cifs)

cnshexiahan:~ # mount -t cifs //150.236.226.103/LAISHARE -o username=eyanlai,password="**********",domain=eapac /mnt/remote

cnshexiahan:~ # ls /mnt/remotefriends vnc-4.0-x86_win32

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

2\. mount remote Linux directory to local directory:

cnshexiahan:~ # pwd/rootcnshexiahan:~ # mkdir homecnshexiahan:~ #cnshexiahan:~ # mount ecnshna001:/vol/vol_file2/unix-home/exiahan -t nfs homecnshexiahan:~ # cd homecnshexiahan:~/home # ls

Desktop ISUP_Parameters.cpp   
  
---

