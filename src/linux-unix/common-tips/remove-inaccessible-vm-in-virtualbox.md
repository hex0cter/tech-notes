
date: None  
author(s): None  

# [Remove Inaccessible VM in VirtualBox - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/remove-inaccessible-vm-in-virtualbox)

http://levlaz.blogspot.se/2013/11/remove-inaccessible-vm-in-virtualbox-on.html

I recently deleted some Virtual Machines from an external hard drive in VirtualBox and when launching Virtualbox for the first time these old VM's are listed as "Inaccessible".  


Right clicking on the machine and removing it does nothing. Now, these machines do not hurt anyone by being there, but if you have OCD like I do about a clean desktop/clean UI then you will want to get rid of these. 

In order to get rid of these VM's we will have to use the Terminal.App and a couple of handy command line tools. 

1) Open Terminal.App 

2) Enter the following command 

> vboxmanage list vms 

The output will be a list of your currently installed VMS and should look something like this. 

> "<inaccessible>" {1e94b410-5df6-4f97-a4b5-9eda522347d9}"<inaccessible>" {b33743c8-8216-4bf7-83e9-99710c87ae68}"Debian XFCE Stable " {841a1a03-f6c3-4faa-9bf9-826085826e8b}

The ones that are listed as "<inaccessible>" are the ones that we want to remove, so copy the long numbers inside the {brackets}

3) In order to remove the VM's, run the following command for each machine that you want to remove.

> vboxmanage unregistervm 1e94b410-5df6-4f97-a4b5-9eda522347d9

  
4) You are done, Virtualbox will instantly remove the inaccessible machine form your list of VMs. You are now free to enjoy a clean VirtualBox dashboard!  
  
---

