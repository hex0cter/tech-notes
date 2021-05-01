# [Debian 9/10快速开启Google BBR的方法，实现高效单边加速 ](https://www.4spaces.org/speed-up-your-vps-with-bbr-plus/)


<https://www.fomcom.com/7.html>
<https://www.4spaces.org/speed-up-your-vps-with-bbr-plus/>

使用Google BBR拥塞算法加速TCP教程，由于 Debian 9默认的就是4.9的内核而且编译了TCP BBR的内容，所以可以直接通过参数开启。

提示：目前最新版Debian 10内核为4.19，也可以直接用该方法开启BBR。

## 方法
1、修改系统变量
```
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
```
2、保存生效
```
sysctl -p
```
3、查看内核是否已开启BBR
```
sysctl net.ipv4.tcp_available_congestion_control
```
显示以下即已开启：
```
sysctl net.ipv4.tcp_available_congestion_control net.ipv4.tcp_available_congestion_control = bbr cubic reno
```
4、查看BBR是否启动
```
lsmod | grep bbr
```
显示以下即启动成功：
```
lsmod | grep bbr tcp_bbr 20480 14
```
