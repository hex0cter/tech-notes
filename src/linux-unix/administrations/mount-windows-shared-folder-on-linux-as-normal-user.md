
# Mount windows shared folder on Linux as normal user

1.
```
sudo apt-get install cifs-utils
```

2.
```
sudo vi /etc/fstab
```
with:
```
//10.216.0.25/simcert  /simcert cifs  noauto,user 0 0
```

3
```
chmod u+s /sbin/mount.cifs
```

4. now
```
mount /simcert (your password towards the Windows server might be needed)
```

as normal user

Another way:
```
/sbin/mount.cifs //10.216.0.25/simcert /home/handaniel/simcert/ -o user=handaniel,domain=ACCOUNTS
```
This is tested as root on Red Hat Enterprise Linux Server release 6.5 (Santiago)
