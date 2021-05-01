# [Changing Network Interface Name on Linux](http://www.cyberciti.biz/faq/howto-linux-rename-ethernet-devices-named-using-udev/)

Awireless NIC (Network Interface Controller) is showing as wlan0 but I need to be appear as eth1. How can I rename wlan0 devices through udev as eth1? How do I change or rename eth0 as wan0 under Linux operating systems?

The best way to rename Ethernet devices is through udev. It is the device manager for the Linux kernel. Primarily, it manages device nodes in /dev. It is the successor of devfs and hotplug, which means that it handles /dev directory and all user space actions when adding/removing devices, including firmware load.

The order of the network interfaces may be unpredictable under certain configurations. Between reboots it usually stays the same, but often after an upgrade to a new kernel or the addition or replacement of a network card (NIC) the order of all network interfaces changes. For example, what used to be rl0 now becomes wlan0 or what used to be eth0 now becoems eth2 or visa versa.

Type the following command:
`# ifconfig -a | grep -i --color hwaddr`

Sample outputs:


    eth0      Link encap:Ethernet  HWaddr b8:ac:6f:65:31:e5
    pan0      Link encap:Ethernet  HWaddr 4a:71:40:ed:5d:99
    vmnet1    Link encap:Ethernet  HWaddr 00:50:56:c0:00:01
    vmnet8    Link encap:Ethernet  HWaddr 00:50:56:c0:00:08
    wlan0     Link encap:Ethernet  HWaddr 00:21:6a:ca:9b:10


Note down the MAC address.

## Step #2: Rename eth0 as wan0

To rename eth0 as wan0, edit a file called `70-persistent-net.rules` in`/etc/udev/rules.d/` directory, enter:
`# vi /etc/udev/rules.d/70-persistent-net.rules`
The names of the Ethernet devices are listed in this file as follows:


     
    # PCI device 0x14e4:0x1680 (tg3)
    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="b8:ac:6f:65:31:e5", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
     

Locate and identify the line with the NIC from step 1 (look for the MAC address). It may look like above. In this example, the interface eth0 will be renamed to wan0 (change `NAME="eth0"`to `NAME="wan0"`):


     
    # PCI device 0x14e4:0x1680 (tg3)
    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="b8:ac:6f:65:31:e5", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="eth*", NAME="wan0"
     

Save and close the file. [Reboot the system to test changes](http://www.cyberciti.biz/faq/howto-reboot-linux/):
```
# reboot
```

Verify new settings:

```
# ifconfig -a
# ifconfig wan0
# ifconfig -a | less
# ip addr show
```
