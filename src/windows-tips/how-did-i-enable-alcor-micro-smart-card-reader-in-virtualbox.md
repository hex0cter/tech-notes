
date: None  
author(s): None  

# [How did I enable Alcor Micro Smart Card reader in Virtualbox - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/how-did-i-enable-alcor-micro-smart-card-reader-in-virtualbox)

Software: Windows 7 64bit. 

Hardware: HP Elitebook 8460P Notebook PC

Target: Make the built-in Alcor Micro smart card reader work on the guest OS.

C:\Program Files\Oracle\VirtualBox>VBoxManage list usbhost

Host USB Devices:

UUID: 9edb62ed-aaf9-403b-97e6-ab69bea836cc

VendorId: 0x03f0 (03F0)

ProductId: 0x3a1d (3A1D)

Revision: 0.0 (0000)

Port: 0

USB version/speed: 2/2

Address: {36fc9e60-c465-11cf-8056-444553540000}\0009

Current State: Captured

UUID: c2a753e9-662e-42f2-8090-c60d060b65e5

VendorId: 0x046d (046D)

ProductId: 0xc062 (C062)

Revision: 49.0 (4900)

Port: 0

USB version/speed: 2/2

Manufacturer: Logitech

Product: USB Laser Mouse

Address: {745a17a0-74d3-11d0-b6fe-00a0c90f57da}\0040

Current State: Busy

UUID: 86a32467-2968-4a07-abb0-23bf09b700e6

VendorId: 0x046d (046D)

ProductId: 0xc31d (C31D)

Revision: 102.1 (10201)

Port: 0

USB version/speed: 1/1

Manufacturer: Logitech

Product: USB Keyboard

Address: {36fc9e60-c465-11cf-8056-444553540000}\0040

Current State: Busy

UUID: 790e38b5-b41f-4c71-a3cd-12dc3111a174

VendorId: 0x0529 (0529)

ProductId: 0x0001 (0001)

Revision: 1.0 (0100)

Port: 0

USB version/speed: 1/1

Manufacturer: AKS

Product: Hardlock USB 1.12

Address: {36fc9e60-c465-11cf-8056-444553540000}\0047

Current State: Busy

 **UUID: 5ca23bce-a86c-4d46-b053-738eed5ae0f9**

 **VendorId: 0x058f (058F)**

 **ProductId: 0x9540 (9540)**

 **Revision: 1.32 (0132)**

 **Port: 0**

 **USB version/speed: 1/1**

 **Manufacturer: Generic**

 **Product: EMV Smartcard Reader**

 **Address: {50dd5230-ba8a-11d1-bf5d-0000f805f530}\0000**

 **Current State: Busy**

UUID: 528b875a-6518-484c-9fd9-287b47a6cab4

VendorId: 0x138a (138A)

ProductId: 0x003c (003C)

Revision: 0.134 (00134)

Port: 0

USB version/speed: 1/1

Address: {53d29ef7-377c-4d14-864b-eb3a85769359}\0000

Current State: Busy

UUID: ff4be7d3-6719-42da-87a2-d8523fe941cc

VendorId: 0x1bcf (1BCF)

ProductId: 0x2888 (2888)

Revision: 3.4 (0304)

Port: 0

USB version/speed: 2/2

Manufacturer: 6047B0021702A0117K8SY

Product: HP HD Webcam [Fixed]

Address: {36fc9e60-c465-11cf-8056-444553540000}\0008

Current State: Busy

The vendor ID and product ID can be verified by Device Manager, detailed information of Alcor Micro Smart Card Reader.

[![](https://sites.google.com/site/xiangyangsite/_/rsrc/1392798469298/home/technical-tips/windows-tips/how-did-i-enable-alcor-micro-smart-card-reader-in-virtualbox/smartcardreader.png)](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/how-did-i-enable-alcor-micro-smart-card-reader-in-virtualbox/smartcardreader.png?attredirects=0)

  


2\. On Virtualbox, change setting of the guest. USB -> Add filters --> Choose device 0580:9540. Check the box and start the guest OS.

3\. When the guest is started, it will indicate new hardware is found. Installing the driver automatically ends up with a failure.

4\. Download the driver from HP's website manually. 

http://h20566.www2.hp.com/portal/site/hpsc/template.PAGE/public/psi/swdHome/?sp4ts.oid=5056943&spf_p.tpst=swdMain&spf_p.prp_swdMain=wsrp-navigationalState%3DswEnvOID%253D1093%257CswLang%253D%257Caction%253DlistDriver&javax.portlet.begCacheTok=com.vignette.cachetoken&javax.portlet.endCacheTok=com.vignette.cachetoken

http://ftp.hp.com/pub/softpaq/sp63501-64000/sp63565.exe

5\. Install and reboot, Done!

