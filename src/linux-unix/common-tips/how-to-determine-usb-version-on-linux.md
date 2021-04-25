
date: None  
author(s): None  

# [How to determine USB version on Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-determine-usb-version-on-linux)

<http://serverfault.com/questions/96663/how-to-determine-usb-version-1-1-or-2-0>

Plug your device in, then see syslog:

> $ tail -n 2 /var/log/syslog  
> Dec 22 17:25:14 localhost kernel: [73348.931267] **usb 2-3** : new **high speed** USB device using ehci_hcd and address 13  
>  Dec 22 17:25:14 localhost kernel: [73349.084555] usb 2-3: configuration #1 chosen from 3 choices

Note the device bus id there: `usb 2-3`. Now get the version:

> $ cat /sys/bus/usb/devices/2-3/version  
> 2.00  
  
---

