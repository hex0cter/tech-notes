# [How to see package version without install?](http://unix.stackexchange.com/questions/39261/how-to-see-package-version-without-install)


```
daniel@daniel-IdeaPad ~ $ apt-cache policy eclipse

eclipse:

Installed: (none)

Candidate: 3.7.0-0ubuntu1

Version table:

3.7.0-0ubuntu1 0

500 http://archive.ubuntu.com/ubuntu/ oneiric/universe i386 Packages

daniel@daniel-IdeaPad ~ $ apt-cache show eclipse

Package: eclipse

Priority: optional

Section: universe/devel

Installed-Size: 128

Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>

Original-Maintainer: Debian Orbital Alignment Team <pkg-java-maintainers@lists.alioth.debian.org>

Architecture: all

Version: 3.7.0-0ubuntu1

Depends: eclipse-jdt (>= 3.7.0-0ubuntu1), eclipse-pde (>= 3.7.0-0ubuntu1)

Filename: pool/universe/e/eclipse/eclipse_3.7.0-0ubuntu1_all.deb

Size: 17294

MD5sum: 654dba8437e6722a0a8a690abf63d102

SHA1: 9ca36c647f17bb7907280514ed51a953babecf40

SHA256: bc5351162eeb85929a54e74552f946de9ed9d9d3f689e8862ae8e71c94f61892

Description-en: Extensible Tool Platform and Java IDE

The Eclipse Platform is an open and extensible platform for anything and yet

nothing in particular. It provides a foundation for constructing and running

integrated software-development tools. The Eclipse Platform allows tool

builders to independently develop tools that integrate with other people's

tools so seamlessly you can't tell where one tool ends and another starts.

.

This package provides the whole Eclipse SDK, along with the Java Development

Tools (JDT) and the Plugin Development Environment (PDE). Please note that

many plugins will fail to install if you don't have the eclipse-pde package

installed.

Homepage: http://www.eclipse.org/

Description-md5: d4d9de7c13498bc51b5ad0b7977aea24

Bugs: https://bugs.launchpad.net/ubuntu/+filebug

Origin: Ubuntu
```
