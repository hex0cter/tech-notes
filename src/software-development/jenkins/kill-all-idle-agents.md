
date: None  
author(s): None  

# [Kill all idle agents - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/jenkins/kill-all-idle-agents)

`for (aSlave in hudson.model.Hudson.instance.slaves) {`

` println('====================');`

` println('Name: ' + aSlave.name);`

` //println('getLabelString: ' + aSlave.getLabelString());`

` //println('getNumExectutors: ' + aSlave.getNumExecutors());`

` //println('getRemoteFS: ' + aSlave.getRemoteFS());`

` //println('getMode: ' + aSlave.getMode());`

` //println('getRootPath: ' + aSlave.getRootPath());`

` //println('getDescriptor: ' + aSlave.getDescriptor());`

` //println('getComputer: ' + aSlave.getComputer());`

` //println('computer.isAcceptingTasks: ' + aSlave.getComputer().isAcceptingTasks());`

` //println('computer.isLaunchSupported: ' + aSlave.getComputer().isLaunchSupported());`

` //println('computer.getConnectTime: ' + aSlave.getComputer().getConnectTime());`

` //println('computer.getDemandStartMilliseconds: ' + aSlave.getComputer().getDemandStartMilliseconds());`

` //println('computer.isOffline: ' + aSlave.getComputer().isOffline());`

` //println('computer.countBusy: ' + aSlave.getComputer().countBusy());`

` //println('computer.getBuilds: ' + aSlave.getComputer().getBuilds());`

` if (aSlave.getComputer().isIdle()) {`

` println('Shutting down node!!!!');`

` aSlave.getComputer().setTemporarilyOffline(true,null);`

` aSlave.getComputer().doDoDelete();`

` } else {`

` println('Skip node since it appears busy.');`

` }`

`}`  
  
---

