# [Stop Ubuntu / Debian Linux From Deleting /tmp Files on Boot](http://www.cyberciti.biz/faq/debian-ubuntu-removes-files-at-boot-time/)


Q. I know /tmp as it named is a temporary dircory, Debian policy is to clean /tmp at boot. However, I'd like to configure my Ubuntu Server to stop deleting files from /tmp on boot due to custom configuration issue. How do I configure behavior of boot scripts to stop deleting files on boot?

A. Users should not store files in /tmp, use /home or other partition, if you would like to keep the files. The behavior of boot scripts is controlled via a special configuration file called /etc/default/rcS. Open this file and modify TMPTIME variable.

On boot the files in /tmp will be deleted if their modification time is more than TMPTIME days ago. A value of 0 means that files are removed regardless of age. If you don't want the system to clean /tmp then set TMPTIME to a negative value(-1) or to the word infinite.

## Configuration /etc/default/rcS

Open /etc/default/rcS file, enter:
```
$ sudo vi /etc/default/rcS
```
Set TMPTIME to 60 so that files in /tmp will deleted if their modification time is more than 60 days ago.

```
TMPTIME=60
```


Close and save the file. This configuration is used by /etc/init.d/bootclean script on boot to clean /tmp and other directories under all Debian based Linux distros.

## A note about RHEL / CentOS / Fedora / Redhat Linux

Redhat and friends use **/etc/cron.daily/tmpwatch** cron job to clean files which haven’t been accessed for a period of time from /tmp. The default is 720 hours. If the file has not been accessed for 720 hours, the file is removed from /tmp. You can modify this script as per your requirements:
```
# cp /etc/cron.daily/tmpwatch /etc/cron.daily/tmpwatch.bak
# vi /etc/cron.daily/tmpwatch`
```
