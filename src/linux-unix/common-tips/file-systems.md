
date: None  
author(s): None  

# [File Systems - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/file-systems)

<http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/Lecture_Note_2.htm>

![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull1.gif)| File System| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| Overview| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| A file system is how the storage media is organized to store files.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Different file systems organize the media in different ways, hence different file system cannot understand each other.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| NTFS  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| FAT32  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| ext2  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Usually when we talk about file system, we mean the way hard disks prepared for storing data.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| Partition| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| A disk is usually divided into partitions.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| In a UNIX system one can use [df](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/man/df.1.html) to check on the file system status.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| A partition can be viewed as a logically unit. Different partitions can have different file systems.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| In a PC environment, we can have Windows NTFS or FAT32 on one partition, and Linux ext2 or swap partitions in another.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Each partition consists of the following.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| A boot block  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| A super block  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| A list of i-nodes  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Directory and data blocks  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/figures/partition.jpg)  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| All figures are take from the textbook, "Advanced Programming in the Unix Environment," by W. Richard Stevens, unless stated otherwise.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| i-node| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Every file in a UNIX file system is uniquely represented by an i-node.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Each i-node has a unique i-node number as its identifier.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The i-node can be obtained from st_inode in stat buffer. Here we modify the [myls](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/examples/myls.c) last time to do it.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| We can use "ls -i" to check for the i-node number.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/figures/inode.jpg)  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| Blocks| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| A file (regular or directory) consists of a series of "blocks". Usually we say that the blocks in a regular file "data block", and those of a directory "directory blocks".  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| An i-node has the information (a set of pointers) so that it knows where to find its data/directory blocks.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The block size is usually 512 bytes in a UNIX file system.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The data blocks store the contents of a regular file.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The directory blocks store the information of subdirectories and files under this directory. The basic information include the following.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The i-node number  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The name of this entities.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/figures/directory.jpg)  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Recall that we use the opendir, readdir, and closedir to read the contents of a directory. We get exactly the "contents" of the directory file in the dirent structure. See this example [myls](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/examples/myls.c).  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| There are two additional entities in directory files. Remember to skip them when traversing a directory tree.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| . (the current directory)  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| .. (the parent directory)  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Let's look a more complex example. Here we build a directory called "dir", within it we have a subdirectory "subdir", and a file "file".   
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| Hard links| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| To create a file (be it regular file or directory), we simply add a entry in the parent directory, which consists of the i-node number and the name.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Since a file is created this way, we can make two pathnames pointing to the same i-node. This is called hard link.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| We can use the link system call to make two pathnames sharing the same i-node. Here is the program to do it.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| We can say that an i-node is the file, a pathname is simply a way to get to a i-node.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Notice that only the superuser can create hardlink for directory, since this might create file system chaos.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| Link count| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Since more than one pathname may refer to the same i-node, each i-node maintains a reference count (or link count).  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The link count can be obtained by st_nlink in the stat buffer, now we modify the [myls](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/examples/myls.c) to do it.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| We reclaim the storage held by an i-node only when its link count becomes 0. Therefore we refer to this action as "remove a link", rather than delete a file. This is accomplished by the system call unlink.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| One can only [unlink](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/man/unlink.2.html) a file when he has execute and write permission on the directory this file is in. The permission on the file is irrelevant. (Recall the sticky bit).  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| An unlink example.-- [examples/apue/file/unlink.c](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/examples/apue/file/unlink.c)  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Similarly, we can [rename](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/man/rename.2.html) a file within the same directory by the system call rename, which simply replace one entry by another. If we were to move a file from one directory to another, then we need permission on both directories. That is why rename a file is done by the [mv](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/man/mv.1.html) command.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| Symbolic links| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| This is also called "soft links". It is actually a special file that directs you somewhere else.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Symbolic link id different from hard link.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| It can go across file system, in fact it is just a string so it can even go non-existing places.   
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| It does not have link count.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Anyone can create a symbolic link.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| In fact a symbolic link is very much like the "shortcut" in Windows. However, in Windows only file can have shortcut, not directory.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| We maintain symbolic links mainly for convenience. | ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| I can create a symbolic link to go to the directories that i often visit.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The system can maintain a consistent look. For example, I always put the most up-to-date X distribution (maybe X11R6) under /usr, and use a symbolic link called X to refer it. In that case /usr/X is always the one I want.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Here we would to distinguish two operation modes when we perform operation on a symbolic file.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Follow the link  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Do not follow the link.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Many functions we have encounter have two version -- one with l as the prefix and the other without. | ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Without l: it will follow the link. That means if you apply stat on a file, it will give you the status of the file the symbolic link points to.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Otherwise, like lstat, it gives you the status of the symbolic link itself.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Now you should understand in this program why lstat is used. Check the following program [examples/apue/file/filetype.c](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/examples/apue/file/filetype.c)  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Operations on symbolic links| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| [symlink](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/man/symlink.2.html)| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| It creates a symbolic link.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| [readlink](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/man/readlink.2.html)| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| It read the contents of a symbolic link.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| Now we modify the tar program so that it handles symbolic links.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| In the tar function, when we encounter a symbolic link, we must use readlink to get its contents, and store it into the archive.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| In the untar function, we must read the symbolic link contents from the archive file, and use symlink to restore it.   
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull1.gif)| i-nodes addressing example| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| BSD 4.4 style inode  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/figures/inode-detail.jpg)  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| This figure is taken from "Operation System Concepts" by Silberschatz and Galvin.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| The block size is 4K.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| 12 direct pointers can go to 12 blocks (48K).  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| It has one single indirect pointer pointing to a "pointer block" of 1K pointers (4 bytes per pointer), which in turn point to 1K data blocks, so the total size is now 12 + 1024 blocks.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| It has one double indirect pointer pointing to a "pointer block" of 1K single indirect pointers, so the total size is now 12 + 1024 + 1024*1024 blocks.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| Finally it has a triple indirect pointer, so the total is 12 + 1024 + 1024*1024 + 1024 * 1024 * 1024 blocks.  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull1.gif)| File size| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| There are three file sizes| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| one reported by st_size from the stat call.| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The logical size when access by I/O routines  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| by du| ![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull3.gif)| The disk space used.  
---|---  
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)| A "hole" can be made by the seeking functions -- fseek from stdio.h or the lseek system calls. They move the pointer within a file without actually writing the data. See the following example.[examples/apue/file/hole.c](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/examples/apue/file/hole.c)

