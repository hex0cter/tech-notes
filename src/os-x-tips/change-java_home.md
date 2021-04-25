
date: None  
author(s): None  

# [Three ways to update JAVA_HOME on Mac OS X - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/os-x-tips/change-java_home)

1\.  vi ~/Library/LaunchAgents/environment.plist

`<?xml version="1.0" encoding="UTF-8"?>`

`<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">`

`<plist version="1.0">`

`<dict>`

` ``<key>Label</key>`

` ``<string>my.startup</string>`

` ``<key>ProgramArguments</key>`

` ``<array>`

` ``<string>sh</string>`

` ``<string>-c</string>`

` ``<string>`

` ``launchctl setenv JAVA_HOME /Library/Java/JavaVirtualMachines/jdk1.8.0_60.jdk/Contents/Home`

` ``launchctl setenv PATH /Library/Java/JavaVirtualMachines/jdk1.8.0_60.jdk/Contents/Home/bin:$PATH`

` ``</string>`

` ``</array>`

` ``<key>RunAtLoad</key>`

` ``<true/>`

`</dict>`

`</plist>`

  


2\. vi .MacOSX/environment.plist

`<?xml version="1.0" encoding="UTF-8"?>`

`<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">`

`<plist version="1.0">`

`<dict>`

`<key>JAVA_HOME</key>`

`<string>/Library/Java/JavaVirtualMachines/jdk1.8.0_60.jdk/Contents/Home</string>`

`</dict>`

`</plist>`

3\. edit shell rc file  
  
---

