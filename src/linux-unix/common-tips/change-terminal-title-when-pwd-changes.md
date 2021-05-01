
date: None
author(s): None

# [Change terminal title when PWD change](http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x264.html)


<http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x264.html>

<http://ubuntuforums.org/archive/index.php/t-448614.html>

```
export PROMPT_COMMAND='echo -en "\033]2;$PWD\007"'
```
