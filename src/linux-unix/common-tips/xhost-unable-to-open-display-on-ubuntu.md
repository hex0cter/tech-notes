
date: None  
author(s): None  

# ["xhost: unable to open display" on Ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/xhost-unable-to-open-display-on-ubuntu)

On Ubuntu you can use **_export_** _**DISPLAY=:0.0, xhost+**_ , but you cannot use ** _export DISPLAY=lPaddress:0.0, xhost+_** , b'cos it complains "xhost: unable to open display". Here is the solution:

sudo gedit /etc/gdm/gdm.schemasfind:<schema><key>security/DisallowTCP</key><signature>b</signature><default>true</default></schema>shift from true to false:<schema><key>security/DisallowTCP</key><signature>b</signature><default>false</default></schema>

save file gdm.schemas

And reboot the machine(it seems not working if you only restart gdm).

<http://ubuntuforums.org/showthread.php?t=1310771>  
  
---

