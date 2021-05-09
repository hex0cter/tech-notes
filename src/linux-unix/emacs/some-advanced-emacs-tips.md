
date: 2018-09-09
author(s): Xah Lee

# [Some Advanced Emacs Tips](http://xahlee.org/emacs/emacs_adv_tips.html)


This page is some advanced emacs tips. Advanced, but still commonly needed. If you don't know emacs basics, please see: [Emacs Intermediate Tips](http://xahlee.org/emacs/emacs_int.html).

To call a emacs command named “xyz”, type 【`Alt`+`x` xyz】. In [ErgoEmacs](http://ergoemacs.org/), the key is 【`Alt`+`a`】.

## Search Text, Find ＆ Replace Text

### How to search text?

Press 【`Ctrl`+`s`】 (search-forward), then type your text. Emacs will search as you type. To advance to the next occurrence, press 【`Ctrl`+`s`】 again. To go to previous occurrence, type 【`Ctrl`+`r`】. To stop, press `Enter` or arrow key to leave the cursor there. Or type 【`Ctrl`+`g`】 to return to the spot before search was started.

This command is also under the menu “Edit▸Search”.

To search for the word that is under cursor, type 【`Ctrl`+`s` `Ctrl`+`w`】. This can save you some typing. Also, 【`Ctrl`+`s`】 twice will search your last searched word.

### How to find ＆ replace?

Type 【`Alt`+`%`】 (query-replace). Then, emacs will prompt you for the find string and replace string. Once emacs found a match, you can type `y` to replace, `n` to skip, or `!` to do all replacement without asking. To cancel further finding, type 【`Ctrl`+`g`】.

If you made a mistake, you can cancel by pressing 【`Ctrl`+`g`】. If you want to revert the find ＆ replace you did, you can call undo by pressing 【`Ctrl`+`_`】.

If you want to do find ＆ replace using a regex pattern, type 【`Ctrl`+`Alt`+`%`】 (query-replace-regexp).

If you would like to do replacement on a region, in one shot, without emacs prompting you for each match, you can call “replace-string” or “replace-regexp”.

For detailed turorial on issues of matching or replacing letter cases, see: [Find ＆ Replace with Emacs](http://xahlee.org/emacs/emacs_find_replace.html).

![Find ＆ Replace menus in emacs](http://xahlee.org/emacs/i/emacs_menu_replace.png)

Replace commands are under the menu “Edit▸Replace”

Whatever you do in emacs, don't forget the menu. The menu is very helpful in reminding you the commands or hotkey.

### How to find ＆ replace for all files in a dir?

Type 【`Ctrl`+`x` `d`】 (dired), type dir path, mark the files you want to work on (`m` to mark, `u` to unmark), then press `Q` (dired-do-query-replace-regexp).

Once in dired, you can find the command under the menu “Operate▸Query Replace in Files...”.

For a detailed step-by-step tutorial, see [Interactive Find ＆ Replace String Patterns on Multiple Files](http://xahlee.org/emacs/find_replace_inter.html).

## Editing Related Questions

### How to insert/delete comment?

Select a block of text and press 【`Alt`+`;`】 to make the region into a comment or uncomment.

### How to add a prefix to every line? (such as # or //)

Mark 【`Ctrl`+`Space`】 the beginning of first line and move cursor to the beginning of the last line, then type 【`Ctrl`+`x` `r` `t`】 (string-rectangle), then type what you want to insert. This command can be used to insert a vertical column of string across mulitple lines at any column position, not just at the beginning of lines.

### How to delete the first few n chars of every line?

Mark 【`Ctrl`+`Space`】 the beginning of first line and move cursor to the last line, and move it to the right n chars. Then type 【`Ctrl`+`x` `r` `k`】 (kill-rectangle). This command can be used to delete any rectangular block of text, not just at the beginning of lines.

### How to replace unprintable characters such as tabs or line return chars in Emacs?

Call “query-replace” or “query-replace-regexp”. When you need to insert a Tab, type 【`Ctrl`+`q`】 first, then press `Tab`. Same for inserting a line return.

Here's a short table on how to enter common unprintable chars:

Name| ASCII Code| string notation| Caret Notation| Input method
---|---|---|---|---
horizontal tab| 9| \t| ^I| `Ctrl`+`q` `Ctrl`+`i` or `Ctrl`+`q` `Tab`
line feed| 10| \n| ^J| `Ctrl`+`q` `Ctrl`+`j`
carriage return| 13| \r| ^M| `Ctrl`+`q` `Ctrl`+`m` or `Ctrl`+`q` `Enter`

Note, in emacs buffer, line returns are all represented by “line feed” (ascii 10), doesn't matter if you are on unix or Windows or Mac. When the buffer is saved, the right line return char will be used according to the variable “buffer-file-coding-system”.

If you are confused by all these notations, see: [Emacs's Key Notations Explained (/r, ^M, C-m, RET, <return>, M-, meta)](http://xahlee.org/emacs/keystroke_rep.html).

### How to change file line endings between Windows/Unix/Mac?

Call “set-buffer-file-coding-system”, then give a value of “mac”, “dos”, “unix”. For detail, see: Emacs Line Return And Dos, Unix, Mac, All That ^M ^J.
### How to record a sequence of keystrokes?

To record keystrokes, press 【`Ctrl`+`x` `(`】 (kmacro-start-macro) then start typing your keystrokes. When done, press 【`Ctrl`+`x` `)`】 (kmacro-end-macro). This records your keystrokes. To run the keystrokes you've recorded, press 【`Ctrl`+`x` `e`】 (kmacro-end-and-call-macro) or call “call-last-kbd-macro”. There's also “apply-macro-to-region-lines”, which i use often.

For more detail and examples, see: [Emacs Keyboard Macro and Examples](http://xahlee.org/emacs/emacs_macro_example.html).

### How to move thru camelCaseWords?

You can set emacs so that word moving commands will move cursor into between CamelCaseWords. (word deletion behavior also changes accordingly.)

To toggle it globally, call “global-subword-mode”. To set it for current file only, call “subword-mode”. (subword mode is available in [Emacs 23.2](http://xahlee.org/emacs/emacs23.2_features.html))

To set it permanently, put one of the following in your emacs init file:


    (subword-mode 1) ; 1 for on, 0 for off
    (global-subword-mode 1) ; 1 for on, 0 for off


### How to have spell-checker turned on?

Type 【`Alt`+`x` flyspell-mode】 or 【`Alt`+`x` flyspell-buffer】. To have it always on, put in your emacs init file this code:


    (defun turn-spell-checking-on ()
    "Turn speck-mode or flyspell-mode on."
    ;; (speck-mode 1)
    (flyspell-mode 1)
    )

    (add-hook 'text-mode-hook 'turn-spell-checking-on)


This is under the menu “Tools▸Spell Checking”.

For discussion of problems about spell checking, see [Emacs Spell Checker Problems](http://xahlee.org/emacs/emacs_spell_checker_problems.html).

## Emacs Customization

### How to disable emacs's automatic backup?

Use this code:


    (setq make-backup-files nil) ; stop creating those backup~ files
    (setq auto-save-default nil) ; stop creating those #auto-save# files


### How to stop emacs's backup changing the file's creation date of the original file?

Put this code in your emacs init file:


    (setq backup-by-copying t)


Explanation: when emacs does a backup, by default it renames the original file into the backup file name, then create a new file and insert the current data into it. This effectively destroys the creation date of your file. (If a file is created in 2001, and you modified it today, the file's creation date will become today. Note: unixes (including linux and bsd) do not record file creation date, so this doesn't matter. (ctime is not creation date.) Windows and OS X do record file creation date.).

### How to set emacs so that all backups are placed into one backup folder? e.g. 〔~/myBackups〕

Use the following lisp code in init file:


    ; return a backup file path of a give file path
    ; with full directory mirroring from a root dir
    ; non-existant dir will be created
    (defun my-backup-file-name (fpath) "Return a new file path of a given file path.
    If the new path's directories does not exist, create them." (let (backup-root bpath) (setq backup-root "~/.emacs.d/emacs-backup") (setq bpath (concat backup-root fpath "~"))
        (make-directory (file-name-directory bpath) bpath)
        bpath
      )
    )
    (setq make-backup-file-name-function 'my-backup-file-name)


The above will mirror all directories at the given backup dir. For example, if you are editing a file 〔/Users/jane/web/xyz/myfile.txt〕, and your backup root is 〔/Users/jane/.emacs.d/emacs-backup〕, then the backup will be at 〔/Users/jane/.emacs.d/emacs-backup/Users/jane/web/xyz/myfile.txt~〕.

If you want all backup to be flat in a dir, use the following:


    (setq backup-directory-alist '(("" . "~/.emacs.d/emacs-backup")))


This will create backup files flat in the given dir, and the backup file names will have “!” characters in place of the directory separator. For example, if you are editing a file at 〔/Users/jane/web/xyz/myfile.txt〕, and your backup dir is set at 〔/Users/jane/.emacs.d/emacs-backup〕, then the backup file will be at: 〔/Users/jane/.emacs.d/emacs-backup/Users!jane!web!emacs!myfile.txt~〕. If you use long file names or many nested dirs, this scheme will reach file name length limit quickly.

### How to startup emacs without loading any customization?

To run emacs without loading your personal init file, start emacs like this:`emacs -q`. To not load any site-wide startup file, start emacs with `emacs -Q`. The site-wide startup file is usually part of your emacs distribution, such as from Carbon emacs, Aquamacs, ErgoEmacs. Starting emacs with “-Q” is like running a bare bone GNU Emacs.

short| long| comment
---|---|---
-q| \--no-init-file| Don't load your personal init file.
-Q| \--quick| same as “--no-init-file --no-site-file --no-splash”.

[(info "(emacs) Initial Options")](http://xahlee.org/emacs_manual/Initial-Options.html)
