# Cancel jobs in the queue from Jenkins console

Jenkins:
```java
import hudson.model.*

def q = Jenkins.instance.queue

q.items.findAll.each { q.cancel(it.task) }
```

Or:

```java
import hudson.model.*

def q = jenkins.model.Jenkins.getInstance().getQueue()

def items = q.getItems()

for (i=0;i<items.length;i++){

 items[i].doCancelQueue()

}
```
