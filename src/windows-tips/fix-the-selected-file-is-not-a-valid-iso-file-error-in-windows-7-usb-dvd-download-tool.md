# [Fix: “The Selected File Is Not A Valid ISO File” Error In Windows 7 USB/DVD Download Tool](http://www.intowindows.com/fix-the-selected-file-is-not-a-valid-iso-file-error-in-windows-7-usbdvd-download-tool/)

These days, a large number of PC users prefer [installing Windows OS from a USB drive](http://www.intowindows.com/how-to-install-windows-7vista-from-usb-drive-detailed-100-working-guide/) instead of traditional DVD disc. Even though there are plenty of better tools out there like Rufus to [create bootable USB from an ISO file](http://www.intowindows.com/how-to-create-bootable-windows-7-usb-to-install-windows-7-from-usb-flash-drive-using-windows-7-dvdusb-tool/), most PC users prefer using the official [Windows 7 USB/DVD Download Tool](http://www.intowindows.com/how-to-create-bootable-windows-7-usb-to-install-windows-7-from-usb-flash-drive-using-windows-7-dvdusb-tool/).

[![Selected File isn't ISO](http://www.intowindows.com/wp-content/uploads/2013/11/Selected-File-isnt-ISO_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/Selected-File-isnt-ISO.jpg)

Windows 7 USB/DVD Download Tool sports an easy-to-use interface and is [compatible with Windows 8 and 8.1 as well](http://www.intowindows.com/use-windows-7-usbdvd-download-tool-to-create-windows-8-1-installation-media/), but at times when you open Windows ISO file by clicking the Browse button, the tool shows “The selected file is not a valid ISO file. Please select a valid ISO file and try again” error.

While I am no expert, the error occurs when the selected ISO file has only ISO9660 file system, and missing UDF and Joliet. In order to fix this error, you need to re-build the ISO file with ISO9660 + UDF + Joliet file system.

A quick Google search reveals that there are plenty of guides out there to fix this error but the catch is that all of them ask you download PowerISO or UltraISO software. The real catch is that both UltraISO and PowerISO aren’t free and you need to purchase their licenses. And no, the trail software can’t handle large ISO files.

Users who want to fix “The selected file is not a valid ISO file. Please select a valid ISO file and try again” error with the help of a free software can follow the given below instructions.

## Method 1:

Step 1: Download ImgBurn software from [here](http://www.imgburn.com/index.php?act=download) and install the same on your PC. As some of you know, ImgBurn is a free software and is compatible with all recent versions of Windows, both 32-bit and 64-bit systems.

Step 2: Launch ImgBurn, click Create image file from files/folder. Drag and drop the ISO file to ImgBurn window to add it to the source list.

[![The Selected File is not a valid ISO file Step1](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step1_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step1.jpg)

[![The Selected File is not a valid ISO file Step2](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step2_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step2.jpg)

Step 3: Select a location to save the new ISO file by clicking the Browse button next to Destination box.

Step 4: Click on the Options tab on the right-side pane of ImgBurn and select the file system as ISO9660 + Joliet + UDF from the drop-down menu.

[![The Selected File is not a valid ISO file Step3](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step3_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step3.jpg)

Step 5: Finally, click the Build button (see picture) to begin saving the edited ISO file with new file system. Click Yes button when you see the confirmation dialog and click Yes button again if you see confirm Volume Label dialog box, and finally, click OK button to begin saving the ISO file.

[![The Selected File is not a valid ISO file Step4](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step4_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step4.jpg)

[![The Selected File is not a valid ISO file Step6](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step6_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step6.jpg)

[![The Selected File is not a valid ISO file Step7](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step7_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step7.jpg)

[![The Selected File is not a valid ISO file Step8](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step8_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step8.jpg)

[![The Selected File is not a valid ISO file Step9](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step9_thumb.jpg)](http://www.intowindows.com/wp-content/uploads/2013/11/The-Selected-File-is-not-a-valid-ISO-file-Step9.jpg)

Once the job is done, you can run Windows 7 USB/DVD Download Tool again and browse to the newly created ISO file to prepare the bootable USB/DVD without any issues.

## Method 2:

If “The selected file is not a valid ISO file. Please select a valid ISO file and try again” error is appearing even after following the above mentioned workaround, we suggest you go ahead and download the popular [Rufus tool](http://www.intowindows.com/how-to-install-windows-8-1-from-usb-flash-drive/) and then follow the simple instructions in [how to install Windows 8.1 from bootable USB](http://www.intowindows.com/how-to-install-windows-8-1-from-usb-flash-drive/) guide to create the bootable media without any errors.
