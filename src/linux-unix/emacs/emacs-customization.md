
date: None  
author(s): None  

# [Emacs customization (example) - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/emacs-customization)

[Download `espresso.el`](http://download.savannah.gnu.org/releases-noredirect/espresso/espresso.el) and put it somewhere in your `load-path`. Then add the following to your `.emacs`:
    
    
          (autoload #'espresso-mode "espresso" "Start espresso-mode" t)
          (add-to-list 'auto-mode-alist '("\\.js$" . espresso-mode))
          (add-to-list 'auto-mode-alist '("\\.json$" . espresso-mode))  
  
---

