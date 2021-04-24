
# [How to Install ClockworkMod Recovery on Samsung Galaxy S2 / i9100](http://wiki.cyanogenmod.org/w/Install_CM_for_i9100)


Samsung devices come with a unique boot mode called [Download Mode](http://wiki.cyanogenmod.org/w/Glossary#Download_Mode) which is very similar to [Fastboot Mode](http://wiki.cyanogenmod.org/w/Glossary#Fastboot_Mode) on some devices with unlocked bootloaders. [Heimdall](http://www.glassechidna.com.au/products/heimdall/) is a cross-platform, open source tool for interfacing with Download Mode on Samsung devices. The preferred method of installing a custom recovery is through this boot mode. Rooting the stock firmware is neither recommended nor necessary.

1. Download and install the [Heimdall Suite](http://glassechidna.com.au/heimdall/#downloads)


*  **Windows:** Extract the Heimdall suite and take note of the directory holding `heimdall.exe`. You can verify Heimdall is working by opening a command prompt in this directory and typing `heimdall version`. If you receive an error, be sure that you have the [Microsoft Visual C++ 2012 Redistributable Package (x86/32bit)](http://www.microsoft.com/en-us/download/details.aspx?id=30679) installed on your computer.
*  **Linux:** Pick the appropriate installation package based on your distribution. The `-frontend` packages are not required for this guide. After installation, heimdall should be available from the terminal; type `heimdall version` to verify installation succeeded.
*  **Mac:** Install the dmg package. After installation, heimdall should be available from the terminal; type `heimdall version` to verify installation succeeded.
*  **Building from source:** The source code for the Heimdall Suite is available on [Github](http://github.com/Benjamin-Dobell/Heimdall). For more details about how to compile the Heimdall Suite, please refer to the [`README`](http://github.com/Benjamin-Dobell/Heimdall) file on Github under the relevant operating system directory. You can also refer to the [Install and compile Heimdall](http://wiki.cyanogenmod.org/w/Install_and_compile_Heimdall) instructions on this wiki.

2. Download codeworkx's ClockworkMod Recovery. You can directly download the recovery image using the link below, or visit [clockworkmod.com/rommanager](http://clockworkmod.com/rommanager) to download the latest version. Be careful to select the right image! The downloaded file should have _i9100_ in the name.
3. Rename the recovery image to `recovery.img`.
  *  _Windows users:_ move recovery.img to the same directory where heimdall.exe is located.
4. Windows (only) driver installation - _Skip this step if you are using Linux or Mac_.
    A more complete set of the following instructions can be found in the [Zadig User Guide](http://github.com/pbatard/libwdi/wiki/Zadig).
    1. Run `zadig.exe` from the **Drivers** folder of the Heimdall Suite.
    2. Choose **Options** » **List All Devices** from the menu.
    3. Select **Samsung USB Composite Device** or **MSM8x60** or **Gadget Serial** or **Device Name** from the drop down menu. (If nothing relevant appears, try uninstalling any Samsung related Windows software, like Samsung Windows drivers and/or [Kies](http://en.wikipedia.org/wiki/Samsung_Kies)).
    4. Click **Replace Driver** (having selecting "Installed Driver" from the drop down list built into the button).
    5. If you are prompted with a warning that the installer is unable to verify the publisher of the driver, select **Install this driver anyway.** You may receive two more prompts about security. Select the options that allow you to carry on.
5. Power off the Galaxy S II and connect the USB adapter to the computer but not to the Galaxy S II, yet.
6. Boot the Galaxy S II into download mode by holding **Volume Down** , **Home** & **Power**. Accept the disclaimer on the device. Then, insert the USB cable into the device.
7. At this point, familiarize yourself with the _Flashing heimdall_ notes below so that you are prepared for any strange behavior if it occurs.
8. On the computer, open a terminal (or Command Prompt on Windows) in the directory where the recovery image is located and type:
  `heimdall flash --kernel recovery.img --no-reboot`
9. A blue transfer bar will appear on the device showing the recovery being transferred.
10. Unplug the USB cable from your device
11. You can now manually reboot the phone into ClockworkMod Recovery mode by holding **Volume Up** , **Home** , & **Power**.
12. The Galaxy S II now has ClockworkMod Recovery installed.
