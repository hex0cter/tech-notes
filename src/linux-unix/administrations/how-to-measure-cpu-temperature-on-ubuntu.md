
date: None  
author(s): None  

# [How to measure CPU temperature on Ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/how-to-measure-cpu-temperature-on-ubuntu)

1\. sudo apt-get install lm-sensors

2\. sensors-detect 

To load everything that is needed, add this to /etc/modules:

#----cut here----

# Chip drivers

coretemp

#----cut here----

3\. sudo modprobe coretemp

4\. sensors  
  
---

