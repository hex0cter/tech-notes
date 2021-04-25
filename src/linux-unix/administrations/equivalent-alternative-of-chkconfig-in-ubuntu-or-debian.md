# [equivalent/alternative of chkconfig in Ubuntu or Debian](http://linuxhostingsupport.net/blog/what-is-equivalentalternative-of-chkconfig-in-ubuntu-or-debian)


The alternative / equivalent of chkconfig in Ubuntu is “sysv-rc-conf”. To install sysv-rc-conf, ssh to the server and execute:
```
# apt-get install sysv-rc-conf
```
to start manging the services, execute
```
# sysv-rc-conf
```

It’s an easy to use interface for managing /etc/rc{runlevel}.d/ symlinks.  sysv-rc-conf provides a graphical view for turning services on and off at startup.
