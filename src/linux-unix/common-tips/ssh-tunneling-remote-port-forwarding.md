# [SSH Tunneling (remote port forwarding)](https://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html?utm_source=cronweekly.com)

Say that you’re developing a Rails application on your local machine, and you’d like to show it to a friend. Unfortunately your ISP didn’t provide you with a public IP address, so it’s not possible to connect to your machine directly via the internet.

Sometimes this can be solved by configuring NAT (Network Address Translation) on your router, but this doesn’t always work, and it requires you to change the configuration on your router, which isn’t always desirable. This solution also doesn’t work when you don’t have admin access on your network.

To fix this problem you need to have another computer, which is publicly accessible and have SSH access to it. It can be any server on the internet, as long as you can connect to it. We’ll tell SSH to make a tunnel that opens up a new port on the server, and connects it to a local port on your machine.

```
    $ ssh -R 9000:localhost:3000 user@example.com
```

The syntax here is very similar to local port forwarding, with a single change of `-L` for `-R`. But as with local port forwarding, the syntax remains the same.

First you need to specify the port on which th remote server will listen, which in this case is `9000`, and next follows `localhost` for your local machine, and the local port, which in this case is `3000`.

There is one more thing you need to do to enable this. SSH doesn’t by default allow remote hosts to forwarded ports. To enable this open `/etc/ssh/sshd_config` and add the following line somewhere in that config file.
```
GatewayPorts yes
```

Make sure you add it only once!

```
    $ sudo vim /etc/ssh/sshd_config
```

And restart SSH

```
    $ sudo service ssh restart
```

After this you should be able to connect to the server remotely, even from your local machine. The way this would work is that you would first create an SSH tunnel that forwards traffic from the server on port `9000` to your local machine on port `3000`. This means that if you connect to the server on port `9000` from your local machine, you’ll actually make a request to your machine through the SSH tunnel.
