# export jenkins job config to xml

```
java -jar $path/jenkins-cli.jar -s http://jenkins.internal.machines/jenkins/ get-job E2E-test-DEVELOP/ --username "daniel.han" --password "xxxxxxxx" > jenkins-config.xml
```
