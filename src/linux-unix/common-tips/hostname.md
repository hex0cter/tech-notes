# [Linux: find out information about current domain name and host name](http://www.cyberciti.biz/faq/linux-find-domain-hostname/)

Q. Under Windows Server 2003 I can use active directory domain tools to get information about current domain and hostname. Can you tell me command to list current domain name and hostname under Red hat enterprise Linux 5?

A. Both Linux / UNIX comes with the following utilities to display hostname / domain name:

a) **hostname** \- show or set the system’s host name

b) **domainname** \- show or set the system’s NIS/YP domain name

c) **dnsdomainname** \- show the system’s DNS domain name

d) **nisdomainname** \- show or set system’s NIS/YP domain name

e) **ypdomainname** \- show or set the system’s NIS/YP domain name

For example, hostname is the program that is used to either set or display the current host, domain or node name of the system. These names are used by many of the networking programs to identify the machine.
```
$ hostname
```
Output
```
sun521nixcraft.com
```
The domain name is also used by NIS/YP or Internet DNS:
```
$ dnsdomainname
```
Output:
```
nixcraft.comFrom:
```
