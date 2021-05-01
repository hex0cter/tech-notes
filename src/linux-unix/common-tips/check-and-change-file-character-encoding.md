# [Check and change file character encoding](http://mindspill.net/computing/linux-notes/determine-and-change-file-character-encoding/)


Determine what character encoding is used by a file
```
file -bi [filename]
```
Example output:

```
steph@localhost ~ $ file -bi test.txt
text/plain; charset=us-ascii
```

Change a file's encoding from the command line
To convert the file contents to from ASCII to UTF-8:

```
iconv -f ascii -t utf8 [filename] > [newfilename]
```
Or

```
recode UTF-8 [filename]
```
To convert the file contents from UTF-8 to ASCII:

```
iconv -f utf8 -t ascii [filename]
```
