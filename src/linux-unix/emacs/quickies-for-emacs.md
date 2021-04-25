
date: None  
author(s): None  

# [Quickies for emacs - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/quickies-for-emacs)

<http://borkware.com/quickies/one?topic=emacs>

  * **Disabling control-Z from backgrounding emacs** [[permalink](http://borkware.com/quickies/single?id=15)]   
I find emacs' control-Z behavior to be pretty annoying (it backgrounds the program if you're in a shell, or hides the window if you're in X). Add this to your `.emacs` file:  
`(global-set-key "C-Z" nil)`
  *  **Fixing "no job control in this shell"** [[permalink](http://borkware.com/quickies/single?id=57)] Emacs in Mac OS X 10.1.3 (and other versions) has an annoying habit of having broken shells when you do M-x shell. You get an error like "Inappropriate ioctl for device, no job control in this shell", which makes interrupting or backgrounding programs in shell mode impossible. Domo-kun gave me a one-line patch to the emacs source:

`#define DONT_REOPEN_PTY`

  
. Add that to darwin.h and build emacs. You can get the emacs source from the [Darwin projects page](http://www.opensource.apple.com/projects/darwin/1.4/projects.html). If you'd like a binary, drop [us some mail.](mailto:gimmemacs@borkware.com)
  *  **Fixing emacs C mode indenting** [[permalink](http://borkware.com/quickies/single?id=73)]   
Here's a way to change the C indenting style to a major style, and override some of the pre-set values (like how emacs 21 changed the bsd indent level from 4 to 8. Gee thanks guys):
    
        (setq c-default-style "bsd"
          c-basic-offset 4)

  *  **Fixing emacs backspace in screen** [[permalink](http://borkware.com/quickies/single?id=325)]   
When running emacs insde of screen, screen helpfully turns the backspace/delete key into "^[[3~", which gets turned into a forward-delete. Unfortunately, just bashing `deletechar` into `backward-delete-char-untabify` causes backspace in incremental search to cancel the search, which is annoying.

One option is to set the TERM env var to rxvt:
    
        % setenv TERM rxvt

Before cranking up screen.
  *  **Macro recording** [[permalink](http://borkware.com/quickies/single?id=328)]   
`C-x (` : start recording keyboard macro  
`C-x )` : stop recording keyboard macro  
`C-x e` : replay current keyboard macro
  *  **Make emacs indent code with spaces instead of tabs** [[permalink](http://borkware.com/quickies/single?id=145)]   
Personally, I prefer emacs' default indentation with a mixture of tabs and spaces. If you're working on a project or for a client that requires indentation with spaces, add this to your `.emacs` file. This will make spaces the indent character, and use 4 spaces per indent level, for C, C++, and Objective C:
    
        (setq c-mode-hook
        (function (lambda ()
                    (setq indent-tabs-mode nil)
                    (setq c-indent-level 4))))
    (setq objc-mode-hook
        (function (lambda ()
                    (setq indent-tabs-mode nil)
                    (setq c-indent-level 4))))
    (setq c++-mode-hook
        (function (lambda ()
                    (setq indent-tabs-mode nil)
                    (setq c-indent-level 4))))
    

  * **Resetting shell mode's idea of the current working directory** [[permalink](http://borkware.com/quickies/single?id=72)]   
Sometimes the shell mode will get confused as to what the current working directory is (like if you use aliases to move to a new directory, or if you use the conveniences like `!$`). `M-x dirs` will tell the shell buffer to figure out what the current working directory is.
  *  **Restrict editing to the region** [[permalink](http://borkware.com/quickies/single?id=236)]   
`M-x narrow-to-region`

Hides everything not in the current region.

  *  **Revisiting / reloading a file in emacs** [[permalink](http://borkware.com/quickies/single?id=104)]   
The `$Id: $` tags for CVS are nice, but it can be a pain when you're doing lots of checkins and have to re-load the file each time. You can either execute `M-x revert-bufer` or bind that to a key, or else use a trick by doing `C-x C-v` which invokes `find-alternate-file`, but just so happens to have the current buffer name, so you just have to do `C-x C-v RET`
  *  **Running shell command pasting result back into the buffer** [[permalink](http://borkware.com/quickies/single?id=366)]   
So to run `uuidgen`, for instance:

`C-U M-!` ret `uuidgen` ret

  *  **Scroll line with cursor to the top of the window** [[permalink](http://borkware.com/quickies/single?id=116)]   
`C-U 0 C-L`

(you can put in another number besides zero to scroll the line with the cursor to that particular line in the buffer)

  *  **Setting variables when loading a file** [[permalink](http://borkware.com/quickies/single?id=316)]   
So say you're working on a project with two-space indents, but most of your other work happens with four-space indents. If the two-space crowd is amenable, add this to the bottom of the file:
    
        /* For the emacs weenies in the crowd.
    Local Variables:
       c-basic-offset: 2
    End:
    */

  *  **Showing current column position** [[permalink](http://borkware.com/quickies/single?id=115)]   
`M-x column-number-mode`
  *  **Toggling read-only mode in a buffer** [[permalink](http://borkware.com/quickies/single?id=16)]   
`C-X C-Q`
  *  **Turning off command highlighting in shell mode** [[permalink](http://borkware.com/quickies/single?id=71)]   
Emacs 21, which comes with Mac OS X 10.2, "helpfully" puts into bold the commands you execute in the shell. This drives me nuts, so I figured out how to turn it off. Add this to your .emacs file:

`(setq comint-highlight-input nil)`

  *  **Turning off font-lock mode everywhere** [[permalink](http://borkware.com/quickies/single?id=336)]   
`(global-font-lock-mode -1)`
  *  **Turning off incremental-search highlighting** [[permalink](http://borkware.com/quickies/single?id=70)]   
Emacs 21, which comes with Mac OS X 10.2, has highlighting enabled when doing incremental search (which drives me nuts). You can turn that off by setting this in your .emacs file:

`(setq search-highlight nil)`

You may also need to   
`(setq isearch-lazy-highlight nil)`

To turn off underlining of matching results. Only some OS X installs need this setting.

  *  **Turning off scroll-to-end in shell-mode** [[permalink](http://borkware.com/quickies/single?id=337)]   
`(setq comint-scroll-show-maximum-output nil)`
  *  **Undo within a given region** [[permalink](http://borkware.com/quickies/single?id=117)]   
`C-U C-_`
  *  **Unnarrowing the region** [[permalink](http://borkware.com/quickies/single?id=237)]   
`M-x widen`
  *  **Use only spaces when indenting code** [[permalink](http://borkware.com/quickies/single?id=83)]   
﻿(setq indent-tabs-mode nil)
  *  **Using carriage returns in query-replace / replace-string** [[permalink](http://borkware.com/quickies/single?id=14)]   
Use `C-Q C-J` (control-Q control-J) each time you want to include a carriage return. e.g. to double-space everything

`M-x replace-string RET C-Q C-J RET C-Q C-J C-Q C-J RET`

Or to put "bloogie " at the beginning of every line

`M-x replace-string RET C-Q C-J RET C-Q C-J b l o o g i e SPACE RET`

  *  **compiling emacs .el files** [[permalink](http://borkware.com/quickies/single?id=144)]   
Big emacs `.el` files take a long time to load. You can compile them into `.elc` files by using:  
`% emacs -batch -f batch-byte-compile filename.el`
  *  **emacs registers** [[permalink](http://borkware.com/quickies/single?id=392)]   
Stick something into a register:
    
        (select stuff)
    C-x r x 1
    

where "1" is the register identifier.

Getting stuff out of a register:
    
        C-x r g 1
    



  * **Balance a tag in SGML mode** [[permalink](http://borkware.com/quickies/single?id=390)]   

    
        C-/




