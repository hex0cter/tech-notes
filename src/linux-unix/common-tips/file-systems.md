# [File Systems](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/Lecture_Note_2.htm)

## File System
### Overview
A file system is how the storage media is organized to store files. Different file systems organize the media in different ways, hence different file system cannot understand each other.
* NTFS
* FAT32
* ext2

Usually when we talk about file system, we mean the way hard disks prepared for storing data.
### Partition
A disk is usually divided into partitions.
In a UNIX system one can use df to check on the file system status.
A partition can be viewed as a logically unit. Different partitions can have different file systems.
In a PC environment, we can have Windows NTFS or FAT32 on one partition, and Linux ext2 or swap partitions in another.
Each partition consists of the following.
* A boot block
* A super block
* A list of i-nodes
* Directory and data blocks

![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/figures/partition.jpg)

All figures are take from the textbook, "Advanced Programming in the Unix Environment," by W. Richard Stevens, unless stated otherwise.
![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/_themes/nature/anabull2.gif)

### i-node
Every file in a UNIX file system is uniquely represented by an i-node.

Each i-node has a unique i-node number as its identifier.

The i-node can be obtained from st_inode in stat buffer. Here we modify the myls last time to do it.

We can use "ls -i" to check for the i-node number.

![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/figures/inode.jpg)

### Blocks
A file (regular or directory) consists of a series of "blocks". Usually we say that the blocks in a regular file "data block", and those of a directory "directory blocks".

An i-node has the information (a set of pointers) so that it knows where to find its data/directory blocks.

The block size is usually 512 bytes in a UNIX file system.

The data blocks store the contents of a regular file.

The directory blocks store the information of subdirectories and files under this directory. The basic information include the following.
* The i-node number
* The name of this entities.

Recall that we use the opendir, readdir, and closedir to read the contents of a directory. We get exactly the "contents" of the directory file in the dirent structure. See this example myls.

There are two additional entities in directory files. Remember to skip them when traversing a directory tree.
	. (the current directory)
	.. (the parent directory)

Let's look a more complex example. Here we build a directory called "dir", within it we have a subdirectory "subdir", and a file "file".

### Hard links|
To create a file (be it regular file or directory), we simply add a entry in the parent directory, which consists of the i-node number and the name.

Since a file is created this way, we can make two pathnames pointing to the same i-node. This is called hard link.

We can use the link system call to make two pathnames sharing the same i-node. Here is the program to do it.

We can say that an i-node is the file, a pathname is simply a way to get to a i-node.

Notice that only the superuser can create hardlink for directory, since this might create file system chaos.
### Link count

Since more than one pathname may refer to the same i-node, each i-node maintains a reference count (or link count).

The link count can be obtained by st_nlink in the stat buffer, now we modify the myls to do it.

We reclaim the storage held by an i-node only when its link count becomes 0. Therefore we refer to this action as "remove a link", rather than delete a file. This is accomplished by the system call unlink.

One can only unlink a file when he has execute and write permission on the directory this file is in. The permission on the file is irrelevant. (Recall the sticky bit).

An unlink example.-- examples/apue/file/unlink.c

Similarly, we can rename a file within the same directory by the system call rename, which simply replace one entry by another. If we were to move a file from one directory to another, then we need permission on both directories. That is why rename a file is done by the mv command.

### Symbolic links
This is also called "soft links". It is actually a special file that directs you somewhere else.

Symbolic link id different from hard link.

It can go across file system, in fact it is just a string so it can even go non-existing places.

It does not have link count.

Anyone can create a symbolic link.

In fact a symbolic link is very much like the "shortcut" in Windows. However, in Windows only file can have shortcut, not directory.

We maintain symbolic links mainly for convenience.

I can create a symbolic link to go to the directories that i often visit.

The system can maintain a consistent look. For example, I always put the most up-to-date X distribution (maybe X11R6) under /usr, and use a symbolic link called X to refer it. In that case /usr/X is always the one I want.

Here we would to distinguish two operation modes when we perform operation on a symbolic file.

Follow the link

Do not follow the link.

Many functions we have encounter have two version -- one with l as the prefix and the other without.

Without l: it will follow the link. That means if you apply stat on a file, it will give you the status of the file the symbolic link points to.

Otherwise, like lstat, it gives you the status of the symbolic link itself.

Now you should understand in this program why lstat is used. Check the following program examples/apue/file/filetype.c
Operations on symbolic links
* symlink -It creates a symbolic link.
* readlink - It read the contents of a symbolic link.

Now we modify the tar program so that it handles symbolic links.

In the tar function, when we encounter a symbolic link, we must use readlink to get its contents, and store it into the archive.

In the untar function, we must read the symbolic link contents from the archive file, and use symlink to restore it.

i-nodes addressing example
BSD 4.4 style inode

![](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/figures/inode-detail.jpg)
 This figure is taken from "Operation System Concepts" by Silberschatz and Galvin.

 The block size is 4K.

 12 direct pointers can go to 12 blocks (48K).

 It has one single indirect pointer pointing to a "pointer block" of 1K pointers (4 bytes per pointer), which in turn point to 1K data blocks, so the total size is now 12 + 1024 blocks.

 It has one double indirect pointer pointing to a "pointer block" of 1K single indirect pointers, so the total size is now 12 + 1024 + 1024*1024 blocks.

 Finally it has a triple indirect pointer, so the total is 12 + 1024 + 1024*1024 + 1024 * 1024 * 1024 blocks.

### File size

There are three file sizes:

* one reported by st_size from the stat call.
* The logical size when access by I/O routines by `du`
* The disk space used.

A "hole" can be made by the seeking functions -- fseek from stdio.h or the lseek system calls. They move the pointer within a file without actually writing the data. See the following example. [examples/apue/file/hole.c](http://www.csie.ntu.edu.tw/~pangfeng/System%20Programming/examples/apue/file/hole.c)
