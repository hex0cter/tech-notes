# [vbox 4.0 gives VERR_SUPLIB_OWNER_NOT_ROOT](http://ubuntuforums.org/showthread.php?t=1695134)

```
daniel@daniel-laptop:/opt/VirtualBox$ ls -ld /usr/lib

drwxr-xr-x 246 daniel daniel 69632 2011-07-24 14:46 /usr/lib

daniel@daniel-laptop:/opt/VirtualBox$ sudo chown root /usr/lib/

daniel@daniel-laptop:/opt/VirtualBox$ ls -ld /usr/lib

drwxr-xr-x 246 root daniel 69632 2011-07-24 14:46 /usr/lib
```
Then it works.
