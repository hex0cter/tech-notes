
date: None  
author(s): None  

# [Completely Delete USB Flash Drive Partition in MacOS using diskutil - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/os-x-tips/completely-delete-usb-flash-drive-partition-in-macos-using-diskutil)

https://johnpili.com/completely-delete-usb-flash-drive-partition-in-macos-using-diskutil/

You may want to completely erase the partition table of your USB flash drive including the boot record. In macOS you do easily do that using diskutil. During this COVID-19 lockdown in Malaysia, I wanted to use my weekend time in installing Linux on an old laptop. It turns out that old laptop only support MBR and not GPT boot record and FAT32 instead of EX-FAT. I have to then delete the partition table from GPT to MBR and load LUBUNTU Linux distribution into the flash drive using Unetbootin.

## Commands

To erase and format your USB flash drive into MBR and FAT32 use the following code snippet below
    
    
    diskutil partitionDisk /dev/your-usb-disk MBR MS-DOS FAT32 100%
    

To repartition with an MBR partition table but without formatting the USB you can do that using the following command
    
    
    diskutil partitionDisk /dev/disk2 MBR Free Space 100%
    

## Diskutil Usage
    
    
    Usage:  diskutil partitionDisk MountPoint|DiskIdentifier|DeviceNode
            [numberOfPartitions] [APM[Format]|MBR[Format]|GPT[Format]]
            [part1Format part1Name part1Size part2Format part2Name part2Size
             part3Format part3Name part3Size ...]
    

## Partition Tables

  * APM – Apple Partition Map
  * MBR – Master Boot Record
  * GPT – GUID Partition Table



## Supported filesystem format

  * Case-sensitive APFS (or) APFSX
  * APFS (or) APFSI
  * ExFAT
  * Free Space (or) FREE
  * MS-DOS
  * MS-DOS FAT12
  * MS-DOS FAT16
  * MS-DOS FAT32 (or) FAT32
  * HFS+
  * Case-sensitive HFS+ (or) HFSX
  * Case-sensitive Journaled HFS+ (or) JHFSX
  * Journaled HFS+ (or) JHFS+



## Disclaimer

Using diskutil will erase data on the flash drive or any media you point it on. Please ensure that you made backup of any data from your USB and storage media. Throughly read the documentation of diskutil by running
    
    
    man diskutil
    

I will be not responsible for any data lost or corruption using this guide.  
  
---

