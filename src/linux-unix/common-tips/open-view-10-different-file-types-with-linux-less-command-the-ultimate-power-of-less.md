# [Open & View 10 Different File Types with Linux Less Command](http://www.thegeekstuff.com/2009/04/linux-less-command-open-view-different-files-less-is-more/)

The key point is that you need to add the line below to your $HOME/.bashrc
```
 export LESSOPEN='|/usr/bin/lesspipe %s'
```

Here is the original article:

---


In this article, let us review how Linux less command can be used to **open and view** the following **10 different file types** :

  1. PDF File – *.pdf
  2. Word Document- *.doc
  3. Image Files – *.gif, *.jpg, *.jpeg, *.png
  4. TAR Files – *.tar
  5. TAR Files with gzip – *.tar.gz
  6. Zip Files – *.zip
  7. Gzip and Gzip2 Files – *.gz and *.bz2
  8. ISO Files
  9. Debian Files – *.deb
  10. RPM Files – *.rpm



### Set the LESSOPEN environment variable to lesspipe

First, make sure the following is set in the environment variable.

```
    $ set | grep -i less
    LESSOPEN='|/usr/bin/lesspipe.sh %s'
```

Please note that you can also do the following to setup the lesspipe.

```
    $ eval "($lesspipe)"
    $ cat ~/.bashrc
    eval "($lesspipe)"
```

  *  **lesspipe** , **lessfile** are the input preprocessor for less, which lets it to open all types of files.
  *  **lesspipe** allows you to open while the process of conversion is going on using pipe.
  *  **lessfile** completes the conversion first, and then displays the content. This writes the converted thing to a temporary file then displays it.
  * You can also write your own input preprocessor, and use it.



### File Type 1: How to open a pdf file?

It shows all the text in the pdf file clearly, but ignores the images. The output may have some special characters here and there. But it is definitely readable.


    $ **less Linux-101-Hacks.pdf** ^LLinux 101 Hacks
    www.thegeekstuff.com
    o
    o
    o
    Chapter 1: Powerful CD Command Hacks
    cd is one of the most frequently used commands during a UNIX session.
    The cd command hacks mentioned in this chapter will boost your productivity

### File Type 2: How to open a word document file?


    $ **less pdb.doc** The Python Debugger Pdb
    =======================

    To use the debugger in its simplest form:

            >>> import pdb
            >>> pdb.run

    The debugger's prompt is Pdb.  This will stop in the first
    function call in

### File Type 3: How to open a jpg, jpeg, png file?

While opening a image file (jpeg, jpg and png), less command shows the following information:

  * Name of the file
  * Type of file
  * Number of pixels — width & height
  * Size of the file



```
    $ less testfile.jpeg
    testfile.jpeg JPEG 2304x1728 2304x1728+0+0 DirectClass 8-bit 1.57222mb 0.550u 0:02
```

**Note:** Similar kind of information will be displayed for other image file types.

### File Type 4: How to open an archived file (i.e *.tar) ?

While opening archive file it shows “ls -l” of the files available in the archive, so you can see the size of file, permissions of it and owner, group too.


    $ **less autocorrect.tar** -rwxrwxrwx anthony/anthony 84149 2009-02-02 03:20 autocorrect.dat
    -rwxrwxrwx anthony/anthony 443 2009-02-02 03:21 generator.rb
    -rwxrwxrwx anthony/anthony 181712 2009-02-02 03:21 autocorrect.vim


### File Type 5: How to open an archived, compressed file in gzip format (i.e *.tar.gz format) ?

For the archived and compressed file also less command shows the output in “ls -l” format.


    $ **less XML-Parser-2.36.tar.gz** drwxr-xr-x matt/matt 0 2007-11-20 19:58 XML-Parser-2.36/
    -rw-r--r-- matt/matt 25252 2007-11-20 19:52 XML-Parser-2.36/Changes
    drwxr-xr-x matt/matt 0 2007-11-20 19:58 XML-Parser-2.36/Expat/
    -rw-r--r-- matt/matt 3184 2003-07-27 16:37 XML-Parser-2.36/Expat/encoding.h
    -rw-r--r-- matt/matt 33917 2007-11-20 19:54 XML-Parser-2.36/Expat/Expat.pm
    -rw-r--r-- matt/matt 45555 2007-11-17 01:54 XML-Parser-2.36/Expat/Expat.xs


### File Type 6: How to open an archived and compressed file in zip format (i.e *.zip format)?

It shows the details of archived and compressed file in the following format.

```
    Archive: Archive name
    Length Method Size Ratio Date Time CRC-32 Name
    -------- ------ ------- ----- ---- ---- ------ ----
```

```
    $ less bash-support.zip Archive: bash-support.zip
    Length Method Size Ratio Date Time CRC-32 Name
    -------- ------ ------- ----- ---- ---- ------ ----
    0 Stored 0 0% 01-30-09 19:56 00000000 ftplugin/
    13488 Defl:N 2167 84% 01-30-09 19:53 b1bc6f3c ftplugin/sh.vim
    5567 Defl:N 1880 66% 01-30-09 02:16 0017a875 README.bashsupport
    0 Stored 0 0% 01-30-09 19:56 00000000 doc/
    41013 Defl:N 11574 72% 01-30-09 19:50 0cc22a14 doc/bashsupport.txt
    0 Stored 0 0% 01-30-09 19:56 00000000 bash-support/
    0 Stored 0 0% 01-30-09 19:56 00000000 bash-support/templates/
    513 Defl:N 187 64% 11-16-07 23:06 580ee37c bash-support/templates/bash-file-header
    246 Defl:N 80 68% 01-31-07 21:51 54706588 bash-support/templates/bash-function-description
    175 Defl:N 23 87% 01-31-07 21:51 22db9b2d bash-support/templates/bash-frame
    0 Stored 0 0% 01-30-09 19:56 00000000 bash-support/rc/
    6545 Defl:N 1807 72% 06-17-07 14:01 e7a27099 bash-support/rc/customization.vimrc
    2144 Defl:N 526 76% 01-31-07 21:51 f3a5e8dd bash-support/rc/customization.gvimrc
```

### File Type 7: How to open a compressed file gzip & bzip2.

Shows the content of the compressed file. If the file is only compressed and not archived then it shows the content of the file. However it does not shows the content of a zip file format, it shows the only the information in the format explained in File Type 7.

### File Type 8: How to open an ISO file?

While opening an iso file, it shows information about the iso file and then shows the content of the file.


    $ less knoppix_5.1.1.iso
    CD-ROM is in ISO 9660 format
    System id: LINUX
    Volume id: KNOPPIX
    Volume set id:
    Publisher id: KNOPPER.NET
    Data preparer id: www.knopper.net
    Application id: KNOPPIX LIVE LINUX CD
    Copyright File id:
    Abstract File id:
    Bibliographic File id:
    Volume set size is: 1
    Volume set sequence number is: 1
    Logical block size is: 2048
    Volume size is: 356532
    El Torito VD version 1 found, boot catalog is in sector 763
    Joliet with UCS level 3 found
    Rock Ridge signatures version 1 found
    Eltorito validation header:
    Hid 1
    Arch 0 (x86)
    ID 'KNOPPER.NET'
    Key 55 AA
    Eltorito defaultboot header:
    Bootid 88 (bootable)
    Boot media 0 (No Emulation Boot)
    Load segment 0
    Sys type 0
    Nsect 4
    Bootoff 312 786

    /KNOPPIX
    /autorun.bat
    /autorun.inf
    /autorun.pif
    /boot
    /cdrom.ico
    /index.html
    /KNOPPIX/KNOPPIX
    /KNOPPIX/KNOPPIX-FAQ-EN.txt


### File Type 9: How to open a deb file?

When you open a Debian file, it shows the information about that package and also the “ls -l” of the files available in that package as shown below.


    $ less lshw_02.08.01-1_i386.deb
    lshw_02.08.01-1_i386.deb:
    new debian package, version 2.0.
    size 295134 bytes: control archive= 730 bytes.
    678 bytes, 16 lines control
    246 bytes, 4 lines md5sums
    Package: lshw
    Version: 02.08.01-1
    Section: utils
    Priority: optional
    Architecture: i386
    Depends: libc6 (>= 2.3.6-6), libgcc1 (>= 1:4.1.0), libstdc++6 (>= 4.1.0), lshw-common
    Installed-Size: 716
    Maintainer: Ghe Rivero
    Description: information about hardware configuration
    A small tool to provide detailed information on the hardware
    configuration of the machine. It can report exact memory
    configuration, firmware version, mainboard configuration, CPU version
    and speed, cache configuration, bus speed, etc. on DMI-capable x86
    systems, on some PowerPC machines (PowerMac G4 is known to work) and AMD64.
    .
    Information can be output in plain text, HTML or XML.

    *** Contents:
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/bin/
    -rwxr-xr-x root/root 665052 2006-08-10 04:15 ./usr/bin/lshw
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/share/
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/share/man/
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/share/man/man1/
    -rw-r--r-- root/root 1874 2006-08-10 04:15 ./usr/share/man/man1/lshw.1.gz
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/share/lshw/
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/share/doc/
    drwxr-xr-x root/root 0 2006-08-10 04:15 ./usr/share/doc/lshw/
    -rw-r--r-- root/root 999 2006-08-10 04:13 ./usr/share/doc/lshw/copyright
    -rw-r--r-- root/root 1386 2006-08-10 04:13 ./usr/share/doc/lshw/changelog.Debian.gz


### File Type 10: How to open a rpm file?

less command can show the details of the rpm package, and its contents.


    $ **less openssl-devel-0.9.7a-43.16.i386.rpm**
    openssl-devel-0.9.7a-43.16.i386.rpm:
    Name : openssl-devel Relocations: (not relocatable)
    Version : 0.9.7a Vendor: Scientific Linux , http://www.scientificlinux.org
    Release : 43.16 Build Date: Thu May 3 12:18:00 2007
    Install Date: (not installed) Build Host: lxcert-i386.cern.ch
    Group : Development/Libraries Source RPM: openssl-0.9.7a-43.16.src.rpm
    Size : 3845246 License: BSDish
    Signature : DSA/SHA1, Wed May 9 15:03:20 2007, Key ID 5e03fde51d1e034b
    Packager : Jaroslaw Polok
    URL : http://www.openssl.org/
    Summary : Files for development of applications which will use OpenSSL.
    Description :
    OpenSSL is a toolkit for supporting cryptography. The openssl-devel
    package contains static libraries and include files needed to develop
    applications which support various cryptographic algorithms and
    protocols.

    *** Contents:
    /usr/include/openssl
    /usr/include/openssl/aes.h
    /usr/include/openssl/asn1.h
    /usr/include/openssl/asn1_mac.h
    /usr/include/openssl/asn1t.h
    /usr/include/openssl/bio.h
    /usr/include/openssl/blowfish.h
    /usr/include/openssl/bn.h
    /usr/include/openssl/buffer.h
    /usr/include/openssl/cast.h
    /usr/include/openssl/comp.h
    /usr/include/openssl/conf.h
    /usr/include/openssl/conf_api.h



_This article was written by **SathiyaMoorthy, author of**[15 Practical Linux Find Command Examples](http://www.thegeekstuff.com/2009/03/15-practical-linux-find-command-examples/) article. The Geek Stuff welcomes your tips and [guest articles](http://www.thegeekstuff.com/guest-blogging/)_
