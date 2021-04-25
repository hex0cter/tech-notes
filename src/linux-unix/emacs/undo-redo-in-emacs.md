
date: None  
author(s): None  

# [Undo / Redo in emacs - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/undo-redo-in-emacs)

Emacs treats `‘undo’` as just another command. Therefore you can undo the undo. This is powerful and confusing, because if you are doing several undos and miss the “correct spot”, and do anything at all which is not an undo command, you will be stuck: You broke the chain of undos. When you realize your mistake and try to undo some more, you will first undo your previous undos, then undo the dos, and then you can finally undo some more to find the correct spot. The problem is at least as confusing as this description.

redo.el by [KyleJones](http://www.emacswiki.org/emacs/KyleJones) does away with this. You can get it here:

  * <http://www.wonderworks.com/download/redo.el>

  
  
---

