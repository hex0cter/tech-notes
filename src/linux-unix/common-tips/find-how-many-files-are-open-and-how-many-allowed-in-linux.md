# [Find How Many Files are Open and How Many Allowed in Linux](http://element14.wordpress.com/2008/01/22/find-how-many-files-are-open-and-how-many-allowed-in-linux/)


To find how many files are opne at any given time you can type this on the terminal:
```
cat /proc/sys/fs/file-nr
```
I got this number:
```
6240 ( total allocated file descriptors since boot)
0 ( total free allocated file descriptors)
94297 ( maximum open file descriptors)
```

Not that you can check the maximum open file by using this command: `cat /proc/sys/fs/file-max`

And change the max to your own like with this command: `echo “804854″ > /proc/sys/fs/file-max`

You can use lsof command to also check for the number of files currently open ( `lsof | wc -l` ), but this takes into account open files that are not using file descriptors such as directories, memory mapped files, and executable text files, and will actually show higher numbers than previous method.
