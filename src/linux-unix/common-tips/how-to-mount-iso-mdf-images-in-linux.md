# [How to Mount ISO/MDF Images in Linux](http://lindesk.com/2007/05/how-to-mount-isomdf-images-in-linux/)

```
mount -t iso9660 -o loop <Image_File> <Mount_Point>
```

Mounting Example:
```
mount -t iso9660 -o loop /home/binnyva/Films/300.iso /mnt/Image
```

The ‘-t’ option specifies the filetype – this is optional.

This command works with both ISO and MDF images.
