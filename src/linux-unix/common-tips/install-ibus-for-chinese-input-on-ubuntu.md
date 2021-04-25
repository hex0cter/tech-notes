
date: None  
author(s): None  

# [Install iBus for Chinese input on Ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/install-ibus-for-chinese-input-on-ubuntu)

nstalling Chinese fonts and input methods in Ubuntu 12 or 13 is very similar to my instructions for recent versions, but you'll notice some differences in these screen shots.

 **Note: if you cannot run the Unity interface,** use my instructions for [Ubuntu 10 Chinese setup, ](http://pinyinjoe.com/linux/ubuntu-10-chinese-setup.htm)log into the Gnome interface, and try to install proprietary drivers for your graphics card.

Ubuntu should automatically present this option to you shortly after your first login, if it finds a card that can use such drivers. Then you may be able to restart and boot into Unity.

![No need to install a fully localized Chinese Ubuntu desktop. Just click English](http://pinyinjoe.com/images/ubuntu/1104/Ubuntu-11-install-English-display-language.jpg) **At the installation Welcome screen** you will be asked to pick a display language, as shown on the right here. --->

 _It is not necessary to use a Chinese language desktop if you don't want to,_ because Chinese input methods are available in any locale. You can select "English" or another language now, and use Chinese menus later if you wish.

After the installation is complete and you have logged in, you will find more than one way to get into the Language Support control panel. One is to click the menu at the upper right of the screen, and select System Settings:

![Ubuntu 12 Settings menu](http://pinyinjoe.com/images/ubuntu/1204/systemsettings.jpg)

That will bring up the System Settings panel, where you'll find Language Support:

![Ubuntu 12 : System Settings : Language Support](http://pinyinjoe.com/images/ubuntu/1204/Ubuntu-12-system-settings-language-support.jpg)

Another way to find Language Support is to click the Dash icon at the upper left (or press the Ubuntu (Windows) key on your keyboard), and type "Language" into the search box:

![Ubuntu Dash : search for Language Support](http://pinyinjoe.com/images/ubuntu/1204/dash-language-support-575px.jpg)

Double-click the Language Support icon to open that panel. For "Keyboard input method system", select "ibus" from the menu. (For info on adding the old SCIM framework to this menu, see the [input methods page](http://pinyinjoe.com/linux/ubuntu-10-chinese-input-pinyin-chewing.htm).) Then click the "Install / Remove Languages..." button:

![Ubuntu Language Support panel](http://pinyinjoe.com/images/ubuntu/1204/language-support.jpg)

After clicking that button you will see the Installed Languages panel. Scroll to and click the languages you want to install:

![Ubuntu Installed Languages panel : installing Chinese](http://pinyinjoe.com/images/ubuntu/1204/installed-languages.jpg)

After the file installation process is complete, log out and log back in:

![Ubuntu 11 logout](http://pinyinjoe.com/images/ubuntu/1204/logout.jpg)

Then you will see a friendly keyboard icon on the top panel:

![Ubuntu input method keyboard menu icon](http://pinyinjoe.com/images/ubuntu/1204/notice-keyboard.jpg)

If it's not there don't worry...yet. IBus does that sometimes. Later you can set the floating language panel to always display, and you will be able to switch input methods using <Alt-Shift> if nothing else.

Note: if the keyboard icon **never** appears for you (even after logout/login as mentioned above) open Terminal and enter this:

>  _im-switch -s ibus_

Then logout and login again. You should see the keyboard icon now.

 **There is one more step required** to set up at least one Chinese input method:

> [![Ubuntu Chinese IMEs](http://pinyinjoe.com/images/ubuntu/1010/IME-icons-7.jpg)](http://pinyinjoe.com/linux/ubuntu-10-chinese-input-pinyin-chewing.htm)

