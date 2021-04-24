date:  2012-11-05 17:59:32
author(s): commonslok

# [android pm命令](https://blog.csdn.net/commonslok/article/details/8150018)

pm命令具体可以查看pm help。今天只想说说pm enable、disable、disable-user PACKAGE_OR_COMPONENT命令！

手机必须具有root权限，禁止你指定的应用命令pm disable PACKAGE_OR_COMPONENT。但是怎么恢复呢？

必然会想到pm enable PACKAGE_OR_COMPONENT，但是很遗憾返回Package PACKAGE_OR_COMPONENT new state: disabled。state还是为disable。

其实只要执行命令pm disable-user PACKAGE_OR_COMPONENT，再执行pm enable PACKAGE_OR_COMPONENT就可以了。返回的是Package Package PACKAGE_OR_COMPONENT new state: enabled。手机就可以重新安装这个程序了，也可以恢复为可启动了！

pm disable-user PACKAGE_OR_COMPONENT可以认为是转为user型的disable。我是这样理解的！记录下！希望对大家有用！


附上pm命令用法：

```bash
usage: pm list packages [-f] [-d] [-e] [-s] [-e] [-u] [FILTER]
       pm list permission-groups
       pm list permissions [-g] [-f] [-d] [-u] [GROUP]
       pm list instrumentation [-f] [TARGET-PACKAGE]
       pm list features
       pm list libraries
       pm path PACKAGE
       pm install [-l] [-r] [-t] [-i INSTALLER_PACKAGE_NAME] [-s] [-f] PATH
       pm uninstall [-k] PACKAGE
       pm clear PACKAGE
       pm enable PACKAGE_OR_COMPONENT
       pm disable PACKAGE_OR_COMPONENT
       pm disable-user PACKAGE_OR_COMPONENT
       pm set-install-location [0/auto] [1/internal] [2/external]
       pm get-install-location
       pm createUser USER_NAME
       pm removeUser USER_ID

pm list packages: prints all packages, optionally only
  those whose package name contains the text in FILTER.  Options:
    -f: see their associated file.
    -d: filter to only show disbled packages.
    -e: filter to only show enabled packages.
    -s: filter to only show system packages.
    -3: filter to only show third party packages.
    -u: also include uninstalled packages.

pm list permission-groups: prints all known permission groups.

pm list permissions: prints all known permissions, optionally only
  those in GROUP.  Options:
    -g: organize by group.
    -f: print all information.
    -s: short summary.
    -d: only list dangerous permissions.
    -u: list only the permissions users will see.

pm list instrumentation: use to list all test packages; optionally
  supply <TARGET-PACKAGE> to list the test packages for a particular
  application.  Options:
    -f: list the .apk file for the test package.

pm list features: prints all features of the system.

pm path: print the path to the .apk of the given PACKAGE.

pm install: installs a package to the system.  Options:
    -l: install the package with FORWARD_LOCK.
    -r: reinstall an exisiting app, keeping its data.
    -t: allow test .apks to be installed.
    -i: specify the installer package name.
    -s: install package on sdcard.
    -f: install package on internal flash.

pm uninstall: removes a package from the system. Options:
    -k: keep the data and cache directories around after package removal.

pm clear: deletes all data associated with a package.

pm enable, disable, disable-user: these commands change the enabled state
  of a given package or component (written as "package/class").

pm get-install-location: returns the current install location.
    0 [auto]: Let system decide the best location
    1 [internal]: Install on internal device storage
    2 [external]: Install on external media

pm set-install-location: changes the default install location.
  NOTE: this is only intended for debugging; using this can cause
  applications to break and other undersireable behavior.
    0 [auto]: Let system decide the best location
    1 [internal]: Install on internal device storage
    2 [external]: Install on external media
root@android:/ # pm uninstall -k com.softel.safebox
pm uninstall -k com.softel.safebox
Success
root@android:/ # pm enable com.softel.safebox
pm enable com.softel.safebox
Package com.softel.safebox new state: disabled
root@android:/ # pm enable com.softel.safebox
pm enable com.softel.safebox
Package com.softel.safebox new state: disabled
root@android:/ # pm disable-user com.softel.safebox
pm disable-user com.softel.safebox
Package com.softel.safebox new state: disabled-user
root@android:/ # pm enable com.softel.safebox
pm enable com.softel.safebox
Package com.softel.safebox new state: enabled
root@android:/ # pm disable-user com.qihoo360.mobilesafe
pm disable-user com.qihoo360.mobilesafe
Package com.qihoo360.mobilesafe new state: disabled-user
root@android:/ # pm enable com.qihoo360.mobilesafe
pm enable com.qihoo360.mobilesafe
Package com.qihoo360.mobilesafe new state: enabled
root@android:/ #
C:\Users\jude>adb shell
shell@android:/ $ pm help
pm help
Error: unknown command 'help'
usage: pm list packages [-f] [-d] [-e] [-s] [-e] [-u] [FILTER]
       pm list permission-groups
       pm list permissions [-g] [-f] [-d] [-u] [GROUP]
       pm list instrumentation [-f] [TARGET-PACKAGE]
       pm list features
       pm list libraries
       pm path PACKAGE
       pm install [-l] [-r] [-t] [-i INSTALLER_PACKAGE_NAME] [-s] [-f] PATH
       pm uninstall [-k] PACKAGE
       pm clear PACKAGE
       pm enable PACKAGE_OR_COMPONENT
       pm disable PACKAGE_OR_COMPONENT
       pm disable-user PACKAGE_OR_COMPONENT
       pm set-install-location [0/auto] [1/internal] [2/external]
       pm get-install-location
       pm createUser USER_NAME
       pm removeUser USER_ID

pm list packages: prints all packages, optionally only
  those whose package name contains the text in FILTER.  Options:
    -f: see their associated file.
    -d: filter to only show disbled packages.
    -e: filter to only show enabled packages.
    -s: filter to only show system packages.
    -3: filter to only show third party packages.
    -u: also include uninstalled packages.

pm list permission-groups: prints all known permission groups.

pm list permissions: prints all known permissions, optionally only
  those in GROUP.  Options:
    -g: organize by group.
    -f: print all information.
    -s: short summary.
    -d: only list dangerous permissions.
    -u: list only the permissions users will see.

pm list instrumentation: use to list all test packages; optionally
  supply <TARGET-PACKAGE> to list the test packages for a particular
  application.  Options:
    -f: list the .apk file for the test package.

pm list features: prints all features of the system.

pm path: print the path to the .apk of the given PACKAGE.

pm install: installs a package to the system.  Options:
    -l: install the package with FORWARD_LOCK.
    -r: reinstall an exisiting app, keeping its data.
    -t: allow test .apks to be installed.
    -i: specify the installer package name.
    -s: install package on sdcard.
    -f: install package on internal flash.

pm uninstall: removes a package from the system. Options:
    -k: keep the data and cache directories around after package removal.

pm clear: deletes all data associated with a package.

pm enable, disable, disable-user: these commands change the enabled state
  of a given package or component (written as "package/class").

pm get-install-location: returns the current install location.
    0 [auto]: Let system decide the best location
    1 [internal]: Install on internal device storage
    2 [external]: Install on external media

pm set-install-location: changes the default install location.
  NOTE: this is only intended for debugging; using this can cause
  applications to break and other undersireable behavior.
    0 [auto]: Let system decide the best location
    1 [internal]: Install on internal device storage
    2 [external]: Install on external media
```
