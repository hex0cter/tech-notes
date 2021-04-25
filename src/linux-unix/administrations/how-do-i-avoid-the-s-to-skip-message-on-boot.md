# [How do I avoid the “S to Skip” message on boot?](http://askubuntu.com/questions/120/how-do-i-avoid-the-s-to-skip-message-on-boot)


**Answer**:

You should add the option `nobootwait` to your `/etc/fstab`. So that it looks like:


    UUID=1234-5678 /osshare vfat utf8,auto,rw,user,nobootwait 0 0


From `fstab(5)`:

> The `mountall(8)` program that mounts filesystem during boot also recognises additional options that the ordinary `mount(8)` tool does not. These are: `bootwait` which can be applied to remote filesystems mounted outside of `/usr` or `/var`, without which `mountall(8)` would not hold up the boot for these; `nobootwait` which can be applied to non-remote filesystems to explicitly instruct `mountall(8)` not to hold up the boot for them;

---
