
date: None  
author(s): None  

# [How to suspend/hibernate windows 7 from command line - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/how-to-suspend-hibernate-windows-7-from-command-line)

<http://superuser.com/questions/42124/how-can-i-put-the-computer-to-sleep-from-command-prompt-run-menu>

Shutdown Computer
    
    
    Shutdown.exe -s -t 00
    

Restart Computer
    
    
    Shutdown.exe -r -t 00
    

Lock Workstation
    
    
    Rundll32.exe User32.dll,LockWorkStation
    

Hibernate Computer
    
    
    rundll32.exe PowrProf.dll,SetSuspendState
    

Sleep Computer
    
    
    rundll32.exe powrprof.dll,SetSuspendState 0,1,0

The command `rundll32.exe powrprof.dll,SetSuspendState 0,1,0` for sleep is correct - however, it will hibernate instead of sleep if you don't turn the hibernation off.

Here's how to do that:

Go to the Start Menu and open an elevated Command Prompt by typing `cmd.exe`, right clicking and choosing _Run as administrator_. Type the following command:
    
    
    powercfg -hibernate off  
  
---

