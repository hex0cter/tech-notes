# [How to automatically synchronize the shell history between terminal windows](http://stackoverflow.com/questions/103944/real-time-history-export-amongst-bash-terminal-windows)

Here is the solution (add it into $HOME/.bashrc):

```
HISTSIZE=9000
HISTFILESIZE=$HISTSIZE
HISTCONTROL=ignorespace:ignoredups

history() {
  _bash_history_sync
  builtin history "$@"
}

_bash_history_sync() {
  builtin history -a         #1
  HISTFILESIZE=$HISTFILESIZE #2
  builtin history -c         #3
  builtin history -r         #4
}

PROMPT_COMMAND=_bash_history_sync
```
