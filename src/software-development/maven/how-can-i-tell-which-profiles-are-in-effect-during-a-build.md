# [How can I tell which profiles are in effect during a build?](http://maven.apache.org/guides/introduction/introduction-to-profiles.html)


Determining active profiles will help the user to know what particular profiles has been executed during a build. We can use the [Maven Help Plugin](http://maven.apache.org/plugins/maven-help-plugin/) to tell what profiles are in effect during a build.

```
mvn help:active-profiles
```
