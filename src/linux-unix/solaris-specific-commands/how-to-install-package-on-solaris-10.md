# How to install package on Solaris 10

You should really upgrade to Solaris 11. Much better.

However if you are still stuck on Solaris 10 then you can obtain the packages from the Solaris Companion Disk. This was previously distributed by Sun itself but is nowadays distributed by[SunFreeware](http://www.sunfreeware.com/companioncd.html).

```bash
mkdir /tmp/gawk/ && cp /home/handanie/tmp/SFWgawk.tar.gz /tmp/gawk/
cd /tmp/gawk/
gunzip SFWgawk.tar.gz
tar xvf SFWgawk.tar
cp -r SFWgawk /var/spool/pkg
pkgadd -G SFWgawk
```

gawk will be installed in /opt/sfw/bin/gawk
