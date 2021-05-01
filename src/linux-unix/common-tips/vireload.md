# [How do I reload/re-edit the current file with vim?](http://stevemorin.blogspot.com/2005/11/vim-vi-how-to-reload-file-your-editing.html)

You can use the ":edit" command, without specifying a file name, to reloadthe current file. If you have made modifications to the file, you can use":edit!" to force the reload of the current file (you will lose your modifications).

For more information, read

```
:help :edit
:help :edit!
:help 'confirm'
```
