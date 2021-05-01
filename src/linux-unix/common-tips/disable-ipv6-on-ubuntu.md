
date: None
author(s): None

# [Disable IPv6 on Ubuntu](http://el.web.id/how-to-disable-ipv6-in-ubuntu-12-04-231)

In order to **disable IPv6 in Ubuntu 12.04** , you need to edit **/etc/sysctl.conf** file.

```
    sudo nano /etc/sysctl.conf
```

Add these lines in the very bottom of the file:

```
    # IPv6
    net.ipv6.conf.all.disable_ipv6 = 1
    net.ipv6.conf.default.disable_ipv6 = 1
    net.ipv6.conf.lo.disable_ipv6 = 1
```

Save and exit from the `nano` file editor.

Next, we need to reload the configuration.

```
    sudo sysctl -p
```

Done. Try to reload your browser. Hopefully that IPv6 error is gone.
