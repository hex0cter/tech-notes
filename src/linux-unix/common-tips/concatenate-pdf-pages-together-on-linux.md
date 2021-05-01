# [Concatenate pdf pages together on Linux](http://stackoverflow.com/questions/2507766/merge-convert-multiple-pdf-files-into-one-pdf)


```
sudo apt-get install pdftk
pdftk a.pdf c.pdf d.pdf e.pdf g.pdf j.pdf m.pdf cat output - > out.pdf
```
