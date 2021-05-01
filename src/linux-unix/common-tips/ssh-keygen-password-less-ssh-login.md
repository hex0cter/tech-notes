# [ssh-keygen: password-less SSH login](http://rcsg-gsir.imsb-dsgi.nrc-cnrc.gc.ca/documents/internet/node31.html)

`ssh-keygen` is used to generate that key pair for you. Here is a session where your own personal private/public key pair is created:


    cantin@sodium:~> ssh-keygen -t rsa
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/cantin/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/cantin/.ssh/id_rsa.
    Your public key has been saved in /home/cantin/.ssh/id_rsa.pub.
    The key fingerprint is:
    f6:61:a8:27:35:cf:4c:6d:13:22:70:cf:4c:c8:a0:23 cantin@sodium


    In this case, the content of file id_rsa.pub is


    ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEArkwv9X8eTVK4F7pMlSt45pWoiakFkZMw
    G9BjydOJPGH0RFNAy1QqIWBGWv7vS5K2tr+EEO+F8WL2Y/jK4ZkUoQgoi+n7DWQVOHsR
    ijcS3LvtO+50Np4yjXYWJKh29JL6GHcp8o7+YKEyVUMB2CSDOP99eF9g5Q0d+1U2WVdB
    WQM= cantin@sodium


It is one line in length.

Its content is then copied in file `.ssh/authorized_keys` of the system you wish to SSH to without being prompted for a password.
