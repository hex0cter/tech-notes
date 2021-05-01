# [SSH Tunneling (local port forwarding)](http://www.linuxhorizon.ro/ssh-tunnel.html)

Sintax:

```
ssh -L localport:host:hostport user@ssh_server -N
```

where:
```
-L          - port forwarding parameters (see below)
localport   - local port (chose a port that is not in use by other service)
host        - server that has the port (hostport) that you want to forward
hostport    - remote port
-N          - do not execute a remote command, (you will not have the shell, see below)
user        - user that have ssh access to the ssh server (computer)
ssh_server  - the ssh server that will be used for forwarding/tunneling Without the -N option you will have not only the forwardig port but also the remote shell. Try with and without it to see the difference. Note: 1. Privileged ports (localport lower then 1024) can only be forwarded by root. 2. In the ssh line you can use multiple -L like in the example... 3. Of course, you must have ssh user access on secure_computer and moreover the secure computer must have access to host:hostport 4. Some ssh servers do not allow port forwarding (tunneling). See the sshd man pages for more about port forwarding (the AllowTcpForwarding keyword is set to NO in sshd_config file, by default is set to YES)...
```

**Example:**
```
    ssh -L 8888:www.linuxhorizon.ro:80 user@computer -N
    ssh -L 8888:www.linuxhorizon.ro:80 -L 110:mail.linuxhorizon.ro:110 25:mail.linuxhorizon.ro:25 user@computer -N
```

The second example (see above) show you how to setup your ssh tunnel for web, pop3
and smtp. It is useful to recive/send your e-mails when you don't have direct access
to the mail server.

For the ASCII art and lynx browser fans here is illustrated the first example:
```
   +----------+<--port 22-->+----------+<--port 80-->o-----------+
   |SSH Client|-------------|ssh_server|-------------|   host    |
   +----------+             +----------+             o-----------+
  localhost:8888              computer      www.linuxhorizon.ro:80
```
...And finally:
Open your browser and go to http://localhost:8888 to see if your tunnel is working.
That's all folks!


The SSH man pages say:

-L port:host:hostport
 Specifies that the given port on the local (client) host is to be
 forwarded to the given host and port on the remote side.  This
 works by allocating a socket to listen to port on the local side,
 and whenever a connection is made to this port, the connection is
 forwarded over the secure channel, and a connection is made to
 host port hostport from the remote machine.  Port forwardings can
 also be specified in the configuration file.  Only root can for-
 ward privileged ports.  IPv6 addresses can be specified with an
 alternative syntax: port/host/hostport

-N Do not execute a remote command.  This is useful for just for-
 warding ports (protocol version 2 only).
