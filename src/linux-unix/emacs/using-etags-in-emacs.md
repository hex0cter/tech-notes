
date: None  
author(s): None  

# [Using etags in emacs - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/using-etags-in-emacs)

1\. Generate tags:

in the root source directory,

` ``find . -name "*.[ch]*" -o -name "*.cpp" -o -name "*.hpp" | xargs etags -a`

2\. Set tags in emacs:

3\. Look up tag definitions:

4\. Move back to last tag position:

Once you have a [tags file](http://www.emacswiki.org/emacs/TagsFile#tags_file), you can follow tags (of functions, variables, macros, whatever) to their definitions. These are the basic commands:

  * ``M-.`’ (`‘find-tag’`) – find a tag, that is, use the Tags file to look up a definition 
  * ``M-*`’ (`‘pop-tag-mark’`) – jump back 
  * `‘tags-search’` – [regexp](http://www.emacswiki.org/emacs/RegularExpression#regexp)-search through the source files indexed by a tags file (a bit like `‘grep’`) 
  * `‘tags-query-replace’` – query-replace through the source files indexed by a tags file 
  * ``M-,`’ (`‘tags-loop-continue’`) – resume `‘tags-search’` or `‘tags-query-replace’` starting at [point](http://www.emacswiki.org/emacs/Point#point) in a source file 
  * `‘tags-apropos’` – list all tags in a tags file that match a regexp 
  * `‘list-tags’` – list all tags defined in a source file



See the Emacs manual, node Tags for more information.

[http://www.emacswiki.org/emacs/EmacsTags](http://www.emacswiki.org/emacs/EmacsTags)  
  
---

