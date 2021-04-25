
date: None  
author(s): None  

# [Execute a command on user logon - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/execute-a-command-on-user-logon)

<https://unix.stackexchange.com/questions/122424/execute-a-command-on-user-logon>

The Autostart Directories are $XDG_CONFIG_DIRS/autostart as defined in accordance with the "Referencing this specification" section in the "desktop base directory specification".

If the same filename is located under multiple Autostart Directories only the file under the most important directory should be used.

Example: If $XDG_CONFIG_HOME is not set the Autostart Directory in the user's home directory is ~/.config/autostart/

Example: If $XDG_CONFIG_DIRS is not set the system wide Autostart Directory is /etc/xdg/autostart/

Example: If $XDG_CONFIG_HOME and $XDG_CONFIG_DIRS are not set and the two files /etc/xdg/autostart/foo.desktop and ~/.config/autostart/foo.desktop exist then only the file ~/.config/autostart/foo.desktop will be used because ~/.config/autostart/ is more important than /etc/xdg/autostart/  
  
---

