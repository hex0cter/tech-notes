# [Mount fat32 with read-write permission from command line](http://superuser.com/questions/79813/read-and-write-permission-for-fat32-partition-in-ubuntu)



Try mounting with rw and specify the type:
```
mount -t vfat /dev/sda6 /media/FAT32 -o rw,uid=xxx,gid=xxx
```
where uid and gid are that of your user account (without uid and gid you can only write with root permission).

Use the id command to find your uid and gid from command line.
```
ubuntu@ubuntu:/sdd1/Software/OS/XP$ id ubuntu
uid=999(ubuntu) gid=999(ubuntu) groups=999(ubuntu),4(adm),20(dialout),24(cdrom),46(plugdev),112(lpadmin),120(admin),122(sambashare)
```

See more here:
https://sites.google.com/site/xiangyangsite/home/linux-unix/administrations/in-unix-how-do-i-find-a-user-s-uid-or-gid
