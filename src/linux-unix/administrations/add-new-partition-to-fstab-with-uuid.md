
# [Add new partition to fstab with UUID](http://www.tuxfiles.org/linuxhelp/fstab.html)

1\. Check UUID string with (on Ubuntu):

```
$ sudo blkid

/dev/sda1: UUID="433fb16b-740b-4c54-b392-0fefd59e6568" TYPE="ext4"

/dev/sda2: UUID="2e8ade14-dfdf-4e79-ba2a-c5b3dbb947a1" TYPE="ext4"

/dev/sda3: UUID="bcb4beff-cba5-42f6-a497-d729ab731cae" TYPE="swap"

/dev/sda5: UUID="b727f196-366a-40f2-bc96-eeed359dbc51" TYPE="ext4"

/dev/sda6: UUID="65e2b5a8-ccfd-4c25-b29a-ee866bebed80" TYPE="ext4"

/dev/sda7: UUID="0E66-1E87" TYPE="vfat"
```



2\. Add it into

```
$ sudo vi /etc/fstab

UUID=0E66-1E87 /home/daniel/doc vfat defaults 0 2
```

3\. Reboot or run

```
sudo mount /dev/sda7
```
More options can be found at:

<http://www.tuxfiles.org/linuxhelp/fstab.html>
