# [File type in Linux/Unix](http://www.wellho.net/mouth/1068_ls-l-report-Linux-Unix-types-and-permssions.html)

`ls -l` report, Linux / Unix - types and permssions

What does `drwtrwx---` mean on the start of your `ls -l` report?

The first character (d in my example) tells you the type of symbol you have on the file system, as follows:

```
d - a directory;
b - a block-type special file;
c - a character-type special file;
p - a named pipe;
l - a symbolic link;
S - a socket;
s - a XENIX semaphore;
m - a XENIX shared data (memory) file;
D - a Solaris door;
n - a HP-UX network special file;
- - a plain file.
```

and I've heard rumours of a "*" appearing - anyone know about that?

The following characters are grouped 3 by three:

* First three - the user (file owner's) permissions
* Next three - the group permissions
* First three - the permissions other users have

and the characters you'll find are:
```
r - the file is readable
w - the file is writable
x - the file is executable (or accessible for a directory)
- - the indicated permission is not granted.
```

The user execute character may also be:
```
s - the file has set-user-ID mode
S - the set-user-ID bit is set on the file but it is not executable
```

The group execute character may also be:
```
s - the file has set-group-ID mode;
l - mandatory locking is enabled for the file (standard)
L - mandatory locking is enabled for the file (Posix)
```

And the other group execute character may also be:
```
t - the sticky bit of the mode is on
T - the sticky bit is on but the file is not executable
```
