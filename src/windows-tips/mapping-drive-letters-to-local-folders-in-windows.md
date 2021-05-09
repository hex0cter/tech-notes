
date: November 29, 2005, 7:01pm PST
author(s): Greg Shultz

# [Mapping/mounting drive letters to local folders in Windows](http://www.techrepublic.com/article/mapping-drive-letters-to-local-folders-in-windows-xp/5975262)

If you regularly work with files stored in shared folders on a Windows XP network, chances are that you've used Windows' Map Network Drive command to map a drive letter to that folder. Wouldn't it be nice if you could map a drive letter to a nested folder on your hard disk? Then, you could access nested subfolders just as easily as you can access shared folders on the network.

Fortunately, you can do just that. Unbeknownst to most Windows users, there's an old DOS command called Subst that's designed to associate a drive letter with any local folder—and it's still a viable tool in Windows XP. Here's how to use the Subst command:

  1. Open a Command Prompt window.
  2. Type the following command and press [Enter]:




    subst x: C:\{pathname}\foldername}

In the command, _x:_ is any available drive letter and { _pathname_ }\ _foldername_ } is the complete path to your selected folder. For example:


    subst x: C:\cygwin-linux\home\handanie\workplace\RAT-TVP\fixtures\apduwrapper

Now, instead of typing the full path, you can reach the Drivers folder by accessing drive x: in Windows Explorer.

---
