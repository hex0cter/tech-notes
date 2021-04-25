
date: None  
author(s): None  

# [Open excel in new window instance (very useful when you have dual monitors) - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/open-excel-in-new-window-instance-very-useful-when-you-have-dual-monitors)

Excel can be boring, especial when you have two monitors and want to compare two different files side by side. That's because all files are opened in the same window by default. If you want to open a new instance for each excel sheet, here is how-to:

Open regedit, browse to HKEY_CLASSES_ROOT\Excel.Sheet.8\shell\Open

Delete the ddeexec key, (or just rename it)

Then click on the "command" key and replace the /dde on the end of the (Default) and command strings with "%1"

Quotes around %1 are important.

After the change, the lines should look like this:

`(Default) REG_SZ "C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE" "%1"`

`command REG_MULTI_SZ xb'BV5!!!!!!!!!MKKSkEXCELFiles>VijqBof(Y8'w!FId1gLQ "%1"`

Then do the same for Excel.Sheet.12

Now Both .xls and .xlsx should open in new windows with no errors.

I have tested this on my PC successfully. Hopefully it will also be useful for you!  
  
---

