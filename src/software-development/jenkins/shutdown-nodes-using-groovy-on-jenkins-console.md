# [Shutdown nodes using groovy on Jenkins console](https://wiki.jenkins-ci.org/display/JENKINS/Monitor+and+Restart+Offline+Slaves)

Jenkins slaves management in Groovy:

```java
for (aSlave in hudson.model.Hudson.instance.slaves) {

    println('Shutting down node!!!!');
    println aSlave.name;
    //aSlave.getComputer().kill();
    aSlave.getComputer().setTemporarilyOffline(true,null);
    aSlave.getComputer().doDoDelete();
}
```


Another useful link: <https://wiki.jenkins-ci.org/display/JENKINS/Monitor+and+Restart+Offline+Slaves>
