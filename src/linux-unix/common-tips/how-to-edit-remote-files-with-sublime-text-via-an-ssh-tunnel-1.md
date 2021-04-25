
date: None  
author(s): None  

# [How to Edit Remote Files With Sublime Text via an SSH Tunnel - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-edit-remote-files-with-sublime-text-via-an-ssh-tunnel-1)

http://log.liminastudio.com/writing/tutorials/sublime-tunnel-of-love-how-to-edit-remote-files-with-sublime-text-via-an-ssh-tunnel

Eventually you will need to edit a file in-place on a server, for one reason or another (i.e. working on a Javascript front-end that requires templating from a backend); this is partly what Emacs and Vim are for (and they’re both very good at what they do).

There’s nothing wrong with learning either of those tools, but if you really don’t want to, there are options. If the server is running FTP, you can use something like Transmit to open the file in a local editor and saves will be automatically uploaded to the server. Unfortunately, FTP is a very old and VERY insecure protocol that should not be used anymore. What else can we do?

Using Secure Shell (SSH) Tunneling, we can establish an SSH session that routes arbitrary traffic through it to a specified port for any use we want. Thanks to a [nifty set of scripts called rsub](https://github.com/Drarok/rsub), modified originally from [TextMate’s rmate](http://erniemiller.org/2011/12/12/textmate-2-rmate-awesome/), we can run a little utility server on our local machine that interacts with your remote server for you and lets you open up remote files and save them back, all through an encrypted channel.

### What Do I Do?

  1. As of writing, these instructions work only for Sublime Text 2. If I get a chance I’ll look into forking rsub for the newly released ST3 (which runs Python3).
  2. If you don’t already have Sublime Text’s wonderful package manager, [install it](http://wbond.net/sublime_packages/package_control/installation).
  3. Hit Ctrl+Shift+P, start typing “install” and select “Install Package”
  4. Start typing “rsub” and select it.
  5. Once it’s installed, get on your terminal and do
    
        nano ~/.ssh/config

  6. Paste the following lines:
    
        Host your_remote_server.com
        RemoteForward 52698 127.0.0.1:52698

  7. Save (ctrl+w) and SSH into your server (ssh username@your_remote_server.com).
  8. ‘Install’ the rsub remote script:
    
        sudo wget -O /usr/local/bin/rsub https://raw.github.com/aurora/rmate/master/rmate

  9. Make that script executable:
    
        sudo chmod +x /usr/local/bin/rsub

  10. Lastly, run rsub on the remote file you want to edit locally:
    
        rsub ~/my_project/my_file.html

and it should magically open in Sublime Text!




Let me know if this works for you! Enjoy!  
  
---

