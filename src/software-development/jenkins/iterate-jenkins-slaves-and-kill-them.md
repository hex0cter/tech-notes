# [Iterate jenkins slaves and kill them](https://stackoverflow.com/questions/24072354/jenkins-is-there-a-way-to-remove-all-offline-nodes-slaves-batch-remove-nod)


Uncomment the last three lines if you wanna delete the agents:

```java
for (aSlave in hudson.model.Hudson.instance.slaves) {
  println('====================');
  println('Name: ' + aSlave.name);
  println('getLabelString: ' + aSlave.getLabelString());
  println('getNumExectutors: ' + aSlave.getNumExecutors());
  println('getRemoteFS: ' + aSlave.getRemoteFS());
  println('getMode: ' + aSlave.getMode());
  println('getRootPath: ' + aSlave.getRootPath());
  println('getDescriptor: ' + aSlave.getDescriptor());
  println('getComputer: ' + aSlave.getComputer());
  println('computer.isAcceptingTasks: ' + aSlave.getComputer().isAcceptingTasks());
  println('computer.isLaunchSupported: ' + aSlave.getComputer().isLaunchSupported());
  println('computer.getConnectTime: ' + aSlave.getComputer().getConnectTime());
  println('computer.getDemandStartMilliseconds: ' + aSlave.getComputer().getDemandStartMilliseconds());
  println('computer.isOffline: ' + aSlave.getComputer().isOffline());
  println('computer.countBusy: ' + aSlave.getComputer().countBusy());
  println('computer.getLog: ' + aSlave.getComputer().getLog());
  println('computer.getBuilds: ' + aSlave.getComputer().getBuilds());
  //println('Shutting down node!!!!');
  //aSlave.getComputer().setTemporarilyOffline(true,null);
  //aSlave.getComputer().doDoDelete();
}
```
