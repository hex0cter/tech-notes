
date: None  
author(s): None  

# [Easy Way to Install and Configure OpenVPN Server on Ubuntu 18.04 / Ubuntu 16.04 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/easy-way-to-install-and-configure-openvpn-server-on-ubuntu-18-04-ubuntu-16-04)

Do you want to access the internet securely and safely while leveraging open and untrusted networks like Wi-Fi access points?. [OpenVPN](https://openvpn.net/) is a full-featured, open-source Secure Socket Layer (SSL) VPN solution that supports a wide range of configurations. By making use of [Virtual Private Network](https://en.wikipedia.org/wiki/Virtual_private_network) (VPN), you can securely traverse untrusted networks securely as if you were within the LAN.

In this guide, I’ll show you an easy way to have OpenVPN Server installed on Ubuntu 18.04 and ready for clients to start using it. I know OpenVPN setup through a manual process can be challenging especially for new users not experienced with Linux and VPNs.

### Install and Configure OpenVPN Server on Ubuntu 18.04 / Ubuntu 16.04

This method will work well with both Debian family distributions as well as Red Hat family. This guide is specific to Ubuntu 18.04 and Ubuntu 16.04, but the setup process will be similar for other distributions. It is a scripted way so anyone with basic Linux knowledge can follow along.

Setup Prerequisites

Before you start installing any package on your Ubuntu server, we always recommend making sure that all system packages are updated:
    
    
    $ sudo apt-get update
    $ sudo apt-get upgrade

### Installing and Configuring OpenVPN server on Ubuntu 18.04 / Ubuntu 16.04

Once you update the system, we can begin the installation and configuration of OpenVPN server on Ubuntu 18.04 / Ubuntu 16.04 system. We will use[ openvpn-install ](https://github.com/Nyr/openvpn-install)script which let you set up your own VPN server in no more than a minute, even if you haven’t used OpenVPN before. It has been designed to be as unobtrusive and universal as possible.

Follow below steps to have OpenVPN server installed and running:

#### Step 1: Install git

Install git by running the command:
    
    
    sudo apt-get install git

#### Step 2: Clone openvpn-install repository

Now clone the `openvpn-install` repository using git tool installed in Step one:
    
    
    $ **cd ~**
    $ **git clone**[ **https://github.com/Nyr/openvpn-install.git**](https://github.com/Nyr/openvpn-install.git)
    Cloning into 'openvpn-install'...
    remote: Counting objects: 345, done.
    remote: Total 345 (delta 0), reused 0 (delta 0), pack-reused 345
    Receiving objects: 100% (345/345), 99.15 KiB | 681.00 KiB/s, done.
    Resolving deltas: 100% (170/170), done.

#### Step 3: Change to `openvpn-install` and run OpenVPN installer

cd to the directory`openvpn-install` created by clone and run the installer script.
    
    
    $ **cd openvpn-install/**
    $ **ls -1**
    LICENSE.txt
    README.md
    openvpn-install.sh
    $ **chmod +x openvpn-install.sh**
    $ **sudo ./openvpn-install.sh**

You will get a couple of prompts to change or confirm default settings for the installation
    
    
    Welcome to this OpenVPN "road warrior" installer! I need to ask you a few questions before starting the setup.
    You can leave the default options and just press enter if you are ok with them. First, provide the IPv4 address of the network interface you want OpenVPN
    listening to.
    IP address: **192.168.10.2** Which protocol do you want for OpenVPN connections?
    1) UDP (recommended)
    2) TCP
    Protocol [1-2]: **1** What port do you want OpenVPN listening to?
    Port: **1194** Which DNS do you want to use with the VPN?
    1) Current system resolvers
    2) 1.1.1.1
    3) Google
    4) OpenDNS
    5) Verisign
    DNS [1-5]: **1** Finally, tell me your name for the client certificate.
    Please, use one word only, no special characters.
    Client name: client Okay, that was all I needed. We are ready to set up your OpenVPN server now.
    Press any key to continue... **<Enter>**

Press `<Enter>` after answering all the questions to start the installation process: If the installation was successful, you should get a success message at the end:
    
    
    sing configuration from ./openssl-easyrsa.cnf
    Check that the request matches the signature
    Signature ok
    The Subject's Distinguished Name is as follows
    commonName            :ASN.1 12:'client'
    Certificate is to be certified until Jul  4 07:53:27 2028 GMT (3650 days)
    
    Write out database with 1 new entries
    Data Base Updated
    Using configuration from ./openssl-easyrsa.cnf
    
    An updated CRL has been created.
    CRL file: /etc/openvpn/easy-rsa/pki/crl.pem
    
    394
    
    Finished!
    
    Your client configuration is available at: /root/client.ovpn
    If you want to add more clients, you simply need to run this script again!

Main OpenVPN server configuration file is,`/etc/openvpn/server.conf` you are free to tune and tweak it to your liking.
    
    
    $ cat  /etc/openvpn/server.conf 
    port 1194
    proto udp
    dev tun
    sndbuf 0
    rcvbuf 0
    ca ca.crt
    cert server.crt
    key server.key
    dh dh.pem
    auth SHA512
    tls-auth ta.key 0
    topology subnet
    server 10.8.0.0 255.255.255.0
    ifconfig-pool-persist ipp.txt
    push "redirect-gateway def1 bypass-dhcp"
    push "dhcp-option DNS 8.8.8.8"
    push "dhcp-option DNS 8.8.4.4"
    keepalive 10 120
    cipher AES-256-CBC
    comp-lzo
    user nobody
    group nogroup
    persist-key
    persist-tun
    status openvpn-status.log
    verb 3
    crl-verify crl.pem

A `tun0` virtual interface will be created during the setup process. This is used by OpenVPN clients subnet. Confirm its presence using:
    
    
    $ ip ad | grep tun0
    4: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 100
        inet 10.8.0.1/24 brd 10.8.0.255 scope global tun0

The default subnet for this interface is.`10.8.0.0/24.`OpenVPN server will be assigned `10.8.0.1` IP address:
    
    
    $ ip route | grep tun0
    10.8.0.0/24 dev tun0 proto kernel scope link src 10.8.0.1

To test this, use:
    
    
    $ sudo apt-get install traceroute

Then:
    
    
    $ traceroute 10.8.0.1
    traceroute to 10.8.0.1 (10.8.0.1), 30 hops max, 60 byte packets
     1  node-01.computingforgeeks.com (10.8.0.1)  0.050 ms  0.018 ms  0.019 ms

#### Step 4: Generate OpenVPN user profile (.ovpn file)

After completing step 1 through 3, your VPN Server is ready for use. We need to generate VPN Profiles to be used by the users. The same script we used for the installation will be used for this. It manages the creation and revocation of user profiles.
    
    
    # ./openvpn-install.sh 
    
    Looks like OpenVPN is already installed.
    
    What do you want to do?
       1) Add a new user
       2) Revoke an existing user
       3) Remove OpenVPN
       4) Exit
    Select an option [1-4]: 1
    
    Tell me a name for the client certificate.
    Please, use one word only, no special characters.
    Client name: josphat.mutai
    Generating a 2048 bit RSA private key
    ...+++
    .............................................................................................................................+++
    writing new private key to '/etc/openvpn/easy-rsa/pki/private/josphat.mutai.key.8dsSsOTWPe'
    -----
    Using configuration from ./openssl-easyrsa.cnf
    Check that the request matches the signature
    Signature ok
    The Subject's Distinguished Name is as follows
    commonName            :ASN.1 12:'josphat.mutai'
    Certificate is to be certified until Jul  4 08:10:32 2028 GMT (3650 days)
    
    Write out database with 1 new entries
    Data Base Updated
    
    Client josphat.mutai added, configuration is available at: /root/josphat.mutai.ovpn

From the output you can confirm the location of my profile,`/root/josphat.mutai.ovpn` you need to copy this profile to the user. The location of the associated private key is also provided `/etc/openvpn/easy-rsa/pki/private/josphat.mutai.key.8dsSsOTWPe`

#### Step 5: Connect to OpenVPN Server from the client

You can use the VPN client of your choice to configure OpenVPN client on your operating system. For those who want to use Official OpenVPN client, go to the [downloads page](https://openvpn.net/index.php/open-source/downloads.html) and get the latest release then install it.

[![](https://computingforgeeks.com/wp-content/uploads/2018/07/openvp-client-windows-01.png)](https://computingforgeeks.com/wp-content/uploads/2018/07/openvp-client-windows-01.png)

Once Installed, on Windows, navigate to the directory with the `ovpn` profile, right click on the file name and select “ **Start OpenVPN on this config file** “

For Linux users, you can use NetworkManager and openvpn plugin to connect to OpenVPN server. Check my previous guide for how to: [How to use nmcli to connect to OpenVPN Server on Linux](https://computingforgeeks.com/how-to-use-nmcli-to-connect-to-openvpn-server-on-linux/)

