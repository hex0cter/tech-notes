# Debian Linux 下mount USB 移动硬盘文件名显示为乱码的解决办法

Just add a new record in `/etc/fstab` with the following options:

```
/dev/sdb1 /mnt vfat rw,nosuid,nodev,uid=1000,gid=1000,shortname=mixed,dmask=0077,utf8=1,showexec,flush,uhelper=udisks 0 0`
```

Or from command line,

```
sudo mount /dev/sdb1 /mnt -o utf8
```
