
date: None  
author(s): None  

# [stderr rediection - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/tcsh/stderr-rediection)

With tcsh, you can redirect stderr using ">& filename".

<http://www.m5hosting.com/pipermail/sdbug/2004-May/002617.html>

2.9) How do I redirect stdout and stderr separately in csh? In csh, you can redirect stdout with ">", or stdout and stderr together with ">&" but there is no direct way to redirect stderr only. The best you can do is ( command >stdout_file ) >&stderr_file which runs "command" in a subshell; stdout is redirected inside the subshell to stdout_file, and both stdout and stderr from the subshell are redirected to stderr_file, but by this point stdout has already been redirected so only stderr actually winds up in stderr_file. If what you want is to avoid redirecting stdout at all, let sh do it for you. sh -c 'command 2>stderr_file'

Read more:<http://www.faqs.org/faqs/unix-faq/faq/part2/section-9.html#ixzz0iWHuZCTt>  
  
---

