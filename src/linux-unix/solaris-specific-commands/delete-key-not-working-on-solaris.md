
date: None  
author(s): None  

# [delete key not working on Solaris - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/solaris-specific-commands/delete-key-not-working-on-solaris)

http://www.freebsdwiki.net/index.php/Bash,_fixing_delete_key_behavior

Create $HOME/.inputrc with the following content:
    
    
    set meta-flag on
    set input-meta on
    set convert-meta off
    set output-meta on
    
    "\e[1~": beginning-of-line
    "\e[4~": end-of-line
    "\e[5~": beginning-of-history
    "\e[6~": end-of-history
    "\e[3~": delete-char
    "\e[2~": quoted-insert
    "\e[5C": forward-word
    "\e[5D": backward-word  
  
---

