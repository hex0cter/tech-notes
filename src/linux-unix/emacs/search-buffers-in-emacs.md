# [Search Buffers in Emacs](http://www.emacswiki.org/emacs/SearchBuffers)

Search through multiple (possibly all) buffers.
* Multi-Occur – batch search by regexp across any number of buffers, using a single regexp
* IciclesSearch – incrementally search (and replace) across any number of buffers or files, possibly using multiple regexps
* search-buffers – XEmacs only, included in edit-utils
* far-search-mode – incrementally search by regexp in all buffers
* moccur.el – ‘occur’ in all buffers
* color-moccur.el – extension of moccur – search files like `grep(-find)’ without ‘grep’ or ‘find’ commands – demo (flash)
* moccur-edit.el – with moccur-edit.el, you can edit the results in place after using ‘color-moccur’ – demo (flash)
* grep-buffers – grep-buffers.el
* igrep-visited-files – igrep.el
* GlobRep – edit ‘grep’ output to perform replacements on files

## Multi-Occur

Built into Emacs 23, this command can search any files or buffers matching a regexp for a particular regexp.

To select buffers to search individually:

To select files to search by regexp:


      M-x multi-occur-in-matching-buffers

To select buffers to search by regexp:


      C-u M-x multi-occur-in-matching-buffers

## Search and Replace Using Icicles

You can use [Icicles](http://www.emacswiki.org/emacs/Icicles) to search any number of buffers – pick the buffers individually using [completion](http://www.emacswiki.org/emacs/Completion#completion), or pick all that match a regexp, or pick all. Similarly, you can pick files to open and search.

You can use multiple regexps for searching and change regexps on the fly (incrementally). See [Icicles - Search Commands, Overview](http://www.emacswiki.org/emacs/Icicles_-_Search_Commands%2c_Overview). Search-and-replace across multiple buffers or files, with complex replacement possibilities – see [Icicles - Search-And-Replace](http://www.emacswiki.org/emacs/Icicles_-_Search-And-Replace).

## search-buffers

M-x list-matches-in-buffers

Search all buffers for REGEXP and present matching lines like grep.

Sample


     search-buffers.el<elisp>:53:(defvar search-buffers-current-extent nil)
     search-buffers.el<elisp>:55:(defvar search-buffers-highlight-xtnt nil)
     search-buffers.el<elisp>:57:(defvar search-buffer nil)
     search-buffers.el<elisp>:60:(defun list-matches-in-buffers (regexp)

Screenshot

## moccur

M-x moccur

Search all buffers that have a file name associated with them and present matching lines. And C-c C-c gets you to the occurence.

Sample


     Lines matching def.+
     Buffer: moccur.el<mylisp> File: d:/akihisa/mylisp/moccur.el

      49 (defface moccur-face
      60 (defvar moccur-overlays nil)
      61 (defvar moccur-regexp "")

M-x moccur
    Search all buffers that have a file name associated with them
C-u M-x moccur
    Search all file buffers and not file buffers
M-x dmoccur
    Search files in a directory like grep
C-u M-x dmoccur
    Search files in the directory which is setted in your .emacs
dired-do-moccur, Buffer-menu-moccur,ibuffer-do-occur
    can search from dired,buffer-menu,ibuffer

moccur is basis of color-moccur. You can search all buffers and matched line is displayed to other window.

Screenshot, searching for “setq match”:

moccur-split-word : non-nil means to input word splited by space. You can search “(setq ov (make-overlay (match-beginning 0)” by “setq match” or “match setq”. You don’t need to input complicated regexp.

![http://www.bookshelf.jp/emacswiki/moccur.png](http://www.bookshelf.jp/emacswiki/moccur.png)

Upperside:Search result buffer, lowerside:matched file buffer

### moccur-edit

moccur-edit allows you to edit files by just editing the **Moccur** buffer of color-moccur.

Screenshot, where “ov” is replaced with “moccur-ov”:

![http://www.bookshelf.jp/emacswiki/moccur-edit.png](http://www.bookshelf.jp/emacswiki/moccur-edit.png)

## grep-buffers

M-x grep-buffers

This code lets you grep through all loaded buffers that have a file associated with them. It’s similar to ‘moccur’ and it’s many variants, but uses the standard compilation-mode interface, i.e. next-error, previous-error, etc. all work.

I have the same problem with _symbol-near-point_. Replacing it with _symbol-at-point_ fixes problem. I’m using Emacs 22. -Petteri

Problem should be fixed now. -[ScottFrazer](http://www.emacswiki.org/emacs/ScottFrazer)

## moccur-grep and moccur-grep-find

grep(-find) by elisp

M-x moccur-grep and input directory, regexp, filemask

In [MiniBuffer](http://www.emacswiki.org/emacs/MiniBuffer), input directory

In minibuffer, input regexp and filemask. Last word is filemask.


     Input Regexp and FileMask: gnus el$

M-x moccur-grep-find

How to use is same to M-x moccur-grep.

## offby1's crude but effective method


     (defun search-all-buffers (regexp)
       (interactive "sRegexp: ")
       (multi-occur-in-matching-buffers "." regexp t))
     (global-set-key [f7] 'search-all-buffers)

[CategorySearchAndReplace](http://www.emacswiki.org/emacs/CategorySearchAndReplace)
