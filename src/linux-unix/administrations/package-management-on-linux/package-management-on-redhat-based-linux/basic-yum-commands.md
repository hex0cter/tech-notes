# [Basic Yum Commands](http://yum.baseurl.org/wiki/YumCommands)

This is not an exhaustive list of all yum commands but it is a list of the basic/common/important ones. For a complete list see the yum man page.


       yum list [available|installed|extras|updates|obsoletes|all|recent] [pkgspec]


This command lets you list packages in any repository enabled on your system or installed. It also lets you list specific types of packages as well as refine your list with a package specification of any of the package's name, arch, version, release, epoch.


       yum list


By default 'yum list' without any options will list all packages in all the repositories and all the packages installed on your system. Note: 'yum list all' and 'yum list' give the same output.


       yum list available


Lists all the packages available to be installed in any enabled repository on your system.


       yum list installed


This is equivalent to rpm -qa. It lists all the packages installed on the system.


       yum list extras


This command lists any installed package which no longer appears in any of your enabled repositories. Useful for finding packages which linger between upgrades or things installed not from a repo.


       yum list obsoletes


This command lists any obsoleting relationships between any available package and any installed package.


       yum list updates


This command lists any package in an enabled repository which is an update for any installed package.


       yum list recent


This command lists any package added to any enabled repository in the last seven(7) days.


       yum list pkgspec


This command allows you to refine your listing for particular packages.

Examples of pkgspecs:
>
>
          yum list zsh
          yum list joe\*
          yum list \*.i386
          yum list dovecot-1.0.15
>


       yum install/remove/update


....


       yum check-update


Exactly like **yum list updates** but returns an exit code of **100** if there are updates available. Handy for shell scripting.


       yum grouplist
       yum groupinfo
       yum groupinstall
       yum groupupdate
       yum groupremove


Please see the [YumGroups](http://yum.baseurl.org/wiki/YumGroups) page on this wiki for information about the above commands.


       yum info


This displays more information about any package installed or available. It takes the same arguments as **yum list** but it is best run with a specific package name or glob. Example:
>
>
         $ yum info yum
         Installed Packages
         Name       : yum
         Arch       : noarch
         Version    : 3.2.20
         Release    : 3.fc10
         Size       : 2.5 M
         Repo       : installed
         Summary    : RPM installer/updater
         URL        : http://yum.baseurl.org/
         License    : GPLv2+
         Description: Yum is a utility that can check for and automatically download and
                    : install updated RPM packages. Dependencies are obtained and downloaded
                    : automatically prompting the user as necessary.
>


      yum search


This allows you to search for information from the various metadata available about packages. It can accept multiple arguments. It will output the packages which match the most terms first followed by the next highest number of matches, etc. Specifically yum search looks at the following fields: name, summary, description, url. If you're searching for what package provides a certain command try **yum provides** instead.

Search example:

    $ yum search python rsync ssh
    ========================= Matched: python, rsync, ssh ==========================
    rdiff-backup.i386 : Convenient and transparent local/remote incremental
                      : mirror/backup

    ============================ Matched: python, rsync ============================
    cobbler.noarch : Boot server configurator

    ============================= Matched: python, ssh =============================
    denyhosts.noarch : A script to help thwart ssh server attacks
    pexpect.noarch : Pure Python Expect-like module
    python-paramiko.noarch : A SSH2 protocol library for python
    python-twisted-conch.i386 : Twisted SSHv2 implementation

    ============================= Matched: rsync, ssh ==============================
    duplicity.i386 : Encrypted bandwidth-efficient backup using rsync algorithm
    pssh.noarch : Parallel SSH tools



       yum provides/yum whatprovides


This command searches for which packages provide the requested dependency of file. This also takes wildcards for files. Examples:


    $ yum provides MTA
    2:postfix-2.5.5-1.fc10.i386 : Postfix Mail Transport Agent
    Matched from:
    Other       : MTA

    exim-4.69-7.fc10.i386 : The exim mail transfer agent
    Matched from:
    Other       : MTA

    sendmail-8.14.3-1.fc10.i386 : A widely used Mail Transport Agent (MTA)
    Matched from:
    Other       : Provides-match: MTA


    $ yum provides \*bin/ls
    coreutils-6.12-17.fc10.i386 : The GNU core utilities: a set of tools commonly
                                : used in shell scripts
    Matched from:
    Filename    : /bin/ls




       yum shell


....


       yum makecache


Is used to download and make usable all the metadata for the **currently enabled** yum repos. This is useful if you want to make sure the cache is fully current with all metadata before continuing.


       yum clean


During its normal use yum creates a cache of metadata and packages. This cache can take up a lot of space. The yum clean command allows you to clean up these files. All the files yum clean will act on are normally stored in /var/cache/yum.

Example commands and what they do:


       yum clean packages


This cleans up any cached packages in any enabled repository cache directory.


       yum clean metadata


This cleans up any xml metadata that may have been cached from any enabled repository.


       yum clean dbcache


Yum will create or download some sqlite database files as part of its normal operation. This command clean up the cached copies of those from any enabled repository cache.


       yum clean all


Clean all cached files from any enabled repository. Useful to run from time to time to make sure there is nothing using unnecessary space.
