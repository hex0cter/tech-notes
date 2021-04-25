
date: None  
author(s): None  

# [Upgrade Ubuntu to newer release - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/ubuntu/upgrade-ubuntu-to-newer-release)

<http://www.unixmen.com/how-to-upgrade-from-ubuntu-1004-1010-1104-to-ubuntu-1110-oneiric-ocelot-desktop-a-server/>

**From GUI:**

a- Update the system before to upgrade:

Before to upgrade, we need to update the system, press C **trl+Alt+T** , and enter the following command:
    
    
     **sudo apt-get update && sudo apt-get dist-upgrade**

To upgrade, open terminal and enter the following command:
    
    
     **sudo update-manager -d**

Update Manager should open up and tell you: **New distribution release ’13.04** ‘ is available ( See screenshot bellow).

[![upgrade-ubuntu13.04](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade-ubuntu13.04.png)](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade-ubuntu13.04.png)

Then click : Upgrade

[![upgrade-2](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade-2.png)](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade-2.png)A new screen will appear asking you if you want to start Upgrade:

[![upgrade-4](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade-4.png)](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade-4.png)

Press start upgrade.

Now don`t close your computer until the upgrade is finished.

[![upgrade5](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade5.png)](http://180016988.r.cdn77.net/wp-content/uploads/2011/09/upgrade5.png)

##  **\- From CLI:**

To upgrade from Ubuntu 12.10 on a server system to Ubuntu 13.04:

1- install the `update-manager-core` package if it is not already installed:
    
    
     **sudo apt-get install update-manager-core**

2- Edit **`/etc/update-manager/release-upgrades`** and set **`Prompt=normal`** ;

3- Launch the upgrade tool with the command
    
    
     **sudo do-release-upgrade -d**

and follow the on-screen instructions.

 **Important:** **This is a beta release. Do not install it on production machines. The final stable version will be released 26th of April 2013.**

\- See more at: http://www.unixmen.com/how-to-upgrade-from-ubuntu-1004-1010-1104-to-ubuntu-1110-oneiric-ocelot-desktop-a-server/#sthash.l3sYpXrm.dpuf  
  
---

