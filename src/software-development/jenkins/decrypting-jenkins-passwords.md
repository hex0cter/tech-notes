
date: None  
author(s): None  

# [Decrypting Jenkins Passwords - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/jenkins/decrypting-jenkins-passwords)

http://blog.ehrnhoefer.com/2013-07-02-decrypting-jenkins-passwords/

A short hack to recover a password from the Jenkins configuration files:  


  1. Retrieve the encrypted password from $JENKINS_HOME/config.xml
  2. Open the [Jenkins Script Console](https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+Script+Console)
  3. Execute e.g.  


> hudson.util.Secret.decrypt 'vceV2JWuTNIVc85PceFrk9C3u9AqB2nEQNg2a2xIA78='


  
  
---

