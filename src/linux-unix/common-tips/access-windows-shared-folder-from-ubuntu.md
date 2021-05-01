# [Access Windows shared folder from Ubuntu](http://mytechnotes.wordpress.com/2007/05/21/windows-shared-folder-from-ubuntu/)

1. install smbfs: `$sudo apt-get install smbfs`
2. use ‘mount’ to mount the file share
* for mount you need to create a local folder that will be the mount point for example create a folder test under /media
* then mount the share using
  * `$sudo mount -t smbfs -o username=myusername //192.168.0.10/sharename /media/test`
  * myusername – is a valid username on the windows machine
  * the ip address is the ip of the windows machine
  * sharename is the name given to the share on the windows machine
  * This will prompt you for the passwor d- the password for myusername on the windows machine
  * on successful password you will be able to see the contents of the sharedfolder under /media/test
  * Note: if you this is the first time you are using sudo in this shell session or if sudo has timed out there will be two password prompts first for the sudo next for the share mount. you could avoid this by doing `$sudo -v` before doing the sudo mount

3. to umount:
`$sudo umount /media/test`
