
date: None  
author(s): None  

# [Auto-update tmux status bar with active pane pwd - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/auto-update-tmux-status-bar-with-active-pane-pwd)

https://stackoverflow.com/questions/19200589/auto-update-tmux-status-bar-with-active-pane-pwd

This worked for me with tmux 2.5:
    
    
    export PS1=$PS1'$( [ -n $TMUX ] && tmux rename-window $(basename $PWD))'  
  
---

