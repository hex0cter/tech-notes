
date: None
author(s): None

# MBR tips

Backup:

```
dd if=/dev/sda of=~/mbr.img bs=512 count=1
```

Restore:

```
dd of=/dev/sda if=~/yourfile bs=512 count=1
```

Pay attention to the device name if you are using live CD. They may be someting else.
