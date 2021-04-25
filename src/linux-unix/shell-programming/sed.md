
date: None  
author(s): None  

# [sed, a stream editor - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/sed)

<http://www.gnu.org/software/sed/manual/sed.html#Execution-Cycle>

This file documents version 4.1d of GNU sed, a stream editor. 

Copyright © 1998, 1999, 2001, 2002, 2003, 2004 Free Software Foundation, Inc. 

This document is released under the terms of the GNU Free Documentation License as published by the Free Software Foundation; either version 1.1, or (at your option) any later version. 

You should have received a copy of the GNU Free Documentation License along with GNU sed; see the file COPYING.DOC. If not, write to the Free Software Foundation, 59 Temple Place - Suite 330, Boston, MA 02110-1301, USA. 

There are no Cover Texts and no Invariant Sections; this text, along with its equivalent in the printed manual, constitutes the Title Page. 

\--- The detailed node listing --- 

sed Programs: 

Examples: 

Next: [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed), Previous: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## 1 Introduction

sed is a stream editor. A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline). While in some ways similar to an editor which permits scripted edits (such as ed), sed works by making only one pass over the input(s), and is consequently more efficient. But it is sed's ability to filter text in a pipeline which particularly distinguishes it from other types of editors. 

Next: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs), Previous: [Introduction](http://www.gnu.org/software/sed/manual/sed.html#Introduction), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## 2 Invocation

Normally sed is invoked like this: 
    
    
     sed SCRIPT INPUTFILE...  
    

The full format for invoking sed is: 
    
    
     sed OPTIONS... [SCRIPT] [INPUTFILE...]  
    

If you do not specify INPUTFILE, or if INPUTFILE is -, sed filters the contents of the standard input. The script is actually the first non-option parameter, which sed specially considers a script and not an input file if (and only if) none of the other options specifies a script to be executed, that is if neither of the -e and -f options is specified. 

sed may be invoked with the following command-line options: 

`--version`
    Print out the version of sed that is being run and a copyright notice, then exit.   

`--help`
    Print a usage message briefly summarizing these command-line options and the bug-reporting address, then exit.   

`-n`
`--quiet`
`--silent`
    By default, sed prints out the pattern space at the end of each cycle through the script. These options disable this automatic printing, and sed only produces output when explicitly told to via the `p` command.   

`-e `script
`--expression=`script
    Add the commands in script to the set of commands to be run while processing the input.   

`-f `script-file
`--file=`script-file
    Add the commands contained in the file script-file to the set of commands to be run while processing the input.   

`-i[`SUFFIX`]`
`--in-place[=`SUFFIX`]`
    This option specifies that files are to be edited in-place. GNU sed does this by creating a temporary file and sending output to this file rather than to the standard output.[1](http://www.gnu.org/software/sed/manual/sed.html#fn-1). 

This option implies -s. 

When the end of the file is reached, the temporary file is renamed to the output file's original name. The extension, if supplied, is used to modify the name of the old file before renaming the temporary file, thereby making a backup copy[2](http://www.gnu.org/software/sed/manual/sed.html#fn-2)). 

This rule is followed: if the extension doesn't contain a `*`, then it is appended to the end of the current filename as a suffix; if the extension does contain one or more `*` characters, then _each_ asterisk is replaced with the current filename. This allows you to add a prefix to the backup file, instead of (or in addition to) a suffix, or even to place backup copies of the original files into another directory (provided the directory already exists). 

If no extension is supplied, the original file is overwritten without making a backup.   


`-l `N
`--line-length=`N
    Specify the default line-wrap length for the `l` command. A length of 0 (zero) means to never wrap long lines. If not specified, it is taken to be 70.   

`--posix`
    GNU sed includes several extensions to POSIX sed. In order to simplify writing portable scripts, this option disables all the extensions that this manual documents, including additional commands. Most of the extensions accept sed programs that are outside the syntax mandated by POSIX, but some of them (such as the behavior of the N command described in see [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)) actually violate the standard. If you want to disable only the latter kind of extension, you can set the `POSIXLY_CORRECT` variable to a non-empty value.   

`-b`
`--binary`
    This option is available on every platform, but is only effective where the operating system makes a distinction between text files and binary files. When such a distinction is made—as is the case for MS-DOS, Windows, Cygwin—text files are composed of lines separated by a carriage return _and_ a line feed character, and  sed does not see the ending CR. When this option is specified, sed will open input files in binary mode, thus not requesting this special processing and considering lines to end at a line feed.   

`--follow-symlinks`
    This option is available only on platforms that support symbolic links and has an effect only if option -i is specified. In this case, if the file that is specified on the command line is a symbolic link, sed will follow the link and edit the ultimate destination of the link. The default behavior is to break the symbolic link, so that the link destination will not be modified.   

`-r`
`--regexp-extended`
    Use extended regular expressions rather than basic regular expressions. Extended regexps are those that egrep accepts; they can be clearer because they usually have less backslashes, but are a GNU extension and hence scripts that use them are not portable. See [Extended regular expressions](http://www.gnu.org/software/sed/manual/sed.html#Extended-regexps).   

`-s`
`--separate`
    By default, sed will consider the files specified on the command line as a single continuous long stream. This GNU sed extension allows the user to consider them as separate files: range addresses (such as `/abc/,/def/') are not allowed to span several files, line numbers are relative to the start of each file, `$` refers to the last line of each file, and files invoked from the `R` commands are rewound at the start of each file.   

`-u`
`--unbuffered`
    Buffer both input and output as minimally as practical. (This is particularly useful if the input is coming from the likes of `tail -f', and you wish to see the transformed output as soon as possible.) 

If no -e, -f, \--expression, or \--file options are given on the command-line, then the first non-option argument on the command line is taken to be the script to be executed. 

If any command-line parameters remain after processing the above, these parameters are interpreted as the names of input files to be processed. A file name of `-' refers to the standard input stream. The standard input will be processed if no file names are specified. 

Next: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples), Previous: [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## 3 sed Programs

A sed program consists of one or more sed commands, passed in by one or more of the -e, -f, \--expression, and \--file options, or the first non-option argument if zero of these options are used. This document will refer to “the” sed script; this is understood to mean the in-order catenation of all of the scripts and script-files passed in. 

Each `sed` command consists of an optional address or address range, followed by a one-character command name and any additional command-specific code. 

Next: [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.1 How sed Works

sed maintains two data buffers: the active _pattern_ space, and the auxiliary _hold_ space. Both are initially empty. 

sed operates by performing the following cycle on each lines of input: first, sed reads one line from the input stream, removes any trailing newline, and places it in the pattern space. Then commands are executed; each command can have an address associated to it: addresses are a kind of condition code, and a command is only executed if the condition is verified before the command is to be executed. 

When the end of the script is reached, unless the -n option is in use, the contents of pattern space are printed out to the output stream, adding back the trailing newline if it was removed.[3](http://www.gnu.org/software/sed/manual/sed.html#fn-3) Then the next cycle starts for the next input line. 

Unless special commands (like `D') are used, the pattern space is deleted between two cycles. The hold space, on the other hand, keeps its data between cycles (see commands `h', `H', `x', `g', `G' to move data between both buffers). 

Next: [Regular Expressions](http://www.gnu.org/software/sed/manual/sed.html#Regular-Expressions), Previous: [Execution Cycle](http://www.gnu.org/software/sed/manual/sed.html#Execution-Cycle), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.2 Selecting lines with sed

Addresses in a sed script can be in any of the following forms: 

number
    Specifying a line number will match only that line in the input. (Note that sed counts lines continuously across all input files unless -i or -s options are specified.)   

first`~`step
    This GNU extension matches every stepth line starting with line first. In particular, lines will be selected when there exists a non-negative n such that the current line-number equals first \+ (n * step). Thus, to select the odd-numbered lines, one would use `1~2`; to pick every third line starting with the second, `2~3' would be used; to pick every fifth line starting with the tenth, use `10~5'; and `50~0' is just an obscure way of saying `50`.   

`$`
    This address matches the last line of the last file of input, or the last line of each file when the -i or -s options are specified.   

`/`regexp`/`
    This will select any line which matches the regular expression regexp. If regexp itself includes any `/` characters, each must be escaped by a backslash (`\`). 

The empty regular expression `//' repeats the last regular expression match (the same holds if the empty regular expression is passed to the `s` command). Note that modifiers to regular expressions are evaluated when the regular expression is compiled, thus it is invalid to specify them together with the empty regular expression.   


`\%`regexp`%`
    (The `%` may be replaced by any other single character.) 

This also matches the regular expression regexp, but allows one to use a different delimiter than `/`. This is particularly useful if the regexp itself contains a lot of slashes, since it avoids the tedious escaping of every `/`. If regexp itself includes any delimiter characters, each must be escaped by a backslash (`\`).   


`/`regexp`/I`
`\%`regexp`%I`
    The `I` modifier to regular-expression matching is a GNU extension which causes the regexp to be matched in a case-insensitive manner.   

`/`regexp`/M`
`\%`regexp`%M`
    The `M` modifier to regular-expression matching is a GNU sed extension which causes `^` and `$` to match respectively (in addition to the normal behavior) the empty string after a newline, and the empty string before a newline. There are special character sequences (`\`` and `\'`) which always match the beginning or the end of the buffer. `M` stands for multi-line. 

If no addresses are given, then all lines are matched; if one address is given, then only lines matching that address are matched. 

An address range can be specified by specifying two addresses separated by a comma (`,`). An address range matches lines starting from where the first address matches, and continues until the second address matches (inclusively). 

If the second address is a regexp, then checking for the ending match will start with the line _following_ the line which matched the first address: a range will always span at least two lines (except of course if the input stream ends). 

If the second address is a number less than (or equal to) the line matching the first address, then only the one line is matched. 

GNU sed also supports some special two-address forms; all these are GNU extensions: 

`0,/`regexp`/`
    A line number of `0` can be used in an address specification like `0,/`regexp`/` so that sed will try to match regexp in the first input line too. In other words, `0,/`regexp`/` is similar to `1,/`regexp`/`, except that if addr2 matches the very first line of input the `0,/`regexp`/` form will consider it to end the range, whereas the `1,/`regexp`/` form will match the beginning of its range and hence make the range span up to the _second_ occurrence of the regular expression. 

Note that this is the only place where the `0` address makes sense; there is no 0-th line and commands which are given the `0` address in any other way will give an error.   


addr1`,+`N
    Matches addr1 and the N lines following addr1.   

addr1`,~`N
    Matches addr1 and the lines following addr1 until the next line whose input line number is a multiple of N. 

Appending the `!` character to the end of an address specification negates the sense of the match. That is, if the `!` character follows an address range, then only lines which do _not_ match the address range will be selected. This also works for singleton addresses, and, perhaps perversely, for the null address. 

Next: [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands), Previous: [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.3 Overview of Regular Expression Syntax

To know how to use sed, people should understand regular expressions (regexp for short). A regular expression is a pattern that is matched against a subject string from left to right. Most characters are ordinary: they stand for themselves in a pattern, and match the corresponding characters in the subject. As a trivial example, the pattern 
    
    
     The quick brown fox  
    

matches a portion of a subject string that is identical to itself. The power of regular expressions comes from the ability to include alternatives and repetitions in the pattern. These are encoded in the pattern by the use of special characters, which do not stand for themselves but instead are interpreted in some special way. Here is a brief description of regular expression syntax as used in sed. 

char
    A single ordinary character matches itself.   

`*`
    Matches a sequence of zero or more instances of matches for the preceding regular expression, which must be an ordinary character, a special character preceded by `\`, a `.`, a grouped regexp (see below), or a bracket expression. As a GNU extension, a postfixed regular expression can also be followed by `*`; for example, `a**` is equivalent to `a*`. POSIX 1003.1-2001 says that `*` stands for itself when it appears at the start of a regular expression or subexpression, but many nonGNU implementations do not support this and portable scripts should instead use `\*` in these contexts.   

`\+`
    As `*`, but matches one or more. It is a GNU extension.   

`\?`
    As `*`, but only matches zero or one. It is a GNU extension.   

`\{`i`\}`
    As `*`, but matches exactly i sequences (i is a decimal integer; for portability, keep it between 0 and 255 inclusive).   

`\{`i`,`j`\}`
    Matches between i and j, inclusive, sequences.   

`\{`i`,\}`
    Matches more than or equal to i sequences.   

`\(`regexp`\)`
    Groups the inner regexp as a whole, this is used to: 

  * Apply postfix operators, like `\(abcd\)*`: this will search for zero or more whole sequences of `abcd', while `abcd*` would search for `abc' followed by zero or more occurrences of `d'. Note that support for `\(abcd\)*` is required by POSIX 1003.1-2001, but many non-GNU implementations do not support it and hence it is not universally portable. 
  * Use back references (see below). 

  

`.`
    Matches any character, including newline.   

`^`
    Matches the null string at beginning of line, i.e. what appears after the circumflex must appear at the beginning of line. `^#include` will match only lines where `#include' is the first thing on line—if there are spaces before, for example, the match fails. `^` acts as a special character only at the beginning of the regular expression or subexpression (that is, after `\(` or `\|`). Portable scripts should avoid `^` at the beginning of a subexpression, though, as POSIX allows implementations that treat `^` as an ordinary character in that context.   

`$`
    It is the same as `^`, but refers to end of line. `$` also acts as a special character only at the end of the regular expression or subexpression (that is, before `\)` or `\|`), and its use at the end of a subexpression is not portable.   

`[`list`]`
`[^`list`]`
    Matches any single character in list: for example, `[aeiou]` matches all vowels. A list may include sequences like char1`-`char2, which matches any character between (inclusive) char1 and char2. 

A leading `^` reverses the meaning of list, so that it matches any single character _not_ in  list. To include `]` in the list, make it the first character (after the `^` if needed), to include `-` in the list, make it the first or last; to include `^` put it after the first character. 

The characters `$`, `*`, `.`, `[`, and `\` are normally not special within list. For example, `[\*]` matches either `\' or `*', because the `\` is not special here. However, strings like `[.ch.]`, `[=a=]`, and `[:space:]` are special within list and represent collating symbols, equivalence classes, and character classes, respectively, and `[` is therefore special within list when it is followed by `.`, `=`, or `:`. Also, when not in POSIXLY_CORRECT mode, special escapes like `\n` and `\t` are recognized within list. See [Escapes](http://www.gnu.org/software/sed/manual/sed.html#Escapes).   


regexp1`\|`regexp2
    Matches either regexp1 or regexp2. Use parentheses to use complex alternative regular expressions. The matching process tries each alternative in turn, from left to right, and the first one that succeeds is used. It is a GNU extension.   

regexp1regexp2
    Matches the concatenation of regexp1 and regexp2. Concatenation binds more tightly than `\|`, `^`, and `$`, but less tightly than the other regular expression operators.   

`\`digit
    Matches the digit-th `\(...\)` parenthesized subexpression in the regular expression. This is called a back reference. Subexpressions are implicity numbered by counting occurrences of `\(` left-to-right.   

`\n`
    Matches the newline character.   

`\`char
    Matches char, where char is one of `$`, `*`, `.`, `[`, `\`, or `^`. Note that the only C-like backslash sequences that you can portably assume to be interpreted are `\n` and `\\`; in particular `\t` is not portable, and matches a `t' under most implementations of sed, rather than a tab character. 

Note that the regular expression matcher is greedy, i.e., matches are attempted from left to right and, if two or more matches are possible starting at the same character, it selects the longest. 

Examples: 

`abcdef'
    Matches `abcdef'.   

`a*b'
    Matches zero or more `a's followed by a single `b'. For example, `b' or `aaaaab'.   

`a\?b'
    Matches `b' or `ab'.   

`a\\+b\\+'
    Matches one or more `a's followed by one or more `b's: `ab' is the shortest possible match, but other examples are `aaaab' or `abbbbb' or `aaaaaabbbbbbb'.   

`.*'
`.\\+'
    These two both match all the characters in a string; however, the first matches every string (including the empty string), while the second matches only strings containing at least one character.   

`^main.*(.*)'
    his matches a string starting with `main', followed by an opening and closing parenthesis. The `n', `(' and `)' need not be adjacent.   

`^#'
    This matches a string beginning with `#'.   

`\\\$'
    This matches a string ending with a single backslash. The regexp contains two backslashes for escaping.   

`\$'
    Instead, this matches a string consisting of a single dollar sign, because it is escaped.   

`[a-zA-Z0-9]'
    In the C locale, this matches any ASCII letters or digits.   

`[^ `tab`]\\+'
    (Here `tab` stands for a single tab character.) This matches a string of one or more characters, none of which is a space or a tab. Usually this means a word.   

`^\\(.*\\)\n\1$'
    This matches a string consisting of two equal substrings separated by a newline.   

`.\\{9\\}A$'
    This matches nine characters followed by an `A'.   

`^.\\{15\\}A'
    This matches the start of a string that contains 16 characters, the last of which is an `A'. 

Next: [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command), Previous: [Regular Expressions](http://www.gnu.org/software/sed/manual/sed.html#Regular-Expressions), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.4 Often-Used Commands

If you use sed at all, you will quite likely want to know these commands. 

`#`
    [No addresses allowed.] 

The `#` character begins a comment; the comment continues until the next newline. 

If you are concerned about portability, be aware that some implementations of sed (which are not posix conformant) may only support a single one-line comment, and then only when the very first character of the script is a `#`. 

Warning: if the first two characters of the sed script are `#n`, then the -n (no-autoprint) option is forced. If you want to put a comment in the first line of your script and that comment begins with the letter `n' and you do not want this behavior, then be sure to either use a capital `N', or place at least one space before the `n'.   


`q [`exit-code`]`
    This command only accepts a single address. 

Exit sed without processing any more commands or input. Note that the current pattern space is printed if auto-print is not disabled with the -n options. The ability to return an exit code from the sed script is a GNU sed extension.   


`d`
    Delete the pattern space; immediately start next cycle.   

`p`
    Print out the pattern space (to the standard output). This command is usually only used in conjunction with the -n command-line option.   

`n`
    If auto-print is not disabled, print the pattern space, then, regardless, replace the pattern space with the next line of input. If there is no more input then sed exits without processing any more commands.   

`{ `commands` }`
    A group of commands may be enclosed between `{` and `}` characters. This is particularly useful when you want a group of commands to be triggered by a single address (or address-range) match. 

Next: [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands), Previous: [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.5 The `s` Command

The syntax of the `s` (as in substitute) command is `s/regexp/replacement/flags'. The `/` characters may be uniformly replaced by any other single character within any given `s` command. The `/` character (or whatever other character is used in its stead) can appear in the regexp or replacement only if it is preceded by a `\` character. 

The `s` command is probably the most important in sed and has a lot of different options. Its basic concept is simple: the `s` command attempts to match the pattern space against the supplied regexp; if the match is successful, then that portion of the pattern space which was matched is replaced with replacement. 

The replacement can contain `\`n (n being a number from 1 to 9, inclusive) references, which refer to the portion of the match which is contained between the nth `\(` and its matching `\)`. Also, the replacement can contain unescaped `&` characters which reference the whole matched portion of the pattern space. Finally, as a GNU sed extension, you can include a special sequence made of a backslash and one of the letters `L`, `l`, `U`, `u`, or `E`. The meaning is as follows: 

`\L`
    Turn the replacement to lowercase until a `\U` or `\E` is found,   

`\l`
    Turn the next character to lowercase,   

`\U`
    Turn the replacement to uppercase until a `\L` or `\E` is found,   

`\u`
    Turn the next character to uppercase,   

`\E`
    Stop case conversion started by `\L` or `\U`. 

To include a literal `\`, `&`, or newline in the final replacement, be sure to precede the desired `\`, `&`, or newline in the replacement with a `\`. 

The `s` command can be followed by zero or more of the following flags: 

`g`
    Apply the replacement to _all_ matches to the  regexp, not just the first.   

number
    Only replace the numberth match of the regexp. 

Note: the posix standard does not specify what should happen when you mix the `g` and number modifiers, and currently there is no widely agreed upon meaning across sed implementations. For GNU sed, the interaction is defined to be: ignore matches before the numberth, and then match and replace all matches from the numberth on.   


`p`
    If the substitution was made, then print the new pattern space. 

Note: when both the `p` and `e` options are specified, the relative ordering of the two produces very different results. In general, `ep` (evaluate then print) is what you want, but operating the other way round can be useful for debugging. For this reason, the current version of GNU sed interprets specially the presence of `p` options both before and after `e`, printing the pattern space before and after evaluation, while in general flags for the `s` command show their effect just once. This behavior, although documented, might change in future versions.   


`w `file-name
    If the substitution was made, then write out the result to the named file. As a GNU sed extension, two special values of file-name are supported: /dev/stderr, which writes the result to the standard error, and /dev/stdout, which writes to the standard output.[4](http://www.gnu.org/software/sed/manual/sed.html#fn-4)   

`e`
    This command allows one to pipe input from a shell command into pattern space. If a substitution was made, the command that is found in pattern space is executed and pattern space is replaced with its output. A trailing newline is suppressed; results are undefined if the command to be executed contains a nul character. This is a GNU sed extension.   

`I`
`i`
    The `I` modifier to regular-expression matching is a GNU extension which makes sed match regexp in a case-insensitive manner.   

`M`
`m`
    The `M` modifier to regular-expression matching is a GNU sed extension which causes `^` and `$` to match respectively (in addition to the normal behavior) the empty string after a newline, and the empty string before a newline. There are special character sequences (`\`` and `\'`) which always match the beginning or the end of the buffer. `M` stands for multi-line. 

Next: [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands), Previous: [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.6 Less Frequently-Used Commands

Though perhaps less frequently used than those in the previous section, some very small yet useful sed scripts can be built with these commands. 

`y/`source-chars`/`dest-chars`/`
    (The `/` characters may be uniformly replaced by any other single character within any given `y` command.) 

Transliterate any characters in the pattern space which match any of the source-chars with the corresponding character in dest-chars. 

Instances of the `/` (or whatever other character is used in its stead), `\`, or newlines can appear in the source-chars or dest-chars lists, provide that each instance is escaped by a `\`. The source-chars and dest-chars lists _must_ contain the same number of characters (after de-escaping).   


`a\`
text
    As a GNU extension, this command accepts two addresses. 

Queue the lines of text which follow this command (each but the last ending with a `\`, which are removed from the output) to be output at the end of the current cycle, or when the next input line is read. 

Escape sequences in text are processed, so you should use `\\` in text to print a single backslash. 

As a GNU extension, if between the `a` and the newline there is other than a whitespace-`\` sequence, then the text of this line, starting at the first non-whitespace character after the `a`, is taken as the first line of the text block. (This enables a simplification in scripting a one-line add.) This extension also works with the `i` and `c` commands.   


`i\`
text
    As a GNU extension, this command accepts two addresses. 

Immediately output the lines of text which follow this command (each but the last ending with a `\`, which are removed from the output).   


`c\`
text
    Delete the lines matching the address or address-range, and output the lines of text which follow this command (each but the last ending with a `\`, which are removed from the output) in place of the last line (or in place of each line, if no addresses were specified). A new cycle is started after this command is done, since the pattern space will have been deleted.   

`=`
    As a GNU extension, this command accepts two addresses. 

Print out the current input line number (with a trailing newline).   


`l `n
    Print the pattern space in an unambiguous form: non-printable characters (and the `\` character) are printed in C-style escaped form; long lines are split, with a trailing `\` character to indicate the split; the end of each line is marked with a `$`. 

n specifies the desired line-wrap length; a length of 0 (zero) means to never wrap long lines. If omitted, the default as specified on the command line is used. The n parameter is a GNU sed extension.   


`r `filename
    As a GNU extension, this command accepts two addresses. 

Queue the contents of filename to be read and inserted into the output stream at the end of the current cycle, or when the next input line is read. Note that if filename cannot be read, it is treated as if it were an empty file, without any error indication. 

As a GNU sed extension, the special value /dev/stdin is supported for the file name, which reads the contents of the standard input.   


`w `filename
    Write the pattern space to filename. As a GNU sed extension, two special values of file-name are supported: /dev/stderr, which writes the result to the standard error, and /dev/stdout, which writes to the standard output.[5](http://www.gnu.org/software/sed/manual/sed.html#fn-5)

The file will be created (or truncated) before the first input line is read; all `w` commands (including instances of `w` flag on successful `s` commands) which refer to the same filename are output without closing and reopening the file.   


`D`
    Delete text in the pattern space up to the first newline. If any text is left, restart cycle with the resultant pattern space (without reading a new line of input), otherwise start a normal new cycle.   

`N`
    Add a newline to the pattern space, then append the next line of input to the pattern space. If there is no more input then sed exits without processing any more commands.   

`P`
    Print out the portion of the pattern space up to the first newline.   

`h`
    Replace the contents of the hold space with the contents of the pattern space.   

`H`
    Append a newline to the contents of the hold space, and then append the contents of the pattern space to that of the hold space.   

`g`
    Replace the contents of the pattern space with the contents of the hold space.   

`G`
    Append a newline to the contents of the pattern space, and then append the contents of the hold space to that of the pattern space.   

`x`
    Exchange the contents of the hold and pattern spaces. 

Next: [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands), Previous: [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.7 Commands for sed gurus

In most cases, use of these commands indicates that you are probably better off programming in something like awk or Perl. But occasionally one is committed to sticking with sed, and these commands can enable one to write quite convoluted scripts. 

`: `label
    [No addresses allowed.] 

Specify the location of label for branch commands. In all other respects, a no-op.   


`b `label
    Unconditionally branch to label. The label may be omitted, in which case the next cycle is started.   

`t `label
    Branch to label only if there has been a successful `s`ubstitution since the last input line was read or conditional branch was taken. The label may be omitted, in which case the next cycle is started. 

Next: [Escapes](http://www.gnu.org/software/sed/manual/sed.html#Escapes), Previous: [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.8 Commands Specific to GNU sed

These commands are specific to GNU sed, so you must use them with care and only when you are sure that hindering portability is not evil. They allow you to check for GNU sed extensions or to do tasks that are required quite often, yet are unsupported by standard seds. 

`e [`command`]`
    This command allows one to pipe input from a shell command into pattern space. Without parameters, the `e` command executes the command that is found in pattern space and replaces the pattern space with the output; a trailing newline is suppressed. 

If a parameter is specified, instead, the `e` command interprets it as a command and sends its output to the output stream (like `r` does). The command can run across multiple lines, all but the last ending with a back-slash. 

In both cases, the results are undefined if the command to be executed contains a nul character.   


`L `n
    This GNU sed extension fills and joins lines in pattern space to produce output lines of (at most) n characters, like `fmt` does; if n is omitted, the default as specified on the command line is used. This command is considered a failed experiment and unless there is enough request (which seems unlikely) will be removed in future versions.   

`Q [`exit-code`]`
    This command only accepts a single address. 

This command is the same as `q`, but will not print the contents of pattern space. Like `q`, it provides the ability to return an exit code to the caller. 

This command can be useful because the only alternative ways to accomplish this apparently trivial function are to use the -n option (which can unnecessarily complicate your script) or resorting to the following snippet, which wastes time by reading the whole file without any visible effect: 
    
    
     :eat  
     $d Quit silently on the last line  
     N Read another line, silently  
     g Overwrite pattern space each time to save memory          b eat

  

`R `filename
    Queue a line of filename to be read and inserted into the output stream at the end of the current cycle, or when the next input line is read. Note that if filename cannot be read, or if its end is reached, no line is appended, without any error indication. 

As with the `r` command, the special value /dev/stdin is supported for the file name, which reads a line from the standard input.   


`T `label
    Branch to label only if there have been no successful `s`ubstitutions since the last input line was read or conditional branch was taken. The label may be omitted, in which case the next cycle is started.   

`v `version
    This command does nothing, but makes sed fail if GNU sed extensions are not supported, simply because other versions of sed do not implement it. In addition, you can specify the version of sed that your script requires, such as `4.0.5`. The default is `4.0` because that is the first version that implemented this command. 

This command enables all GNU extensions even if POSIXLY_CORRECT is set in the environment.   


`W `filename
    Write to the given filename the portion of the pattern space up to the first newline. Everything said under the `w` command about file handling holds here too. 

Previous: [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands), Up: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)

### 3.9 GNU Extensions for Escapes in Regular Expressions

Until this chapter, we have only encountered escapes of the form `\^', which tell sed not to interpret the circumflex as a special character, but rather to take it literally. For example, `\\*' matches a single asterisk rather than zero or more backslashes. 

This chapter introduces another kind of escape[6](http://www.gnu.org/software/sed/manual/sed.html#fn-6)—that is, escapes that are applied to a character or sequence of characters that ordinarily are taken literally, and that sed replaces with a special character. This provides a way of encoding non-printable characters in patterns in a visible manner. There is no restriction on the appearance of non-printing characters in a sed script but when a script is being prepared in the shell or by text editing, it is usually easier to use one of the following escape sequences than the binary character it represents: 

The list of these escapes is: 

`\a`
    Produces or matches a bel character, that is an “alert” (ascii 7).   

`\f`
    Produces or matches a form feed (ascii 12).   

`\n`
    Produces or matches a newline (ascii 10).   

`\r`
    Produces or matches a carriage return (ascii 13).   

`\t`
    Produces or matches a horizontal tab (ascii 9).   

`\v`
    Produces or matches a so called “vertical tab” (ascii 11).   

`\c`x
    Produces or matches Control`-`x, where x is any character. The precise effect of `\cx' is as follows: if x is a lower case letter, it is converted to upper case. Then bit 6 of the character (hex 40) is inverted. Thus `\cz' becomes hex 1A, but `\c{' becomes hex 3B, while `\c;' becomes hex 7B.   

`\d`xxx
    Produces or matches a character whose decimal ascii value is xxx.   

`\o`xxx
    Produces or matches a character whose octal ascii value is xxx.   

`\x`xx
    Produces or matches a character whose hexadecimal ascii value is xx. 

`\b' (backspace) was omitted because of the conflict with the existing “word boundary” meaning. 

Other escapes match a particular character class and are valid only in regular expressions: 

`\w`
    Matches any “word” character. A “word” character is any letter or digit or the underscore character.   

`\W`
    Matches any “non-word” character.   

`\b`
    Matches a word boundary; that is it matches if the character to the left is a “word” character and the character to the right is a “non-word” character, or vice-versa.   

`\B`
    Matches everywhere but on a word boundary; that is it matches if the character to the left and the character to the right are either both “word” characters or both “non-word” characters.   

`\``
    Matches only at the start of pattern space. This is different from `^` in multi-line mode.   

`\'`
    Matches only at the end of pattern space. This is different from `$` in multi-line mode. 

Next: [Limitations](http://www.gnu.org/software/sed/manual/sed.html#Limitations), Previous: [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## 4 Some Sample Scripts

Here are some sed scripts to guide you in the art of mastering sed. 

Some exotic examples: 

Emulating standard utilities: 

  * [tac](http://www.gnu.org/software/sed/manual/sed.html#tac): Reverse lines of files 
  * [cat -n](http://www.gnu.org/software/sed/manual/sed.html#cat-_002dn): Numbering lines 
  * [cat -b](http://www.gnu.org/software/sed/manual/sed.html#cat-_002db): Numbering non-blank lines 
  * [wc -c](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dc): Counting chars 
  * [wc -w](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dw): Counting words 
  * [wc -l](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dl): Counting lines 
  * [head](http://www.gnu.org/software/sed/manual/sed.html#head): Printing the first lines 
  * [tail](http://www.gnu.org/software/sed/manual/sed.html#tail): Printing the last lines 
  * [uniq](http://www.gnu.org/software/sed/manual/sed.html#uniq): Make duplicate lines unique 
  * [uniq -d](http://www.gnu.org/software/sed/manual/sed.html#uniq-_002dd): Print duplicated lines of input 
  * [uniq -u](http://www.gnu.org/software/sed/manual/sed.html#uniq-_002du): Remove all duplicated lines 
  * [cat -s](http://www.gnu.org/software/sed/manual/sed.html#cat-_002ds): Squeezing blank lines 



Next: [Increment a number](http://www.gnu.org/software/sed/manual/sed.html#Increment-a-number), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.1 Centering Lines

This script centers all lines of a file on a 80 columns width. To change that width, the number in `\{...\}` must be replaced, and the number of added spaces also must be changed. 

Note how the buffer commands are used to separate parts in the regular expressions to be matched—this is a common technique. 
    
    
     #!/usr/bin/sed -f # Put 80 spaces in the buffer 1 { x s/^$/ / s/^.*$/&&&&&&&&/ x } # del leading and trailing spaces
    
     y/tab/ /
    
         s/^ *//     s/ *$//          # add a newline and 80 spaces to end of line     G          # keep first 81 chars (80 + a newline)     s/^\(.\{81\}\).*$/\1/          # \2 matches half of the spaces, which are moved to the beginning     s/^\(.*\)\n\(.*\)\2/\2\1/

Next: [Rename files to lower case](http://www.gnu.org/software/sed/manual/sed.html#Rename-files-to-lower-case), Previous: [Centering lines](http://www.gnu.org/software/sed/manual/sed.html#Centering-lines), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.2 Increment a Number

This script is one of a few that demonstrate how to do arithmetic in sed. This is indeed possible,[7](http://www.gnu.org/software/sed/manual/sed.html#fn-7) but must be done manually. 

To increment one number you just add 1 to last digit, replacing it by the following digit. There is one exception: when the digit is a nine the previous digits must be also incremented until you don't have a nine. 

This solution by Bruno Haible is very clever and smart because it uses a single buffer; if you don't have this limitation, the algorithm used in [Numbering lines](http://www.gnu.org/software/sed/manual/sed.html#cat-_002dn), is faster. It works by replacing trailing nines with an underscore, then using multiple `s` commands to increment the last digit, and then again substituting underscores with zeros. 
    
    
     #!/usr/bin/sed -f /[^0-9]/ d # replace all leading 9s by _ (any other character except digits, could # be used) :d s/9\(_*\)$/_\1/ td # incr last digit only. The first line adds a most-significant # digit of 1 if we have to add a digit. #
    
     # The tn commands are not necessary, but make the thing
    
         # faster          s/^\(_*\)$/1\1/; tn     s/8\(_*\)$/9\1/; tn     s/7\(_*\)$/8\1/; tn     s/6\(_*\)$/7\1/; tn     s/5\(_*\)$/6\1/; tn     s/4\(_*\)$/5\1/; tn     s/3\(_*\)$/4\1/; tn     s/2\(_*\)$/3\1/; tn     s/1\(_*\)$/2\1/; tn     s/0\(_*\)$/1\1/; tn          :n     y/_/0/

Next: [Print bash environment](http://www.gnu.org/software/sed/manual/sed.html#Print-bash-environment), Previous: [Increment a number](http://www.gnu.org/software/sed/manual/sed.html#Increment-a-number), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.3 Rename Files to Lower Case

This is a pretty strange use of sed. We transform text, and transform it to be shell commands, then just feed them to shell. Don't worry, even worse hacks are done when using sed; I have seen a script converting the output of date into a bc program! 

The main body of this is the sed script, which remaps the name from lower to upper (or vice-versa) and even checks out if the remapped name is the same as the original name. Note how the script is parameterized using shell variables and proper quoting. 
    
    
         #! /bin/sh     # rename files to lower/upper case...     #     # usage:     #    move-to-lower *     #    move-to-upper *     # or     #    move-to-lower -R .     #    move-to-upper -R .     #          help()     {     	cat << eof     Usage: $0 [-n] [-r] [-h] files...          -n      do nothing, only see what would be done     -R      recursive (use find)     -h      this message     files   files to remap to lower case          Examples:            $0 -n *        (see if everything is ok, then...)            $0 *                 $0 -R .          eof     }          apply_cmd='sh'     finder='echo "$@" | tr " " "\n"'     files_only=          while :     do         case "$1" in             -n) apply_cmd='cat' ;;             -R) finder='find "$@" -type f';;             -h) help ; exit 1 ;;             *) break ;;         esac         shift     done          if [ -z "$1" ]; then             echo Usage: $0 [-h] [-n] [-r] files...             exit 1     fi          LOWER='abcdefghijklmnopqrstuvwxyz'     UPPER='ABCDEFGHIJKLMNOPQRSTUVWXYZ'          case `basename $0` in             *upper*) TO=$UPPER; FROM=$LOWER ;;             *)       FROM=$UPPER; TO=$LOWER ;;     esac          eval $finder | sed -n '          # remove all trailing slashes     s/\/*$//          # add ./ if there is no path, only a filename     /\//! s/^/.\//          # save path+filename     h          # remove path     s/.*\///          # do conversion only on filename     y/'$FROM'/'$TO'/          # now line contains original path+file, while     # hold space contains the new filename     x          # add converted file name to line, which now contains     # path/file-name\nconverted-file-name     G          # check if converted file name is equal to original file name,     # if it is, do not print nothing     /^.*\/\(.*\)\n\1/b          # now, transform path/fromfile\n, into     # mv path/fromfile path/tofile and print it     s/^\(.*\/\)\(.*\)\n\(.*\)$/mv "\1\2" "\1\3"/p          ' | $apply_cmd

### 4.4 Print bash Environment

This script strips the definition of the shell functions from the output of the set Bourne-shell command. 
    
    
     #!/bin/sh set | sed -n ' :x 
    
     # if no occurrence of `=()' print and load next line
    
         /=()/! { p; b; }     / () $/! { p; b; }          # possible start of functions section     # save the line in case this is a var like FOO="() "     h          # if the next line has a brace, we quit because     # nothing comes after functions     n     /^{/ q          # print the old line     x; p          # work on the new line now     x; bx     '

Next: [tac](http://www.gnu.org/software/sed/manual/sed.html#tac), Previous: [Print bash environment](http://www.gnu.org/software/sed/manual/sed.html#Print-bash-environment), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.5 Reverse Characters of Lines

This script can be used to reverse the position of characters in lines. The technique moves two characters at a time, hence it is faster than more intuitive implementations. 

Note the `tx` command before the definition of the label. This is often needed to reset the flag that is tested by the `t` command. 

Imaginative readers will find uses for this script. An example is reversing the output of banner.[8](http://www.gnu.org/software/sed/manual/sed.html#fn-8)
    
    
         #!/usr/bin/sed -f          /../! b          # Reverse a line.  Begin embedding the line between two newlines     s/^.*$/\     &\     /          # Move first character at the end.  The regexp matches until     # there are zero or one characters between the markers     tx     :x     s/\(\n.\)\(.*\)\(.\n\)/\3\2\1/     tx          # Remove the newline markers     s/\n//g

Next: [cat -n](http://www.gnu.org/software/sed/manual/sed.html#cat-_002dn), Previous: [Reverse chars of lines](http://www.gnu.org/software/sed/manual/sed.html#Reverse-chars-of-lines), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.6 Reverse Lines of Files

This one begins a series of totally useless (yet interesting) scripts emulating various Unix commands. This, in particular, is a tac workalike. 

Note that on implementations other than GNU sed this script might easily overflow internal buffers. 
    
    
         #!/usr/bin/sed -nf          # reverse all lines of input, i.e. first line became last, ...          # from the second line, the buffer (which contains all previous lines)     # is *appended* to current line, so, the order will be reversed     1! G          # on the last line we're done -- print everything     $ p          # store everything on the buffer again     h

Next: [cat -b](http://www.gnu.org/software/sed/manual/sed.html#cat-_002db), Previous: [tac](http://www.gnu.org/software/sed/manual/sed.html#tac), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.7 Numbering Lines

This script replaces `cat -n'; in fact it formats its output exactly like GNU cat does. 

Of course this is completely useless and for two reasons: first, because somebody else did it in C, second, because the following Bourne-shell script could be used for the same purpose and would be much faster: 
    
    
         #! /bin/sh     sed -e "=" $@ | sed -e '       s/^/      /       N       s/^ *\(......\)\n/\1  /     '

It uses sed to print the line number, then groups lines two by two using `N`. Of course, this script does not teach as much as the one presented below. 

The algorithm used for incrementing uses both buffers, so the line is printed as soon as possible and then discarded. The number is split so that changing digits go in a buffer and unchanged ones go in the other; the changed digits are modified in a single step (using a `y` command). The line number for the next line is then composed and stored in the hold space, to be used in the next iteration. 
    
    
         #!/usr/bin/sed -nf          # Prime the pump on the first line     x     /^$/ s/^.*$/1/          # Add the correct line number before the pattern     G     h          # Format it and print it     s/^/      /     s/^ *\(......\)\n/\1  /p          # Get the line number from hold space; add a zero     # if we're going to add a digit on the next line     g     s/\n.*$//     /^9*$/ s/^/0/          # separate changing/unchanged digits with an x     s/.9*$/x&/          # keep changing digits in hold space     h     s/^.*x//     y/0123456789/1234567890/     x          # keep unchanged digits in pattern space     s/x.*$//          # compose the new number, remove the newline implicitly added by G     G     s/\n//     h

Next: [wc -c](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dc), Previous: [cat -n](http://www.gnu.org/software/sed/manual/sed.html#cat-_002dn), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.8 Numbering Non-blank Lines

Emulating `cat -b' is almost the same as `cat -n'—we only have to select which lines are to be numbered and which are not. 

The part that is common to this script and the previous one is not commented to show how important it is to comment sed scripts properly... 
    
    
         #!/usr/bin/sed -nf          /^$/ {       p       b     }          # Same as cat -n from now     x     /^$/ s/^.*$/1/     G     h     s/^/      /     s/^ *\(......\)\n/\1  /p     x     s/\n.*$//     /^9*$/ s/^/0/     s/.9*$/x&/     h     s/^.*x//     y/0123456789/1234567890/     x     s/x.*$//     G     s/\n//     h

Next: [wc -w](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dw), Previous: [cat -b](http://www.gnu.org/software/sed/manual/sed.html#cat-_002db), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.9 Counting Characters

This script shows another way to do arithmetic with sed. In this case we have to add possibly large numbers, so implementing this by successive increments would not be feasible (and possibly even more complicated to contrive than this script). 

The approach is to map numbers to letters, kind of an abacus implemented with sed. `a's are units, `b's are tens and so on: we simply add the number of characters on the current line as units, and then propagate the carry to tens, hundreds, and so on. 

As usual, running totals are kept in hold space. 

On the last line, we convert the abacus form back to decimal. For the sake of variety, this is done with a loop rather than with some 80 `s` commands[9](http://www.gnu.org/software/sed/manual/sed.html#fn-9): first we convert units, removing `a's from the number; then we rotate letters so that tens become `a's, and so on until no more letters remain. 
    
    
         #!/usr/bin/sed -nf          # Add n+1 a's to hold space (+1 is for the newline)     s/./a/g     H     x     s/\n/a/          # Do the carry.  The t's and b's are not necessary,     # but they do speed up the thing     t a     : a;  s/aaaaaaaaaa/b/g; t b; b done     : b;  s/bbbbbbbbbb/c/g; t c; b done     : c;  s/cccccccccc/d/g; t d; b done     : d;  s/dddddddddd/e/g; t e; b done     : e;  s/eeeeeeeeee/f/g; t f; b done     : f;  s/ffffffffff/g/g; t g; b done     : g;  s/gggggggggg/h/g; t h; b done     : h;  s/hhhhhhhhhh//g          : done     $! {       h       b     }          # On the last line, convert back to decimal          : loop     /a/! s/[b-h]*/&0/     s/aaaaaaaaa/9/     s/aaaaaaaa/8/     s/aaaaaaa/7/     s/aaaaaa/6/     s/aaaaa/5/     s/aaaa/4/     s/aaa/3/     s/aa/2/     s/a/1/          : next     y/bcdefgh/abcdefg/     /[a-h]/ b loop     p

Next: [wc -l](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dl), Previous: [wc -c](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dc), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.10 Counting Words

This script is almost the same as the previous one, once each of the words on the line is converted to a single `a' (in the previous script each letter was changed to an `a'). 

It is interesting that real wc programs have optimized loops for `wc -c', so they are much slower at counting words rather than characters. This script's bottleneck, instead, is arithmetic, and hence the word-counting one is faster (it has to manage smaller numbers). 

Again, the common parts are not commented to show the importance of commenting sed scripts. 
    
    
     #!/usr/bin/sed -nf # Convert words to a's
    
     s/[ tab][ tab]*/ /g
    
         s/^/ /     s/ [^ ][^ ]*/a /g     s/ //g          # Append them to hold space     H     x     s/\n//          # From here on it is the same as in wc -c.     /aaaaaaaaaa/! bx;   s/aaaaaaaaaa/b/g     /bbbbbbbbbb/! bx;   s/bbbbbbbbbb/c/g     /cccccccccc/! bx;   s/cccccccccc/d/g     /dddddddddd/! bx;   s/dddddddddd/e/g     /eeeeeeeeee/! bx;   s/eeeeeeeeee/f/g     /ffffffffff/! bx;   s/ffffffffff/g/g     /gggggggggg/! bx;   s/gggggggggg/h/g     s/hhhhhhhhhh//g     :x     $! { h; b; }     :y     /a/! s/[b-h]*/&0/     s/aaaaaaaaa/9/     s/aaaaaaaa/8/     s/aaaaaaa/7/     s/aaaaaa/6/     s/aaaaa/5/     s/aaaa/4/     s/aaa/3/     s/aa/2/     s/a/1/     y/bcdefgh/abcdefg/     /[a-h]/ by     p

Next: [head](http://www.gnu.org/software/sed/manual/sed.html#head), Previous: [wc -w](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dw), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.11 Counting Lines

No strange things are done now, because sed gives us `wc -l' functionality for free!!! Look: 
    
    
         #!/usr/bin/sed -nf     $=

Next: [tail](http://www.gnu.org/software/sed/manual/sed.html#tail), Previous: [wc -l](http://www.gnu.org/software/sed/manual/sed.html#wc-_002dl), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.12 Printing the First Lines

This script is probably the simplest useful sed script. It displays the first 10 lines of input; the number of displayed lines is right before the `q` command. 
    
    
         #!/usr/bin/sed -f     10q

Next: [uniq](http://www.gnu.org/software/sed/manual/sed.html#uniq), Previous: [head](http://www.gnu.org/software/sed/manual/sed.html#head), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.13 Printing the Last Lines

Printing the last n lines rather than the first is more complex but indeed possible. n is encoded in the second line, before the bang character. 

This script is similar to the tac script in that it keeps the final output in the hold space and prints it at the end: 
    
    
         #!/usr/bin/sed -nf          1! {; H; g; }     1,10 !s/[^\n]*\n//     $p     h

Mainly, the scripts keeps a window of 10 lines and slides it by adding a line and deleting the oldest (the substitution command on the second line works like a `D` command but does not restart the loop). 

The “sliding window” technique is a very powerful way to write efficient and complex sed scripts, because commands like `P` would require a lot of work if implemented manually. 

To introduce the technique, which is fully demonstrated in the rest of this chapter and is based on the `N`, `P` and `D` commands, here is an implementation of tail using a simple “sliding window.” 

This looks complicated but in fact the working is the same as the last script: after we have kicked in the appropriate number of lines, however, we stop using the hold space to keep inter-line state, and instead use `N` and `D` to slide pattern space by one line: 
    
    
         #!/usr/bin/sed -f          1h     2,10 {; H; g; }     $q     1,9d     N     D

Note how the first, second and fourth line are inactive after the first ten lines of input. After that, all the script does is: exiting on the last line of input, appending the next input line to pattern space, and removing the first line. 

Next: [uniq -d](http://www.gnu.org/software/sed/manual/sed.html#uniq-_002dd), Previous: [tail](http://www.gnu.org/software/sed/manual/sed.html#tail), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.14 Make Duplicate Lines Unique

This is an example of the art of using the `N`, `P` and `D` commands, probably the most difficult to master. 
    
    
     #!/usr/bin/sed -f h :b # On the last line, print and exit $b N /^\(.*\)\n\1$/ { # The two lines are identical. Undo the effect of # the n command. g bb } 
    
     # If the N command had added the last line, print and exit
    
         $b          # The lines are different; print the first and go     # back working on the second.     P     D

As you can see, we mantain a 2-line window using `P` and `D`. This technique is often used in advanced sed scripts. 

Next: [uniq -u](http://www.gnu.org/software/sed/manual/sed.html#uniq-_002du), Previous: [uniq](http://www.gnu.org/software/sed/manual/sed.html#uniq), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.15 Print Duplicated Lines of Input

This script prints only duplicated lines, like `uniq -d'. 
    
    
         #!/usr/bin/sed -nf          $b     N     /^\(.*\)\n\1$/ {         # Print the first of the duplicated lines         s/.*\n//         p              # Loop until we get a different line         :b         $b         N         /^\(.*\)\n\1$/ {             s/.*\n//             bb         }     }          # The last line cannot be followed by duplicates     $b          # Found a different one.  Leave it alone in the pattern space     # and go back to the top, hunting its duplicates     D

Next: [cat -s](http://www.gnu.org/software/sed/manual/sed.html#cat-_002ds), Previous: [uniq -d](http://www.gnu.org/software/sed/manual/sed.html#uniq-_002dd), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.16 Remove All Duplicated Lines

This script prints only unique lines, like `uniq -u'. 
    
    
     #!/usr/bin/sed -f # Search for a duplicate line --- until that, print what you find. $b N /^\(.*\)\n\1$/ ! { P D } :c # Got two equal lines in pattern space. At the # end of the file we simply exit $d 
    
     # Else, we keep reading lines with N until we
    
         # find a different one     s/.*\n//     N     /^\(.*\)\n\1$/ {         bc     }          # Remove the last instance of the duplicate line     # and go back to the top     D

Previous: [uniq -u](http://www.gnu.org/software/sed/manual/sed.html#uniq-_002du), Up: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples)

### 4.17 Squeezing Blank Lines

As a final example, here are three scripts, of increasing complexity and speed, that implement the same function as `cat -s', that is squeezing blank lines. 

The first leaves a blank line at the beginning and end if there are some already. 
    
    
         #!/usr/bin/sed -f          # on empty lines, join with next     # Note there is a star in the regexp     :x     /^\n*$/ {     N     bx     }          # now, squeeze all '\n', this can be also done by:     # s/^\(\n\)*/\1/     s/\n*/\     /

This one is a bit more complex and removes all empty lines at the beginning. It does leave a single blank line at end if one was there. 
    
    
         #!/usr/bin/sed -f          # delete all leading empty lines     1,/^./{     /./!d     }          # on an empty line we remove it and all the following     # empty lines, but one     :x     /./!{     N     s/^\n$//     tx     }

This removes leading and trailing blank lines. It is also the fastest. Note that loops are completely done with `n` and `b`, without relying on sed to restart the the script automatically at the end of a line. 
    
    
         #!/usr/bin/sed -nf          # delete all (leading) blanks     /./!d          # get here: so there is a non empty     :x     # print it     p     # get next     n     # got chars? print it again, etc...     /./bx          # no, don't have chars: got an empty line     :z     # get next, if last line we finish here so no trailing     # empty lines are written     n     # also empty? then ignore it, and get next... this will     # remove ALL empty lines     /./!bz          # all empty lines were deleted/ignored, but we have a non empty.  As     # what we want to do is to squeeze, insert a blank line artificially     i\          bx

Next: [Other Resources](http://www.gnu.org/software/sed/manual/sed.html#Other-Resources), Previous: [Examples](http://www.gnu.org/software/sed/manual/sed.html#Examples), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## 5 GNU sed's Limitations and Non-limitations

For those who want to write portable sed scripts, be aware that some implementations have been known to limit line lengths (for the pattern and hold spaces) to be no more than 4000 bytes. The posix standard specifies that conforming sed implementations shall support at least 8192 byte line lengths. GNU sed has no built-in limit on line length; as long as it can `malloc()` more (virtual) memory, you can feed or construct lines as long as you like. 

However, recursion is used to handle subpatterns and indefinite repetition. This means that the available stack space may limit the size of the buffer that can be processed by certain patterns. 

Next: [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs), Previous: [Limitations](http://www.gnu.org/software/sed/manual/sed.html#Limitations), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## 6 Other Resources for Learning About sed

In addition to several books that have been written about sed (either specifically or as chapters in books which discuss shell programming), one can find out more about sed (including suggestions of a few books) from the FAQ for the `sed-users` mailing list, available from any of: 
    
    
     <http://www.student.northpark.edu/pemente/sed/sedfaq.html>  
     <http://sed.sf.net/grabbag/tutorials/sedfaq.html>  
    

Also of interest are <http://www.student.northpark.edu/pemente/sed/index.htm> and <http://sed.sf.net/grabbag>, which include sed tutorials and other sed-related goodies. 

The `sed-users` mailing list itself maintained by Sven Guckes. To subscribe, visit [http://groups.yahoo.com](http://groups.yahoo.com/) and search for the `sed-users` mailing list. 

Next: [Extended regexps](http://www.gnu.org/software/sed/manual/sed.html#Extended-regexps), Previous: [Other Resources](http://www.gnu.org/software/sed/manual/sed.html#Other-Resources), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## 7 Reporting Bugs

Email bug reports to [bonzini@gnu.org](mailto:bonzini@gnu.org). Be sure to include the word “sed” somewhere in the `Subject:` field. Also, please include the output of `sed --version' in the body of your report if at all possible. 

Please do not send a bug report like this: 
    
    
     while building frobme-1.3.4     $ configure     error--> sed: file sedscr line 1: Unknown option to 's'

If GNU sed doesn't configure your favorite package, take a few extra minutes to identify the specific problem and make a stand-alone test case. Unlike other programs such as C compilers, making such test cases for sed is quite simple. 

A stand-alone test case includes all the data necessary to perform the test, and the specific invocation of sed that causes the problem. The smaller a stand-alone test case is, the better. A test case should not involve something as far removed from sed as “try to configure frobme-1.3.4”. Yes, that is in principle enough information to look for the bug, but that is not a very practical prospect. 

Here are a few commonly reported bugs that are not bugs. 

`N` command on the last line
     Most versions of sed exit without printing anything when the N command is issued on the last line of a file. GNU sed prints pattern space before exiting unless of course the -n command switch has been specified. This choice is by design. 

For example, the behavior of 
    
    
     sed N foo bar  
         

would depend on whether foo has an even or an odd number of lines[10](http://www.gnu.org/software/sed/manual/sed.html#fn-10). Or, when writing a script to read the next few lines following a pattern match, traditional implementations of `sed` would force you to write something like 
    
    
     /foo/{ $!N; $!N; $!N; $!N; $!N; $!N; $!N; $!N; $!N }  
         

instead of just 
    
    
     /foo/{ N;N;N;N;N;N;N;N;N; }  
         

In any case, the simplest workaround is to use `$d;N` in scripts that rely on the traditional behavior, or to set the `POSIXLY_CORRECT` variable to a non-empty value.   


Regex syntax clashes (problems with backslashes)
    sed uses the posix basic regular expression syntax. According to the standard, the meaning of some escape sequences is undefined in this syntax; notable in the case of sed are `\|`, `\+`, `\?`, `\``, `\'`, `\<`, `\>`, `\b`, `\B`, `\w`, and `\W`. 

As in all GNU programs that use posix basic regular expressions, sed interprets these escape sequences as special characters. So, `x\+` matches one or more occurrences of `x'. `abc\|def` matches either `abc' or `def'. 

This syntax may cause problems when running scripts written for other seds. Some sed programs have been written with the assumption that `\|` and `\+` match the literal characters `|` and `+`. Such scripts must be modified by removing the spurious backslashes if they are to be used with modern implementations of sed, like GNU sed. 

On the other hand, some scripts use s|abc\|def||g to remove occurrences of _either_ `abc` or `def`. While this worked until  sed 4.0.x, newer versions interpret this as removing the string `abc|def`. This is again undefined behavior according to POSIX, and this interpretation is arguably more robust: older seds, for example, required that the regex matcher parsed `\/` as `/` in the common case of escaping a slash, which is again undefined behavior; the new behavior avoids this, and this is good because the regex matcher is only partially under our control. 

In addition, this version of sed supports several escape characters (some of which are multi-character) to insert non-printable characters in scripts (`\a`, `\c`, `\d`, `\o`, `\r`, `\t`, `\v`, `\x`). These can cause similar problems with scripts written for other seds.   


-i clobbers read-only files
     In short, `sed -i' will let you delete the contents of a read-only file, and in general the -i option (see [Invocation](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)) lets you clobber protected files. This is not a bug, but rather a consequence of how the Unix filesystem works. 

The permissions on a file say what can happen to the data in that file, while the permissions on a directory say what can happen to the list of files in that directory. `sed -i' will not ever open for writing a file that is already on disk. Rather, it will work on a temporary file that is finally renamed to the original name: if you rename or delete files, you're actually modifying the contents of the directory, so the operation depends on the permissions of the directory, not of the file. For this same reason, sed does not let you use -i on a writeable file in a read-only directory, and will break hard or symbolic links when -i is used on such a file.   


`0a` does not work (gives an error)
    There is no line 0. 0 is a special address that is only used to treat addresses like `0,/`RE`/` as active when the script starts: if you write `1,/abc/d` and the first line includes the word `abc', then that match would be ignored because address ranges must span at least two lines (barring the end of the file); but what you probably wanted is to delete every line up to the first one including `abc', and this is obtained with `0,/abc/d`.   

`[a-z]` is case insensitive
    You are encountering problems with locales. POSIX mandates that `[a-z]` uses the current locale's collation order – in C parlance, that means using `strcoll(3)` instead of `strcmp(3)`. Some locales have a case-insensitive collation order, others don't. 

Another problem is that `[a-z]` tries to use collation symbols. This only happens if you are on the GNU system, using GNU libc's regular expression matcher instead of compiling the one supplied with GNU sed. In a Danish locale, for example, the regular expression `^[a-z]$` matches the string `aa', because this is a single collating symbol that comes after `a' and before `b'; `ll' behaves similarly in Spanish locales, or `ij' in Dutch locales. 

To work around these problems, which may cause bugs in shell scripts, set the LC_COLLATE and LC_CTYPE environment variables to `C'. 

Next: [Concept Index](http://www.gnu.org/software/sed/manual/sed.html#Concept-Index), Previous: [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## Appendix A Extended regular expressions

The only difference between basic and extended regular expressions is in the behavior of a few characters: `?', `+', parentheses, and braces (`{}'). While basic regular expressions require these to be escaped if you want them to behave as special characters, when using extended regular expressions you must escape them if you want them _to match a literal character_. 

Examples: 

`abc?`
    becomes `abc\?' when using extended regular expressions. It matches the literal string `abc?'.   

`c\+`
    becomes `c+' when using extended regular expressions. It matches one or more `c's.   

`a\{3,\}`
    becomes `a{3,}' when using extended regular expressions. It matches three or more `a's.   

`\(abc\)\{2,3\}`
    becomes `(abc){2,3}' when using extended regular expressions. It matches either `abcabc' or `abcabcabc'.   

`\(abc*\)\1`
    becomes `(abc*)\1' when using extended regular expressions. Backreferences must still be escaped when using extended regular expressions. 

Next: [Command and Option Index](http://www.gnu.org/software/sed/manual/sed.html#Command-and-Option-Index), Previous: [Extended regexps](http://www.gnu.org/software/sed/manual/sed.html#Extended-regexps), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## Concept Index

This is a general index of all issues discussed in this manual, with the exception of the sed commands and command-line options. 

  * [Additional reading about sed](http://www.gnu.org/software/sed/manual/sed.html#index-Additional-reading-about-_0040command_007bsed_007d-216): [Other Resources](http://www.gnu.org/software/sed/manual/sed.html#Other-Resources)
  * [addr1,+N](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040var_007baddr1_007d_002c_002bN-66): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [addr1,~N](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040var_007baddr1_007d_002c_007eN-67): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Address, as a regular expression](http://www.gnu.org/software/sed/manual/sed.html#index-Address_002c-as-a-regular-expression-54): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Address, last line](http://www.gnu.org/software/sed/manual/sed.html#index-Address_002c-last-line-51): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Address, numeric](http://www.gnu.org/software/sed/manual/sed.html#index-Address_002c-numeric-48): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Addresses, in sed scripts](http://www.gnu.org/software/sed/manual/sed.html#index-Addresses_002c-in-_0040command_007bsed_007d-scripts-45): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Append hold space to pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Append-hold-space-to-pattern-space-169): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Append next input line to pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Append-next-input-line-to-pattern-space-154): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Append pattern space to hold space](http://www.gnu.org/software/sed/manual/sed.html#index-Append-pattern-space-to-hold-space-162): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Appending text after a line](http://www.gnu.org/software/sed/manual/sed.html#index-Appending-text-after-a-line-125): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Backreferences, in regular expressions](http://www.gnu.org/software/sed/manual/sed.html#index-Backreferences_002c-in-regular-expressions-100): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Branch to a label, if `s///` failed](http://www.gnu.org/software/sed/manual/sed.html#index-Branch-to-a-label_002c-if-_0040code_007bs_002f_002f_002f_007d-failed-204): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Branch to a label, if `s///` succeeded](http://www.gnu.org/software/sed/manual/sed.html#index-Branch-to-a-label_002c-if-_0040code_007bs_002f_002f_002f_007d-succeeded-181): [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands)
  * [Branch to a label, unconditionally](http://www.gnu.org/software/sed/manual/sed.html#index-Branch-to-a-label_002c-unconditionally-178): [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands)
  * [Buffer spaces, pattern and hold](http://www.gnu.org/software/sed/manual/sed.html#index-Buffer-spaces_002c-pattern-and-hold-41): [Execution Cycle](http://www.gnu.org/software/sed/manual/sed.html#Execution-Cycle)
  * [Bugs, reporting](http://www.gnu.org/software/sed/manual/sed.html#index-Bugs_002c-reporting-217): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [Case-insensitive matching](http://www.gnu.org/software/sed/manual/sed.html#index-Case_002dinsensitive-matching-119): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Caveat — #n on first line](http://www.gnu.org/software/sed/manual/sed.html#index-Caveat-_002d_002d_002d-_0023n-on-first-line-86): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Command groups](http://www.gnu.org/software/sed/manual/sed.html#index-Command-groups-99): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Comments, in scripts](http://www.gnu.org/software/sed/manual/sed.html#index-Comments_002c-in-scripts-83): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Conditional branch](http://www.gnu.org/software/sed/manual/sed.html#index-Conditional-branch-205): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Conditional branch](http://www.gnu.org/software/sed/manual/sed.html#index-Conditional-branch-182): [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands)
  * [Copy hold space into pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Copy-hold-space-into-pattern-space-165): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Copy pattern space into hold space](http://www.gnu.org/software/sed/manual/sed.html#index-Copy-pattern-space-into-hold-space-158): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Delete first line from pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Delete-first-line-from-pattern-space-151): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Disabling autoprint, from command line](http://www.gnu.org/software/sed/manual/sed.html#index-Disabling-autoprint_002c-from-command-line-9): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [empty regular expression](http://www.gnu.org/software/sed/manual/sed.html#index-empty-regular-expression-56): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Evaluate Bourne-shell commands](http://www.gnu.org/software/sed/manual/sed.html#index-Evaluate-Bourne_002dshell-commands-184): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Evaluate Bourne-shell commands, after substitution](http://www.gnu.org/software/sed/manual/sed.html#index-Evaluate-Bourne_002dshell-commands_002c-after-substitution-114): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Exchange hold space with pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Exchange-hold-space-with-pattern-space-172): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Excluding lines](http://www.gnu.org/software/sed/manual/sed.html#index-Excluding-lines-73): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Extended regular expressions, choosing](http://www.gnu.org/software/sed/manual/sed.html#index-Extended-regular-expressions_002c-choosing-31): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Extended regular expressions, syntax](http://www.gnu.org/software/sed/manual/sed.html#index-Extended-regular-expressions_002c-syntax-227): [Extended regexps](http://www.gnu.org/software/sed/manual/sed.html#Extended-regexps)
  * [Files to be processed as input](http://www.gnu.org/software/sed/manual/sed.html#index-Files-to-be-processed-as-input-37): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Flow of control in scripts](http://www.gnu.org/software/sed/manual/sed.html#index-Flow-of-control-in-scripts-174): [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands)
  * [Global substitution](http://www.gnu.org/software/sed/manual/sed.html#index-Global-substitution-105): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, /dev/stderr file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040file_007b_002fdev_002fstderr_007d-file-149): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [GNU extensions, /dev/stderr file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040file_007b_002fdev_002fstderr_007d-file-113): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, /dev/stdin file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040file_007b_002fdev_002fstdin_007d-file-201): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, /dev/stdin file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040file_007b_002fdev_002fstdin_007d-file-145): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [GNU extensions, /dev/stdout file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040file_007b_002fdev_002fstdout_007d-file-228): [Footnotes](http://www.gnu.org/software/sed/manual/sed.html#Footnotes)
  * [GNU extensions, /dev/stdout file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040file_007b_002fdev_002fstdout_007d-file-148): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [GNU extensions, /dev/stdout file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040file_007b_002fdev_002fstdout_007d-file-112): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, `0` address](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-_0040code_007b0_007d-address-69): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, 0,addr2 addressing](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-0_002c_0040var_007baddr2_007d-addressing-70): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, addr1,+N addressing](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-_0040var_007baddr1_007d_002c_002b_0040var_007bN_007d-addressing-71): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, addr1,~N addressing](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-_0040var_007baddr1_007d_002c_007e_0040var_007bN_007d-addressing-72): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, branch if `s///` failed](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-branch-if-_0040code_007bs_002f_002f_002f_007d-failed-203): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, case modifiers in `s` commands](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-case-modifiers-in-_0040code_007bs_007d-commands-102): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, checking for their presence](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-checking-for-their-presence-207): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, disabling](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-disabling-24): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [GNU extensions, evaluating Bourne-shell commands](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-evaluating-Bourne_002dshell-commands-186): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, evaluating Bourne-shell commands](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-evaluating-Bourne_002dshell-commands-116): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, extended regular expressions](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-extended-regular-expressions-32): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [GNU extensions, `g` and number modifier interaction in `s` command](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-_0040code_007bg_007d-and-_0040var_007bnumber_007d-modifier-interaction-in-_0040code_007bs_007d-command-108): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, `I` modifier](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-_0040code_007bI_007d-modifier-118): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, `I` modifier](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-_0040code_007bI_007d-modifier-59): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, in-place editing](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-in_002dplace-editing-225): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [GNU extensions, in-place editing](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-in_002dplace-editing-19): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [GNU extensions, `L` command](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040code_007bL_007d-command-192): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, `M` modifier](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040code_007bM_007d-modifier-120): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, modifiers and the empty regular expression](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-modifiers-and-the-empty-regular-expression-57): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, `n~m' addresses](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-_0040samp_007b_0040var_007bn_007d_007e_0040var_007bm_007d_007d-addresses-50): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, quitting silently](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-quitting-silently-194): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, `R` command](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-_0040code_007bR_007d-command-200): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, reading a file a line at a time](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-reading-a-file-a-line-at-a-time-199): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, reformatting paragraphs](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-reformatting-paragraphs-191): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, returning an exit code](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-returning-an-exit-code-195): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, returning an exit code](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-returning-an-exit-code-88): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [GNU extensions, setting line length](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-setting-line-length-141): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [GNU extensions, special escapes](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-special-escapes-223): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [GNU extensions, special escapes](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-special-escapes-212): [Escapes](http://www.gnu.org/software/sed/manual/sed.html#Escapes)
  * [GNU extensions, special two-address forms](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-special-two_002daddress-forms-68): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [GNU extensions, subprocesses](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-subprocesses-187): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [GNU extensions, subprocesses](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-subprocesses-117): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [GNU extensions, to basic regular expressions](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-to-basic-regular-expressions-221): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [GNU extensions, to basic regular expressions](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-to-basic-regular-expressions-75): [Regular Expressions](http://www.gnu.org/software/sed/manual/sed.html#Regular-Expressions)
  * [GNU extensions, two addresses supported by most commands](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-two-addresses-supported-by-most-commands-123): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [GNU extensions, unlimited line length](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040acronym_007bGNU_007d-extensions_002c-unlimited-line-length-214): [Limitations](http://www.gnu.org/software/sed/manual/sed.html#Limitations)
  * [GNU extensions, writing first line to a file](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040value_007bSSEDEXT_007d_002c-writing-first-line-to-a-file-211): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Goto, in scripts](http://www.gnu.org/software/sed/manual/sed.html#index-Goto_002c-in-scripts-179): [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands)
  * [Greedy regular expression matching](http://www.gnu.org/software/sed/manual/sed.html#index-Greedy-regular-expression-matching-81): [Regular Expressions](http://www.gnu.org/software/sed/manual/sed.html#Regular-Expressions)
  * [Grouping commands](http://www.gnu.org/software/sed/manual/sed.html#index-Grouping-commands-98): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Hold space, appending from pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Hold-space_002c-appending-from-pattern-space-163): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Hold space, appending to pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Hold-space_002c-appending-to-pattern-space-170): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Hold space, copy into pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Hold-space_002c-copy-into-pattern-space-167): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Hold space, copying pattern space into](http://www.gnu.org/software/sed/manual/sed.html#index-Hold-space_002c-copying-pattern-space-into-160): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Hold space, definition](http://www.gnu.org/software/sed/manual/sed.html#index-Hold-space_002c-definition-44): [Execution Cycle](http://www.gnu.org/software/sed/manual/sed.html#Execution-Cycle)
  * [Hold space, exchange with pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Hold-space_002c-exchange-with-pattern-space-173): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [In-place editing](http://www.gnu.org/software/sed/manual/sed.html#index-In_002dplace-editing-224): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [In-place editing, activating](http://www.gnu.org/software/sed/manual/sed.html#index-In_002dplace-editing_002c-activating-18): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [In-place editing, Perl-style backup file names](http://www.gnu.org/software/sed/manual/sed.html#index-In_002dplace-editing_002c-Perl_002dstyle-backup-file-names-20): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Inserting text before a line](http://www.gnu.org/software/sed/manual/sed.html#index-Inserting-text-before-a-line-129): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Labels, in scripts](http://www.gnu.org/software/sed/manual/sed.html#index-Labels_002c-in-scripts-176): [Programming Commands](http://www.gnu.org/software/sed/manual/sed.html#Programming-Commands)
  * [Last line, selecting](http://www.gnu.org/software/sed/manual/sed.html#index-Last-line_002c-selecting-52): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Line length, setting](http://www.gnu.org/software/sed/manual/sed.html#index-Line-length_002c-setting-140): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Line length, setting](http://www.gnu.org/software/sed/manual/sed.html#index-Line-length_002c-setting-23): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Line number, printing](http://www.gnu.org/software/sed/manual/sed.html#index-Line-number_002c-printing-136): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Line selection](http://www.gnu.org/software/sed/manual/sed.html#index-Line-selection-46): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Line, selecting by number](http://www.gnu.org/software/sed/manual/sed.html#index-Line_002c-selecting-by-number-49): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Line, selecting by regular expression match](http://www.gnu.org/software/sed/manual/sed.html#index-Line_002c-selecting-by-regular-expression-match-55): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Line, selecting last](http://www.gnu.org/software/sed/manual/sed.html#index-Line_002c-selecting-last-53): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [List pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-List-pattern-space-138): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Mixing `g` and number modifiers in the `s` command](http://www.gnu.org/software/sed/manual/sed.html#index-Mixing-_0040code_007bg_007d-and-_0040var_007bnumber_007d-modifiers-in-the-_0040code_007bs_007d-command-109): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Next input line, append to pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Next-input-line_002c-append-to-pattern-space-153): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Next input line, replace pattern space with](http://www.gnu.org/software/sed/manual/sed.html#index-Next-input-line_002c-replace-pattern-space-with-95): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Non-bugs, in-place editing](http://www.gnu.org/software/sed/manual/sed.html#index-Non_002dbugs_002c-in_002dplace-editing-226): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [Non-bugs, `N` command on the last line](http://www.gnu.org/software/sed/manual/sed.html#index-Non_002dbugs_002c-_0040code_007bN_007d-command-on-the-last-line-219): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [Non-bugs, regex syntax clashes](http://www.gnu.org/software/sed/manual/sed.html#index-Non_002dbugs_002c-regex-syntax-clashes-222): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [Parenthesized substrings](http://www.gnu.org/software/sed/manual/sed.html#index-Parenthesized-substrings-101): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Pattern space, definition](http://www.gnu.org/software/sed/manual/sed.html#index-Pattern-space_002c-definition-43): [Execution Cycle](http://www.gnu.org/software/sed/manual/sed.html#Execution-Cycle)
  * [Perl-style regular expressions, multiline](http://www.gnu.org/software/sed/manual/sed.html#index-Perl_002dstyle-regular-expressions_002c-multiline-60): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Portability, comments](http://www.gnu.org/software/sed/manual/sed.html#index-Portability_002c-comments-84): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Portability, line length limitations](http://www.gnu.org/software/sed/manual/sed.html#index-Portability_002c-line-length-limitations-215): [Limitations](http://www.gnu.org/software/sed/manual/sed.html#Limitations)
  * [Portability, `N` command on the last line](http://www.gnu.org/software/sed/manual/sed.html#index-Portability_002c-_0040code_007bN_007d-command-on-the-last-line-218): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [`POSIXLY_CORRECT` behavior, bracket expressions](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040code_007bPOSIXLY_005fCORRECT_007d-behavior_002c-bracket-expressions-79): [Regular Expressions](http://www.gnu.org/software/sed/manual/sed.html#Regular-Expressions)
  * [`POSIXLY_CORRECT` behavior, enabling](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040code_007bPOSIXLY_005fCORRECT_007d-behavior_002c-enabling-25): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [`POSIXLY_CORRECT` behavior, escapes](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040code_007bPOSIXLY_005fCORRECT_007d-behavior_002c-escapes-213): [Escapes](http://www.gnu.org/software/sed/manual/sed.html#Escapes)
  * [`POSIXLY_CORRECT` behavior, `N` command](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040code_007bPOSIXLY_005fCORRECT_007d-behavior_002c-_0040code_007bN_007d-command-220): [Reporting Bugs](http://www.gnu.org/software/sed/manual/sed.html#Reporting-Bugs)
  * [Print first line from pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Print-first-line-from-pattern-space-156): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Printing line number](http://www.gnu.org/software/sed/manual/sed.html#index-Printing-line-number-135): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Printing text unambiguously](http://www.gnu.org/software/sed/manual/sed.html#index-Printing-text-unambiguously-139): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Quitting](http://www.gnu.org/software/sed/manual/sed.html#index-Quitting-196): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Quitting](http://www.gnu.org/software/sed/manual/sed.html#index-Quitting-89): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Range of lines](http://www.gnu.org/software/sed/manual/sed.html#index-Range-of-lines-61): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Range with start address of zero](http://www.gnu.org/software/sed/manual/sed.html#index-Range-with-start-address-of-zero-64): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Read next input line](http://www.gnu.org/software/sed/manual/sed.html#index-Read-next-input-line-96): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Read text from a file](http://www.gnu.org/software/sed/manual/sed.html#index-Read-text-from-a-file-198): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Read text from a file](http://www.gnu.org/software/sed/manual/sed.html#index-Read-text-from-a-file-144): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Reformat pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Reformat-pattern-space-189): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Reformatting paragraphs](http://www.gnu.org/software/sed/manual/sed.html#index-Reformatting-paragraphs-190): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Replace hold space with copy of pattern space](http://www.gnu.org/software/sed/manual/sed.html#index-Replace-hold-space-with-copy-of-pattern-space-159): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Replace pattern space with copy of hold space](http://www.gnu.org/software/sed/manual/sed.html#index-Replace-pattern-space-with-copy-of-hold-space-166): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Replacing all text matching regexp in a line](http://www.gnu.org/software/sed/manual/sed.html#index-Replacing-all-text-matching-regexp-in-a-line-106): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Replacing only nth match of regexp in a line](http://www.gnu.org/software/sed/manual/sed.html#index-Replacing-only-_0040var_007bn_007dth-match-of-regexp-in-a-line-107): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Replacing selected lines with other text](http://www.gnu.org/software/sed/manual/sed.html#index-Replacing-selected-lines-with-other-text-132): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Requiring GNU sed](http://www.gnu.org/software/sed/manual/sed.html#index-Requiring-_0040value_007bSSED_007d-208): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Script structure](http://www.gnu.org/software/sed/manual/sed.html#index-Script-structure-40): [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)
  * [Script, from a file](http://www.gnu.org/software/sed/manual/sed.html#index-Script_002c-from-a-file-15): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Script, from command line](http://www.gnu.org/software/sed/manual/sed.html#index-Script_002c-from-command-line-12): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [sed program structure](http://www.gnu.org/software/sed/manual/sed.html#index-g_t_0040command_007bsed_007d-program-structure-39): [sed Programs](http://www.gnu.org/software/sed/manual/sed.html#sed-Programs)
  * [Selecting lines to process](http://www.gnu.org/software/sed/manual/sed.html#index-Selecting-lines-to-process-47): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Selecting non-matching lines](http://www.gnu.org/software/sed/manual/sed.html#index-Selecting-non_002dmatching-lines-74): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Several lines, selecting](http://www.gnu.org/software/sed/manual/sed.html#index-Several-lines_002c-selecting-62): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Slash character, in regular expressions](http://www.gnu.org/software/sed/manual/sed.html#index-Slash-character_002c-in-regular-expressions-58): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Spaces, pattern and hold](http://www.gnu.org/software/sed/manual/sed.html#index-Spaces_002c-pattern-and-hold-42): [Execution Cycle](http://www.gnu.org/software/sed/manual/sed.html#Execution-Cycle)
  * [Special addressing forms](http://www.gnu.org/software/sed/manual/sed.html#index-Special-addressing-forms-63): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)
  * [Standard input, processing as input](http://www.gnu.org/software/sed/manual/sed.html#index-Standard-input_002c-processing-as-input-38): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Stream editor](http://www.gnu.org/software/sed/manual/sed.html#index-Stream-editor-1): [Introduction](http://www.gnu.org/software/sed/manual/sed.html#Introduction)
  * [Subprocesses](http://www.gnu.org/software/sed/manual/sed.html#index-Subprocesses-185): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Subprocesses](http://www.gnu.org/software/sed/manual/sed.html#index-Subprocesses-115): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Substitution of text, options](http://www.gnu.org/software/sed/manual/sed.html#index-Substitution-of-text_002c-options-104): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Text, appending](http://www.gnu.org/software/sed/manual/sed.html#index-Text_002c-appending-126): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Text, deleting](http://www.gnu.org/software/sed/manual/sed.html#index-Text_002c-deleting-91): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Text, insertion](http://www.gnu.org/software/sed/manual/sed.html#index-Text_002c-insertion-130): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Text, printing](http://www.gnu.org/software/sed/manual/sed.html#index-Text_002c-printing-93): [Common Commands](http://www.gnu.org/software/sed/manual/sed.html#Common-Commands)
  * [Text, printing after substitution](http://www.gnu.org/software/sed/manual/sed.html#index-Text_002c-printing-after-substitution-110): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Text, writing to a file after substitution](http://www.gnu.org/software/sed/manual/sed.html#index-Text_002c-writing-to-a-file-after-substitution-111): [The "s" Command](http://www.gnu.org/software/sed/manual/sed.html#The-_0022s_0022-Command)
  * [Transliteration](http://www.gnu.org/software/sed/manual/sed.html#index-Transliteration-122): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Unbuffered I/O, choosing](http://www.gnu.org/software/sed/manual/sed.html#index-Unbuffered-I_002fO_002c-choosing-36): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Usage summary, printing](http://www.gnu.org/software/sed/manual/sed.html#index-Usage-summary_002c-printing-5): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Version, printing](http://www.gnu.org/software/sed/manual/sed.html#index-Version_002c-printing-3): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Working on separate files](http://www.gnu.org/software/sed/manual/sed.html#index-Working-on-separate-files-33): [Invoking sed](http://www.gnu.org/software/sed/manual/sed.html#Invoking-sed)
  * [Write first line to a file](http://www.gnu.org/software/sed/manual/sed.html#index-Write-first-line-to-a-file-210): [Extended Commands](http://www.gnu.org/software/sed/manual/sed.html#Extended-Commands)
  * [Write to a file](http://www.gnu.org/software/sed/manual/sed.html#index-Write-to-a-file-147): [Other Commands](http://www.gnu.org/software/sed/manual/sed.html#Other-Commands)
  * [Zero, as range start address](http://www.gnu.org/software/sed/manual/sed.html#index-Zero_002c-as-range-start-address-65): [Addresses](http://www.gnu.org/software/sed/manual/sed.html#Addresses)



Previous: [Concept Index](http://www.gnu.org/software/sed/manual/sed.html#Concept-Index), Up: [Top](http://www.gnu.org/software/sed/manual/sed.html#Top)

## Command and Option Index

This is an alphabetical list of all sed commands and command-line options. 

## Table of Contents

[[1](http://www.gnu.org/software/sed/manual/sed.html#fnd-1)] This applies to commands such as `=`, `a`, `c`, `i`, `l`, `p`. You can still write to the standard output by using the `w` or `W` commands together with the /dev/stdout special file

[[2](http://www.gnu.org/software/sed/manual/sed.html#fnd-2)] Note that GNU sed creates the backup file whether or not any output is actually changed.

[[3](http://www.gnu.org/software/sed/manual/sed.html#fnd-3)] Actually, if sed prints a line without the terminating newline, it will nevertheless print the missing newline as soon as more text is sent to the same output stream, which gives the “least expected surprise” even though it does not make commands like `sed -n p' exactly identical to cat.

[[4](http://www.gnu.org/software/sed/manual/sed.html#fnd-4)] This is equivalent to `p` unless the -i option is being used.

[[5](http://www.gnu.org/software/sed/manual/sed.html#fnd-5)] This is equivalent to `p` unless the -i option is being used.

[[6](http://www.gnu.org/software/sed/manual/sed.html#fnd-6)] All the escapes introduced here are GNU extensions, with the exception of `\n`. In basic regular expression mode, setting `POSIXLY_CORRECT` disables them inside bracket expressions.

[[7](http://www.gnu.org/software/sed/manual/sed.html#fnd-7)] sed guru Greg Ubben wrote an implementation of the dc rpn calculator! It is distributed together with sed.

[[8](http://www.gnu.org/software/sed/manual/sed.html#fnd-8)] This requires another script to pad the output of banner; for example 
    
    
         #! /bin/sh          banner -w $1 $2 $3 $4 |       sed -e :a -e '/^.\{0,'$1'\}$/ { s/$/ /; ba; }' |       ~/sedscripts/reverseline.sed

[[9](http://www.gnu.org/software/sed/manual/sed.html#fnd-9)] Some implementations have a limit of 199 commands per script

[[10](http://www.gnu.org/software/sed/manual/sed.html#fnd-10)] which is the actual “bug” that prompted the change in behavior

