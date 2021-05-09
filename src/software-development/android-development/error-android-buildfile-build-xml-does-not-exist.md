# [Error: Android: Buildfile: build.xml does not exist!](http://www.howtoforge.com/android-buildfile-build.xml-does-not-exist)


```
ant debug
Buildfile: build.xml does not exist!
Build failed
```

Run

```
android update project --target 5 --path /path/to/android/project
```

or, if you are in your project's root directory already:

```
android update project --target 5 --path .
```

target is the build target for your project. Run

```
android list targets
```
