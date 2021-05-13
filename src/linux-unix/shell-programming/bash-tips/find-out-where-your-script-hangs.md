# [A running bash script is hung somewhere. Can I find out what line it is on?](http://stackoverflow.com/questions/4640794/a-running-bash-script-is-hung-somewhere-can-i-find-out-what-line-it-is-on)


No real solution. But in most cases a script is waiting for a child process to terminate:
```
ps --ppid  $(pidof yourscript)
```

You could also setup signal handlers in you shell skript do toggle the printing of commands:
```
#!/bin/bash

trap "set -x" SIGUSR1
trap "set +x" SIGUSR2

while true; do
    sleep 1
done
```

Then use
```
kill -USR1 $(pidof yourscript)
kill -USR2 $(pidof yourscript)
```
There are ways to find out a lot more about a running process than you would expect.

Use `lsof -p $pid` to see what files are open, which may give you some clues. Note that some files, while "deleted", can still be kept open by the script. As long as the script doesn't close the file, it can still read and write from it - and the file still takes up room on the file system.

Use `strace` to actively trace the system calls used by the script. The script will read the script file, so you can see some of the commands as they are read prior to execution. Look for `read` commands with this command:


    strace -p $pid -s 1024


This makes the commands print strings up to 1024 characters long (normally, the `strace` command would truncate strings much shorter than that).

Examine the directory `/proc/$pid` in order to see details about the script; in particular note, see`/proc/$pid/environ` which will give you the process environment separated by nulls. To read this "file" properly, use this command:


    xargs -0 -i{} < /proc/$pid/environ


You can pipe that into `less` or save it in a file. There is also `/proc/$pid/cmdline` but it is possible that that will only give you the shell name (`-bash` for instance).
