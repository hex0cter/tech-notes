
date: None  
author(s): None  

# [How to safely update your packages.json - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/javascript/how-to-safely-update-packages-json)

A tip that could save us from unexpected issues in future: try to not manually touch or even delete `yarn.lock` AND `package.json` (in the ideal case)

`* to add new dep: `yarn add foo` | `yarn add --dev foo` | `yarn add --peer foo``

`* to remove: `yarn remove dep``

`* to upgrade / bump to a new version: `yarn upgrade foo` | `yarn upgrade foo@1.2.3``

`* to see outdated stuff: `yarn outdated``

Lockfile should be changed only through its "interface" to achieve the main point of Yarn – "deterministic builds".

Also in 99% of cases it's not necessary to `rm -rf node_modules/` if you didn't do anything low-level like manually added symlinks inside, just `yarn` after switching to a new branch should be enough.

The easiest way to keep your Yarn up to date (it's important in some cases) is to have it installed with homebrew: `brew install yarn --without-node` and then `brew update && brew upgrade` from time to time.  
  
---

