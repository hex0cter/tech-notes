# [Open new instance for each excel sheet](http://forums.whirlpool.net.au/archive/850718)


This worked for Windows 7, excel 2010:

In Windows 7 you have to edit the registry to remove DDE completely.
You can first try checking the "Ignore other applications that use Dynamic Data Exchange (DDE)" box in Excel -> Excel Options -> Advanced. This alone might work for some – but generally it just results in an error message.

So the more comprehensive way is to:

Open regedit, browse to `HKEY_CLASSES_ROOT\Excel.Sheet.8\shell\Open`

Delete the ddeexec key, (or just rename it)

Then click on the "command" key and replace the /e on the end of the (Default) and command strings with "%1"

 **Quotes around %1 are important.**

After the change, the lines should look like this:

```
(Default) REG_SZ "C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE" "%1"
command REG_MULTI_SZ xb'BV5!!!!!!!!!MKKSkEXCELFiles>VijqBof(Y8'w!FId1gLQ "%1"
```

 **Then do the same for Excel.Sheet.12**

Now Both .xls and .xlsx should open in new windows with no errors.
