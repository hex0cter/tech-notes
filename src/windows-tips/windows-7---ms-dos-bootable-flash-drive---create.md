# [Windows 7 - MS-DOS Bootable Flash Drive - Create](http://www.sevenforums.com/tutorials/46707-ms-dos-bootable-flash-drive-create.html)

**Information**

This will show you how to create a flash drive that is able to boot your computer into a **MS-DOS environment**. This will be accomplished by using the **HP Flash Utility** and the **Windows 98 MS-DOS System Files**

**Warning**

The flash drive being used in this process will be **formatted**. Please backup all of your data on the drive beforehand!

## Here's How:

>  **1. Download** the HP Flash Utility **_[hpflash1.zip](http://www.sevenforums.com/attachments/tutorials/42022d1260810265-ms-dos-bootable-flash-drive-create-hpflash1.zip)_** and also download the Windows 98 MS-DOS System Files [](http://javascript%3Cb%3E%3C/b%3E:void\(fileWindow\('46c48f5eee1de3a374bb34ab1ce36573'\)\);)**_[win98boot.zip](http://www.sevenforums.com/attachments/tutorials/42023d1260810265-ms-dos-bootable-flash-drive-create-win98boot.zip)_**. **Extract** hpflash1 to a location readily accessible
>
>> [![MS-DOS Bootable Flash Drive - Create-pic1.jpg](http://www.sevenforums.com/attachments/tutorials/42026d1260810481t-ms-dos-bootable-flash-drive-create-pic1.jpg)](http://www.sevenforums.com/attachments/tutorials/42026d1260810481-ms-dos-bootable-flash-drive-create-pic1.jpg)
> [![MS-DOS Bootable Flash Drive - Create-pic1-1.jpg](http://www.sevenforums.com/attachments/tutorials/42027d1260810481t-ms-dos-bootable-flash-drive-create-pic1-1.jpg)](http://www.sevenforums.com/attachments/tutorials/42027d1260810481-ms-dos-bootable-flash-drive-create-pic1-1.jpg)
>
>
>  **2.** **Run** the installer and follow the simple on-screen instructions
>
>>
>
>>
>> [![MS-DOS Bootable Flash Drive - Create-pic2.jpg](http://www.sevenforums.com/attachments/tutorials/41978d1260774561t-ms-dos-bootable-flash-drive-create-pic2.jpg)](http://www.sevenforums.com/attachments/tutorials/41978d1260774561-ms-dos-bootable-flash-drive-create-pic2.jpg)
>>
>> [![MS-DOS Bootable Flash Drive - Create-pic3.jpg](http://www.sevenforums.com/attachments/tutorials/41979d1260774561t-ms-dos-bootable-flash-drive-create-pic3.jpg)](http://www.sevenforums.com/attachments/tutorials/41979d1260774561-ms-dos-bootable-flash-drive-create-pic3.jpg)
>
>  **3.** **Extract** the contents of "win98boot" to a location readily accessible
>
>> [![MS-DOS Bootable Flash Drive - Create-pic4.jpg](http://www.sevenforums.com/attachments/tutorials/41990d1260778829t-ms-dos-bootable-flash-drive-create-pic4.jpg)](http://www.sevenforums.com/attachments/tutorials/41990d1260778829-ms-dos-bootable-flash-drive-create-pic4.jpg)
>

>  **4.** **Run** the **HP USB Disk Storage Format Tool** that was just installed. **Choose your flash drive** from the drop down list at the top. Also make sure that the **file system is set to FAT32**.
>
>> [![MS-DOS Bootable Flash Drive - Create-pic5.jpg](http://www.sevenforums.com/attachments/tutorials/41984d1260774848t-ms-dos-bootable-flash-drive-create-pic5.jpg)](http://www.sevenforums.com/attachments/tutorials/41984d1260774848-ms-dos-bootable-flash-drive-create-pic5.jpg)
>

>  **5.** Under **Format Options** tick the " **Create a DOS startup disk** " option. Click the "..." button near the empty text box to **browse to** the location of where you **extracted** the **Windows 98 MS-DOS System Files** (see _step 3_ ).
>
> ![Tip](http://www.sevenforums.com/images/tipsmall.png) Tip
>
> Tick " **Quick Format** " under **Format Options** to speed the process up (if you don't want a comprehensive format). You may also want to give the drive a **label** by typing one in the **Volume Label** text field
>
>> [![MS-DOS Bootable Flash Drive - Create-pic6.jpg](http://www.sevenforums.com/attachments/tutorials/41991d1260778829t-ms-dos-bootable-flash-drive-create-pic6.jpg)](http://www.sevenforums.com/attachments/tutorials/41991d1260778829-ms-dos-bootable-flash-drive-create-pic6.jpg)
>
>
>  **6.** **Click** the "Start" button.
>
> ![warning](http://www.sevenforums.com/images/warnsmall.png) Warning
>
> After you **click the "Start" button** , you will be given one final prompt that warns you that the flash drive selected will be formatted. **This is your last chance** to backup data on the drive; after you click yes it will be too late
>
>> [![MS-DOS Bootable Flash Drive - Create-pic7.jpg](http://www.sevenforums.com/attachments/tutorials/41992d1260778829t-ms-dos-bootable-flash-drive-create-pic7.jpg)](http://www.sevenforums.com/attachments/tutorials/41992d1260778829-ms-dos-bootable-flash-drive-create-pic7.jpg)
> [![MS-DOS Bootable Flash Drive - Create-pic8.jpg](http://www.sevenforums.com/attachments/tutorials/41993d1260778829t-ms-dos-bootable-flash-drive-create-pic8.jpg)](http://www.sevenforums.com/attachments/tutorials/41993d1260778829-ms-dos-bootable-flash-drive-create-pic8.jpg)
>
> ![Tip](http://www.sevenforums.com/images/tipsmall.png) Tip
>
> You may remove the files extracted from the archive "win98boot", they are not needed anymore
>
>
>

 _ **Frequently Asked Questions**_

 **Q:** **Why would a MS-DOS USB Drive be useful today? Wasn't that included in older Operating Systems?**


 **A:** MS-DOS was the underlying layer of the Windows 9x series of Operating Systems (Windows 1-ME) that was the "functionality" of the system. A MS-DOS bootable disc can be used to run many recovery tools (still used today) and also update the BIOS of the computer. If you are running an x64 system with no floppy drive and a manufactuer who only provides a 16-bit BIOS updater, this method is the only way to update your BIOS.

 **Q:** **I checked my flash drive after applying the steps above and it is empty? What gives?!**


 **A:** Unless the option to show protected operating system files is checked in folder options, Windows will hide these files due to their attributes matching that of system files. Don't worry, the relevant files are still there

 **Q:** **Alright I successfully completed the steps above, now what do I do?**


 **A:** Now you can download the tool you wanted to run (such as CHKDSK) or your BIOS update application (from the manufactuer) and place the files on to the root of the flash drive. You can find most tools by doing a simple google search

![Tip](http://www.sevenforums.com/images/tipsmall.png) Tip

The Windows 98 MS-DOS System Files archive (win98boot) above has some system tools already included (ex. FORMAT, FDISK, SYS). Just drag and drop these files onto your flash drive

 **Q:** **My flash drive has been converted to the MS-DOS System Disc and I have some tools/BIOS revisions on the drive as well, how do I boot up MS-DOS?**


 **A:** This will largely depend on your model of computer but you will need to restart you computer with the flash drive plugged in and boot to the drive by means of a boot menu or by modifying your BIOS to boot to the flash drive first. Consult the manual of your computer or the respective manufactuer's website for further details.

 **Q:** **I have no further need for the MS-DOS System Disc, how can I remove it from my flash drive?**


 **A:** You may format the flash drive with the built in Windows format utility or you may format it by using the HP USB Disk Storage Format Tool that was used above.

Hope it helps,


Chris

---
