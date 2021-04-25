
date: None  
author(s): None  

# [How to disable SSH timeout - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-disable-ssh-timeout)

<http://docs.oseems.com/general/application/ssh/disable-timeout>

By default, most SSH servers are set to disconnect clients who has been inactive or idle after a certain period of time. You'll be prompted with message similar to the following upon disconnection;
    
    
    Read from remote host oseems.com: Connection reset by peer
    Connection to oseems.com closed.

To avoid being disconnected, you have the choice to either configure your SSH client, or the server itself if you have the required permission.

This method is the way to go if you have no administrator access to the server you are connecting to. This method will apply to all the servers you are connecting to, instead of only to a specific server.

What you're basically to do is to configure your SSH client client to periodically send keep alive message to the SSH server. If you're running Ubuntu / Debian, edit `/etc/ssh/ssh_config` and set`ServerAliveInterval` option to the following;
    
    
    ServerAliveInterval 100

This option is to tell your SSH client to automatically send the keep alive message every 100 seconds to the SSH server, even if you're away from your client machine. The server will assume you're not idling and will not disconnect your session.

If you have administrator access to the server, you can configure the`ClientAliveInterval`, `TCPKeepAlive` and `ClientAliveCountMax` options in the SSHd configuration file. If you're running Ubuntu / Debian, the file's path is `/etc/ssh/sshd_config`
    
    
    ClientAliveInterval 30
    TCPKeepAlive yes 
    ClientAliveCountMax 99999

You will need to restart the SSH server for the changes to take effect.
    
    
    sudo /etc/init.d/sshd restart  
  
---

