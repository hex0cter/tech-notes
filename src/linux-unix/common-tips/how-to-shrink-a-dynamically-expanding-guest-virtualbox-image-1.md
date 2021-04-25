
date: None  
author(s): None  

# [How to shrink a dynamically-expanding guest virtualbox image - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-shrink-a-dynamically-expanding-guest-virtualbox-image-1)

Sometimes bigger isn’t always better. If your dynamically-expanding virtual machine images are growing out of control, then here’s how to trim them back…

#### Background

I’m a big fan of VirtualBox, and use separate virtual machines (VMs) for the various separate bits and pieces I’ve got on the go (as I invariably end up messing something up, and can just trash the image and start again, without taking down whatever else it is I’m playing with at the time).

All my VMs use a [dynamically expanding image](http://www.virtualbox.org/manual/ch05.html#vdidetails) for their hard drive, where you set the maximum size of the disk, but the system will only grow to fill that space if required. By setting this nice and high, I can be sure that the hard drive space is there if I need it, without taking space away unnecessarily from the rest of the system.

Unfortunately, whilst VirtualBox will dynamically expand the hard drive as it’s required, it won’t dynamically shrink it again if you free up space in the VM. This can be a problem, especially if, like me, the sum total of all those theoretical maximums exceeds the actual maximum capacity of the hard drive hosting all these VMs.

The good news is that you can shrink those images back down again. The bad news is that a lot of the guides on the internet are out-of-date, and woefully misleading. Here’s what I did to get the job done…

#### 1\. Free up space in the client machine

It’s a bit of an obvious first step, but you can only shrink down the client VM by the size of the available free space therein, so delete the files and uninstall the programs that you no longer need but are hogging your resources.

#### 2\. Zero out the free space

VirtualBox only knows that the space is really free if it’s been set to zero, and standard deletion won’t do this.

##### If it’s an Ubuntu VM

You’ll want to use [zerofree](http://manpages.ubuntu.com/manpages/natty/man8/zerofree.8.html):

  * install with _sudo aptitude install zerofree_
  * (if you don’t have aptitude, you can either use apt-get to install zerofree ( _sudo apt-get install zerofree_ ) or use apt-get to install aptitude ( _sudo apt-get install aptitude_ ). I’d recommend getting hold of aptitude, as it does a great job of managing packages in Ubuntu)
  * Reboot the machine ( _sudo shutdown -r now_ ). During boot, hold down the left shift key. A menu will appear, you need to select “recovery mode”; this should be the second item in the list.
  * You’ll get another menu, towards the bottom there should be the option to “Drop to root shell prompt”
  * Run _df_ and look for the mount point that’s that the biggest – this is where all your files are, and is the one we’ll need to run zerofree against. For the rest of this guide, we’ll assume it’s /dev/sda1
  * The following three commands (thanks, [VirtualBox forum](http://forum.virtualbox.org/viewtopic.php?f=6&p=148554)!) stop background services that we can’t have running:
    *  _service network-manager stop_
    *  _killall dhclient_
    *  _
      *  _

`Daniel's notes: For me I just booted into the recovery mode of Ubuntu by pressing and holding the left shift key during start up. Then I chose Drop to root shell prompt.`

_
_
  * Once they’ve stopped, you can re-mount the partition as readonly (zerofree needs this)
    *  _mount -n -o remount,ro -t ext3 /dev/sda1 /_
  * You can now run zerofree
  * Finally, shut down the VM



##### If it’s a Windows VM

You’ll need to run _sdelete_ ; I’ve never done this, but there are instructions on that [here](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/compacting-virtualbox-disk-images---windows-guests):

`Daniel's note: Run **_VBoxManage.exe list hdds_** to list all disks.`

` Instructions for Windows are here: `https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/compacting-virtualbox-disk-images---windows-guests

3\. Shrink the VM

Quite a lot of the online guides say that you’ll have to clone the hard drive image to shrink it, as VirtualBox 2.2 and above dropped support for compacting the image. This isn’t true, certainly not for version 4.0.4, and you can shrink the image in-place with the following command:

  *  _VBoxManage modifyhd my.vdi –compact_



With any luck, you’ll now have plenty of disk space to fill will equally useless tat…

