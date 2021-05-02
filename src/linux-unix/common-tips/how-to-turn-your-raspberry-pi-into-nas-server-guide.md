# [How To Turn Your Raspberry Pi into NAS Server [Guide]](https://www.ubuntupit.com/how-to-turn-your-raspberry-pi-into-nas-server-guide/)

In this modern age of science and technology, data is like the heart and soul of a system. How many times have you bought external hard drives for extra storage till now? Plenty, I guess. But wouldn’t it be awesome to have your personal [storage in the cloud](https://www.ubuntupit.com/best-cloud-computing-companies-and-platforms/) with unlimited space just to save your information and data? It’s possible! All you need is a raspberry pi with an external or USB hard drive, and your personal NAS system will be ready in no time! With a Raspberry Pi NAS Server, you can easily store anything from movies to games in virtual storage and access it from any device and anywhere in the world. Also, a NAS server will ensure that your data is totally safe, and no one else can access them except you. So, follow this article step by step to turn your Raspberry Pi into a NAS Server.

## **What’s a NAS?**

A NAS is a network-connected storage device that you can use to store or retrieve data from a central server while being at home with any device. You can now store anything, including movies and games, in your NAS network and run on them on multiple devices. The best thing about a NAS is that it will give you a nonstop 24/7 service. It’s like getting a private office on the cloud with fast service and unlimited storage.

![NAS Server](https://www.ubuntupit.com/wp-content/uploads/2020/10/NAS-Server.jpg)

Companies like [Synology ](https://www.synology.com/en-uk)and [Asustor](https://www.asustor.com/en/) have been selling out many ready-built NAS devices for a long time. You just have to buy one and connect it with a hard drive. But you can guess how expensive they can be! So, imagine how amazing it would be to make the server yourself at home!

## **Turning Raspberry Pi into NAS Server**

If you are a [Raspberry Pi enthusiast](https://www.ubuntupit.com/20-best-raspberry-pi-projects-that-you-can-start-right-now/) looking forward to getting a NAS for yourself, nothing can be cheapest than turning your spare Raspberry into a NAS server. However, make sure to take a backup of your data beforehand as Raspberry Pi isn’t very ideal in data redundancy. So, if you have an unused Pi laying off in your storage, upgrading it to a self-made Synology NAS model for long-term use is a great idea.

### **Things You Will Need**

There are certain things you will need to turn your raspberry into a NAS server. You should try to get all of them before starting the project.

![Raspberry Pi Kit](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-Kit.jpg)

**1\. Raspberry Pi: ** Since you turn a raspberry pi into a NAS server, a Raspberry Pi is the first thing you will need for this project. You should try to get the most updated version of the Pi. Make sure to get the accessories with it, including a MicroSD card, a mouse, a power supply, and a keyboard.

**2\. Storage:** MicroSD card isn’t the best choice if you want to store data files like movies, songs, games, or any kind of large files. So, please keep something as additional storage. A powered USB hub and also an external hard drive can be ideal for this situation. In case you want something cleaner, you can find some internal drives that are designed especially for network-attached storage.

**3\. SSH Connection: ** You will have to install the Raspberry Pi by connecting it through an SSH. So, please find an SSH client beforehand.

**4\. Network Access: ** If you want your NAS to work at its best, you will have to connect it to the home network with an Ethernet cable. While you can use wireless connections, they are not fast enough. So, you better make all the arrangements for wired network access.

### **Step 1: Installing the Raspberry Pi OS**

After you have gathered all the necessary equipment, it’s time to download and install the [Raspberry Pi OS](https://www.ubuntupit.com/best-raspberry-pi-os-available/). While downloading, make sure to get the Lite version as the regular ones will take unnecessary space minimizing the efficiency.

  * At first, download the Raspberry Pi imager for your OS.
  * Open on the installer and complete the whole setup.
  * Plug a microSD card into the computer.![Raspberry Pi into NAS server - Imager](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-into-NAS-server-Imager.jpg)
  * Run the Raspberry Pi Imager.
  * Choose Raspbian as your operating system.



![Raspbian](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspbian.jpg)

  * Select an SD card on which you want to write the OS.



![raspberry pi imager SD card](https://www.ubuntupit.com/wp-content/uploads/2020/10/raspberry-pi-imager-SD-card.jpg)

  * Ensure the final configuration.
  * Select “write” on the screen and wait until the process finishes.



After you have successfully installed your Pi OS on the SD card, you are free to take it out from your device and plug in your Raspberry Pi for boot up. If everything’s fine, it will take you directly to a fully-functional desktop.

Once you are done with this one, take out the microSD card and reinsert it. Then go to Windows Explorer and direct to the SD card. Use the file view of the microSD card and right-click on any of the blank areas. Then, choose “New -> Text Document.”

![Raspberry Pi into NAS server - text document](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-into-NAS-server-text-document.jpg)

The new document should be shown with the file extension. If it doesn’t show the extension, you will have to change the menu options manually. You can rename the file to “SSH” once everything’s fine.

![SSH](https://www.ubuntupit.com/wp-content/uploads/2020/10/SSH.jpg)

Now, plug your microSD card back into the Raspberry Pi and connect your Pi to the network using an ethernet cable to transfer your files fast. After opening the Raspbian, you will be asked to set a new password for it. Then, download the updates and attach the hard drive to one of the USB ports of the raspberry pi.

### **Step 2: Getting the IP Address**

In this step, you will have to find your Pi’s IP address to connect the SSH with it. You can get that in a couple of ways. But the easiest one is to logging in to your router to access the client list. Your device should be listed as “raspberrypi”. Now, note the IP address.

![Raspberry Pi into NAS server - IP Address](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-into-NAS-server-IP-Address.jpg)

You can also get it from the “DHCP Server” from the assigned router menu. In this case, you will have to use the “Address Reservation” to give a static IP address permanently to your NAS.

If any of the above techniques don’t work, you can try connecting a monitor with a keyboard to your Pi and write a command-line:` ip add `. Now, take the IP Address shown right next to your ethernet interface.

### **Step 3: Securing the NAS Server**

The main point of getting the IP address was to add SSH or HTTPS protocol to your NAS server. Here are some steps you need to follow to do that:

  * Go to the window’s PuTTY and write your IP address on the “Host Name” field.



![putty host name](https://www.ubuntupit.com/wp-content/uploads/2020/10/putty_host_name.jpg)

  * You will get a security warning. Select “Yes” to continue
  * Now, log in to the terminal as “Pi” with “Raspberry” as the password.
  * You will have to give a new password to prevent unauthorized users from getting in using the common default password. Use the following code for that:




    Passwd

![Raspberry Pi into NAS server - password](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-into-NAS-server-password.jpg)

Make sure to assign a strong password.

### **Step 4: Download and Install OpenMediaVault5**

Before you start downloading the [OpenMediaVault5](https://www.openmediavault.org/), make sure you have updated your OS to the latest version. If not, you can use the following command:


    sudo apt update && sudo apt -y upgrade
    sudo rm -f /etc/systemd/network/99-default.link

![Raspberry Pi Update](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-Update.jpg)

After that, restart your Pi:


    sudo reboot

You might need to add SSH once again after rebooting the Raspberry Pi. Follow the previous step to do that.

To download OMV5, you will need an external computer. After you have downloaded the file, use the following command to install it:


    wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash

![Installing OpenMediaVault5](https://www.ubuntupit.com/wp-content/uploads/2020/10/Installing-OpenMediaVault5.jpg)

The installation might take 20-30 minutes to complete. At that time, leave the computer and avoid any kind of interruptions. If you are successful with the installation, the Pi will restart automatically.

### **Step 5: Logging onto the Web Interface**

After you are done with the base of your [NAS Server](https://www.ubuntupit.com/best-linux-nas-solutions-and-linux-san-software/), you should now log in to the web frontend where the real configuration happens. To do that, go to your computer’s browser and open the IP Address in the URL bar. You will get a default login information for your NAS distribution.


    Username: admin
    Password: openmediavault

Once the login is successful, OMV5’s start menu will open with a summary of the services available along with their information. Make your way to the “General Settings” from there, the part under the settings menu. You will get the “Web Administration” tab there. Change the “auto logout” settings to one day from 5 minutes to avoid the timeout. Select the save button and wait for a confirmation. Click “yes” on all the pop-ups.

### **Step 6: Change Password and Basic Setups**

You can change the default password to a more secure and stronger one using the “Web Administrator Password” tab. Do remember to click the save button after you are done. Now, it’s time to do some basic setup before we get to the next step.

![Raspberry Pi into NAS server - openmediavault password change](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-into-NAS-server-openmediavault-password-change.jpg)

Change the date and time of the device according to your suitable time zone from the “Date & Time” sub-menu. If you want it to update the accurate time automatically, allow the “Use NTP Server” option that will enable you to use the Network Time Protocol.

![openmediavault5 time zone settings](https://www.ubuntupit.com/wp-content/uploads/2020/10/openmediavault5-time-zone-settings.jpg)

You should remember to hit the save button every time you make a change in the settings. Also, don’t leave the tab unless you get a confirmation pop up. After you are done with the basic settings, go to the “Update Management” sub-menu and select the “check” button to see any available updates.

![Openmediavault installing updates](https://www.ubuntupit.com/wp-content/uploads/2020/10/Openmediavault-installing-updates.jpg)

Check all the boxes and select the “Install” button to start all the pending updates. Make sure the process doesn’t get interrupted by anything. You can close the installation pop-up once everything’s updated.

## **Step 7: Connecting and Preparing Storage for NAS Server**


In this step, you will have to connect the storage media to the Pi so that the NAS server can give you service as central file storage. To do that, make your way to the “Storage” menu followed by the “Disks” sub-menu. You should see the microSD card option in the OMV5 housing.

![Raspberry Pi into NAS server - openmediavault storage](https://www.ubuntupit.com/wp-content/uploads/2020/10/EXT4-Files.jpg)

Your drive can have previous data saved. If you want to delete any of the existing data, select the “wipe” button after choosing the correct drive. You will get a confirmation prompt with a selection choice between “Secure” and “Quick” methods. Go to the “File Systems” after you are done.

Cleaning the drive will make it absent due to the file system lacking. If that happens to you, just select the “create” button and then set up your preference file system. After that, choose your hard drive from the drop-down menu and name it in the label field. At last, select the “EXT4 Filesystem” for the best performance on your OS. Confirm all the pop-ups.

![ext4_files](https://www.ubuntupit.com/wp-content/uploads/2020/10/ext4_files.jpg)

Finally, select the mount button after choosing the external hard drive to connect it with the Raspberry Pi NAS System. Make sure to leave the “boot” and “omv” parts unchanged since they are an important portion of the NAS distribution.

### **Step 8: User Access and Privilege Assigning**

OpenMediaVault5 features a granular control over the users so that you can choose who can or can’t have access to the shared folders on the NAS. You can do that from the “Access Rights Management” menu, followed by the “User” sub-menu. You will see an account named “Pi” with access to every system function on your server.

If you want to add a user, go to the “Add” drop-down menu and then click on the “Add” button. You will get an “Add User” pop up window which will ask for a username and email address with an optional comment section.

![raspberry pi into NAS server - Openmediavault add user](https://www.ubuntupit.com/wp-content/uploads/2020/10/raspberry-pi-into-NAS-server-Openmediavault-add-user.jpg)

After that, head over to the “Groups” tab to add the new users to your created groups. While the “users” group will be selected by default, you will have to check other groups, including “sambashare”, “ssh” and “sum”. Don’t forget to save your changes!

![OpenMediaVault5](https://www.ubuntupit.com/wp-content/uploads/2020/10/OpenMediaVault5.jpg)

You can use this step to allow as many users as you like. But only give them access to the “sambashare” group along with the default group.

### **Step 9: Shared Folders**

You should set up the shared folders first before moving into the settings tab. To do that, go to the “Add” button on the “Shared Folders” sub-menu. You can start with a folder that will have the files shared by the users and applications.

Enter your folder’s name in the “Add Shared folder” pop-up box. Now, you can see the external drive option on the drop-down menu that you had mounted previously. As you are making a shared folder, choose the “Everyone: read/write” option on the “permissions” menu to allow easy access to everyone. Save your changes.

![Openmediavault5 add shared folder](https://www.ubuntupit.com/wp-content/uploads/2020/10/Openmediavault5-add-shared-folder.jpg)

You can change the access information anytime from the drop-down menu called “Permissions”. While you can give everyone different access options, restricting users from getting your data is also possible. Moreover, you will get the option to restrict everyone but yourself when there are any sensitive data. To do that, use the “Privileges” button on the top and highlight the desired folder.

The “shared folder privileges” window will pop-up form to give restrictions to other users with suitable checkboxes.

### **Step 10: Referencing Folders**

Now, you will have to reference folders in the OMV5 to access them from anywhere on the network. To do that, go to the “Services” menu and choose a protocol from the “SMB/CIFS” or “NFS” options. The CIFS has great compatibility with Windows and Mac systems.

![add share](https://www.ubuntupit.com/wp-content/uploads/2020/10/add_share.jpg)

If you choose the “SMB/CIFS” sub-menu, you will be taken to the general settings tab. Choose the Add button to get to the “Add Share” window. You will get a “enable” toggle button in the subsequence, which should be turned green by default.

Go to the “Shared Folders” menu and choose our common folder followed by the guest allowed option from the “Public” menu. Check if the “Honor Existing AC’s” and “Set Browseable” toggle options are enabled. Save your changes.

![add share menu settings](https://www.ubuntupit.com/wp-content/uploads/2020/10/add_share_menu_settings.jpg)

Follow the same process for other folders. If you select the no option instead of the “Guest Allowed”, no one but only the registered users can access the folder. After you are done with this step, make your way to the settings tab on the same sub-menu and enable the toggle button for the “General Settings”. Click the save button.

Now, you have successfully turned your Raspberry Pi into the NAS server. It’s time to see if everything’s okay!

### **Step 11: Accessing the Raspberry Pi NAS**

Since you are done with all the necessary configuration, you should try to access it from another computer on the same network.

First, open your PC to go to the NAS. Go to the files explorer followed by the network section to see your Raspberry Pi NAs running as “RASPBERRYPI” the default hostname. Double click on it to find the shared list.

In case you have a problem finding the NAS, go to the “Advanced Shared Settings” from the network and sharing center through the Windows Control Panel. Then enable the “File and Printer Sharing radio” with the “Network Discovery” button.

![Raspberry Pi into NAS Server](https://www.ubuntupit.com/wp-content/uploads/2020/10/Raspberry-Pi-into-NAS-Server.jpg)

If it still doesn’t work, press the windows+R to get the Run dialogue box. Now you just have to enter the NAS’s IP Address with two following backslashes and enter. You can do the same in the file explorer window’s address bar. Once you can get into the NAS, double click on the folder to get inside.

If you are using a Linux or Ubuntu system, you will have to find the “Connect to server” option from the file manager and input the IP address with the smb:// prefix. That’s all you need to get the connection done.

### **Step 12: Additional Features**

Your Raspberry Pi NAS system is ready to create, save, or share files. But besides these basic functionalities, you can find some additional features, including other protocols like FTP or Apple AFS. You can add these features to make your Raspberry Pi NAS more interesting and adventurous. For instance, [Docker](https://www.ubuntupit.com/important-docker-commands-for-software-developers/) can be an easy way of making your NAS suitable for multiple functions.

![Installing FileRun on NAS using Docker](https://www.ubuntupit.com/wp-content/uploads/2020/10/Installing-FileRun-on-NAS-using-Docker.jpg)

## **Finally, Insights**

So, you have successfully created your first Raspberry Pi NAS system, which is ready to store anything from anywhere. A NAS system can be quite expensive; creating one using your own Raspberry Pi is an affordable choice and a fun project to initiate. This NAS system will save and protect your data like any other purchased storage space. I hope you had fun turning your raspberry pi into a NAS Server and have managed to make it work successfully. Do mention your thoughts in the comment section!
