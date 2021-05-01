# [Exclude/Hide a user from GDM Logon Window](http://forums.fedoraforum.org/showthread.php?t=246103)


vi /etc/gdm/custom.conf with the following:

```
    [greeter]
    Exclude=user1, user2
```
