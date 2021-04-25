
date: None  
author(s): None  

# [常见网络协议头结构图 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/network/protocol-headers)

IP：

[![](http://blog.csdn.net/images/blog_csdn_net/goodboy1881/193693/r_ip-protocol.JPG)](javascript:void\(0\);)

TCP:

![](http://www.ibm.com/developerworks/cn/linux/cluster/linux_cluster/part8/fig2.gif)

UDP：

[![](http://www.net130.com/CMS/Files/Uploadimages/2004101216931.gif)](javascript:void\(0\);)

  


 **传输层：**

对于UDP协议来说，整个包的最大长度为65535，其中包头长度是65535-20=65515； 

对于TCP协议来说，整个包的最大长度是由最大传输大小（MSS，Maxitum Segment Size）决定，MSS就是TCP数据包每次能够传 

输的最大数据分段。为了达到最佳的传输效能TCP协议在建立连接的时候通常要协商双方的MSS值，这个值TCP协议在实现的时候往往用MTU值代替（需 

要减去IP数据包包头的大小20Bytes和TCP数据段的包头20Bytes）所以往往MSS为1460。通讯双方会根据双方提供的MSS值得最小值 

确定为这次连接的最大MSS值。 

**IP层：**  


对于IP协议来说，IP包的大小由MTU决定（IP数据包长度就是MTU-28（包头长度）。 MTU值越大，封包就越大，理论上可增加传送速率，但 

MTU值又不能设得太大，因为封包太大，传送时出现错误的机会大增。一般默认的设置，PPPoE连接的最高MTU值是1492, 而以太网 

（Ethernet）的最高MTU值则是1500,而在Internet上，默认的MTU大小是576字节   
  
---

