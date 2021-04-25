
date: None  
author(s): None  

# [How to read NETSTAT -AN results - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/networks-related-commands-on-linux/how-to-read-netstat--an-results)

<http://www.dti.ulaval.ca/webdav/site/sit/shared/Librairie/di/operations/informatique/windows/netstat_results.htm>

This document is mainly written for [news.grc.com](news://news.grc.com), for the *ahem* newbies that heard about the Netstat command showing hidden trojans/servers on your system in an obfuscated way. After answering a few of those posts, I noticed I was pretty much the only one actually analyzing those Netstat listings myself, instead of posting a link to a document that explains those listings. So to fall in line with the others, I created this document to refer to myself. :)  
Netstat is a old-school DOS program that displays all TCP connections on your Windows system. The command line parameter -A adds all listening ports (both TCP and UDP) and any other TCP pseudo-connections. The N parameter makes all ports and IP addresses numerical instead of named (like nbname instead of 137, localhost instead of 127.0.0.1). A typical result from NETSTAT -AN looks like this: (this is a slightly edited result of my (online) machine)
    
    
    Active Connections Proto Local Address Foreign Address State TCP 0.0.0.0:44334 0.0.0.0:0 LISTENING TCP 0.0.0.0:27374 0.0.0.0:0 LISTENING TCP 0.0.0.0:1963 0.0.0.0:0 LISTENING TCP 0.0.0.0:1964 0.0.0.0:0 LISTENING TCP 0.0.0.0:1965 0.0.0.0:0 LISTENING TCP 0.0.0.0:1966 0.0.0.0:0 LISTENING TCP 0.0.0.0:1967 0.0.0.0:0 LISTENING TCP 0.0.0.0:1969 0.0.0.0:0 LISTENING TCP 10.0.0.17:135 0.0.0.0:0 LISTENING TCP 10.0.0.17:137 0.0.0.0:0 LISTENING TCP 10.0.0.17:138 0.0.0.0:0 LISTENING TCP 10.0.0.17:139 0.0.0.0:0 LISTENING TCP 10.0.0.17:5000 0.0.0.0:0 LISTENING TCP 10.0.0.17:1963 195.40.6.34:80 ESTABLISHED TCP 10.0.0.17:1964 195.40.6.34:80 ESTABLISHED TCP 10.0.0.17:1965 195.40.6.34:80 ESTABLISHED TCP 10.0.0.17:1966 195.40.6.34:80 ESTABLISHED TCP 10.0.0.17:1967 204.152.184.80:6667 ESTABLISHED TCP 10.0.0.17:1969 207.71.92.194:119 ESTABLISHED UDP 0.0.0.0:44334 *:* UDP 10.0.0.17:137 *:* UDP 10.0.0.17:138 *:*
    

I can imagine that anyone seeing this for the first time must be instantly freaking out over all the 'LISTENING' entries - their machine must be infested with trojans! But if they know a little more about Netstat, they'll calm down again. Now, read and learn:

  * In lines saying 'ESTABLISHED', you need the _remote_ port to identify what has connected to the remote site.
  * In lines saying 'LISTENING', you need the _local_ port to identify what is listening there.
  * Each outbound TCP connection also causes a LISTENING entry on the same port.
  * Most UDP listening ports are duplicates from a listening TCP port. Ignore them unless they don't have a TCP twin.
  * TIME_WAIT entries are not important.
  * If it says 0.0.0.0 on the Local Address column, it means that port is listening on all 'network interfaces' (i.e. your computer, your modem(s) and your network card(s)).
  * If it says 127.0.0.1 on the Local Address column, it means that port is ONLY listening for connections from your PC itself, not from the Internet or network. No danger there.
  * If it displays your online IP on the Local Address column, it means that port is ONLY listening for connections from the Internet.
  * If it displays your local network IP on the Local Address column, it means that port is ONLY listening for connections from the local network.

So, if we look at the above list again, adding explanations for each line:
    
    
    Active Connections Proto Local Address Foreign Address State TCP 0.0.0.0:44334 0.0.0.0:0 LISTENING TCP 0.0.0.0:27374 0.0.0.0:0 LISTENING TCP 0.0.0.0:1963 0.0.0.0:0 LISTENING <- from TCP #1 TCP 0.0.0.0:1964 0.0.0.0:0 LISTENING <- from TCP #2 TCP 0.0.0.0:1965 0.0.0.0:0 LISTENING <- from TCP #3 TCP 0.0.0.0:1966 0.0.0.0:0 LISTENING <- from TCP #4 TCP 0.0.0.0:1967 0.0.0.0:0 LISTENING <- from TCP #5 TCP 0.0.0.0:1969 0.0.0.0:0 LISTENING <- from TCP #6 TCP 10.0.0.17:135 0.0.0.0:0 LISTENING TCP 10.0.0.17:137 0.0.0.0:0 LISTENING TCP 10.0.0.17:138 0.0.0.0:0 LISTENING TCP 10.0.0.17:139 0.0.0.0:0 LISTENING TCP 10.0.0.17:5000 0.0.0.0:0 LISTENING TCP 10.0.0.17:1963 195.40.6.34:80 ESTABLISHED <- TCP #1 TCP 10.0.0.17:1964 195.40.6.34:80 ESTABLISHED <- TCP #2 TCP 10.0.0.17:1965 195.40.6.34:80 ESTABLISHED <- TCP #3 TCP 10.0.0.17:1966 195.40.6.34:80 ESTABLISHED <- TCP #4 TCP 10.0.0.17:1967 204.152.184.80:6667 ESTABLISHED <- TCP #5 TCP 10.0.0.17:1969 207.71.92.194:119 ESTABLISHED <- TCP #6 UDP 0.0.0.0:44334 *:* <- \ UDP 10.0.0.17:137 *:* <- |- who cares? UDP 10.0.0.17:138 *:* <- /
    

Breaking down the TCP connections:

  * #1-#4 - HTTP connections to [bofh.ntk.net](http://bofh.ntk.net/). Most browsers use multiple connections to fetch webpages to speed up the process.
  * #5 - IRC connection. I was connected to SorceryNet with mIRC at the time. Note: If you're not running an IRC client and see a line like this, you might be infected with a IRC bot trojan.
  * #6 - NNTP connection to [news.grc.com](news://news.grc.com).

So what entries are left that are important?
    
    
    Active Connections Proto Local Address Foreign Address State TCP 0.0.0.0:44334 0.0.0.0:0 LISTENING TCP 0.0.0.0:27374 0.0.0.0:0 LISTENING TCP 10.0.0.17:135 0.0.0.0:0 LISTENING TCP 10.0.0.17:137 0.0.0.0:0 LISTENING TCP 10.0.0.17:138 0.0.0.0:0 LISTENING TCP 10.0.0.17:139 0.0.0.0:0 LISTENING TCP 10.0.0.17:5000 0.0.0.0:0 LISTENING
    

That doesn't look so bad, does it now? Time to break down the last listening ports:

  * Port 44334 - my firewall [Tiny Personal Firewall](http://www.tinysoftware.com/pwall.php), listening for connections from the TPF admin program.
  * Port 135 - DCOM/RPCSS, a Microsoft program that's supposed to facilitate usage of programs that use DCOM, blah blah blah. If you have Windows 9x/ME, this can be disabled. See below.
  * Port 137/138/139 - NetBIOS, used for File & Printer Sharing. If you are on a non-networked PC, you can disable this too. See below.
  * Port 5000 - Universal Plug & Play, comes standard with Windows ME. Can definitely be disabled. See below.
  * Port 27374 - The only one left not part of a default Windows install. To find out what ports like these are, you need documentation. After a quick search through Robert Grahams [Firewall Forensics: What am I seeing?](http://www.robertgraham.com/pubs/firewall-seen.html) leads to the conclusion that this is the Sub7 trojan horse. Use a virusscanner to remove it.

  
  
 **Closing ports**  
I'll try to keep this list as complete as possible, but if you happen to find an open port on your system you can't explain or have an addition to this list, email me at the address at the bottom of this article. (If you're including a line from a Netstat listing, include the _entire_ listing please!)

  * TCP port 135 \- Microsoft DCOM/RPCSS. Impossible to close in Windows NT/2000/XP Pro. Windows 9x/ME/XP Home: Start REGEDIT.EXE, go to HKLM\Software\Microsoft\OLE and change both EnableDCOM and EnableRemoteConnect to 'N'. Reboot. Optional: delete C:\WINDOWS\SYSTEM\RPCSS.EXE.
  * TCP ports 137,138,139 and UDP ports 137,138 \- Microsoft File & Printer Sharing. Go to Control Panel, Network, click the 'File & Printer Sharing' button and deselect both options. Click OK, OK and reboot.
  * TCP port 445 \- Microsoft Windows NT File & Printer Sharing. Go to Control Panel, Dial-Up & Network Connctions, click Advanced, Bindings and unbind File & Printer Sharing from the TCP/IP protocol.
  * TCP port 5000 \- Microsoft Universal Plug & Play (Windows ME only). Go to Control Panel, Add/Remove Software, select 'Universal Plug & Play' and hit Remove, OK.

Hope this all clears up some things for you :)

> Klont, [klont@windhoos2000.nl](mailto:klont@windhoos2000.nl?subject=Netstat%20-an%20results)  
  
---

