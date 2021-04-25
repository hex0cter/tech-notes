
date: None  
author(s): None  

# [Compacting VirtualBox Disk Images - Windows Guests - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/compacting-virtualbox-disk-images---windows-guests)

VirtualBox is a Net Reliant favorite when it comes to virtualization. It is a professional, enterprise grade solution that runs on Windows, Linux, Macintosh, and Solaris hosts.

VirtualBox allows for flexible storage management by allowing for the creation of dynamically allocated guest images. Most users go for the dynamically expanding images in VirtualBox as they do not want to limit themselves to a small virtual disk size and at the same time do not want to waste disk space on their host while the guest doesn't actually need it. Although these images will initially be very small and occupy minimal storage space, over time the images will grow. This is due to the image expanding every time a disk sector (virtual) is written to for the first time.

To help reduce excess disk usage, VirtualBox provides a mechanism for compacting dynamically allocated guest images. Below are the steps to follow if your guest operating system is Windows:

  1. Start the Windows virtual machine and delete any unnecessary files;
  2. Defragment the disk of the Windows virtual machine;
  3. Clean the free space on the disk of the Windows virtual machine;
  4. Shutdown the Windows virtual machine;
  5. Use the VirtualBox VBoxManage utility to compact the Windows guest image.



 **Step 1: Start the Windows Virtual Machine and Delete Unnecessary Files  
**

Start the Windows Virtual Machine and delete any files that you don't need. Places to start are:

  * Empty the recycle bin;
  * Delete files in your temp folders;
  * Clear any web browser caches;
  * Clear any application caches.



 **Step 2: Defragment the Disk**

  * Locate your hard disk drive using Windows Explorer in the virtual machine;
  * Right-click the drive and choose the Properties option;
  * Then select the Tools tab and click the Defragment now ... button.



Follow the steps to defragment the virtual Windows disk.

 **Step 3: Clean any free disk space**

After the disk has been defragmented, the virtual Windows drive will still have unused space containing garbage bits and bytes. These garbage bits and bytes are from the contents of files that used to occupy that space but that are no longer there.

The most effective way to clean free disk space on a Windows drive is to overwrite the unused space with a bitstream of zeros or to zero-fill any free space.

Windows does not come with a native utility to zero-fill unused space but you can find the excellent SDelete tool at Microsoft's TechNet: <http://technet.microsoft.com/en-us/sysinternals/bb897443.aspx>

SDelete (or Secure Delete) is a command line utility. So to zero-fill the virtual Windows disk, type the following at the DOS prompt:
    
    
    C:\> sdelete.exe -z

where -z is the SDelete parameter to zero any free space.

You can also use:
    
    
    C:\> sdelete.exe -c

where -c is the SDelete parameter to clean any free space.

Once SDelete is running you will see a message similar to the following:
    
    
    SDelete is set for one pass.  
    Cleaning free space on c:: 12%

 **Step 4: Shutdown the Windows Virtual Machine**

When SDelete has finished running and the free space cleaned or zeroed is 100%, shutdown the Windows virtual machine.

 **Step 5: Compact the Windows guest image**

To compact the Windows guest image, use the VirtualBox VBoxManage utility. Assuming a Windows host, use the following command at the DOS prompt:
    
    
    VBoxManage modifyhd --compact "[drive]:\[path_to_image_file]\[name_of_image_file].vdi"

Ensure that you replace the items in square brackets with your parameters.

If your Windows host complains that VBoxManage cannot be found or is an invalid command, you may need to explicitly specify the path to the VirtualBox executables. So a complete example for compacting a Windows guest image at the DOS prompt is as follows:
    
    
    C:\> path C:\Program Files\Oracle\VirtualBox  
    C:\> VBoxManage modifyhd --compact "C:\netreliant_VMs\windowsXP_001.vdi"

Once the VirtualBox VBoxManage utility is running you will see progress indicators in 10% increments starting from 0% to 100%. And once the process is complete, you should have a smaller disk image file.

