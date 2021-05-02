# [Installing Ubuntu Software Center on Linux Mint](http://community.linuxmint.com/tutorial/view/682)

**sudo apt-get install software-center**

<http://www.noobslab.com/2011/12/install-ubuntu-software-center-in-linux.html>

 **Install Ubuntu Software Center in Linux Mint 12 Lisa**

Under Linux Mint 12, launch the terminal and install Ubuntu Software Center with this command:


>   * sudo apt-get install software-center
>


 **2.** Run now this command to create the LinuxMint.py file:


>   * sudo cp -r /usr/share/software-center/softwarecenter/distro/Ubuntu.py /usr/share/software-center/softwarecenter/distro/LinuxMint.py
>


 **3.** Edit now this file with this command:


>   * gksudo gedit /usr/share/software-center/softwarecenter/distro/LinuxMint.py
>


 **4.** Find now this line:

> class Ubuntu(Debian)

And replace it with this line:

> class LinuxMint(Debian)

<http://community.linuxmint.com/tutorial/view/682>
