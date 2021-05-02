# [Keeping Your SSH Connection Alive](http://pthree.org/2008/04/16/keeping-your-ssh-connection-alive/)

Being an instructor for [Guru Labs](http://gurulabs.com/), I’m in training centers all over the nation. As such, I never know what hardware I’ll be facing, or for that matter, their network setup. This can be problematic, as setting up for class could present troubleshooting on my end before students arrive and class starts.

One of the issues that has plagued me, but I haven’t bothered to do anything about it until this morning, is networks dropping my TCP connections if there is no activity after a given interval. Currently, I’m in Mountain View, California teaching a Linux course, and the training center network is one such network with dropping inactive TCP connections after 60 seconds. Annoyed (being a heavy SSH user), I began digging in the SSH man page on my machine, and found a way to keep my connection alive.

There are two options for addressing my need: TCPKeepAlive and ServerAliveInterval. Each of those are explained here:

  * TCPKeepAlive: This uses the KEEPALIVE option of the TCP/IP protocol to keep a connection alive after a specified interval of inactivity. On most systems, this means 2 hours. So, with the TCPKeepAlive option passed to SSH, the SSH client will send an encrypted packet to the SSH server, keeping your TCP connection up and running.

    ssh -o TCPKeepAlive=yes user@some.host.com

  * ServerAliveInterval: This sets a timeout interval in seconds, which is specified by you, from which if no packets are sent from the SSH client to the SSH server, SSH will send an encrypted request to the server for a TCP response. To make that request every 30 seconds:

    ssh -o ServerAliveInterval=30 user@some.host.com

If ServerAliveInterval is used in the SSH command, then TCPKeepAlive is not needed, and should be turned off.

Now, in the training centers I visit, giving this option will ensure that my SSH connection stays connected, so I can stay on top of my IRC and MUC.
