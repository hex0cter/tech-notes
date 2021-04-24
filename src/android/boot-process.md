
date: 2015-10-30 20:03:37  
author(s): Saad Faruque  

# [Android bootloader/fastboot mode and recovery mode explained/Android boot process](https://tektab.com/2015/10/31/android-bootloaderfastboot-mode-and-recovery-mode-explained/)

  


Besides normal booting of an android device, there are two more systems maintenance mode. The bootloader or fastboot mode and the recovery mode. We can get into both the modes via startup key combinations or by using adb commands.

[![android, booting, recovery, fastboot, bootloader, adb boot-loader, adb recovery](https://saadfaruque.files.wordpress.com/2015/10/android-booting-process.png?w=663)](https://saadfaruque.files.wordpress.com/2015/10/android-booting-process.png)Android booting process, recovery mode, boot-loader/fastboot mode

**What is a bootloader and how to get into the bootloader mode on your android device?**

A bootloader is a computer program that loads an operating system (OS) or runtime environment for the computer after completion of the self-tests.

Bootloader is like BOIS to your computer. It is the first thing that runs when you boot up your Android device. It packages the instructions to boot operating system kernel. Basically, Android device has a storage space(disk) that has several partitions, which holds the Android system file in one and all the app data in another. Bootloader serves as a security checkpoint that is responsible for checking and initializing the hardware and starting software. You can get into this mode using adb command as well as by pressing device-specific buttons.

**To enter into fastboot mode using adb command use the following steps:**

  1. Ensure you have adb and fastboot tools installed on your system
  2. Appropriate usb drivers installed on the PC for your android device
  3. USB debugging is activated on your phone
  4. Connect your android device with your computer over a usb 2 port



Test the connectivity using the following command (provided your phone screen is unlocked)
    
    
    adb devices

should give output such as  
List of devices attached  
…………………… device

to get into fastboot mode use the following command
    
    
    adb reboot-bootloader

Once you enter your device screen shall indicate that has entered in fastboot mode

the following command will list the connected device which is in fastboot mode
    
    
    fastboot devices

shall display something like

mt6582_phone fastboot

On the device screen you should see something like the following

[![fastboot,bootloader,android, adb reboot-bootloader](https://saadfaruque.files.wordpress.com/2015/10/fastboot.jpg?w=318)](https://saadfaruque.files.wordpress.com/2015/10/fastboot.jpg) [![fastboot-bootloader-1](https://saadfaruque.files.wordpress.com/2015/10/fastboot-bootloader-1.jpg?w=365)](https://saadfaruque.files.wordpress.com/2015/10/fastboot-bootloader-1.jpg)  
**Some of the most commonly used “fastboot” commands include:**

  * flash – rewrites a partition with a binary image stored on the host computer
  * erase – erases a specific partition
  * reboot – reboots the device into either the main operating system, the system recovery partition or back into its boot loader
  * devices – displays a list of all devices (with the serial number) connected to the host computer
  * format – formats a specific partition; the file system of the partition must be recognized by the device



to get out of the bootloader/fastboot mode

use
    
    
    fastboot continue

or
    
    
    fastboot reboot

Fastboot/recovery more (Summery)  
Fastboot mode/recovery mode is mostly used to erase or install various images such as system, boot, userdata, and more. You may end up using fastboot tool and fastboot/recovery mode when you are installing a custom rom or restoring factory image on your android device.

#### **What is android recovery mode, custom recovery and how to get into the recovery mode?**

Android devices come with Google’s recovery environment, this is also known “stock recovery.” You can boot to the recovery system by pressing device-specific buttons as your android device or use adb command that boots your device to recovery mode.

These options can be selected using the volume up/down button and power button. In this mode, adb or fastboot tools has no use.

There are various custom recovery /third party recovery environments are available such as Cyanogen recovery, ClockworkMod recovery (CWM), Team Win Recovery Project (TWRP) etc. You can install custom recovery from the bootloader/fastboot mode. Custom recovery images are usually has additional features such as better backup and recovery. In general, custom recoveries are only necessary if you plan on flashing a custom ROM. Most Android users wouldn’t even notice a difference between a device with the stock recovery system installed and one with a custom recovery.

**To enter into recovery mode using adb command use the following steps:**

  1. Ensure you have adb and fastboot tools installed on your system
  2. Appropriate usb drivers installed on the PC for your android device
  3. USB debugging is activated on your phone
  4. Connect your android device with your computer over a usb 2 port



Test the connectivity using the following command (provided your phone screen is unlocked)
    
    
    adb devices

should give output such as  
List of devices attached  
…………………… device

to get into recovery mode use the following command
    
    
    adb reboot recovery

[![android recovery mode, adb reboot recovery](https://saadfaruque.files.wordpress.com/2015/10/android-system-recovery-3e.jpg?w=549)](https://saadfaruque.files.wordpress.com/2015/10/android-system-recovery-3e.jpg)

Once in recovery mode, shall see a recovery menu, which provides list of fixed options. such as

  * reboot system
  * apply update from SD card
  * apply update from cache
  * wipe data/factory reset
  * backup user data
  * restore user data



To exit the recovery mode, select reboot system now and the system will boot back into the installed system.

