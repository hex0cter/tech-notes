# [Create zip file on linux](http://kb.iu.edu/data/aeqx.html)


In Unix, how do I create or decompress zip files?

To create a zip file, at the Unix prompt, enter:
```
zip filename inputfile1 inputfile2
```

Replace filename with the name you want to give the zip file. The .zip extension is automatically appended to the end of the filename. Replace inputfile1 and inputfile2 with the names of the files you wish to include in the zip archive. You can include any number of files here, or you may use an asterisk (*) to include all files in the current directory.

To include the contents of a directory or directories in a zip archive, use the -r flag:
```
zip -r filename directory
```

Replace directory with the name of the directory you want to include. This will create the archive filename.zip that contains the files and subdirectories of directory.

Files created by zip can normally be decoded by programs such as WinZip and StuffIt Expander.

To decompress a zip file in Unix, use the unzip command. At the Unix prompt, enter:
```
unzip filename
```

Replace filename with the name of the zip archive.For more information about zip and unzip, see their manual pages:
```
man zip
man unzip
```
