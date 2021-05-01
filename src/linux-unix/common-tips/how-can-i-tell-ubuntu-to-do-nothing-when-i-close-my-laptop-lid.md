# [How can I tell Ubuntu to do nothing when I close my laptop lid?](http://askubuntu.com/questions/15520/how-can-i-tell-ubuntu-to-do-nothing-when-i-close-my-laptop-lid)


To make Ubuntu do nothing when laptop lid is closed:

  1. Open the `/etc/systemd/logind.conf` file in a text editor as root, for example,
```
        sudo -H gedit /etc/systemd/logind.conf
```

  2. Add a line `HandleLidSwitch=ignore` (make sure it's not commented out!),
  3. Restart the systemd daemon with this command:
```
        sudo restart systemd-logind
```
