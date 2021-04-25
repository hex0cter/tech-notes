
date: None  
author(s): None  

# [距离矢量路由协议（distance vector） VS 链路状态路由协议（link-state） - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/network/network-routing)

**一、PK第一番**

距离矢量:

运行距离矢量路由协议的路由器,会将所有它知道的路由信息与邻居共享,但是只与直连邻居共享！

链路状态:

运行链路状态路由协议的路由器,只将它所直连的链路状态与邻居共享,这个邻居是指一个域内(domain),或一个区域内(area)的所有路由器！

**二、PK第二番**

所有距离矢量路由协议均使用Bellman-Ford(Ford-Fulkerson)算法，容易产生路由环路（loop）和计数到无穷大（counting to infinity）的问题。因此它们必须结合一些防环机制：

split-horizon

route poisoning

poison reverse

hold-down timer

trigger updates

同时由于每台路由器都必须在将从邻居学到的路由转发给其它路由器之前，运行路由算法，所以网络的规模越大，其收敛速度越慢。

链路状态路由协议均使用了强健的SPF算法，如OSPF的dijkstra，不易产生路由环路，或是一些错误的路由信息。路由器在转发链路状态包时（描述链路状态、拓扑变化的包），没必要首先进行路由运算，再给邻居进行发送，从而加快了网络的收敛速度。

**三、PK第三番**

距离矢量路由协议，更新的是“路由条目”！一条重要的链路如果发生变化，意味着需通告多条涉及到的路由条目！

链路状态路由协议，更新的是“拓扑”！每台路由器上都有完全相同的拓扑，他们各自分别进行SPF算法，计算出路由条目！一条重要链路的变化，不必再发送所有被波及的路由条目，只需发送一条链路通告，告知其它路由器本链路发生故障即可。其它路由器会根据链路状态，改变自已的拓扑数据库，重新计算路由条目。

**四、PK第四番**

距离矢量路由协议发送周期性更新、完整路由表更新（periodic & full）

而链路状态路由协议更新是非周期性的（nonperiodic），部分的（partial）

<http://sxzx.360doc.com/content/081231/18/36491_2235770.html>  
  
---
