# [Mount a remote file system through ssh Using sshfs (SSH)](http://www.debianadmin.com/mount-a-remote-file-system-through-ssh-using-sshfs.html)

If you want to access a remote [file system](http://www.debianadmin.com/mount-a-remote-file-system-through-ssh-using-sshfs.html#) through ssh you need to install sshfs.sshfs is a filesystem client based on the SSH File Transfer Protocol. Since most [SSH servers](http://www.debianadmin.com/mount-a-remote-file-system-through-ssh-using-sshfs.html#) already support this protocol it is very easy to set up: i.e. on the server side there's nothing to do. On the client side mounting the file system is as easy as logging into the server with ssh.

 **sshfs Features**

  * Based on FUSE (the best userspace filesystem framework for linux)


  * Multithreading: more than one request can be on it's way to the server


  * Allowing large reads (max 64k)


  * Caching directory contents


  * sshfs runs entirely in user space. A user using sshfs does not need to deal with the [root account](http://www.debianadmin.com/mount-a-remote-file-system-through-ssh-using-sshfs.html#) of the remote machine. In the case of NFS, Samba etc., the admin of the remote machine has to grant access to those who will be using the services.



 **Install SSHFS in Debian**
```
# apt-get install fuse-utils sshfs
```
Next, let’s make sure the following condition is met. In the local system, type (as root)
```
# modprobe fuse
```

This will load the FUSE kernel module. Besides SSHFS, the FUSE module allows to do lots of other nifty tricks with file systems, such as the BitTorrent file system, the Bluetooth file system, the User-level versioning file system, the CryptoFS, the Compressed read-only file system and many others.

Now you need to make sure you have installed ssh in your [debian server](http://www.debianadmin.com/mount-a-remote-file-system-through-ssh-using-sshfs.html#) using the following command
```
# apt-get install ssh
```

 **Using SSHFS**

SSHFS is very simple to use. The following command
```
$ sshfs user@host: mountpoint
```
This will mount the [home directory](http://www.debianadmin.com/mount-a-remote-file-system-through-ssh-using-sshfs.html#) of the user@host account into the [local directory](http://www.debianadmin.com/mount-a-remote-file-system-through-ssh-using-sshfs.html#) named mountpoint. That’s as easy as it gets. (Of course, the mountpoint directory must already exist and have the appropriate permissions).


 **Example**

create the mount point
```
#mkdir /mnt/remote
#chown [user-name]:[group-name] /mnt/remote/
```

Add yourself to the fuse group
```
adduser [your-user] fuse
```
switch to your user and mount the remote filesystem.
```
sshfs remote-user@remote.server:/remote/directory /mnt/remote/
```
If you want to mount a directory other than the home directory, you can specify it after the colon. Actually, a generic sshfs command looks like this:
```
$ sshfs [user@]host:[dir] mountpoint [options]
```
 **Unmount Your Directory**

If you want to unmount your directory use the following command
```
fusermount -u mountpoint
```
