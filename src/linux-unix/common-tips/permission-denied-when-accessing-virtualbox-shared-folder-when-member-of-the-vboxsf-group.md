# [Permission denied when accessing VirtualBox shared folder when member of the vboxsf group](http://superuser.com/questions/307853/permission-denied-when-accessing-virtualbox-shared-folder-when-member-of-the-vbo)

```
sudo usermod -a -G vboxsf <username>
```

Add the user to the vboxsf group, log out and in again.
