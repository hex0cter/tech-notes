# [Take control of startup and login items on OS X](http://www.macworld.com/article/2047747/take-control-of-startup-and-login-items.html)

When you turn on your Mac, various apps, add-ons (such as menu extras), and invisible background processes open by themselves. Usually these automated actions are exactly what you want, but you may sometimes see items running—either visibly or according to a listing in Activity Monitor (located in /Applications/Utilities)—that you don’t recall adding yourself. Where do they come from? Because such items can increase your Mac’s startup time (and may decrease its performance), you’ll want your machine to load only items that are useful to you. Here’s a quick primer on the various kinds of startup and login items and how to manage them.

## Login items

Open the _Users & Groups_ pane of System Preferences and click the _Login Items_ tab, and you’ll see a list of apps (and even files and folders) that open every time you log in. (This list is different for each user account on your Mac.) More often than not, items appear in this list because apps added them to it. Most apps that do so ask you for permission first or offer an ‘Open at Login’ checkbox for you to check, but not all are so well behaved. In any case, you can add an item to the list manually by clicking the plus sign (+) button, or remove an item by selecting it and clicking the minus sign (-) button.

![](http://images.techhive.com/images/article/2013/08/loginitems-100052043-large.png)Everything in the Login Items list—whether added by you or by an app—opens automatically when you log in.

## Startup items

Earlier versions of OS X relied on two folders—/Library/StartupItems and /System/Library/StartupItems—to hold items designated to load when you start your Mac. Apple now discourages the use of startup items, but some programs (mostly older apps) still use this mechanism. Normally your /System/Library/StartupItems folder should be empty; but if it contains something that you don’t use anymore, you can drag the unwanted item to the Trash to prevent it from loading automatically the next time you start your Mac.

## Launch daemons and agents

Since OS X 10.4 Tiger, Apple has given developers another mechanism for launching items automatically: [launch daemons and agents](https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html), controlled by the[`launchd` process](http://en.wikipedia.org/wiki/Launchd). This approach provides more flexibility than either login items or startup items, but it is less transparent to users.

 **Behind the UNIX curtain:** Instead of opening apps directly, launchd loads specially formatted .plist documents (XML preference files) that specify what should launch and under what circumstances. Sometimes these launch items run constantly in the background, sometimes they run at scheduled intervals, and sometimes they run as needed—for example, in response to an event such as a change in a certain file or folder—and then quit.

The .plist files that launchd uses can occupy any of five folders, and their location determines when the items load and with what privileges:

  * Items in /Library/LaunchDaemons and /System/Library/LaunchDaemons load when your Mac starts up, and run as the root user.

  * Items in /Library/LaunchAgents and /System/Library/LaunchAgents load when _any_ user logs in, and run as that user.

  * Items in /Users/ _your-username_ /Library/LaunchAgents load only when that particular user logs in, and run as that user.




 **Keep your hands off of some:** Of those five folders, the two located in the /System folder (/System/Library/LaunchDaemons and /System/Library/LaunchAgents) are for components included as part of OS X, and you should resist the temptation to remove or alter them—they’re essential to keep your Mac running correctly.

 **Modify others as you like:** As for the items in the other folders, feel free to browse through them and see what’s there. You _can_ modify them—for instance, to disable them or to change how often they run—but before you do, you should understand a few things about how they work.

When you start your Mac or log in, the launch items in the relevant folders are _loaded_ (that is, registered with the system) unless they have a Disabled flag set. Thereafter, their instructions will be carried out until you restart, even if you drag the launch item to the Trash. To see a list of all the currently loaded launch items on your Mac, open _Terminal_ (in /Applications/Utilities) and type `launchctl list` and then press Return.

If you want to stop a launch item from running without your having to restart, open _Terminal_ and type `launchctl unload `followed by a space and the full path to the launch item. (An easy way to add an item’s full path is to drag it to the Terminal window.) For example, take this code:


     launchctl unload ~/Library/LaunchAgents/com.apple.FolderActions.enabled.plist

It unloads the launch agent that enables AppleScript folder actions. Repeat the command with `load` instead of `unload` to turn it back on.

Because most launch items run on a schedule or on demand, and because any of them could be disabled, the fact that something is present in one folder doesn’t necessarily mean the process it governs is currently running. To see what’s running at the moment, open Activity Monitor—but bear in mind that the name of a given process as shown in Activity Monitor might not resemble the name of the .plist file that tells OS X to launch it.

 **Try a helpful utility:** For seeing what launch items do—or for enabling or disabling them, or for deleting them (except those in the /System folder)—without any futzing in Terminal, my favorite tool is Peter Borg’s $10 [Lingon X](http://www.peterborgapps.com/lingon/). There’s also a less-expensive [Lingon 3](http://target.georiot.com/Proxy.ashx?TSID=14156&GR_URL=https%3A%2F%2Fitunes.apple.com%2Fgb%2Fapp%2Flingon-3%2Fid450201424%3Fls%3D1%26mt%3D12), but it can do its work only on the current user’s launch items, which makes it much less powerful. Lingon X provides a friendly graphical interface rather than an inscrutable XML file, although you’ll still need a little geek mojo to understand some of its capabilities.

![](http://images.techhive.com/images/article/2013/08/lingon-100052044-large.png) Lingon X provides a user-friendly interface for viewing and editing launch items.

## Spontaneously reopening apps at startup

![](http://images.techhive.com/images/article/2013/08/resume-100052042-medium.png)

If the checkbox is selected (as shown here) when you shut down or restart, whatever apps are open at that time will reopen automatically.

By default, when you restart your Mac, OS X 10.7 Lion and later reopen whatever applications and documents were open when you shut down. Whether this happens depends on the decision you make when you choose Restart or Shut Down from the Apple menu. In the dialog box that appears, if the ‘Reopen windows when logging back in’ checkbox is selected, the items will reopen; if not, not. However, you must make this decision before you shut down or restart, and it’s all or nothing—if you want to open only specific items, you’ll have to uncheck this box and add the items that you want to open at login to Login Items.

## Other explanations for mystery processes

Although the methods I’ve mentioned so far are the most common ways to launch apps automatically in OS X, they aren’t the only ones. If you have a mystery process that you can’t track down in any of these places, it could also be one of these:

 **A kernel extension:** Kernel extensions, or kexts, live in /System/Library/Extensions and load at startup. They provide low-level features such as processing audio and adding support for peripherals. Most kexts on your Mac are part of OS X. The safest way to remove a third-party kext is to run an uninstaller provided by the developer.

 **A cron job:** Cron is a Unix scheduling utility built into OS X. The easiest way to view and edit cron jobs without using Terminal is to download the free [Cronnix](https://code.google.com/p/cronnix/)utility by Sven A. Schmidt.

 **A login script:** [Login scripts](https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CustomLogin.html), like startup items, were used in older versions of OS X but are now deprecated.
