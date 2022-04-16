# How to disable systemd-resolved in Ubuntu?

This method works on the Ubuntu releases 17.04 (Zesty), 17.10 (Artful), 18.04 (Bionic), 18.10 (Cosmic), 19.04 (Disco) and 20.04 (Focal):

Disable and stop the systemd-resolved service:
```
sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-resolved
```
Then put the following line in the [main] section of your /etc/NetworkManager/NetworkManager.conf:
```
dns=default
```
Delete the symlink /etc/resolv.conf
```
rm /etc/resolv.conf
```
Restart NetworkManager
```
sudo systemctl restart NetworkManager
```
Also be aware that disabling systemd-resolvd might break name resolution in VPN for some users. See this bug on launchpad (Thanks, Vincent).
