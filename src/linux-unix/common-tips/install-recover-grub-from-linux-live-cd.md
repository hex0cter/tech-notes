# INSTALL/RECOVER GRUB FROM LINUX LIVE CD

Boot your Live CD/USB and open Terminal after that follow the commands:
You need the root:

```
sudo -i
```

To check the drives:
```
sudo fdisk -l
```

Now select your Linux drive and change the number in following commands(Only change ' **x** ' with your drive number) and change (sda) with your hard drive it can be (sdb, sdc, etc) you can see this in Partition Manager:

```
sudo mount /dev/sda x /mnt
sudo mount /dev/sda x /mnt/boot
sudo mount --bind /dev /mnt/dev/
```

Now Permission command:
```
sudo chroot /mnt
```

Now grub install command and Change the 'sda' with your hard drive check in Partition Manager:

```
grub-install /dev/sda
```

Now installation finished, Enter following commands to unmount:

```
sudo umount /mnt/dev
sudo umount /mnt
```

Now Reboot your pc. That's it, Enjoy.

<http://www.noobslab.com/2012/10/installrecover-grub-from-linux-live-cd.html>
<http://www.noobslab.com/2011/10/install-grub2-from-live-cdusb-after.html>
