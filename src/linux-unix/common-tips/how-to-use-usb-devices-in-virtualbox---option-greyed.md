# [How to use USB devices in VirtualBox - option greyed](http://www.dedoimedo.com/computers/virtualbox-usb.html)

This is is a question often asked. Not only that, I have received a formal request from one of my readers to write a tutorial on this topic. Studying the internals of the problem into some depth, I really did discover that most people are having a hard time playing with USB devices in [VirtualBox](http://www.virtualbox.org/). Therefore, I decided to make the world a better place and write this howto.

![Teaser](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-found.jpg)

Using USB devices of any kind, like thumb drives, Web camera and others, in your virtual machine can improve the quality of your virtual experience. It makes the virtual machine more usable. You can enjoy the virtual machine as more than just a test bed or a dire necessity because one of your programs may not work in the host operating system. It can become a second reality, where you use your system resources to the max, including all kinds of cool peripherals.

Convinced? Surely. Now, let's examine the functionality, up close.

We will examine the problem in Linux. In Windows, the issue is far more trivial, but still, you might want to read anyway. The choice of the guest operating system is not important, the only difference in the setup concerns the host operating system.

Important note: You will need VirtualBox PUEL edition. The OSE edition does not offer USB support. Make sure you download the right version, otherwise you may hit an insurmountable obstacle.

### Step 1: Install virtual machine

You know all about this. I've written tons of tutorials on how to do this, including some fairly elaborate multi-boot setup. Windows, Linux, take [your](http://www.dedoimedo.com/computer_software.html) pick.

### Step 2: Configure USB support in virtual machine settings

Click on Settings for your virtual machine, go to USB tab. Check the two boxes, since you do want USB 2.0 support. In theory, this is all, but there's one step we will need to do afterwards to get this really working. True for Windows, Linux needs a bit more sweat. We will address that soon.

![Settings](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-settings.jpg)

USB filter

USB filter is a nice feature that allows you to automatically connect USB devices to your virtual machine. Any device listed in the filter box will be plugged in when you power the guest operating system. Other devices will require that you manually connect them.

![Filter](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-filter.jpg)

![Zoomed](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-filter-zoomed.jpg)

### Step 3: Install Virtual Guest Additions

This is required to have the USB support enabled. Much like [VMware Tools](http://www.dedoimedo.com/computers/vmware-tools.html) for VMware products, the Guest Additions expose additional functionality in the virtual machine, boost performance, enhance sharing, and more. We've had a long [tutorial](http://www.dedoimedo.com/computers/virtualbox-guest-addons.html), which explains how to achieve this in both Windows and Linux virtual machines.

![Install](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-install.jpg)

![Addons installed](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-addons-installed.jpg)

### Step 4: Test and fail

We will try to connect a 16GB Kingston DataTraveler G2 USB thumb drive, which has a single JPG image on it, just for fun. Testbed: Ubuntu [Lucid](http://www.dedoimedo.com/computers/ubuntu-lucid.html) with VirtualBox 3.2, running a Windows XP virtual machine.

![Example](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-example.jpg)

Boot your virtual machine. Now try to connect a USB device. Go to Devices > USB Devices and choose the one you need. Oops, the options will all be grayed out.

![Grayed out](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-mount-device-grayed.jpg)

So what do you do?

### Step 5: Fix the group permissions

Yes, this geeky step is part of the setup. You will need to add your user to the VirtualBox group to be able to share USB resources. You can do this from the command line or try the GUI menus.

All right, so we're running Ubuntu with Gnome desktop. Therefore, go to System > Administration > Users and Groups. In the menu that opens, click on Manage Groups. Scroll and look for the vboxusers group.

![Manage groups](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-manage-groups.png)

Click on the Properties button. Make sure your user is listed and checked in the Group Members field.

![Properties](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-properties.png)

You will need to logout and login back into the session for the effects to take change. Now, power on the virtual machine once more and see what happens.

### Step 6: Test again and succeed

This time, it will work properly. If you've used filters, the device will be automounted. You will have the USB device ready for use in your virtual machine. It can be a storage device or some other cool gadget. You may even use iPhone, iPod or similar, in case the host operating system does not support the device sync or whatnot.

![Found device](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-found.jpg)

![Attached](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-attached.jpg)

![Zoomed](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-attached-zoomed.jpg)

![Working](http://www.dedoimedo.com/images/computers_years/2010_2/vbox-usb-working.jpg)

In the past, you would have to change all kinds of other permissions manually, so there's hope and progress after all, but an automation of this step would make it so much easier for the average user. But we're done, everything works!
