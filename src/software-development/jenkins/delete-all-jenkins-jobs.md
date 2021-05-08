# [Delete all jenkins jobs](hhttps://gist.github.com/nextrevision/d11b2df4e8b229c6855b)

```java
import jenkins.model.*

Jenkins.instance.items.findAll { job ->

  if (job.name =~ /^jenkins/) {
      println 'SKIPPING ' + job.name
  } else {
      println job.name
    job.delete()

  }
}
```
