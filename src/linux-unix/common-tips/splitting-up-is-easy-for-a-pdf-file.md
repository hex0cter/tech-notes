# [Splitting up is easy for a PDF file](http://linuxcommando.blogspot.se/2013/02/splitting-up-is-easy-for-pdf-file.html)

Occasionally, I needed to extract some pages from a multi-page pdf document. Suppose you have a 6-page pdf document named _myoldfile.pdf_. You want to extract into a new pdf file _mynewfile.pdf_ containing only pages 1 and 2, 4 and 5 from _myoldfile.pdf_.

I did exactly that using _pdktk_ , a command-line tool.

If _pdftk_ is not already installed, install it like this on a Debian or Ubuntu-based computer.

```
$ sudo apt-get update
$ sudo apt-get install pdftk
```

Then, to make a new pdf with just pages 1, 2, 4, and 5 from the old pdf, do this:

```
$ pdftk myoldfile.pdf cat 1 2 4 5 output mynewfile.pdf
```

Note that _cat_ and output are special _pdftk_ keywords. _cat_ specifies the operation to perform on the input file. _output_ signals that what follows is the name of the output pdf file.

You can specify page ranges like this:

```
$ pdftk myoldfile.pdf cat 1-2 4-5 output mynewfile.pdf
```

_pdftk_ has a few more tricks in its back pocket. For example, you can specify a _burst_ operation to split each page in the input file into a separate output file.

```
$ pdftk myoldfile.pdf burst
```

By default, the output files are named _pg_0001.pdf_ , _pg_0002.pdf_ , etc.

 _pdftk_ is also capable of merging multiple pdf files into one pdf.

```
$ pdftk pg_0001.pdf pg_0002.pdf pg_0004.pdf pg_0005.pdf output mynewfile.pdf
```

That would merge the files corresponding to the first, second, fourth and fifth pages into a single output pdf.

If you know of another easy way to split up pages from a pdf file, please tell us in a comment. Much appreciated.
