
date: None  
author(s): None  

# [Cancel jobs in the queue from Jenkins console - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/jenkins/cancel-jobs-in-the-queue-from-jenkins-console)

Jenkins:

`import hudson.model.*`

`def q = Jenkins.instance.queue`

`q.items.findAll.each { q.cancel(it.task) }`

Or:

`import hudson.model.* `` `

`def q = jenkins.model.Jenkins.getInstance().getQueue()`` `

`def items = q.getItems() `` `

`for (i=0;i<items.length;i++){ `` `

` ``items[i].doCancelQueue() `` `

`} `` `  
  
---

