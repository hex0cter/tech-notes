
date: None  
author(s): None  

# [How to interpret the status of dpkg (–list)? - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/package-management-on-linux/how-to-interpret-the-status-of-dpkg-list)

<http://linuxprograms.wordpress.com/2010/05/11/status-dpkg-list/>

**First character** : The possible value for the first character. The first character signifies the desired state, like we (or some user) is marking the package for installation

  1. u: Unknown (an unknown state)
  2. i: Install (marked for installation)
  3. r: Remove (marked for removal)
  4. p: Purge (marked for purging)
  5. h: Hold



 **Second Character** : The second character signifies the current state, whether it is installed or not. The possible values are

  1. n: Not- The package is not installed
  2. i: Inst – The package is successfully installed
  3. c: Cfg-files – Configuration files are present
  4. u: Unpacked- The package is stilled unpacked
  5. f: Failed-cfg- Failed to remove configuration files
  6. h: Half-inst- The package is only partially installed
  7. W: trig-aWait
  8. t: Trig-pend



Let’s move to the third character  
 **Third Character** : This corresponds to the error state. The possible value include

  1. R: Reinst-required The package must be installed.



Now you can easily interpret what [ii](http://linuxprograms.wordpress.com/ii-dpkg-list/), [pn](http://linuxprograms.wordpress.com/pn-dpkg-list/) and [rc](http://linuxprograms.wordpress.com/rc-dpkg-list/) correspond to.  
  
---

