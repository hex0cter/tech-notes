# [regexp](http://www.mkssoftware.com/docs/man5/regexp.5.asp)


## DESCRIPTION

Many MKS commands match strings of text in text files using a type of pattern known as a **_regular expression_**. Simply stated, a **_regular expression_** lets you find strings in text files not only by direct match, but also by extended matches, similar to, but much more powerful than the file name patterns described in [**`sh`**](http://www.mkssoftware.com/docs/man1/sh.1.asp).

The newline character at the end of each input line is never explicitly matched by any regular expression or part thereof.

[**`expr`**](http://www.mkssoftware.com/docs/man1/expr.1.asp), [**`ex`**](http://www.mkssoftware.com/docs/man1/vi.1.asp), [**`vi`**](http://www.mkssoftware.com/docs/man1/vi.1.asp), and [**`ed`**](http://www.mkssoftware.com/docs/man1/ed.1.asp) take basic regular expressions; all other MKS commands accept extended regular expressions. [**`grep`**](http://www.mkssoftware.com/docs/man1/grep.1.asp) and [**`sed`**](http://www.mkssoftware.com/docs/man1/sed.1.asp) accept basic regular expressions, but can accept extended regular expressions if the **`-E`** option is used.

Regular expressions may be made up of normal characters and/or special characters, sometimes called **_metacharacters_**. Basic and extended regular expressions differ only in the metacharacters they can contain.

The basic regular expression metacharacters are:

>
>     ^ $ . * \( \) [ \{ \} \
>     >

The extended regular expression metacharacters are:

>
>     | ^ $ . * + ? ( ) [ { } \
>     >

In addition, [**`vi`**](http://www.mkssoftware.com/docs/man1/vi.1.asp), [**`ex`**](http://www.mkssoftware.com/docs/man1/vi.1.asp), and [**`egrep`**](http://www.mkssoftware.com/docs/man1/grep.1.asp) ([ **`grep`**](http://www.mkssoftware.com/docs/man1/grep.1.asp) **`-E`** ) also accept these two metacharacters:

>
>     \< \>
>     >

These have the following meanings:

`.`


A dot character matches any single character of the input line.

`^`


The `^` character does not match any character but represents the beginning of the input line. For example, `^A` is a regular expression matching the letter `A` at the beginning of a line. The `^` character is only special at the beginning of a regular expression, or after a `(` or `|`.

`$`


This does not match any character but represents the end of the input line. For example, `A$` is a regular expression matching the letter `A` at the end of a line. The `$` character is only special at the end of a a regular expression, or before a `)` or `|`.

`[` _bracket-expression_` ]`


A bracket expression enclosed in square brackets is a regular expression that matches a single character, or collating element.

a)


If the initial character is a circumflex `^`, then this bracket expression is complemented. It shall match any character or collating-element except for the expressions specified in the bracket expression.

b)


If the first character after any potential circumflex is either a dash (`-`), or a closing square bracket (`]`), then that character shall match exactly that character; that is a literal dash or closing square bracket.

c)


Collating sequences may be specified by enclosing their name inside square bracket period. For example, `[.ch.]` matches the multi-character collating sequence `ch` (if the current language supports that collating sequence). Any single character is itself. It is an error to give a collating sequence that isn't part of the current locale.

d)


Equivalence classes may be specified by enclosing a character or collating sequence inside square bracket equals. For example, `[=a=]` matches any character in the same equivalence class as `a`. This normally expands to all the variants of `a` in the current locale: for example, `a`, `\(a:`, `\(a``, ... On some locales it might include both the uppercase and lowercase of a given character. In the POSIX locale, this always expands to only the character given.

e)


Within a character class expression (one made with square brackets), the following constructs may be used to represent sets of characters. These constructs are used for internationalization and handle the different collating sequences as required by POSIX.

`[:alpha:]`
     Any alphabetic character.
`[:lower:]`
     Any lowercase alphabetic character.
`[:upper:]`
     Any uppercase alphabetic character.
`[:digit:]`
     Any digit character.
`[:alnum:]`
     Any alphanumeric character (alphabetic or digit).
`[:space:]`
     Any white space character (blank, horizontal tab, vertical tab).
`[:graph:]`
     Any printable character, except the blank character.
`[:print:]`
     Any printable character, including the blank character.
`[:punct:]`
     Any printable character that is not white space or alphanumeric.
`[:cntrl:]`
     Any non-printable character.

For example, given the character class expression

>
>     [:alpha:]
>     >

you need to enclose the expression within another set of square brackets, as in:

>
>     /[[:alpha:]]/
>     >

f)


Character ranges are specified by a dash (`-`) between two characters, or collating sequences. This indicates all character or collating sequences which collate between two characters or collating sequences. The range does not refer to the native character set. For example, in the POSIX locale, `[a-z]` means all lowercase letters, even if they don't agree with the binary machine ordering. However, since many other locales do not collate in this manner, ranges should not be used in Strictly Conforming POSIX.2 applications. A collating sequence may explicitly be an endpoint of a range; for example, `[[.ch.]-[.ll.]]` is valid; however equivalence classes or character classes may not: `[[=a=]-z]` is illegal.

`\`


This character is used to turn off the special meaning of metacharacters. For example, `\.` only matches a dot character. Note that `\\` matches a literal `\` character. Also note the special case of ``\` _d_ ' described below.

`\` _d_


For _d_ representing any single decimal digit (from 1 to 9), this pattern is equivalent to the string matching the _d_ th expression enclosed within the `()` characters (or `\(\)` for some commands) found at an earlier point in the regular expression. Parenthesized expressions are numbered by counting `(` characters from the left.

Constructs of this form can be used in the replacement strings of substitution commands (for example, the **`s`** command in Ex, or the ` sub` function of [**`awk`**](http://www.mkssoftware.com/docs/man1/awk.1.asp)), to stand for constructs matched by parts of the regular expression. For example, in the following Ex command

>
>     s/\(.*\):\(.*\)/\2:\1/
>     >

the ` \1` stands for everything matched by the first `\(.*\)` and the `\2` stands for everything matched by the second. The result of the command is to swap everything before the `:` with everything after.

_regexp_` *`


A regular expression _regexp_ followed by ` *` matches a string of **`zero`** or more strings that would match _regexp_. For example, ` A*` matches `A`, `AA`, `AAA`, and so on. It also matches the null string (zero occurrences of `A`).

_regexp_` +`


A regular expression _regexp_ followed by ` +` matches a string of one or more strings that would match _regexp_.

_regexp_`?`


A regular expression _regexp_ followed by `?` matches a string of zero or one occurrences of strings that would match _regexp_.

_char_` {` _n_` }`
_char_` \{` _n_` \}`


In this expression (and the ones to follow), _char_ is a regular expression that stands for a single character (for example, a literal character or a period (`.` )). Such a regular expression followed by a number in brace brackets stands for that number of repetitions of a character. For example, `X\{3\}` stands for `XXX`. In basic regular expressions, in order to reduce the number of special characters, `{` and `}` must be escaped by the `\` character to make them special, as shown in the second form (and the ones to follow).

_char_` {` _min,_` }`
_char_` \{` _min,_` \}`


When a number, _min_ , followed by a comma appears in braces following a single-character regular expression, it stands for at least _min_ repetitions of a character. For example, ` X\{3,\}` stands for at least three repetitions of `X`.

_char_` {` _min,max_` }`
_char_` \{` _min,max_` \}`


When a single-character regular expression is followed by a pair of numbers in braces, it stands for at least _min_ repetitions and no more than _max_ repetitions of a character. For example, ` X\{3,7\}` stands for three to seven repetitions of `X`.

_regexp1_` |` _regexp2_


This expression matches either regular expression _regexp1_ or _regexp2_.

` (` _regexp_
` \(` _regexp_` \)`


This lets you group parts of regular expressions. Except where overridden by parentheses, concatenation has the highest precedence. In basic regular expressions, in order to reduce the number of special characters, `(` and `)` must be escaped by the `\` character to make them special, as shown in the second form.

`\<`


This matches the beginning of an identifier, defined as the boundary between non-alphanumerics and alphanumerics (including underscore). This matches no characters, only the context.

`\>`


This construct is analogous to the `\<` notation except that it matches the end of an identifier.

Several regular expressions can be concatenated to form a larger regular expression.

### EX and Vi

The metacharacters available in the Ex and Vi editors are:

>
>     ^ $ . * \( \) [ \ \< \>
>     >

The regular expressions accepted by Ex and Vi are similar to basic regular expressions, except that the `\{` and `\}` characters are not special, the [: :] character class expressions are not available, and the `\<` and `\>` metacharacters can be used.

### Summary

The commands that use basic and extended regular expressions are as follows.

basic


[**`csplit`**](http://www.mkssoftware.com/docs/man1/csplit.1.asp), [**`ed`**](http://www.mkssoftware.com/docs/man1/ed.1.asp), [**`ex`**](http://www.mkssoftware.com/docs/man1/vi.1.asp), [**`grep`**](http://www.mkssoftware.com/docs/man1/grep.1.asp), [**`expr`**](http://www.mkssoftware.com/docs/man1/expr.1.asp), [**`sed`**](http://www.mkssoftware.com/docs/man1/sed.1.asp), and [**`vi`**](http://www.mkssoftware.com/docs/man1/vi.1.asp).

extended


[**`awk`**](http://www.mkssoftware.com/docs/man1/awk.1.asp), [**`egrep`**](http://www.mkssoftware.com/docs/man1/grep.1.asp) ([ **`grep`**](http://www.mkssoftware.com/docs/man1/grep.1.asp) **`-E`** ), [**`gres`**](http://www.mkssoftware.com/docs/man1/gres.1.asp), and [**`sed`**](http://www.mkssoftware.com/docs/man1/sed.1.asp) with the **`-E`** option.

Table 1 summarizes which features apply to which MKS Toolkit commands:

**Notation** |  **awk** |  **ed** |  **egrep** |  **expr** |  **gres** |  **pg** |  **sed** |  **vi**
---|---|---|---|---|---|---|---|---
**.** |  •  |  •  |  •  |  •  |  •  |  •  |  •  |  •
**^** |  •  |  •  |  •  |
|  •  |  •  |  •  |  •
**$** |  •  |  •  |  •  |  •  |  •  |  •  |  •  |  •
**[...]** |  •  |  •  |  •  |  •  |  •  |  •  |  •  |  •
**[::]** |  •  |  •  |  •  |  •  |  •  |  •  |  •  |
_re_ ***** |  •  |  •  |  •  |  •  |  •  |  •  |  •  |  •
_re_ **+** |  •  | |  •  | |  •  |  •  | |
_re_ **?** |  •  | |  •  | |  •  |  •  | |
_re_ **|** _re_ |  •  | |  •  | |  •  |  •  | |
**\** _d_ |  •  |  •  |  •  |  •  |  •  |  •  |  •  |  •
**(...)** |  •  | |  •  | |  •  |  •  | |
**\\(...\\)** | |  •  | |  •  | | |  •  |  •
**\<** | | |  •  | | | | |  •
**\>** | | |  •  | | | | |  •
**\\{ \\}** |  •  | |  •  | |  •  |  •  |  •  |
**{ }** |  •  | |  •  | | | | |


Table 1: Regular Expression Features

## EXAMPLES

The following patterns are given as illustrations, along with plain language descriptions of what they match:

` abc`


matches any line of text containing the three letters `abc` in that order.

`a.c`


matches any string beginning with the letter `a`, followed by **_any_** character, followed by the letter ` c`.

`^.$`


matches any line containing exactly one character (the newline is not counted).

`a(b*|c*)d`


matches any string beginning with a letter `a`, followed by either zero or more of the letter `b`, or zero or more of the letter `c`, followed by the letter `d`.

`.* [a-z]+ .*`


matches any line containing a **_word_** , consisting of lowercase alphabetic characters, delimited by at least one space on each side.

`(morty).*\1`
`morty.*morty`


These expressions both match lines containing at least two occurrences of the string `morty`.

`[[:space:][:alnum:]]`


Matches any character that is either a white space character or alphanumeric.




## SEE ALSO

**Commands:**
    [ **`awk`**](http://www.mkssoftware.com/docs/man1/awk.1.asp), [**`ed`**](http://www.mkssoftware.com/docs/man1/ed.1.asp), [**`expr`**](http://www.mkssoftware.com/docs/man1/expr.1.asp), [**`grep`**](http://www.mkssoftware.com/docs/man1/grep.1.asp), [**`gres`**](http://www.mkssoftware.com/docs/man1/gres.1.asp), [**`pg`**](http://www.mkssoftware.com/docs/man1/pg.1.asp), [**`sed`**](http://www.mkssoftware.com/docs/man1/sed.1.asp), [**`vi`**](http://www.mkssoftware.com/docs/man1/vi.1.asp)
