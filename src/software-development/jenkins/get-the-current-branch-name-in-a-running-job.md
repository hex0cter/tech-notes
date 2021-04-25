
date: None  
author(s): None  

# [Get the current branch name in a running job - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/jenkins/get-the-current-branch-name-in-a-running-job)

  


Add the following code as a build step of "Execute system groovy step" [(](https://wiki.jenkins.io/display/JENKINS/Groovy+plugin)[Groovy plugin](https://wiki.jenkins.io/display/JENKINS/Groovy+plugin) is needed)

`import jenkins.*`

`import jenkins.model.*`

`import hudson.*`

`import hudson.model.*`

`import java.util.regex.*`

`def currentBuild = build.getFullDisplayName()`

`println('The current build is:' + currentBuild)`

`// parse the branch in the build full Name. Keep in mind that the banch in`

`// the build name is populated after we do git clone in the job`

`def currentBuildRegexGroups = currentBuild =~ /^(.*) #(\d+) (.*)$/`

`if (currentBuildRegexGroups.matches()) { // means that the build is triggered by a branch`

` def currentBranch = currentBuildRegexGroups[0][3]`

` println('Build branch name is:' + currentBranch)`

`}`

`build.doStop() `  
  
---

