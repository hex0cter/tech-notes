
date: None  
author(s): None  

# [export jenkins job config to xml - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/jenkins/export-jenkins-job-config-to-xml)

java -jar $path/jenkins-cli.jar -s http://jenkins.internal.machines/jenkins/ get-job E2E-test-DEVELOP/ --username "daniel.han" --password "xxxxxxxx" > jenkins-config.xml  
  
---

