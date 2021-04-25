
date: None  
author(s): None  

# [File can't be moved by root on OS X - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/os-x-tips/file-can-t-be-moved-by-root-on-os-x)

http://apple.stackexchange.com/questions/101328/file-cant-be-moved-by-root-on-os-x

| 

up vote10down voteaccepted

| 

Sounds like the file is locked to me, which is why the uchg attribute is appearing. You should be able to use the following command to remove the locked attribute:
    
    
    chflags nouchg file
    

or right-click the file in the Finder, click "Get Info" then uncheck the "Locked" checkbox

| | 

answered Sep 9 '13 at 19:25

[![](https://i.stack.imgur.com/fLTXE.jpg?s=32&g=1)](http://apple.stackexchange.com/users/18202/binarybob)  
  
---|---  
|   
  
| 

For people stumbling upon this in an OS X 10.11+ era (El Capitan or newer): [Apple has added a whole new layer of security in OS X](https://apple.stackexchange.com/questions/193368/what-is-the-rootless-feature-in-el-capitan-really). They have taken away some privileges from root. The file you are trying to modify has a `restricted` flag. Only `restricted` processes which are signed by Apple will be able to modify these files. However, you can disable this security system by booting in recovery mode and disabling it in a Terminal by doing: `csrutil disable`.

Alternatively, try booting in a Linux environment with HFS+ support to change the file.  
  
---|---  
  


https://oliverdowling.com.au/2014/03/28/java-se-8-on-mac-os-x/

  * Mac OS X 10.11 El Capitan is currently a Developer Preview. I would recommend against running this as your main operating system.
  * I’ve read that Java 6 is temporarily unavailable in El Capitan.
  * A new mode called “Rootless” is enabled by default, which will prevent you from modifying System files. You can disable it by opening Terminal, running

1

| 

`sudo` `nvram boot-args=”rootless=0″`  
  
---|---  
  
and restarting your computer.

  * You can disable Rootless mode later with:



