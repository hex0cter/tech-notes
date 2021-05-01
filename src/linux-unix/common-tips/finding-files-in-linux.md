# [Finding Files in Linux](http://www.comptechdoc.org/os/linux/usersguide/linux_ugfinding.html)


There are three good methods of finding files in linux:

  1. The slocate database
  2. The whereis command
  3. The find command

### The slocate database

To use the locate command, you will need to have a slocate database set up on your system. On many systems it is updated periodically by the cron daemon. Try the slocate command to see if it will work on your system:
```
locate whereis
```
Will list all files that contain the string "whereis". If that command did not work you will need to run the command:
```
slocate -u
```
This command will build the slocate database which will allow you to use the locate command. This command will take a few minutes to run.

### The whereis command

This command will locate binary (or executable) programs and their respective man pages. The command:
```
whereis linuxconf
```
will find all binaries and manpages with the name linuxconf.


The following are examples of the find command:

command|description
---|---
find /home -user mark | Will find every file under the directory /home owned by the user mark.
find /usr -name *spec | Will find every file under the directory /usr ending in ".spec".
find /var/spool -mtime +40 | Will find every file under the directory /var/spool that has data older than 40 days.

Find is a very powerful program and very useful for finding files with various characteristics. For more information, read the man page about find by typing "man find".

### Locating man pages by subject

There is a keyword option in the man command that can be used to find man pages that have specific words in their descriptions. An example is:
```
man -k process
```
to find all man pages that talk about processes. Use the command:
```
man -k process | grep kernel
```
to find information on kernel processes. An equivalent command is the apropos command as follows:
```
apropos process
```
### The which command

The which(1) program is a useful command for finding the full path of the executable program that would be executed if the name of the executable program is entered on the command line. The command:
```
which startx
```
Will show the full path of the startx command that will be run if "startx" is entered on the command line when an X session is started.
