# Korn Shell

The Korn shell (ksh) is a Unix shell which was developed by David Korn (AT&T Bell Laboratories) in the early 1980s. It is backwards-compatible with the Bourne shell and includes many features of the C shell as well, such as a command history, which was inspired by the requests of Bell Labs users.

The main advantage of ksh over the traditional Unix shell is in its use as a programming language. Since its conception, several features were gradually added, while maintaining strong backwards compatibility with the Bourne shell.

The ksh93 version supports associative arrays and built-in floating point arithmetic.

For interactive use, ksh provides the ability to edit the command line in a WYSIWYG fashion, by hitting the appropriate cursor-up or previous-line key-sequence to recall a previous command, and then edit the command as if the users were in edit line mode. Three modes are available, compatible with vi, emacs and gmacs.

ksh aims to respect the Shell Language Standard (POSIX 1003.2 "Shell and Utilities Language Committee").

Until 2000, Korn Shell remained AT&T's proprietary software. Since then it has been open source software, originally under a license peculiar to AT&T but, since the 93q release in early 2005, it has been licensed under the Common Public License. Korn Shell is available as part of the AT&T Software Technology (AST) Open Source Software Collection. As ksh was initially only available through a commercial license from AT&T, a number of free and open source alternatives were created. These include the public domain pdksh, the Free Software Foundation's Bourne-Again-Shell bash, and zsh.

Although the ksh93 version added many improvements (associative arrays, floating point arithmetic, etc.), some vendors still ship their own version of the older ksh88 as /bin/ksh, sometimes with extensions (as of 2005[update] only Solaris and NCR UNIX (a.k.a. MP-RAS) ship ksh88, all other Unix vendors migrated to ksh93 and even Linux distributions started shipping ksh93). There are also two modified versions of ksh93 which add features for manipulating the graphical user interface: dtksh which is part of CDE and tksh which provides access to the Tk widget toolkit.

SKsh is an AmigaOS version, that offers several Amiga-specific features such as ARexx interoperability.
