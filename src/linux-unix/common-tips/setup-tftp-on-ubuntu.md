# [Setup tftp on Ubuntu](http://www.davidsudjiman.info/2006/03/27/installing-and-setting-tftpd-in-ubuntu/)

<http://www.davidsudjiman.info/2006/03/27/installing-and-setting-tftpd-in-ubuntu/>

<http://pjpramod.blogspot.com/2009/08/setting-up-tftp-server-on-ubuntu-904.html>

## tftpd Setup

Install tftpd on your system.

```
#sudo apt-get install tftpd
```

Configuring the tftpd directory:
```
#sudo mkdir /tftpboot ; if directory is not yet created
#sudo chmod -R 777 /tftpboot
#sudo chown -R username:username /tftpboot ;replace 'username' with your actual username
```

Create /etc/xinetd.d/tftp and insert the following:
```
service tftp
{
socket_type = dgram
protocol = udp
wait = yes
user = username ; Enter your user name
server = /usr/sbin/in.tftpd
server_args = -s /tftpboot
per_source = 11
cps = 100 2
disable = no
}
```

Now restart the tftpd server
```
#sudo /etc/init.d/xinetd start
```
