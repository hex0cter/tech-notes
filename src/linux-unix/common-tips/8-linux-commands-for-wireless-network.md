
date: None  
author(s): None  

# [8 Linux Commands For Wireless Network - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/8-linux-commands-for-wireless-network)

Linux operating systems comes with various set of tools allowing you to manipulate the Wireless Extensions and monitor wireless networks. This is a list of tools used for wireless network monitoring tools that can be used from your laptop or desktop system to find out network speed, bit rate, signal quality/strength, and much more.  


## #1: Find out your wireless card chipset information

Type the following command to list installed wireless card, enter:  
`$ [lspci](http://www.cyberciti.biz/faq/tag/lspci-command/)  
$ [lspci | grep -i wireless](http://www.cyberciti.biz/tips/linux-find-supported-pci-hardware-drivers.html)  
$ [lspci | egrep -i --color 'wifi|wlan|wireless'](http://www.cyberciti.biz/tips/tag/lspci-command)`  
Sample outputs:
    
    
    0c:00.0 Network controller: Intel Corporation Ultimate N WiFi Link 5300

Please note down the 0c:00.0.

## #2: Find out wireless card driver information

Type the following command to get [information about wireless card driver](http://www.cyberciti.biz/faq/linux-find-wireless-driver-chipset/), enter:  
`$ [lspci -vv -s 0c:00.0](http://www.cyberciti.biz/faq/tag/lspci-command/)`  
Sample outputs:
    
    
    0c:00.0 Network controller: Intel Corporation Ultimate N WiFi Link 5300
    	Subsystem: Intel Corporation Device 1121
    	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
    	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- SERR-
    	Kernel driver in use: iwlwifi

## #3: Disabling wireless networking ( Wi-Fi )

You may want to disable Wi-Fi on all laptops as it poses a serious security risk to sensitive or classified systems and networks. You can easily [disable Wi-Fi under Linux using the techniques](http://www.cyberciti.biz/faq/linux-remove-wireless-networking-wifi-802-11-support-drivers/) described in this tutorial.

## #4: Configure a wireless network interface

iwconfig command is similar to [ifconfig command](http://www.cyberciti.biz/faq/tag/ifconfig-command/), but is dedicated to the Linux wireless interfaces. It is used to manipulate the basic wireless parameters such as ssid, mode, channel, bit rates, encryption key, power and much more. To display information about wlan0 wireless interface, enter:
    
    
    iwconfig Interface-Name-Here
    iwconfig wlan0

Sample outputs:
    
    
    wlan0 IEEE 802.11abgn **ESSID:"nixcraft5g"** Mode:Managed **Frequency:5.18 GHz** Access Point: 74:44:44:44:57:FC **Bit Rate=6 Mb/s** Tx-Power=15 dBm Retry long limit:7 RTS thr:off Fragment thr:off Encryption key:off Power Management:off **Link Quality=41/70** **Signal level=-69 dBm**
              Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
              Tx excessive retries:0  Invalid misc:28   Missed beacon:0

In the above output iwconfig command shows lots of information:

  1. The name of the MAC protocol used
  2. ESSID (Network Name)
  3. The NWID
  4. The frequency (or channel)
  5. The sensitivity
  6. The mode of operation
  7. Access Point address
  8. The bit-rate
  9. The RTS threshold
  10. The fragmentation threshold
  11. The encryption key
  12. The power management settings



### How do I find out link quality?

You can get overall quality of the link. This may be based on the level of contention or interference, the bit or frame error rate, how good the received signal is, some timing synchronisation, or other hardware metric.  
`# iwconfig wlan0 | grep -i --color quality`  
Sample outputs:
    
    
     **Link Quality=41/70**  Signal level=-69 dBm

41/70 is is an aggregate value, and depends totally on the driver and hardware.

### How do I find out signal level?

To find out received signal strength (RSSI - how strong the received signal is). This may be arbitrary units or dBm, iwconfig uses driver meta information to interpret the raw value given by /proc/net/wireless and display the proper unit or maximum value (using 8 bit arithmetic). In Ad-Hoc mode, this may be undefined and you should use the iwspy command.  
`# iwconfig wlan0 | grep -i --color signal`  
Sample outputs:
    
    
    Link Quality=41/70 **Signal level=-69 dBm**

Some parameters are only displayed in short/abbreviated form (such as encryption). You need to use the iwlist command to get all the details.

## #5: See link quality continuously on screen

You can use /proc/net/wireless file. The iwconfig will also display its content as described above.
    
    
     
    cat /proc/net/wireless
     

Better use the [watch (gnuwatch, bsdwatch) command](http://www.cyberciti.biz/tips/how-do-i-monitor-linuxbsd-system-over-time-without-scrolling-output.html) to run cat command repeatedly, displaying wireless signal on screen:
    
    
     
    watch -n 1 cat /proc/net/wireless
     

Sample outputs:  


[![Linux watch wireless signal](http://s0.cyberciti.org/images/tips/2012/06/wireless-link-speed.png)](http://s0.cyberciti.org/images/tips/2012/06/wireless-link-speed.png)

Fig.01: Linux watch wireless signal with /proc file system

  
Note: Again values will depend on the driver and the hardware specifics, so you need to refer to your driver documentation for proper interpretation of those values.

## #6: Gnome NetworkManager

[![Gnome Network Manger ](http://s0.cyberciti.org/images/tips/2012/06/gnome-network-manager.png)](http://s0.cyberciti.org/images/tips/2012/06/gnome-network-manager.png)

Fig:02: Gnome Network Manger

  
Gnome and many other Linux desktop operating system can use NetworkManager to keep an active network connection available at all times. he point of NetworkManager is to make networking configuration and setup as painless and automatic as possible. This package contains a systray applet for GNOME's notification area but it also works for other desktop environments which provide a systray like KDE or XFCE. It displays the available networks and allows to easily switch between them. For encrypted networks it will prompt the user for the key/passphrase and it can optionally store them in the gnome-keyring.

Please note that NetworkManager is configured through graphical interfaces, which are available for both GNOME and KDE.

## #7: Say hello to wavemon

wavemon is a ncurses-based monitoring application for wireless network devices. It displays continuously updated information about signal levels as well as wireless-specific and general network information. Currently, wavemon can be used for monitoring devices supported by the wireless extensions, included in kernels version 2.4 and higher. Just type the following command to see the details:  
`$ wavemon`  


[![wavemon - a wireless network monitor application](http://s0.cyberciti.org/images/tips/2012/06/wavemon.png)](http://s0.cyberciti.org/images/tips/2012/06/wavemon.png)

Fig.03: wavemon - a wireless network monitor application for Linux

## #8: Other options

You can use the following tools too:

  1. [Wicd](https://launchpad.net/wicd) which stands for Wireless Interface Connection Daemon, is an open source software utility to manage both wireless and wired networks for Linux.
  2.  **iwevent command** displays Wireless Events received through the RTNetlink socket. Each line displays the specific Wireless Event which describes what has happened on the specified wireless interface. Sample outputs from iwevents:
    
        Waiting for Wireless Events from interfaces...
    07:11:57.124553   wlan0    Set Mode:Managed
    07:11:57.124621   wlan0    Set ESSID:off/any
    07:12:00.391527   wlan0    Scan request completed
    07:12:10.428741   wlan0    Scan request completed
    07:12:10.432618   wlan0    Set Mode:Managed
    07:12:10.432642   wlan0    Set ESSID:off/any
    07:12:10.432651   wlan0    Set Frequency:5.18 GHz (Channel 36)
    07:12:10.432722   wlan0    Set ESSID:"nixcraft5g"
    07:12:10.647943   wlan0    Association Response IEs:01088C129824B048606C2D1A7E081BFFFFFF00010000000000C20101000000000000000000003D16240D0000000000000000000000000000000000000000DD0
    07:12:10.648019   wlan0    New Access Point/Cell address:74:44:44:44:57:FC
    07:12:22.310182   wlan0    Scan request completed
    

  3. **iwgetid command** report ESSID, NWID or AP/Cell Address of wireless network. iwgetid is easier to integrate in various scripts. A sample output from iwgetid command:
    
        wlan0     ESSID:"nixcraft5g"

  4.  **iwlist command** Get more detailed wireless information from a wireless interface. A typical usage is as follows:
    
        Usage: iwlist [interface] scanning [essid NNN] [last]
                  [interface] frequency
                  [interface] channel
                  [interface] bitrate
                  [interface] rate
                  [interface] encryption
                  [interface] keys
                  [interface] power
                  [interface] txpower
                  [interface] retry
                  [interface] ap
                  [interface] accesspoints
                  [interface] peers
                  [interface] event
                  [interface] auth
                  [interface] wpakeys
                  [interface] genie
                  [interface] modulation
    




#### See also:

  * man pages iwlist, iw, iwconfig, iwgetid, iwevent, iwlist
  * [Linux wireless](http://linuxwireless.org/) wiki



Have a favorite wireless tool for Linux? Let's hear about it in the comments.

