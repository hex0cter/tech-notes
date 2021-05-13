# [File can't be moved by root on OS X](http://apple.stackexchange.com/questions/101328/file-cant-be-moved-by-root-on-os-x)


Sounds like the file is locked to me, which is why the uchg attribute is appearing. You should be able to use the following command to remove the locked attribute:


    chflags nouchg file


or right-click the file in the Finder, click "Get Info" then uncheck the "Locked" checkbox

<http://apple.stackexchange.com/questions/101328/file-cant-be-moved-by-root-on-os-x>

## Update Jun 2015 regarding El Capitan:

Mac OS X 10.11 El Capitan is currently a Developer Preview. I would recommend against running this as your main operating system.

I’ve read that Java 6 is temporarily unavailable in El Capitan.

A new mode called “Rootless” is enabled by default, which will prevent you from modifying System files. You can disable it by opening Terminal, running

```
sudo nvram boot-args=”rootless=0″
and restarting your computer.
```

You can disable Rootless mode later with:
```
sudo nvram -d boot-args
```

<https://oliverdowling.com.au/2014/03/28/java-se-8-on-mac-os-x/>
