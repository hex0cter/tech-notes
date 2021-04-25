
date: None  
author(s): None  

# [Mount windows shared folder on Linux as normal user - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/mount-windows-shared-folder-on-linux-as-normal-user)

1.

`sudo apt-get install cifs-utils`

2\. with:

`//10.216.0.25/simcert ` `/simcert` `cifs ` `noauto,user 0 0`

3

`chmod u+s /sbin/mount.cifs`

4\. now

`mount /simcert (your password towards the Windows server might be needed)`

as normal user

Another way:

`/sbin/mount.cifs //10.216.0.25/simcert /home/handaniel/simcert/ -o user=handaniel,domain=ACCOUNTS`

This is tested as root on Red Hat Enterprise Linux Server release 6.5 (Santiago)  
  
---

