
date: None  
author(s): None  

# [SSHFS in Windows - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/sshfs-in-windows)

This post will cover the required steps to configure a working SSHFS client set-up in Windows. With SSHFS you can mount a remote directory via SSH as if it were a local drive, while SSHFS is common on Linux/Nix* Windows is a different story. To make use of SSHFS in Windows you will need to download [win sshfs](http://code.google.com/p/win-sshfs/) a free SSHFS application.

You will need to download the following files to have a working SSHFS setup:

## Let’s Start

Note:I’ve only used password for authentication, I have not tried key files yet…

You will need to download win sshfs from the following link [code.google.com/p/win-sshfs/](http://code.google.com/p/win-sshfs/) , once the download completes install the application.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_1.png)

Click on **Next** to continue.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_2.png)

 **Accept** the license agreement and click on **Next**.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_3.png)

Hopefully you already installed the pre-requisites I mentioned above, otherwise the application will refuse to install. Otherwise, go back an install them. Click on **Next** to continue.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_4.png)

Accept the default path and click on **Next**.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_5.png)

Click on **Finish** to launch the application.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_6.png)

Now in SSHFS Manager click on **Add** , we need to add a new connection.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_7.png)

This is where we connect to the SSH server, in my case the server runs Ubuntu 12.04. Enter a name, server IP address, user credentials and for the rest go with the defaults if you like.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_8.png)

First click on **Save** and then click on **Mount**.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_9.png)

If you provided the correct server information your SSHFS connection should now be mounted.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_10.png)

You can verify this by going to **My Computer** , the new SSHFS drive will be mounted as a removable drive.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_11.png)

By default the application will start at start-up, you can change this behavior by going to Taskbar, right clicking on the application icon and un-checking **Run at startup**.

![Windows SSHFS](http://linhost.info/content/2012-09/windows_sshfs_12.png)

Win SSHFS so far as worked quite well for me, I like the idea of having access to SSHFS from my Windows 7 computer. If you find any mistakes of have suggestions don’t to leave a comment.

## Links

Dokan library 0.6.0 [dokan-dev.net/en/download/](http://dokan-dev.net/en/download/)

win sshfs [code.google.com/p/win-sshfs/](http://code.google.com/p/win-sshfs/downloads/list/)

.NET Framework 4.0 [microsoft.com/en-us/download/](http://www.microsoft.com/en-us/download/details.aspx?id=17851)

