
date: None  
author(s): None  

# [Grub Customizer - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/grub-customizer)

**GRUB CUSTOMIZER & GRUB 1.99 ISSUES**  
Daniel Richter has released Grub Customizer 2.2 , which deals with the new submenu structure in Grub 1.99 and later. See post #158 for the announcement. If you are using the default bootloader in Natty or later, please update your version of Grub Customizer to the latest version.

 **Images/Fonts**

  
Grub 1.99 allows placing an image directly in _/boot/grub_ for use as a background image. Because of the way Grub sets the background image priority, if an image resides in /boot/grub it will be used even if the user selects an image in Grub Customizer. If using Grub Customizer, remove all image files from the _/boot/grub_ folder, set the image in Grub Customizer, and do not copy the image to the grub folder.

These issues are addressed with a bit more detail starting in Post #108, and the developer, Daniel Richter, responds in Post # 118. (Thanks Daniel).

 **GRUB CUSTOMIZER**

  
Daniel Richter has developed a GUI configuration tool to allow users to change the Grub 2 settings without using the command line. The application allows the user to add, remove, freeze, rename and reorder boot menu items. It will also allow changes to the Grub 2 configuration settings such as background image and menu timeout. For long-time users familiar with StartUp-Manager, this application performs many of the same capabilities with additional options. It also makes convoluted guides such as my "Grub 2 Title Tweaks" unnecessary for all but the most devoted command-line enthusiasts!

The purpose of this guide is to briefly explain how to use Grub Customizer. I am not going 'under the hood' to explain what happens at the file level. For those interested in how the application actually accomplishes the tasks, please refer to [Daniel's Grub Customizer FAQ](https://answers.launchpad.net/grub-customizer/+faq/1355).

I will include thumbnails of the primary screens. While full-scale graphics would be more convenient, thumbnails comply with the Forum's guidelines for posting images. Eventually I may create an Ubuntu Community documnet with complete graphics and will post a link should I undertake that project.

 **1\. Installation**

  
I've found adding the repository via some of the GUI apps to be a bit troublesome at times, and since Synaptic is no longer included, it's easiest to just open a terminal, add the repository, and install Grub Customizer:

  1. Terminal:  
Add the repository to your system. The following commands will add the repository, import the security key, update the list of available packages and install Grub Customizer.
    * Open a terminal  
Applications > Accessories > Terminal
    * Install Grub Customizer  


Code:
        
                sudo add-apt-repository ppa:danielrichter2007/grub-customizer
        sudo apt-get update
        sudo apt-get install grub-customizer

  2. Manual Download from the [Grub Customizer Launchpad site](https://launchpad.net/grub-customizer).   
I don't recommend installing it via this method as other methods will properly install and keep the correct version updated. If manually downloading the package please ensure you choose the correct version.
    * You can get the latest version from <https://launchpad.net/ubuntu-tweak/+download>here.
      * The current version requires python 2.7 or later. Maverick uses python 2.6 and Lucid uses python 2.5.5.
      * If you must or still desire to download the package from the site, Lucid/Maverick users should select an older version to install.
      * Updates will not be automatically available unless the repository is added.



 **2\. Starting Grub-Customizer**

  
Since this application modifies system files you will be asked to enter your password to gain access.

GUI: Applications > System Tools > Grub Customizer

Terminal: _gksu grub-customizer_

 **3\. Main Menu Interface**

  
[Grub.Customizer.main.png](http://ubuntuforums.org/attachment.php?attachmentid=180683&d=1294684047)  
 **Categories**  
Each Grub 2 script in the _/etc/grub.d_ folder which finds operating systems is depicted in an expanded tree view: linux, memtest86+, os-prober, 40_custom, 41_custom, etc.  


  *  **Main:**
    * Scripts are displayed by their name (in numerical order) in the /etc/grub.d folder.
    * Only scripts which deal with operating systems are displayed in the tree. There are no entries for 00_header and 05_header in the tree view.
    * Scripts which are active are displayed with a filled orange tick box.
    * Scripts which are currently not executable are present but unticked.
    * If the main category title is unticked, the subsections are not included in the Grub menu, even if selected.
  *  **Sub Sections:**
    * linux - The 10_linux script. Listings of your primary Ubuntu OS kernels.
    * memtest86+ - The 20_memtest86+ script.
    * os-prober - The 30_os-prober script. Finds and displays other operating systems, including Windows and linux systems installed on other partitions.
    * custom - In a default installation, the first 'custom' refers to 40_custom, and the second 'custom' refers to 41_custom.

  
 **4\. Making Changes** (from Main Page)  


  *  **Removing / Hiding Entries**
    * Hide An Entire Section: Untick the main header ( _linux, os-prober_ , etc)
      * Example: Unticking _os-prober_ will disable the script and remove all entries normally found by it - Windows, other Ubuntu installations, etc. Even if the entries within the subsection are enabled, they will not be displayed.
      * Hide Specific Entries: Untick the entry
        * Example: Unticking _Ubuntu, with 2.6.35-24-generic_ will remove that specific entry in the Grub 2 menu.
  *  **Freezing Entries (new Entries)**
    * Unticking "new Entries" prevents the addition of any new Grub 2 menu entries for that section. New options found during updates may be included in the tree view but will not be selected by default.
      * If a new item is found by an enabled script, it will _not_ be added to the Grub 2 menu.
    * Example: If 'new Entries' in 'linux' is deselected, when a new kernel is installed on the main system it will not appear in the menu.
  *  **Adding Entries**
    * Tick the applicable entry.
    * Selecting a main category will enable the script.
    * Selecting an item within a main category will add it to the Grub 2 menu _if it's parent is enabled_.
  *  **Renaming Entries**
    * Double-click a menu title to enable the editing mode. Type the new title and click elsewhere on the page to complete the edit.
  *  **Moving Entries**
    * To move a main section, highlight the entry and use the Up/Dn arrows on the main menu to change the menu order. Moving a main category will move all its submenus.
      * Example: If you want Windows to appear before the main Ubuntu entries, move _os-prober_ to the top of the list.
    * To move a title up or down within a subsection, highlight the entry and use the Up/Dn arrows on the main menu to change the menu order.
      * A titles can only be moved within its own subsection.

  
 **5\. Preferences Tabs** (Edit > Preferences)

  *  **General**  
[Grub.Customizer.settings.General.png](http://ubuntuforums.org/attachment.php?attachmentid=180691&d=1294692196)  
Initial display options such as whether the menu is shown, which menu entry is highlighted, and what kernel options to add to the instructions.
    * Default entry
      *  **How to Specify the Default Entry by Name:**
        * 'default entry' > 'predefined': Click on "Entry 1", on the expanded selection screen choose the exact title from the right column.
        * This works for Grub 1.98. Grub 1.99/Natty introduces submenus and using exact titles will change. I don't know if GC has accounted for this change yet. In the meantime, you can refer to this link on how to manually add a default entry from a submenu: [Grub 1.99 Submenus](http://ubuntuforums.org/showthread.php?p=10720316#post10720316)
    * visibility - Menu display, other OS selections, and timeout.
    * kernel parameters - Add options such as _nomodeset, noapic, quiet, splash, etc_
  *  **Appearance**  
[Grub.Customizer.settings.Appearance.png](http://ubuntuforums.org/attachment.php?attachmentid=180689&d=1294692196)  
Menu eye candy - resolutions, colors, background images.
    * custom resolution
    * menu colors
    * background image
  *  **Advanced**  
[Grub.Customizer.settings.Appearance.png](http://ubuntuforums.org/attachment.php?attachmentid=180689&d=1294692196)  
Selection of options normally found in the _/etc/default/grub_ file. The user can enable/disable individual items and can modify the existing entries by double-clicking the 'value' column and entering the desired value.
    * The only items listed in this section are those which currently exist in _/etc/default/grub_. The user can enable items displayed here, but cannot add items which do not already exist in the file.
    * Ticked items are included in the Grub 2 configuration file.
    * Unticked items will not be included in the Grub 2 configuration file. Unticking an entry places a # (comment) symbol at the start of the line in _/etc/default/grub_

  
 **6\. Partition Selector**  
Accessed via the main menu "File" option, GC allows the user to select a partition on which to perform operations. This allows the user to accomplish tasks on another OS's partition via the _chroot_ process. This is useful when you are running one OS but use another OS's Grub run the boot process. 

For instance, running "update-grub" will update the menu on the current OS. If another partition's Grub 2 is controlling things, no change in the boot menu will occur unless the change is made within the controlling Grub's partition. This option allows you to make these changes without booting the controlling OS.

 **7\. Returning to Grub 2 Defaults**

Daniel Richter describes how to revert to the normal files in his [_Grub Customizer FAQ_](https://answers.launchpad.net/grub-customizer/+faq/1355). 

  
Note: Original files which Grub Customizer will modify are moved to the _/etc/grub.d/proxifiedScripts_ folder, with the leading numeric designation removed.

The _/etc/grub.d/proxifiedScripts_ and _/etc/grub.d/bin_ folders, and any *_proxy files are only created if a Grub 2 script has to be modified. If only changes normally made to _/etc/default/grub_ are invoked by Grub Customizer, the following won't be necessary.

To restore the normal Grub 2 control of the boot menu:

  * Remove the _/etc/grub.d/bin_ folder
  * Move the contents of _/etc/grub.d/proxifiedScritps_ back to the _/etc/grub.d_ folder.
    * Any files moved back need to be renamed to the original name.
    *  _linux_ back to _10_linux_ , _os-prober_ back to _30_os-prober_ , etc.
  * Remove the _/etc/grub.d/proxifiedScipts_ folder  once it is empty.
  * Check the settings in _/etc/default/grub_ and make any desired changes (default kernel, timeout, etc).
  * Run "sudo update-grub".



<http://ubuntuforums.org/showthread.php?p=10340183#post10340183>

See others at:

<http://ubuntuforums.org/showthread.php?t=1287602>

