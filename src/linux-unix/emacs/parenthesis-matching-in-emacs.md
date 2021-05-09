# [Parenthesis Matching in Emacs](http://www.emacswiki.org/emacs/ParenthesisMatching)

Here are a number of shortcuts for dealing with sexp:
```
  C-M-f     Move forward over a balanced expression
  C-M-b     Move backward over a balanced expression
  C-M-k     Kill balanced expression forward
  C-M-SPC   put the mark at the end of the sexp.
```

## The syntax table

One of **Emacs** ’ strengths is the way it matches parentheses. Depending on what mode the buffer is in, different things are considered to be parentheses; for example, in **Emacs** Lisp mode, hitting “(” followed by “)” will briefly highlight the open parenthesis if it is visible on screen, and if it is not visible, it will print a message in the echo area showing you the context of the open that you just closed. (This is the default behavior; you or your site manager can change the default.)

Nearly all modes support “(,)” as parentheses, and most also support square brackets “[,]” and curly brackets “{,}”. However, you can make any pair of characters a parenthesis-pair, by using the following command:


        (modify-syntax-entry ?^ "($")
        (modify-syntax-entry ?$ ")^")

The first command modifies the current [EmacsSyntaxTable](http://www.emacswiki.org/emacs/EmacsSyntaxTable) to make “^” an open parenthesis, to be matched to “$”. The second command does the opposite. You can modify a specific [EmacsSyntaxTable](http://www.emacswiki.org/emacs/EmacsSyntaxTable) like this:


        (modify-syntax-entry ?^ "($" perl-mode-syntax-table)

This adds `^` as an open parenthesis matching `$` in perl mode’s syntax table. You could add that statement to your . **emacs** file along with the corresponding closed parenthesis statement.

You can remove a pair of delimiters, just by redefining them as words constituents or punctuation characters. For example, if you want the command `forward-sexp`, bound by default to `C-M-f`, to ignore the meaning of [ and ] as parenthesis delimiters, put the following in your [InitFile](http://www.emacswiki.org/emacs/InitFile):


      (defvar my-wacky-syntax-table
          (let ((table (make-syntax-table)))
            (modify-syntax-entry ?[ "w" table)
            (modify-syntax-entry ?] "w" table)
            table))

      (global-set-key "\C-\M-f" '(lambda ()
               (interactive)
               (with-syntax-table my-wacky-syntax-table (forward-sexp))))

You can make `my-wacky-syntax-table` available to all commands by using:


      (set-syntax-table my-wacky-syntax-table)

Note that opening delimiters can be matched in regular expressions with `\s(`. For closing delimiters, use `\s)`

## Working with balanced expressions

A balanced expression is an expression starting with an opening delimiter, and ending with the matching closing delimiter, given by the syntax table. Such expression is called a `sexp`. Strings, symbols and numbers are also often considered as sexp, depending on the current mode.

Here are a number of shortcuts for dealing with sexp:


      C-M-f     Move forward over a balanced expression


      C-M-b     Move backward over a balanced expression


      C-M-k     Kill balanced expression forward


      C-M-SPC   put the mark at the end of the sexp.

Here is a short example; let us consider the following sexp in text mode:


        (with-current-buffer "foo.tex" (insert " \\emph{first chapter} "))

If the cursor is before the first parenthesis, `C-M-f` puts it right after the last parenthesis. With cursor on the word current, `C-M-f` puts it at the end of the word `buffer`. If cursor is on the first “ character, `C-M-f` puts it just in front of the . character. Indeed, “ is not an open delimiter, so the cursor only moves forward one word. The { character howewer is recognized as a delimiter and the cursor will **jump** just after the corresponding }.

Now if we want to remove the second parenthesized group, when the cursor is on the parenthesis at the beginning of this group, we just type `C-M-k`. If we want to put it in the kill ring without removing it, we first type `C-M-SPC`, followed by `M-w`. We can then yank it somewhere else with the usual command `C-y`.

## Navigating Parenthesis groups

Note that there are corresponding shortcuts to deal with parenthesis groups only:


      C-M-n  Move forward over a parenthetical group


      C-M-p  Move backward over a parenthetical group

These commands see nothing but parentheses (according to the syntax table; {} are considered as parentheses in text-mode for example).

Let us return to the example of the previous section. With cursor on the word `current`, `C-M-f` puts it at the end of the word buffer, because `with-current-buffer` is considered as an sexp in text-mode. On the other hand, `C-M-n` puts the cursor in front of the last parenthesis. That is, the cursor jumped over the next parenthesis group, given by `(insert " \\emph{first chapter} ")`.

## vi emulation of the % command

This code from <http://emacro.sourceforge.net/> gives a vi-like way of moving over parenthesis groups. I bind it to C-%, from vi heritage. (Note M-% searches and replaces)


    (defun goto-match-paren (arg)
      "Go to the matching parenthesis if on parenthesis, otherwise insert %.
    vi style of % jumping to matching brace."
      (interactive "p")
      (cond ((looking-at "\\s\(") (forward-list 1) (backward-char 1))
            ((looking-at "\\s\)") (forward-char 1) (backward-list 1))
            (t (self-insert-command (or arg 1)))))


### Alternative method with added flexibility

This modification of the above code works when the point is either right before or right after (), {}, or [] Note: when you are in a cluster of nested brackets, the default association is with the **bracket** that you are immediately **outside** of, to match the behavior of forward-sexp and backward-sexp


    (defun goto-match-paren (arg) "Go to the matching if on (){}[], similar to vi style of % " (interactive "p") ;; first, check for "outside of **bracket** " positions expected by forward-sexp, etc. (cond ((looking-at "[\[\(\{]") (forward-sexp)) ((looking-back "[\]\)\}]" 1) (backward-sexp)) ;; now, try to succeed from inside of a **bracket**
            ((looking-at "[\]\)\}]") (forward-char) (backward-sexp))
            ((looking-back "[\[\(\{]" 1) (backward-char) (forward-sexp))
            (t nil)))


### Another method for vi emulation of the % command

You could also bind a modified version of the first command to the “%” key:


    (defun goto-match-paren (arg)
      "Go to the matching parenthesis if on parenthesis AND last command is a movement command, otherwise insert %.
    vi style of % jumping to matching brace."
      (interactive "p")
      (message "%s" last-command)
      (if (not (memq last-command '(
                                    set-mark
                                    cua-set-mark
                                    goto-match-paren
                                    down-list
                                    up-list
                                    end-of-defun
                                    beginning-of-defun
                                    backward-sexp
                                    forward-sexp
                                    backward-up-list
                                    forward-paragraph
                                    backward-paragraph
                                    end-of-buffer
                                    beginning-of-buffer
                                    backward-word
                                    forward-word
                                    mwheel-scroll
                                    backward-word
                                    forward-word
                                    mouse-start-secondary
                                    mouse-yank-secondary
                                    mouse-secondary-save-then-kill
                                    move-end-of-line
                                    move-beginning-of-line
                                    backward-char
                                    forward-char
                                    scroll-up
                                    scroll-down
                                    scroll-left
                                    scroll-right
                                    mouse-set-point
                                    next-buffer
                                    previous-buffer
                                    )
                     ))
          (self-insert-command (or arg 1))
        (cond ((looking-at "\\s\(") (forward-list 1) (backward-char 1))
              ((looking-at "\\s\)") (forward-char 1) (backward-list 1))
              (t (self-insert-command (or arg 1))))))


When your last command is a movement command, and your cursor is at a parenthesis, then it emulates vi’s % command. Otherwise it just types the % in the current buffer.


     - MLF

## Additional ways to match parentheses

See [NavigatingParentheses](http://www.emacswiki.org/emacs/NavigatingParentheses) for other ways to navigate between parentheses.

A popular approach is to use a single function button to bounce between parentheses. Here is a self-exlanatory excerpt from my . **emacs** :


       (defun match-parenthesis (arg)
         "Match the current character according to the syntax table.


       Based on the freely available match-paren.el by Kayvan Sylvan.
       I merged code from goto-matching-paren-or-insert and match-it.


     You can define new \"parentheses\" (matching pairs). Example: angle brackets. Add the following to your . **emacs** file:


       	(modify-syntax-entry ?< \"(>\" )
       	(modify-syntax-entry ?> \")<\" )


       You can set hot keys to perform matching with one keystroke.
       Example: f6 and Control-C 6.


       	(global-set-key \"\\C-c6\" 'match-parenthesis)
       	(global-set-key [f6] 'match-parenthesis)


       Simon Hawkin <cema@cs.umd.edu> 03/14/1998"
         (interactive "p")
         (let
             ((syntax (char-syntax (following-char))))
         (cond
          ((= syntax ?\()
           (forward-sexp 1) (backward-char))
          ((= syntax ?\))
           (forward-char) (backward-sexp 1))
          (t (message "No match"))
          )
         ))

Discussion in [[1]](http://www.livejournal.com/community/emacs/2494.html)

I use a modified version. If triggered between parentheses it will bounce back to the opening parenthesis instead of triggering an error and it will **jump** to one char after the closing parenthesis and thus match the highlighting of show-paren-mode. ( [1 [x y] cursor 3] ? cursor[1 [x y] 3] ? [1 [x y] 3]cursor )


       (defun goto-match-paren (arg)
         "Go to the matching parenthesis if on parenthesis. Else go to the
       opening parenthesis one level up."
         (interactive "p")
         (cond ((looking-at "\\s\(") (forward-list 1))
               (t
                (backward-char 1)
                (cond ((looking-at "\\s\)")
                       (forward-char 1) (backward-list 1))
                      (t
                       (while (not (looking-at "\\s("))
                         (backward-char 1)
                         (cond ((looking-at "\\s\)")
                                (message "->> )")
                                (forward-char 1)
                                (backward-list 1)
                                (backward-char 1)))
                         ))))))

## Strict parenthesis matching

It should be noted that the syntax-table makes all delimiters “even”. That means that a beginning parenthesis ( may match a closing **bracket** ] if the delimiters are not balanced as a whole. Try `C-M-f` on the following expression:


         (  [   )  ]

Here is a short piece of Lisp code in which such a situation occurs:


      (while
         (re-search-forward "\\(\\[[0-9]\\),\\([0-9]\\]\\)" nil t)
         (replace-match (concat (match-string 1) "." (match-string 2))))

This code replaces, e.g. `[4,5]` by `[4.5]`. Now, in the regular expression between quotes `" "`, the first opening **bracket** [ matches the first closing parenthesis ), whereas the last opening parenthesis ( matches the last closing **bracket** ]. This is a bit surprising at first sight.

Some people consider such behaviour as uncorrect, and have devised new matching commands to ensure that a starting ( is always matched by a closing ). The following code comes from the _gnu- **emacs** -help_ archive [[2]](http://lists.gnu.org/archive/html/help-gnu-emacs/2004-09/msg00350.html) and provides a new definition for the `forward-sexp` command, which is bound by default to `C-M-f`. Note that these commands do not rely on the syntax table, which may be seen as a limitation.


      (defun skip-string-forward (&optional limit)
         (if (eq (char-after) ?\")
             (catch 'done
               (forward-char 1)
               (while t
                 (skip-chars-forward "^\\\\\"" limit)
                 (cond ((eq (point) limit)
                       (throw 'done nil) )
                       ((eq (char-after) ?\")
                       (forward-char 1)
                       (throw 'done nil) )
                       (t
                       (forward-char 1)
                       (if (eq (point) limit)
                            (throw 'done nil)
                          (forward-char 1) ) ) ) ) ) ) )

       (defun skip-string-backward (&optional limit)
         (if (eq (char-before) ?\")
             (catch 'done
               (forward-char -1)
               (while t
                 (skip-chars-backward "^\"" limit)
                 (if (eq (point) limit)
                     (throw 'done nil) )
                 (forward-char -1)
                 (if (eq (point) limit)
                     (throw 'done nil) )
                 (if (not (eq (char-before) ?\\))
                     (throw 'done nil) ) ) ) ) )

       (defun forward-pexp (&optional arg)
         (interactive "p")
         (or arg (setq arg 1))
         (let (open close next notstrc notstro notstre depth pair)
           (catch 'done
             (cond ((> arg 0)
                    (skip-chars-forward " \t\n")
                    (if (not (memq (char-after) '(?\( ?\[ ?\{ ?\<)))
                       (goto-char (or (scan-sexps (point) arg) (buffer-end arg)))
                      (skip-chars-forward "^([{<\"")
                      (while (eq (char-after) ?\")
                       (skip-string-forward)
                       (skip-chars-forward "^([{<\"") )
                      (setq open (char-after))
                      (if (setq close (cadr (assq open '( (?\( ?\))
                                                          (?\[ ?\])
                                                          (?\{ ?\})
                                                          (?\< ?\>) ) ) ) )
                          (progn
                            (setq notstro (string ?^ open ?\")
                                  notstre (string ?^ open close ?\") )
                            (while (and (> arg 0) (not (eobp)))
                              (skip-chars-forward notstro)
                              (while (eq (char-after) ?\")
                               (if (eq (char-before) ?\\)
                                    (forward-char 1)
                                  (skip-string-forward) )
                               (skip-chars-forward notstro) )
                              (forward-char 1)
                              (setq depth 1)
                              (while (and (> depth 0) (not (eobp)))
                               (skip-chars-forward notstre)
                               (while (eq (char-after) ?\")
                                  (if (eq (char-before) ?\\)
                                      (forward-char 1)
                                    (skip-string-forward) )
                                  (skip-chars-forward notstre) )
                               (setq next (char-after))
                               (cond ((eq next open)
                                       (setq depth (1+ depth)) )
                                      ((eq next close)
                                       (setq depth (1- depth)) )
                                      (t
                                       (throw 'done nil) ) )
                               (forward-char 1) )
                              (setq arg (1- arg) ) ) ) ) ) )
                   ((< arg 0)
                    (skip-chars-backward " \t\t")
                    (if (not (memq (char-before) '(?\) ?\] ?\} ?\>)))
                       (progn
                          (goto-char (or (scan-sexps (point) arg) (buffer-end arg)))
                          (backward-prefix-chars) )
                      (skip-chars-backward "^)]}>\"")
                      (while (eq (char-before) ?\")
                       (skip-string-backward)
                       (skip-chars-backward "^)]}>\"") )
                      (setq close (char-before))
                      (if (setq open (cadr (assq close '( (?\) ?\()
                                                          (?\] ?\[)
                                                          (?\} ?\{)
                                                          (?\> ?\<) ) ) ) )
                          (progn
                            (setq notstrc (string ?^ close ?\")
                                  notstre (string ?^ close open ?\") )
                            (while (and (< arg 0) (not (bobp)))
                              (skip-chars-backward notstrc)
                              (while (eq (char-before) ?\")
                               (if (eq (char-before (1- (point))) ?\\)
                                    (forward-char -1)
                                  (skip-string-backward) )
                               (skip-chars-backward notstrc) )
                              (forward-char -1)
                              (setq depth 1)
                              (while (and (> depth 0) (not (bobp)))
                               (skip-chars-backward notstre)
                               (while (eq (char-before) ?\")
                                  (if (eq (char-before (1- (point))) ?\\)
                                      (forward-char -1)
                                    (skip-string-backward) )
                                  (skip-chars-backward notstre) )
                               (setq next (char-before))
                               (cond ((eq next close)
                                       (setq depth (1+ depth)) )
                                      ((eq next open)
                                       (setq depth (1- depth)) )
                                      (t
                                       (throw 'done nil) ) )
                               (forward-char -1) )
                              (setq arg (1+ arg)) ) ) ) ) ) ) ) ))

       (setq forward-sexp-function 'forward-pexp)
