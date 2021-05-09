# [Simple Emacs Configuration](http://homepages.inf.ed.ac.uk/s0243221/emacs/index.html)


Emacs can automatically correct your spelling mistake as you type (such as correcting "thier" with "their"), or expand your own abbreviations for full word (such as replacing "Indie" with "Independent"). Emacs can do this when you enable the "Abbrev" minor mode.

Add the following code to your `~/.emacs` file to enable the Abbrev minor mode, to load in abbreviations from `~/.abbrev_defs` and to save changes you make to the abbreviations table when you exit Emacs.

```
;; ===== Automatically load abbreviations table =====

;; Note that emacs chooses, by default, the filename
;; "~/.abbrev_defs", so don't try to be too clever
;; by changing its name

(setq-default abbrev-mode t)
(read-abbrev-file "~/.abbrev_defs")
(setq save-abbrevs t)
```

To display a list of the current abbreviations Emacs uses, enter the command `**list-abbrevs**`.

## Highlight Current Line

To make Emacs highlight the line the curosr is currently on, add the following to your `~/.emacs` :
```
;; ===== Set the highlight current line minor mode =====

;; In every buffer, the line which contains the cursor will be fully
;; highlighted

(global-hl-line-mode 1)
```
## Set Indent Size

To set the standard indent size to some value other than default add the following to your `~/.emacs` :

```
;; ===== Set standard indent to 2 rather that 4 ====
(setq standard-indent 2)
```

## Line-by-Line Scrolling

By default Emacs will scroll the buffer by several lines whenever the cursor goes above or below the current view. The cursor is also returned to the middle-line of the current view.

This can be confusing to work with since the cursor appears to jump around. If you prefer to have the cursor remain at the top or bottom of the screen as scrolling takes place then use:
```
;; ========== Line by line scrolling ==========

;; This makes the buffer scroll by only a single line when the up or
;; down cursor keys push the cursor (tool-bar-mode) outside the
;; buffer. The standard emacs behaviour is to reposition the cursor in
;; the center of the screen, but this can make the scrolling confusing

(setq scroll-step 1)
```

## Turn Off Tab Character

To stop Emacs from entering the tab character into your files (when you press the "tab" key) add the following to your `~/.emacs` :
```
;; ===== Turn off tab character =====

;;
;; Emacs normally uses both tabs and spaces to indent lines. If you
;; prefer, all indentation can be made from spaces only. To request this,
;; set `indent-tabs-mode' to `nil'. This is a per-buffer variable;
;; altering the variable affects only the current buffer, but it can be
;; disabled for all buffers.

;;
;; Use (setq ...) to set value locally to a buffer
;; Use (setq-default ...) to set value globally
;;
(setq-default indent-tabs-mode nil)
```

## Enable Wheel-Mouse Scrolling

By default Emacs does not respond to actions of a scroll button on a wheel mouse; however, it can be made to do so with a simple configuration entry:

```
;; ========== Prevent Emacs from making backup files ==========
(setq make-backup-files nil)
```

## Prevent Backup File Creation

By default Emacs will automatically create backups of your open files (these are the files with the ~ character appended to the filename). Add the following to your `~/.emacs` to prevent these backup files from being created :

```
;; ========== Prevent Emacs from making backup files ==========
(setq make-backup-files nil)
```

## Saving Backup Files to a Specific Directory

Backup files can occassionally be usful, so rather than completely disabelling them, Emacs can be configured to place them in a specified directory. Do this by adding the following to your `~/.emacs` files:

```
;; ========== Place Backup Files in Specific Directory ==========

;; Enable backup files.
(setq make-backup-files t)

;; Enable versioning with default values (keep five last versions, I think!)
(setq version-control t)

;; Save all backup file in this directory.
(setq backup-directory-alist (quote ((".*" . "~/.emacs_backups/"))))
```


## Enable Line and Column Numbering

Emacs can display the current line and column number on which the cursor currently resides. The numbers appear in the mode-line :

```
;; ========== Enable Line and Column Numbering ==========

;; Show line-number in the mode line
(line-number-mode 1)

;; Show column-number in the mode line
(column-number-mode 1)
```

## Set Fill Column

The fill column influences how Emacs justifies paragraphs. For best results choose a value less than 80:

```
;; ========== Set the fill column ==========

;; Enable backup files.
(setq-default fill-column 72)
```

## Enable Auto Fill mode

Auto fill is useful when editing text files. Lines are automatically wrapped when the cursor goes beyond the column limit :
```
;; ===== Turn on Auto Fill mode automatically in all modes =====

;; Auto-fill-mode the the automatic wrapping of lines and insertion of
;; newlines when the cursor goes over the column limit.

;; This should actually turn on auto-fill-mode by default in all major
;; modes. The other way to do this is to turn on the fill for specific modes
;; via hooks.

(setq auto-fill-mode 1)
```

## Treat New Buffers as Text

Specify that new buffers should be treated as text files:

```
;; ===== Make Text mode the default mode for new buffers =====
(setq default-major-mode 'text-mode)
```

## Set Basic Colours

Emacs does allow the various colours it uses for highlighting code to be configured by the user. However a quick way to set the basic colours used f or all buffers is:
```
;; ========= Set colours ==========

;; Set cursor and mouse-pointer colours
(set-cursor-color "red")
(set-mouse-color "goldenrod")

;; Set region background colour
(set-face-background 'region "blue")

;; Set emacs background colour
(set-background-color "black")
```

## Delete the Current Line

In order to provide Emacs with a key for deleting the current line an appropriate delete-line function has to be first defined, and then a key-sequence binding defined to invoke it :

```
;; ===== Function to delete a line =====

;; First define a variable which will store the previous column position
(defvar previous-column nil "Save the column position")

;; Define the nuke-line function. The line is killed, then the newline
;; character is deleted. The column which the cursor was positioned at is then
;; restored. Because the kill-line function is used, the contents deleted can
;; be later restored by usibackward-delete-char-untabifyng the yank commands.
(defun nuke-line()
  "Kill an entire line, including the trailing newline character"
  (interactive)

  ;; Store the current column position, so it can later be restored for a more
  ;; natural feel to the deletion
  (setq previous-column (current-column))

  ;; Now move to the end of the current line
  (end-of-line)

  ;; Test the length of the line. If it is 0, there is no need for a
  ;; kill-line. All that happens in this case is that the new-line character
  ;; is deleted.
  (if (= (current-column) 0)
    (delete-char 1)

    ;; This is the 'else' clause. The current line being deleted is not zero
    ;; in length. First remove the line by moving to its start and then
    ;; killing, followed by deletion of the newline character, and then
    ;; finally restoration of the column position.
    (progn
      (beginning-of-line)
      (kill-line)
      (delete-char 1)
      (move-to-column previous-column))))

;; Now bind the delete line function to the F8 key
(global-set-key [f8] 'nuke-line)
```
