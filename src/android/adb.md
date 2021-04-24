
# [Ten adb commands you should know](http://www.androidcentral.com/android-201-10-basic-terminal-commands-you-should-know)

For a lot of us, the fact that we can [plug our Android phone or tablet into our computer and interact with it](http://www.androidcentral.com/android-z-what-adb)is a big plus. Besides the times when we've broken something and need to fix it, there are plenty of reasons why an advanced Android user would want to talk to his or her device. To do that, you need to have a few tools and know a few commands. That's what we're going to talk about today. Granted, this won't be the end-all be-all discussion of adb commands, but there are 10 basic commands everyone should know if they plan to get down and dirty with the command line.

The tools are easy. If you're a Mac or Linux user, you'll want to install the SDK as explained at [the Android developers site](http://developer.android.com/sdk/index.html). It's not hard, and you don't have the whole driver mess that Windows users do. Follow the directions and get things set up while I talk to the Windows using folks for a minute.

If you're using Windows, things are easier and harder at the same time. The tools themselves are the easy part. [Download this file](http://www.androidcentral.com/sites/androidcentral.com/files/uploads/tools/android-tools.zip). Open the zip file and you'll see a folder named android-tools. Drag that folder somewhere easy to get to. Next, visit the manufacturers page for your device and install the adb and fastboot drivers for Windows. You'll need this so that your computer can talk to your Android device. If you hit a snag, visit the forums and somebody is bound to be able to help you through it.

Now that we're all on the same page, enable USB debugging on your device (see your devices manual if you need help finding it, and remember it was [hidden in Android 4.2](http://www.androidcentral.com/how-enable-developer-settings-android-42)), and plug it in to your computer. Now skip past the break and let's begin!

### 1\. The adb devices command

[![location](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/location_0.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/location_0.jpg)

The **adb devices** command is the most important one of the bunch, as it's what is used to make sure your computer and Android device are communicating. That's why we're covering it first.

If you're a pro at the operating system on your computer, you'll want to add the directory with the Android tools to your path. If you're not, no worries. Just start up your terminal or command console and point it at the folder with the tools in it. This will be [the file](http://www.androidcentral.com/android-201-10-basic-terminal-commands-you-should-know#tools) you downloaded earlier if you use Windows, or the platform-tools folder in the fully installed Android SDK. Windows users have another easy shortcut here, and can simply Shift + right click on the folder itself to open a console in the right spot. Mac and Linux users need to navigate there once the terminal is open, or install an extension for your file manager to do the same right click magic that's in Windows by default.

Once you're sure that you are in the right folder, type " _adb devices_ " (without the quotes) at the command prompt. If you get a serial number, you're good to go! If you don't, make sure you're in the right folder and that you have the device driver installed correctly if you're using Windows. And be sure you have USB debugging turned on!

Now that we have everything set up, let's look at a few more commands.

### 2\. The adb push command

[![adb push](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/adb-push.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/adb-push.jpg)

If you want to move a file onto your Android device programmatically, you want to use the **adb push** command. You'll need to know a few parameters, namely the full path of the file you're pushing, and the full path to where you want to put it. Let's practice by placing a short video (in my case it's a poorly done cover of the Rick James tune _Superfreak_ ) into the Movies folder on your device storage.

I copied the superfreak.mp4 file into the android-tools folder so I didn't need to type out a long path to my desktop. I suggest you do the same. I jumped back to the command line and typed " _adb push superfreak.mp4 /sdcard/Movies/_" and the file copied itself to my Nexus 4, right in the Movies folder. If I hadn't dropped the file into my tools folder, I would have had to specify the full path to it -- something like C:\Users\Jerry\Desktop\superfreak.mp4. Either way works, but it's always easier to just drop the file into your tools folder and save the typing.

You also have to specify the full path on your device where you want the file to go. Use any of the popular Android file explorer apps from Google Play to find this. Windows users need to remember that on Android, you use forward slashes (one of these -- / ) to switch folders because it's Linux.

### 3\. The adb pull command

[![adb pull](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/adb-pull.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/adb-pull.jpg)

If adb push sends files to your Android device, it stands to reason the **adb pull** command gets them out. That's exactly what it does, and it works the same way as the adb push command did. You need to know both the path of the file you want to pull off, as well as the path you want it placed into. You can leave the destination path blank and it will drop the file into your tools folder to make things easy.

In this example, I did it the hard way so you can see what it looks like. The path of the file on the device is "/sdcard/Movies/superfreak.mp4" and I put it on my Windows 8 desktop at "C:\Users\Jerry\Desktop". Again, the easy way it to just let it drop into your tools folder by not giving a destination, which would have been " _adb pull /sdcard/Movies/ superfreak.mp4_". Remember your forwards slash for the Android side, and you'll have no problems here.

### 4\. The adb reboot command

[![adb reboot](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/adb-reboot.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/adb-reboot.jpg)

This is exactly what you think it is -- a way to reboot your device from the command line. Running it is simple, just type " _adb reboot_ " and enter. Before you say "I can just push the button!" you have to understand that these commands can be scripted, and your device can reboot in the middle of a script if you need it to. And it's a good segue to number five.

### 5\. The adb reboot-bootloader and adb reboot recovery commands

[![bootloader](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/reboot-bootloader.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/reboot-bootloader.jpg)

Not only can you reboot your device, you can specify that it reboots to the bootloader. This is awfully handy, as sometimes those button combos are touchy, and if you have a lot of devices you can never remember them all. Some devices (the LG Optimus Black comes to mind) don't even a way to boot to the bootloader without this command. And once again, being able to use this command in a script is priceless. Doing it is easy, just type " _adb reboot-bootloader_ " and hit the enter key.

Most devices can also boot to the recovery directly with the " _adb reboot recovery_ " (note there is no hyphen in this one) and some can't. It won't hurt anything to try, and if yours can't nothing will happen.

### 6\. The fastboot devices command

[![fastboot devices](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/fastboot-devices.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/fastboot-devices.jpg)

When you're working in the bootloader, adb no longer works. You're not yet booted into Android, and the debugging tools aren't active to communicate with. We use the fastboot command in it's place.

Fastboot is probably the most powerful tool available, and many devices don't have it enabled. If you're does, you need to be sure things are communicating. That's where the **fastboot devices** command comes into play. At the prompt, just type in " _fastboot devices_ " and you should see a serial number, just like the adb devices command we looked at earlier.

If things aren't working and you are using Windows, you likely have a driver issue. Hit those forums for the answer.

### 7\. The fastboot oem unlock command

[![unlock](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/unlock.png)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/unlock.png)

The holy grail of Android commands, **fastboot oem unlock** does one thing, and one thing only -- unlocks your Nexus device (or an HTC device using their official tool). If you're using a phone from a different manufacturer, you have a different method of unlocking things -- maybe with ODIN or .sbf files -- and this won't apply to you. We're including it because even if you don't need it, it's an important part of Android's openness. Google doesn't care what we do with phones or tablets that we've bought, and include this easy way to crack them open. That's something you usually don't see from any tech company, and a big part of the reason why many of us choose Android.

Using it is easy enough. Once you've used fastboot devices to make sure everything is communicating, just type " _fastboot oem unlock_ " at the prompt and hit enter. Look at your device, read carefully, and choose wisely.

 **Protip: Using "fastboot oem unlock" will erase everything on your device**

### 8\. The adb shell command

[![adb shell](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/shell.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/shell.jpg)

The **adb shell** command confuses a lot of folks. There are two ways to use it, one where you send a command to the device to run in its own command line shell, and one where you actually enter the device's command shell from your terminal. In the image above, I'm inside the device shell, listing the flies and folders on the device. Getting there is easy enough, just type " _adb shell_ " and enter. Once inside, you can escalate yourself to root if you need to. I'll warn you, unless you're familiar with an ash or bash shell, you need to be careful here -- especially if you're root. Things can turn south quickly if you're not careful. If you're not familiar, ash and bash are command shells that a lot of folks use on their Linux or Mac computers. **It's nothing like DOS.**

The other method of using the adb shell command is in conjunction with one of those Ash commands your Android device can run. You'll often use it for more advanced tasks like changing permissions of files or folders, or running a script. Using it is easy -- "adb shell <command>". An example would be changing permissions on a file like so: " _adb shell chmod 666 /data/somefile_ ". As mentioned, be very careful running direct commands using these methods.

### 9\. The adb install command

[![adb install](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/adb-install.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/adb-install.jpg)

While [adb push](http://www.androidcentral.com/android-201-10-basic-terminal-commands-you-should-know#push) can copy files to our Android devices, **adb install** can actually install .apk files. Using it is similar to use the push command, because we need to provide the path to the file we're installing. That means it's always easier to just drop the app you're installing into your tools folder. Once you've got that path, you tell your device to [sideload](http://www.androidcentral.com/what-sideloading-android-z) it like this: " _adb install TheAppName.apk_".

If you're updating an app, you use the -r switch: " _adb install -r TheAppName.apk_". There is also a **-s** switch which tries to install on the SD card if your ROM supports it, and the **-l** switch will forward lock the app (install it to /data/app-private). there are also some very advanced encryption switches, but those are best left for another article.

And finally, you can uninstall apps by their package name with " _adb uninstall TheAppName.apk_". Uninstall has a switch, too. The -k switch will uninstall the app but leave all the app data and cache in place.

### 10\. The adb logcat command

[![adb logcat](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/9274/logcat_0.jpg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/9274/logcat_0.jpg)

The **adb logcat** command is one of the most useful commands for some folks, but just prints a bunch of gibberish unless you understand what you're seeing. It returns the events written to the various logs in the running Android system, providing invaluable information for app developers and system debuggers. Most of us will only run this one when asked by one of those developers, but it's very important that we know how to use it correctly.

To see the log output on your computer screen, just type " _adb logcat_ " and hit enter. Things can scroll by pretty fast, and chances are you won't find what you're looking for. There are two ways to handle this one -- filters, or text output.

The filter switch is used when a developer has placed a tag in his or her application, and wants to see what the event logs are saying about it. If it's needed, the developer will tell you what tag to append to the command. The text output is more useful, as it logs to a .txt file on your computer for reading later. Evoke is like so: " _adb logcat > filename.txt_". Let it run while you're doing whatever it takes to crash the app or system program you're debugging, then close it with the CTRL+C keystroke. You'll find the full log file saved in the directory you're working from, likely your tools folder. This is what you'll send to the developer.

Be warned that sensitive information can be contained in the log files. Be sure you trust the person you're sending them to, or open the log file in a text editor and see just what you're sending and edit as necessary.

There are plenty of other switches for the logcat command. Savvy developers can choose between the main, event, or radio logs, save and rotate log files on the device or their computer, and even change the verbosity of the log entries. These methods are a bit more advanced, and anyone interested should read the Android developer documentation.

### Bonus: The adb sideload command

[![adb sideload](http://www.androidcentral.com/sites/androidcentral.com/files/styles/w680h550/public/postimages/684/adb-sideload_.jpeg)](http://www.androidcentral.com/sites/androidcentral.com/files/styles/xlarge/public/postimages/684/adb-sideload_.jpeg)

This one's relatively new, and it's one of the easier ways to update a stock Nexus device. Every over-the-air update downloads the update file from a public URL. That means you can download the update and install it manually without having to wait for your phone to have the update pushed to it. We call it "manually updating," and the end result is the same as if you wait. But we hate waiting.

All you have to do is download the update to your computer. Plug your phone into the computer. Reboot into recovery on your phone and choose "Apply update from ADB." Then hop into your favorite terminal/command line and type "adb sideload xxxxxxxx.zip," with the variable pointing to the update you downloaded. Let things run their course, and you're golden.

And there you have it. There are plenty more commands to learn if you 're the type who likes to learn commands, but these 10 are the ones you really need to know if you if you want to start digging around at the command prompt.
