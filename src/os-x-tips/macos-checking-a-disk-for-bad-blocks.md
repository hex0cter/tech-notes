
date: None  
author(s): None  

# [MacOS: Checking a disk for bad blocks - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/os-x-tips/macos-checking-a-disk-for-bad-blocks)

Hardware fails, but most disk tools on MacOS only check logical disk structures, not bad blocks.

![](https://wiert.files.wordpress.com/2020/03/screenshot-2018-10-21-21-35-46.png?w=368&h=442)Luckily, `fsck_hfs` can, though Apple is a bit secretive on it: [[WayBack](https://web.archive.org/web/*/https://developer.apple.com/library/archive/documentation/Darwin/Reference/ManPages/man8/fsck_hfs.8.html)] [Page Not Found – Apple Developer: ManPages/man8/fsck_hfs.8.html](https://developer.apple.com/library/archive/documentation/Darwin/Reference/ManPages/man8/fsck_hfs.8.html) is empty, but there is [[WayBack](https://web.archive.org/web/20181021193736/https://www.manpagez.com/man/8/fsck_hfs/)] [man page fsck_hfs section 8](https://www.manpagez.com/man/8/fsck_hfs/) and the gist below.

Disk volumes on MacOS use a successor of HFS called [HFS Plus – Wikipedia](https://en.wikipedia.org/wiki/HFS_Plus), but the tooling never changed names.

I got at the below parameters through [

This is the disk check command:

> 
>     # **sudo fsck_hfs -dylS /dev/disk3s1**
>     _** /dev/rdisk3s1 (NO WRITE) Using cacheBlockSize=32K cacheTotalBlock=65536 cacheSize=2097152K.
>     Scanning entire disk for bad blocks_   Executing fsck_hfs (version hfs-407.50.6).
>     ** Performing live verification.
>     ** Checking Journaled HFS Plus volume.
>        The volume name is SanDisk400GB
>     ** Checking extents overflow file.
>     ** Checking catalog file.
>     ** Checking extended attributes file.
>     ** Checking volume bitmap.
>     ** Checking volume information.
>     ** The volume SanDisk400GB appears to be OK.
>         CheckHFS returned 0, fsmodified = 0
>     

The italic part is the bad block scanning. The normal part the hfs scanning, which will continue even after finding bad blocks.

If bad blocks are found, output looks more like on the right. If it looks like that, basically you know a disk is toast.

It can be slow, as I did not specify a cache, so it defaults to 32 [Kibibyte](https://en.wikipedia.org/wiki/Kibibyte). You can increase that by adding for instance `-c 512m` for 512 [Mebibyte](https://en.wikipedia.org/wiki/Mebibyte) cache, just read the short help or man page below.

This tremendously helps checking volumes containing many files, for instance [[WayBack](https://web.archive.org/web/20181021193754/https://hints.macworld.com/article.php?story=20110829063745320)] [Checking Very Large Time Machine Volumes – Mac OS X Hints](http://hints.macworld.com/article.php?story=20110829063745320)

> 
>     #c fsck_hfs -h
>     fsck_hfs: illegal option -- h
>     usage: fsck_hfs [-b [size] B [path] c [size] e [mode] ESdfglx m [mode] npqruy] special-device
>       b size = size of physical blocks (in bytes) for -B option
>       B path = file containing physical block numbers to map to paths
>       c size = cache size (ex. 512m, 1g)
>       e mode = emulate 'embedded' or 'desktop'
>       E = exit on first major error
>       d = output debugging info
>       f = force fsck even if clean (preen only) 
>       g = GUI output mode
>       x = XML output mode
>       l = live fsck (lock down and test-only)
>       m arg = octal mode used when creating lost+found directory 
>       n = assume a no response 
>       p = just fix normal inconsistencies 
>       q = quick check returns clean, dirty, or failure 
>       r = rebuild catalog btree 
>       S = Scan disk for bad blocks
>       u = usage 
>       y = assume a yes response

