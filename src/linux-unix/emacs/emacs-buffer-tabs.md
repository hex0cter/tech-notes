
date: None  
author(s): None  

# [Emacs: buffer tabs - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/emacs-buffer-tabs)

Tabs to show overlapping windows are becoming more common these days, especially in terminals, browsers, and chat programs. The idea is that a single window can contain several … buffers. Emacs already has this, and has had this for a long time. It's just that by default Emacs doesn't have visible tabs to show the buffers. XEmacs and SXEmacs can show tabs with “buffer tabs”; for GNU Emacs 21 you need to install [TabBar mode](http://www.emacswiki.org/cgi-bin/wiki/TabBarMode) (thanks to[Jemima](http://www.ficml.org/jemimap/wordpress/2004/10/11/tabbar/) for finding this), which gives you tabs like this:

[![screenshot of tabbar-mode](http://3.bp.blogspot.com/_kV9ZnGnZL7M/RjY7lvCgMeI/AAAAAAAAABI/Uqr3dJEYPH8/s400/Picture+1.png)](http://3.bp.blogspot.com/_kV9ZnGnZL7M/RjY7lvCgMeI/AAAAAAAAABI/Uqr3dJEYPH8/s1600-h/Picture+1.png)

Well, it doesn't look like that by default. The standard settings give each tab a 3d button appearance. I wanted something simpler, so I changed the settings:
    
    
     (set-face-attribute 'tabbar-default-face nil :background "gray60") (set-face-attribute 'tabbar-unselected-face nil :background "gray85" :foreground "gray30" :box nil) (set-face-attribute 'tabbar-selected-face nil :background "#f2f2f6" :foreground "black" :box nil) (set-face-attribute 'tabbar-button-face nil :box '(:line-width 1 :color "gray72" :style released-button)) (set-face-attribute 'tabbar-separator-face nil :height 0.7) (tabbar-mode 1) (define-key global-map [(alt j)] 'tabbar-backward) (define-key global-map [(alt k)] 'tabbar-forward)
    

This makes the currently selected tab match my default background (`#f2f2f6`), removes the 3d borders, and adds a bit of space between the tabs. I also define `Alt-j` and `Alt-k` to switch tabs; I use the same keys in other tabbed apps, because they're easier to type than moving my hands to the arrow keys.

TabBar-mode looks neat, but I'm not sure how useful it will be. In Emacs I have lots of buffers—more than will fit as tabs. The main thing I like so far are the keys for cycling between related buffers, but as the number of buffers grows it becomes faster to switch directly to the buffer I want.

<http://amitp.blogspot.com/2007/04/emacs-buffer-tabs.html>

<http://www.emacswiki.org/cgi-bin/wiki/TabBarMode>

<http://packages.debian.org/lenny/all/emacs-goodies-el/download>

