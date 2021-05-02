# [How to mount remote directory under Linux?](http://www.cyberciti.biz/tips/how-to-mount-remote-windows-partition-windows-share-under-linux.html)

1. mount remote partition (windows share):

```
mount -t cifs //150.236.226.**/download -o username=*******,password=*******,domain=*** /mnt/ntserver
```

**Note: No slash ("/") should be added into the end of remote directory. E.g.,**
```
cnshexiahan:~ # mount -t cifs //150.236.226.103/LAISHARE/ -o username=eyanlai,password="**********",domain=eapac   /mnt/remote
retrying with upper case share name
mount error 6 = No such device or address
Refer to the mount.cifs(8) manual page (e.g.man mount.cifs)
cnshexiahan:~ # mount -t cifs //150.236.226.103/LAISHARE -o username=eyanlai,password="**********",domain=eapac   /mnt/remote
cnshexiahan:~ # ls /mnt/remote
friends  vnc-4.0-x86_win32
```

2. mount remote Linux directory to local directory:

```
cnshexiahan:~ # pwd
/root
cnshexiahan:~ # mkdir home
cnshexiahan:~ #
cnshexiahan:~ #  mount  ecnshna001:/vol/vol_file2/unix-home/exiahan -t nfs home
cnshexiahan:~ # cd home
cnshexiahan:~/home # ls
Desktop    ISUP_Parameters.cpp
```
