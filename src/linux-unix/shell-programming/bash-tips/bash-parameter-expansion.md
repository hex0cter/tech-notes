# BASH Parameter Expansion

The ‘$’ character introduces parameter expansion, command substitution, or arithmetic expansion. The parameter name or symbol to be expanded may be enclosed in braces, which are optional but serve to protect the variable to be expanded from characters immediately following it which could be interpreted as part of the name.

When braces are used, the matching ending brace is the first ‘}’ not escaped by a backslash or within a quoted string, and not within an embedded arithmetic expansion, command substitution, or parameter expansion.

The basic form of parameter expansion is ${parameter}. The value of parameter is substituted. The braces are required when parameter is a positional parameter with more than one digit, or whenparameter is followed by a character that is not to be interpreted as part of its name.

If the first character of parameter is an exclamation point (!), a level of variable indirection is introduced. Bash uses the value of the variable formed from the rest of parameter as the name of the variable; this variable is then expanded and that value is used in the rest of the substitution, rather than the value of parameter itself. This is known as `indirect expansion`. The exceptions to this are the expansions of ${!prefix
} and ${!name[@]} described below. The exclamation point must immediately follow the left brace in order to introduce indirection.

In each of the cases below, word is subject to tilde expansion, parameter expansion, command substitution, and arithmetic expansion.

When not performing substring expansion, using the form described below, Bash tests for a parameter that is unset or null. Omitting the colon results in a test only for a parameter that is unset. Put another way, if the colon is included, the operator tests for both parameter’s existence and that its value is not null; if the colon is omitted, the operator tests only for existence.

```
${parameter:-word}
```


If parameter is unset or null, the expansion of word is substituted. Otherwise, the value of parameter is substituted.

```
${parameter:=word}
```


If parameter is unset or null, the expansion of word is assigned to parameter. The value of parameter is then substituted. Positional parameters and special parameters may not be assigned to in this way.

```
${parameter:?word}
```


If parameter is null or unset, the expansion of word (or a message to that effect if word is not present) is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of parameter is substituted.

```
${parameter:+word}
```



If parameter is null or unset, nothing is substituted, otherwise the expansion of word is substituted.

```
${parameter:offset}
${parameter:offset:length}
```


Expands to up to length characters of parameter starting at the character specified by offset. If length is omitted, expands to the substring of parameter starting at the character specified by offset.length and offset are arithmetic expressions (see [Shell Arithmetic](http://www.gnu.org/software/bash/manual/bashref.html#Shell-Arithmetic)). This is referred to as Substring Expansion.

If offset evaluates to a number less than zero, the value is used as an offset from the end of the value of parameter. If length evaluates to a number less than zero, and parameter is not ‘@’ and not an indexed or associative array, it is interpreted as an offset from the end of the value of parameter rather than a number of characters, and the expansion is the characters between the two offsets. If parameter is ‘@’, the result is length positional parameters beginning at offset. If parameter is an indexed array name subscripted by ‘@’ or ‘*’, the result is the length members of the array beginning with `${parameter[offset]}`. A negative offset is taken relative to one greater than the maximum index of the specified array. Substring expansion applied to an associative array produces undefined results.

Note that a negative offset must be separated from the colon by at least one space to avoid being confused with the ‘:-’ expansion. Substring indexing is zero-based unless the positional parameters are used, in which case the indexing starts at 1 by default. If offset is 0, and the positional parameters are used, `$@` is prefixed to the list.

```
${!prefix*}
${!prefix@}
```

Expands to the names of variables whose names begin with prefix, separated by the first character of the `IFS` special variable. When ‘@’ is used and the expansion appears within double quotes, each variable name expands to a separate word.

```
${!name[@]}
${!name[*]}
```

If name is an array variable, expands to the list of array indices (keys) assigned in name. If name is not an array, expands to 0 if name is set and null otherwise. When ‘@’ is used and the expansion appears within double quotes, each key expands to a separate word.
```
${#parameter}
```


The length in characters of the expanded value of parameter is substituted. If parameter is ‘*’ or ‘@’, the value substituted is the number of positional parameters. If parameter is an array name subscripted by ‘*’ or ‘@’, the value substituted is the number of elements in the array.

```
${parameter#word}
${parameter##word}
```


The word is expanded to produce a pattern just as in filename expansion (see [Filename Expansion](http://www.gnu.org/software/bash/manual/bashref.html#Filename-Expansion)). If the pattern matches the beginning of the expanded value of parameter, then the result of the expansion is the expanded value of parameter with the shortest matching pattern (the ‘#’ case) or the longest matching pattern (the ‘##’ case) deleted. If parameter is ‘@’ or ‘*’, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list. If parameter is an array variable subscripted with ‘@’ or ‘*’, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.
```
${parameter%word}
${parameter%%word}
```

The word is expanded to produce a pattern just as in filename expansion. If the pattern matches a trailing portion of the expanded value of parameter, then the result of the expansion is the value of parameter with the shortest matching pattern (the ‘%’ case) or the longest matching pattern (the ‘%%’ case) deleted. If parameter is ‘@’ or ‘*’, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list. If parameter is an array variable subscripted with ‘@’ or ‘*’, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list.

```
${parameter/pattern/string}
```

The pattern is expanded to produce a pattern just as in filename expansion. Parameter is expanded and the longest match of pattern against its value is replaced with string. If pattern begins with ‘/’, all matches of pattern are replaced with string. Normally only the first match is replaced. If pattern begins with ‘#’, it must match at the beginning of the expanded value of parameter. If pattern begins with ‘%’, it must match at the end of the expanded value of parameter. If string is null, matches of pattern are deleted and the `/` following pattern may be omitted. If parameteris ‘@’ or ‘*’, the substitution operation is applied to each positional parameter in turn, and the expansion is the resultant list. If parameter is an array variable subscripted with ‘@’ or ‘*’, the substitution operation is applied to each member of the array in turn, and the expansion is the resultant list.

```
${parameter^pattern}
${parameter^^pattern}
${parameter,pattern}
${parameter,,pattern}
```

This expansion modifies the case of alphabetic characters in parameter. The pattern is expanded to produce a pattern just as in filename expansion. The ‘^’ operator converts lowercase letters matching pattern to uppercase; the ‘,’ operator converts matching uppercase letters to lowercase. The ‘^^’ and ‘,,’ expansions convert each matched character in the expanded value; the ‘^’ and ‘,’ expansions match and convert only the first character in the expanded value. If pattern is omitted, it is treated like a ‘?’, which matches every character. If parameter is ‘@’ or ‘*’, the case modification operation is applied to each positional parameter in turn, and the expansion is the resultant list. If parameter is an array variable subscripted with ‘@’ or ‘*’, the case modification operation is applied to each member of the array in turn, and the expansion is the resultant list.

<http://www.gnu.org/software/bash/manual/bashref.html>

<http://stackoverflow.com/questions/874389/bash-test-for-a-variable-unset-using-a-function>

<http://stackoverflow.com/questions/10416289/how-to-understand-and-in-bash>
