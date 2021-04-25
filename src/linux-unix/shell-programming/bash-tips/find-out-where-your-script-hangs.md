
date: None  
author(s): None  

# [A running bash script is hung somewhere. Can I find out what line it is on? - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/bash-tips/find-out-where-your-script-hangs)

There are ways to find out a lot more about a running process than you would expect.

Use `lsof -p $pid` to see what files are open, which may give you some clues. Note that some files, while "deleted", can still be kept open by the script. As long as the script doesn't close the file, it can still read and write from it - and the file still takes up room on the file system.

Use `strace` to actively trace the system calls used by the script. The script will read the script file, so you can see some of the commands as they are read prior to execution. Look for `read` commands with this command:
    
    
    strace -p $pid -s 1024  
    

This makes the commands print strings up to 1024 characters long (normally, the `strace` command would truncate strings much shorter than that).

Examine the directory `/proc/$pid` in order to see details about the script; in particular note, see`/proc/$pid/environ` which will give you the process environment separated by nulls. To read this "file" properly, use this command:
    
    
    xargs -0 -i{} < /proc/$pid/environ  
    

You can pipe that into `less` or save it in a file. There is also `/proc/$pid/cmdline` but it is possible that that will only give you the shell name (`-bash` for instance).

