# [Cancel all jobs in the queue](https://stackoverflow.com/questions/12305244/cancel-queued-builds-and-aborting-executing-builds-using-groovy-for-jenkins)

```java
import hudson.model.*

def q = Jenkins.instance.queue

q.items.findAll { it.task.name.contains('devops') }.each { q.cancel(it.task) }
```
