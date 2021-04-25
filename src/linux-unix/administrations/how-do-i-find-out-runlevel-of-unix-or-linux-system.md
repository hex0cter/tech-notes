
date: None  
author(s): None  

# [How do I find out runlevel of unix or Linux system? - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/how-do-i-find-out-runlevel-of-unix-or-linux-system)

A runlevel is a software configuration of the system which allows only a selected group of processes to exist. The processes spawned by init command/process for each of these runlevels are defined in the /etc/inittab file. Runlevels 0, 1, and 6 are reserved. Runlevel 0 is used to halt the sys tem, runlevel 6 is used to reboot the system, and runlevel 1 is used to get the system down into single user mode. In order to print current runlevel you need to use command who or runlevel as follows:

1) Print print current runlevel using who command:  


$ who -r
    
    
    run-level 2  Dec 16 11:45                   last=S

2) Find the current and previous system runlevel using runlevel command:

$ runlevel
    
    
    N 2 
    
    
      
    
    
    
    <http://www.cyberciti.biz/howto/question/linux/unix-linux-find-out-runlevel.php>

