# [Decrypting Jenkins Passwords](http://blog.ehrnhoefer.com/2013-07-02-decrypting-jenkins-passwords/)


A short hack to recover a password from the Jenkins configuration files:

  1. Retrieve the encrypted password from `$JENKINS_HOME/config.xml`
  2. Open the [Jenkins Script Console](https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+Script+Console)
  3. Execute e.g.
  ```java
  hudson.util.Secret.decrypt 'vceV2JWuTNIVc85PceFrk9C3u9AqB2nEQNg2a2xIA78='
  ```
