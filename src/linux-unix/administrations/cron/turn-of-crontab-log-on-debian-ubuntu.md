# [Turn on crontab log on debian/ubuntu](http://www.linuxquestions.org/questions/programming-9/crontab-log-does-not-exist-552809/)

```
# nano /etc/rsyslog.conf
add the line below:
cron.* -/var/log/cron
and then
# /etc/init.d/rsyslog restart
```
