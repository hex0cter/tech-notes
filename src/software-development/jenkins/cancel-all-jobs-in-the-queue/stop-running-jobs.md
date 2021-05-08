# Stop running jobs

```groovy
Jenkins.instance.getAllItems(AbstractProject.class).each {it ->
  it.getBuilds().each {
    if (it.isBuilding()) {
      if(it.getDisplayName().contains('devops')) {
          println(it.getFullDisplayName());
          it.doStop()
      }
    }
  }
}
```

https://github.com/cloudbees/jenkins-scripts/blob/master/cancel-running-builds.groovy


```groovy
public int cancelRunning() {
 // Cancel running builds.
 def numCancels = 0;
 for (job in this.hudson.instance.items) {
 for (build in job.builds) {
 if (build == this.build) { continue; } // don't cancel ourself!
 if (!build.hasProperty('causes')) { continue; }
 if (!build.isBuilding()) { continue; }
 for (cause in build.causes) {
 if (!cause.hasProperty('upstreamProject')) { continue; }
 if (cause.upstreamProject == this.upstreamProject &&
                            cause.upstreamBuild == this.upstreamBuild) {
 this.printer.println('Stopping ' + build.toString());
                        build.doStop();
 this.printer.println(build.toString() + ' stopped.');
                        numCancels++;
 break;
                    }
                }
            }
        }
 return numCancels;
    }
```
