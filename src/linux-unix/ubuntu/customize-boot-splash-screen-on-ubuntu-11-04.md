# Customize boot splash screen on Ubuntu 11.04 (Plymouth)

1. Download and unpack the plymouth theme into /lib/plymouth/themes/, for example,
```
cp -r ~/tmp/space_sunrise_1.0_all/space-sunrise/ /lib/plymouth/themes/
```

2.
```
sudo update-alternatives --install /lib/plymouth/themes/default.plymouth default.plymouth /lib/plymouth/themes/space-sunrise/space-sunrise.plymouth 100
```

3.
```
sudo update-alternatives --config default.plymouth
```

4.
```
sudo update-initramfs -u
```

5.
```
sudo reboot
```
