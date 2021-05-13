# [netstat 使用详解](http://javasky.bloghome.cn/posts/1295.html)

　　显示活动的 TCP 连接、计算机侦听的端口、以太网统计信息、IP 路由表、IPv4 统计信息（对于 IP、ICMP、TCP 和 UDP 协议）以及 IPv6 统计信息（对于 IPv6、ICMPv6、通过 IPv6 的 TCP 以及通过 IPv6 的 UDP 协议）。使用时如果不带参数，netstat 显示活动的 TCP 连接。　

　　语法

　　netstat [-a] [-e] [-n] [-o] [-p Protocol] [-r] [-s] [Interval] 　　

　　参数

　　-a

　　显示所有活动的 TCP 连接以及计算机侦听的 TCP 和 UDP 端口。

　　-e

　　显示以太网统计信息，如发送和接收的字节数、数据包数。该参数可以与 -s 结合使用。

　　-n

　　显示活动的 TCP 连接，不过，只以数字形式表现地址和端口号，却不尝试确定名称。

　　-o

　　显示活动的 TCP 连接并包括每个连接的进程 ID (PID)。可以在 Windows 任务管理器中的“进程”选项卡上找到基于 PID 的应用程序。该参数可以与 -a、-n 和 -p 结合使用。

　　-p Protocol

　　显示 Protocol 所指定的协议的连接。在这种情况下，Protocol 可以是 tcp、udp、tcpv6 或 udpv6。如果该参数与 -s 一起使用按协议显示统计信息，则 Protocol 可以是 tcp、udp、icmp、ip、tcpv6、udpv6、icmpv6 或 ipv6。

　　-s

　　按协议显示统计信息。默认情况下，显示 TCP、UDP、ICMP 和 IP 协议的统计信息。如果安装了 Windows XP 的 IPv6 协议，就会显示有关 IPv6 上的 TCP、IPv6 上的 UDP、ICMPv6 和 IPv6 协议的统计信息。可以使用 -p 参数指定协议集。

　　-r

　　显示 IP 路由表的内容。该参数与 route print 命令等价。

　　Interval

　　每隔 Interval 秒重新显示一次选定的信息。按 CTRL+C 停止重新显示统计信息。如果省略该参数，netstat 将只打印一次选定的信息。

　　/?

　　在命令提示符显示帮助。

　　注释

　　与该命令一起使用的参数必须以连字符 (-) 而不是以短斜线 (/) 作为前缀。

　　Netstat 提供下列统计信息：

　　Proto

　　协议的名称（TCP 或 UDP）。 　　

　　Local Address

　　本地计算机的 IP 地址和正在使用的端口号。如果不指定 -n 参数，就显示与 IP 地址和端口的名称对应的本地计算机名称。如果端口尚未建立，端口以星号（*）显示。 　　

　　Foreign Address

　　连接该插槽的远程计算机的 IP 地址和端口号码。如果不指定 -n 参数，就显示与 IP 地址和端口对应的名称。如果端口尚未建立，端口以星号（*）显示。 　　

　　(state)

　　表明 TCP 连接的状态。可能的状态如下： 　　
```
　　CLOSE_WAIT
　　CLOSED
　　ESTABLISHED 　
　　FIN_WAIT_1
　　FIN_WAIT_2
　　LAST_ACK
　　LISTEN
　　SYN_RECEIVED
　　SYN_SEND
　　TIMED_WAIT 　
```
　　有关 TCP 连接状态的信息，请参阅 RFC 793。 　　

　　只有当网际协议 (TCP/IP) 协议在 网络连接中安装为网络适配器属性的组件时，该命令才可用。

　　范例

　　要想显示以太网统计信息和所有协议的统计信息，请键入下列命令： 　

　　netstat -e -s 　　

　　要想仅显示 TCP 和 UDP 协议的统计信息，请键入下列命令： 　

　　netstat -s -p tcp udp 　

　　要想每 5 秒钟显示一次活动的 TCP 连接和进程 ID，请键入下列命令： 　

　　netstat -o 5 　

　　要想以数字形式显示活动的 TCP 连接和进程 ID，请键入下列命令： 　

　　netstat -n Co 　
