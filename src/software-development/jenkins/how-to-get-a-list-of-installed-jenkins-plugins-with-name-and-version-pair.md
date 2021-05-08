# [How to get a list of installed jenkins plugins with name and version pair?](https://stackoverflow.com/questions/9815273/how-to-get-a-list-of-installed-jenkins-plugins-with-name-and-version-pair)


You can retrieve the information using the [Jenkins Script Console](https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+Script+Console) which is accessible by visiting `http://<jenkins-url>/script`. (Given that you are logged in and have the required permissions).

![Screenshot of the Script Console](https://i.stack.imgur.com/fFt7w.png)

Enter the following _Groovy script_ to iterate over the installed plugins and print out the relevant information:

```java
    Jenkins.instance.pluginManager.plugins.each{
      plugin ->
        println ("${plugin.getDisplayName()} (${plugin.getShortName()}): ${plugin.getVersion()}")
    }
```

It will print the results list like this (clipped):

[![SScreenshot of script output](https://i.stack.imgur.com/Siql5.png)](https://i.stack.imgur.com/Siql5.png)

This solutions is similar to [one of the answers above](https://stackoverflow.com/a/9822818/1153530) in that it uses Groovy, but here we are using the script console instead. The script console is extremely helpful when using Jenkins.

 **Update**

If you prefer a sorted list, you can call this [`sort` method](http://docs.groovy-lang.org/latest/html/groovy-jdk/java/lang/Iterable.html#sort\(groovy.lang.Closure\)):

```java
    Jenkins.instance.pluginManager.plugins.sort { it.getDisplayName() }.each{
      plugin ->
        println ("${plugin.getDisplayName()} (${plugin.getShortName()}): ${plugin.getVersion()}")
    }
```

Adjust the Closure to your likings.

Or

```java
Jenkins.instance.pluginManager.plugins.sort { it.getShortName() }.each{
 plugin ->
   println ("${plugin.getShortName()}:${plugin.getVersion()}")
}
```

Daniel's notes: Definition of Jenkins.instance.pluginManager can be found here: <http://javadoc.jenkins-ci.org/hudson/PluginManager.html>
