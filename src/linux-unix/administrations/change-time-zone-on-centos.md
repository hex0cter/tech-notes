
date: None
author(s): None

# [Change time zone on CentOS](https://chrisjean.com/change-timezone-in-centos/)

```
sudo mv /etc/localtime /etc/localtime.bak
sudo ln -s /usr/share/zoneinfo/ **America/Chicago** /etc/localtime
```
