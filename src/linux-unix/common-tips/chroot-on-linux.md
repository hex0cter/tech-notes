
date: None  
author(s): None  

# [chroot on Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/chroot-on-linux)

<http://ubuntuforums.org/showthread.php?t=1434781>

<https://help.ubuntu.com/community/DebootstrapChroot>  


For chrooting a few things must be done:

creation of directory for chroot environment - e.g. /home/chroot

creation subdirectories proc, dev and lib inside above chroot directory:

`mkdir /home/chroot/{dev,proc,lib}`

binding /dev/ and /proc/ directories to this chroot directory:

`mount --bind /dev/ /home/chroot/dev/`

`mount --bind /proc/ /home/chroot/proc/`

copying/link files which will be used in chrooted environment into /home/chroot/ into proper directory - e.g. /bin/bash should be placed in /home/chroot/bin/bash

finding and copying/link library files needed for above files (e.g. /bin/bash) into proper directories, must be used command:

And after all of this you can try to run chroot environment. I hope that I haven't miss anything important. In fact you should try to google for setting chroot

At last, but not least: message cannot run command `/bin/bash': No such file or directory" is not complete and can be misleading. It should be more complete for example like this: cannot run command `/bin/bash': No such file, directory or library files for this command". 

Without 2 last steps of creating chroot list, /bin/bash in chrooted environment won't run even if bash would be placed in /home/chroot/bin/ directory (without proper libraries).  
  
---

