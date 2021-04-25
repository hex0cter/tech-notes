
date: None  
author(s): None  

# [Abort all running jobs for the same branch - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/jenkins/abort-all-running-jobs-for-the-same-branch)

Add below as `System groovy` step

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

` // get all the jobs`

` Jenkins.instance.getItems().each { job ->`

` // check only for `job_prefix_` jobs`

` if (job.getFullDisplayName().startsWith("job_prefix_")) {`

` // for every build in the job `

` job.builds.each { build->`

` // check if build is running`

` if (build.isBuilding()) {`

` // get the full name of the running build and extract the branch name`

` def buildName = build.getFullDisplayName()`

` def buildRegexGroups = buildName =~ /(.*) #(\d+) (.*)/`

` // if anything else with the same branch (other than the current) is running, then abort`

` if (buildRegexGroups.matches() && !currentBuild.equals(buildName)) {`

` def branchOfBuild = buildRegexGroups[0][3]`

` if (branchOfBuild.equals(currentBranch)){`

` println('Aborting: ' + buildName)`

` build.doStop();`

` }`

` }`

` }`

` }`

` }`

` }`

`}`  
  
---

