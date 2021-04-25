
date: None  
author(s): None  

# [Use PuTTY as Cygwin terminal - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/use-putty-as-cygwin-terminal)

_“Cygwin is a Linux-like environment for Windows.”_ This means, you can use linux/unix commandline tools like `ls`, `grep` and `find` on your Windows system. However, the default installation of Cygwin uses Windows’ default commandline terminal `cmd.exe`, which is not really handy. Fortunately, there’s a solution to use [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) as Cygwin terminal.

  1. Download and install [Cygwin](http://www.cygwin.com/). The setup will download all needed packages, so make sure you check what you need (my main reason to install Cygwin was to have a [Git](http://git.or.cz/) client on Windows) 
  2. Download [PuTTYcyg](http://code.google.com/p/puttycyg/) and extract the contents of the archive anywhere on you hard drive 
  3. Start `putty.exe`, select `Cygterm` as connection type and enter `-` (dash) as command. Enter a session name (e.g. `cygwin`) in the text field below `Saved Sessions` and click on `Save`. 
  4. Create a shortcut to `putty.exe`. Right click the shortcut, select `Properties` and append the following string to the target field: `-load "cygwin"`. Of course you have to replace `cygwin` with the name of the session you saved in PuTTYcyg. 
  5. Open the shortcut and you should directly get into your Cygwin shell 



<http://maff.ailoo.net/2008/09/use-putty-as-cygwin-terminal/>


  
  
---

