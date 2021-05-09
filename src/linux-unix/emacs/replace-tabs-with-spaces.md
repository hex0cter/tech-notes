date: May 6, 2011
author(s): [Julien Palard](http://dev-tricks.net/author/mandark)

# [replace tabs with spaces](http://dev-tricks.net/emacs-replace-tabs-with-spaces)

When you want to replace tab with spaces or vice versa don’t use M-% (query-replace) but M-x tabify or M-x untabify. They work on the current selection so if you want it to be applied to a whole buffer, try C-x h (mark-whole-buffer) before to select the whole buffer.
