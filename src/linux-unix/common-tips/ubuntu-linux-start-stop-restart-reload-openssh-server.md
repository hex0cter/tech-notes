# [Ubuntu Linux: Start / Stop / Restart / Reload OpenSSH Server](https://www.cyberciti.biz/faq/howto-start-stop-ssh-server/r)



Type the following command:

`$ sudo /etc/init.d/ssh start`

OR

`$ sudo service ssh start`

OR for systemd based Ubuntu Linux 16.04 LTS or above server:

`$ sudo systemctl start ssh`

## Ubuntu Linux: Stop OpenSSH server

Type the following command:

`$ sudo /etc/init.d/ssh stop`

OR

`$ sudo service ssh stop`

OR for systemd based Ubuntu Linux 16.04 LTS or above server:

`$ sudo systemctl stop ssh`

## Ubuntu Linux: Restart OpenSSH server

Type the following command:

`$ sudo /etc/init.d/ssh restart`

OR

`$ sudo service ssh restart`

OR for systemd based Ubuntu Linux 16.04 LTS or above server:

`$ sudo systemctl restart ssh`




![systemctl start stop restart openssh server on Ubuntu](https://www.cyberciti.biz/media/new/faq/2007/10/systemctl-start-stop-restart-openssh-server-on-Ubuntu.png)

systemctl command in action on Ubuntu Linux desktop

## Ubuntu Linux: See status of OpenSSH server

Type the following command:

`$ sudo /etc/init.d/ssh status`

OR

`$ sudo service ssh status`

OR for systemd based Ubuntu Linux 16.04 LTS or above server:

`$ sudo systemctl status ssh`
