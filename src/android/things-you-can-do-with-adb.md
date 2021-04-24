# [The Most Useful Things You Can Do with ADB and Fastboot on Android](https://lifehacker.com/the-most-useful-things-you-can-do-with-adb-and-fastboot-1590337225)

![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Last week, we showed you [how to install ADB and fastboot on any OS](https://lifehacker.com/the-easiest-way-to-install-androids-adb-and-fastboot-to-1586992378). If you're not sure why you'd want to go to the (relatively minor) trouble, here are just some of the useful things you can do with these two handy tools.

[![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://lifehacker.com/the-easiest-way-to-install-androids-adb-and-fastboot-to-1586992378)

[](https://lifehacker.com/the-easiest-way-to-install-androids-adb-and-fastboot-to-1586992378)

If you’ve ever tried to root your Android phone or flash a ROM, you may have heard about ADB and/or

[Read more](https://lifehacker.com/the-easiest-way-to-install-androids-adb-and-fastboot-to-1586992378)

 _Disclaimer:_ These commands are intended to give you an idea of what you can do with ADB and fastboot. They **are not direct instructions** and not all commands work on all devices. It's perhaps better to think of this as a glossary. Due to the sheer number and variety of devices and implementations in the Android world, it's impossible for us to provide step-by-step instructions for every single device. Be sure to research your specific phone or tablet before throwing commands at it.

### Manage Your Device with ADB

![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

ADB has a wide variety of functions for managing your device, moving content to and from your phone, installing apps, backing up and restoring your software, and more. You can use ADB while your phone is plugged in to a computer. You can also use ADB with your device wirelessly by following [these instructions](http://developer.android.com/tools/help/adb.html#wireless). You'll need to briefly connect your device to your computer with a USB cable for this to work, but it should only take a few seconds to execute these commands and then you're good to use ADB wirelessly if you so choose.

 **adb devices**
 _Function:_ Check connection and get basic information about devices connected to the computer.

When using ADB, this is probably the first one command you'll run. It will return a list of all devices that you have connected to your computer. If it returns a device ID like the one seen above, you're connected and ready to send commands.

 **adb reboot recovery**
 _Function:_ Reboot your phone into recovery mode.

A lot of functions like [flashing ROMs to your phone](https://lifehacker.com/how-to-flash-a-rom-to-your-android-phone-30885281) require you to boot into recovery mode. Normally, this requires you to hold down a particular set of buttons on your phone for a certain length of time, which is obnoxious. This command allows you to boot directly into recovery mode without performing the complex finger dance of your people.

[![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://lifehacker.com/how-to-flash-a-rom-to-your-android-phone-30885281)

[](https://lifehacker.com/how-to-flash-a-rom-to-your-android-phone-30885281)

Android is great, but sometimes, the version you get with your phone—whether its vanilla Android…

[Read more](https://lifehacker.com/how-to-flash-a-rom-to-your-android-phone-30885281)

 **adb reboot-bootloader**
 _Function:_ Reboot your phone into bootloader mode.

Along the same lines as the previous command, this one allows you to boot directly to your phone's bootloader. Once you're in the bootloader, ADB won't work anymore. That's where fastboot comes in (which we'll get to in a bit). However, much like the recovery command, it's much easier to boot into your bootloader with a command on your computer than a complex series of buttons on your phone.

 **adb push [source] [destination]**
 _Function:_ Copy files from your computer to your phone.

The push command allows you to copy files from your computer to your phone without touching your device. This is particularly handy for copying large files from your computer to your phone like movies or ROMs. In order to use this command, you'll need to know the full file path for both your source and destination. If the file you want to copy is already in your tools folder (where ADB lives), you can simply enter the name of the file as the source.

 **adb pull**
 _Function:_ Copy files from your phone to your computer.

The yin to to push's yang, the pull command in ADB allows you to copy files from your phone to your computer. When pulling files, you can choose to leave out the destination parameter. In that case, the file will be copied to the folder on your computer where ADB itself lives. You can then move it to wherever you'd prefer like normal.

 **adb install [source.apk]**
 _Function:_ Remotely install APKs on your phone.

You can use this command to install an app on your phone without touching it. While this isn't a terribly impressive trick for an app that's on the Play Store (where you can already [remotely install, uninstall, and update apps](https://lifehacker.com/the-google-play-web-store-now-lets-you-update-and-unins-5922011)), it's quite handy if you need to sideload an app.

[![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://lifehacker.com/the-google-play-web-store-now-lets-you-update-and-unins-5922011)

[](https://lifehacker.com/the-google-play-web-store-now-lets-you-update-and-unins-5922011)

Google recently made some nice updates to the Google Play store, but they quietly updated the web…

[Read more](https://lifehacker.com/the-google-play-web-store-now-lets-you-update-and-unins-5922011)

 **adb shell [command]**
 _Function:_ Open or run commands in a terminal on the host Android device.

We [love the terminal](https://lifehacker.com/master-the-command-line-this-weekend-5990668) here at Lifehacker. There are [so many great things](http://lifehacker.com/top-10-tools-that-are-better-in-the-command-line-5935869) you can do with it. Most of us don't tend to bother with the terminal in Android because we don't want to type long text-based commands on a tiny touchscreen. However, the adb shell command allows you to open up a full terminal on the host device. Alternatively, you can type "adb shell" followed by a valid terminal command to execute just that one command by itself.

[![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://lifehacker.com/master-the-command-line-this-weekend-5990668)

[](https://lifehacker.com/master-the-command-line-this-weekend-5990668)

Keyboard shortcuts only get you so far. If you really want to harness the real power of your…

[Read more](https://lifehacker.com/master-the-command-line-this-weekend-5990668)

 **adb backup**
 _Function:_ Create a full backup of your phone and save to the computer.

Backing up your Android phone is already something you [can and should be doing automatically](https://lifehacker.com/how-to-set-up-a-fully-automated-app-and-settings-backup-5784857). However, if you need to create a complete backup before hacking away at something particularly risky, you can create a full backup with a single command. You don't even need root access (though this may mean that some protected data can't be backed up). You can read more about the parameters for this command—and there are a lot of them—[here](http://forum.xda-developers.com/galaxy-nexus/general/guide-phone-backup-unlock-root-t1420351).

[![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)](https://lifehacker.com/how-to-set-up-a-fully-automated-app-and-settings-backup-5784857)

[](https://lifehacker.com/how-to-set-up-a-fully-automated-app-and-settings-backup-5784857)

In an ideal world, your Android's apps, their settings, and your system settings would…

[Read more](https://lifehacker.com/how-to-set-up-a-fully-automated-app-and-settings-backup-5784857)

 **adb restore**
 _Function:_ Restore a backup to your phone.

The corollary to the previous command, adb restore allows you to point to an existing backup file and restore it to your device. So, for example, type "adb restore C:\\[restorefile].zip" and your phone will shortly be back to normal.

 **adb sideload**
 _Function:_ Push and flash custom ROMs and zips from your computer.

This command is a relative newcomer to the ADB field and is only supported by some custom recoveries. However, you can use this single command to flash a .zip that's on your computer to your phone. Once again, this allows you to flash whole ROMs (or anything else you can flash with a .zip file) without touching your phone.

These commands are just some of the more useful ones you can use with ADB installed on your computer. You may not want to use it all the time for everyday tasks, but when you need them, you'll be glad you have them.

### Unlock and Modify Your Phone's Firmware with Fastboot

![Illustration for article titled The Most Useful Things You Can Do with ADB and Fastboot on Android](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

As stated in our previous article, fastboot allows you to send commands to your phone while in the bootloader (the one place ADB doesn't work). While you can't do quite as many things here, the things you can do are awesome, including unlocking certain phones—like Nexuses and certain others—as well as flashing custom recoveries and even some ROMs. It should be noted, though, that not all phones support fastboot and if you have a locked bootloader, you're probably out of luck here. That being said, here are some of the most useful tools in fastboot's arsenal.

 **fastboot oem unlock**
 _Function:_ Unlock your bootloader, making root access possible.

When people go on about how "open" Nexus devices are, this is what they're talking about. Most phones require a root exploit to gain superuser access and the ability to heavily modify your phone's firmware. With a Nexus device, you can unlock your bootloader with a single command. From there, you'll be allowed to install custom recoveries or give yourself root access.

It should be noted, this command will also completely wipe your phone. This means it's a great command to run when you get a brand new phone, but if you've been using yours for a while, do a backup first.

 **fastboot devices**
 _Function:_ Check connection and get basic information about devices connected to the computer.

This is essentially the same command as adb devices from earlier. However, it works in the bootloader, which ADB does not. Handy for ensuring that you have properly established a connection.

 **fastboot flash recovery**
 _Function:_ Flash a custom recovery image to your phone.

Flashing a custom recovery is an essential part of the [ROM-swapper lifestyle](https://lifehacker.com/how-to-flash-a-rom-to-your-android-phone-30885281). As with everything else in this list, you can install a custom recovery on your device without touching it by using this command.
