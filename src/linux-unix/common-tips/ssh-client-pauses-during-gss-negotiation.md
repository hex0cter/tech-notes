# [ssh client pauses during GSS negotiation](https://bugs.launchpad.net/ubuntu/+source/openssh/+bug/416264)



1) Specify the option to disable GSSAPI authentication when using SSH or SCP command, e.g.:
ssh -o GSSAPIAuthentication=no appssupp@10.50.100.111

-OR-

2) Explicitly disable GSSAPI authentication in SSH client program configuration file, i.e. edit the /etc/ssh/ssh_config and add in this configuration (if it’s not already in the config file):
GSSAPIAuthentication no

-OR-

3) Like 2 but in your private ssh configEdit /home/YOURUSERNAME/.ssh/config and add

GSSAPIAuthentication no

---
