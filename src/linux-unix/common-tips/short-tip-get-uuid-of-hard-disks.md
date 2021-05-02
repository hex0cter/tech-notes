# [Get UUID of Hard Disks on Linux](http://liquidat.wordpress.com/2007/10/15/short-tip-get-uuid-of-hard-disks/)


There are several ways to get the UUID. The first one uses the `/dev/` directory. While you are on is you might want to check other `by-*` directories, I never knew of them.

```
$ ls -l /dev/disk/by-uuid
lrwxrwxrwx 1 root root 10 11. Okt 18:02 53cdad3b-4b01-4a6c-a099-be1cdf1acf6d -> ../../sda2
```

Another way to get the uuid by usage of the tool `blkid`:

```
$ blkid /dev/sda1
/dev/sda1: LABEL=``"/"` `UUID=``"ee7cf0a0-1922-401b-a1ae-6ec9261484c0"` `SEC_TYPE=``"ext2"` `TYPE=``"ext3"`
```

There you also get the label and other information. Quite useful.

BTW, if you wonder how “unique” this unique is, here a quote from Wikipedia:

> 1 trillion UUIDs would have to be created every nanosecond for 10 billion years to exhaust the number of UUIDs.

Pretty unique.
