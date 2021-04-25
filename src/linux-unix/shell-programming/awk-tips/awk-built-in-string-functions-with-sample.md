
date: None  
author(s): None  

# [Awk Built-in String Functions with Sample - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/awk-tips/awk-built-in-string-functions-with-sample)

Go up to [**Built-in**](http://docs.freebsd.org/info/gawk/gawk.info.Built-in.html) **.  
**
    
    
    Built-in Functions for String Manipulation
    ==========================================
    
       The functions in this section look at or change the text of one or
    more strings.
    
    `index(IN, FIND)'
         This searches the string IN for the first occurrence of the string
         FIND, and returns the position in characters where that occurrence
         begins in the string IN.  For example:
    
              awk 'BEGIN { print index("peanut", "an") }'
    
         prints `3'.  If FIND is not found, `index' returns 0.  (Remember
         that string indices in `awk' start at 1.)
    
    `length(STRING)'
         This gives you the number of characters in STRING.  If STRING is a
         number, the length of the digit string representing that number is
         returned.  For example, `length("abcde")' is 5.  By contrast,
         `length(15 * 35)' works out to 3.  How?  Well, 15 * 35 = 525, and
         525 is then converted to the string `"525"', which has three
         characters.
    
         If no argument is supplied, `length' returns the length of `$0'.
    
         In older versions of `awk', you could call the `length' function
         without any parentheses.  Doing so is marked as "deprecated" in the
         POSIX standard.  This means that while you can do this in your
         programs, it is a feature that can eventually be removed from a
         future version of the standard.  Therefore, for maximal
         portability of your `awk' programs you should always supply the
         parentheses.
    
    `match(STRING, REGEXP)'
         The `match' function searches the string, STRING, for the longest,
         leftmost substring matched by the regular expression, REGEXP.  It
         returns the character position, or "index", of where that
         substring begins (1, if it starts at the beginning of STRING).  If
         no match if found, it returns 0.
    
         The `match' function sets the built-in variable `RSTART' to the
         index.  It also sets the built-in variable `RLENGTH' to the length
         in characters of the matched substring.  If no match is found,
         `RSTART' is set to 0, and `RLENGTH' to -1.
    
         For example:
    
              awk '{
                     if ($1 == "FIND")
                       regex = $2
                     else {
                       where = match($0, regex)
                       if (where)
                         print "Match of", regex, "found at", where, "in", $0
                     }
              }'
    
         This program looks for lines that match the regular expression
         stored in the variable `regex'.  This regular expression can be
         changed.  If the first word on a line is `FIND', `regex' is
         changed to be the second word on that line.  Therefore, given:
    
              FIND fo*bar
              My program was a foobar
              But none of it would doobar
              FIND Melvin
              JF+KM
              This line is property of The Reality Engineering Co.
              This file created by Melvin.
    
         `awk' prints:
    
              Match of fo*bar found at 18 in My program was a foobar
              Match of Melvin found at 26 in This file created by Melvin.
    
    `split(STRING, ARRAY, FIELDSEP)'
         This divides STRING into pieces separated by FIELDSEP, and stores
         the pieces in ARRAY.  The first piece is stored in `ARRAY[1]', the
         second piece in `ARRAY[2]', and so forth.  The string value of the
         third argument, FIELDSEP, is a regexp describing where to split
         STRING (much as `FS' can be a regexp describing where to split
         input records).  If the FIELDSEP is omitted, the value of `FS' is
         used.  `split' returns the number of elements created.
    
         The `split' function, then, splits strings into pieces in a manner
         similar to the way input lines are split into fields.  For example:
    
              split("auto-da-fe", a, "-")
    
         splits the string `auto-da-fe' into three fields using `-' as the
         separator.  It sets the contents of the array `a' as follows:
    
              a[1] = "auto"
              a[2] = "da"
              a[3] = "fe"
    
         The value returned by this call to `split' is 3.
    
         As with input field-splitting, when the value of FIELDSEP is `"
         "', leading and trailing whitespace is ignored, and the elements
         are separated by runs of whitespace.
    
    `sprintf(FORMAT, EXPRESSION1,...)'
         This returns (without printing) the string that `printf' would
         have printed out with the same arguments (*note Using `printf'
         Statements for Fancier Printing: Printf.).  For example:
    
              sprintf("pi = %.2f (approx.)", 22/7)
    
         returns the string `"pi = 3.14 (approx.)"'.
    
    `sub(REGEXP, REPLACEMENT, TARGET)'
         The `sub' function alters the value of TARGET.  It searches this
         value, which should be a string, for the leftmost substring
         matched by the regular expression, REGEXP, extending this match as
         far as possible.  Then the entire string is changed by replacing
         the matched text with REPLACEMENT.  The modified string becomes
         the new value of TARGET.
    
         This function is peculiar because TARGET is not simply used to
         compute a value, and not just any expression will do: it must be a
         variable, field or array reference, so that `sub' can store a
         modified value there.  If this argument is omitted, then the
         default is to use and alter `$0'.
    
         For example:
    
              str = "water, water, everywhere"
              sub(/at/, "ith", str)
    
         sets `str' to `"wither, water, everywhere"', by replacing the
         leftmost, longest occurrence of `at' with `ith'.
    
         The `sub' function returns the number of substitutions made (either
         one or zero).
    
         If the special character `&' appears in REPLACEMENT, it stands for
         the precise substring that was matched by REGEXP.  (If the regexp
         can match more than one string, then this precise substring may
         vary.)  For example:
    
              awk '{ sub(/candidate/, "& and his wife"); print }'
    
         changes the first occurrence of `candidate' to `candidate and his
         wife' on each input line.
    
         Here is another example:
    
              awk 'BEGIN {
                      str = "daabaaa"
                      sub(/a*/, "c&c", str)
                      print str
              }'
    
         prints `dcaacbaaa'.  This show how `&' can represent a non-constant
         string, and also illustrates the "leftmost, longest" rule.
    
         The effect of this special character (`&') can be turned off by
         putting a backslash before it in the string.  As usual, to insert
         one backslash in the string, you must write two backslashes.
         Therefore, write `\\&' in a string constant to include a literal
         `&' in the replacement.  For example, here is how to replace the
         first `|' on each line with an `&':
    
              awk '{ sub(/\|/, "\\&"); print }'
    
         *Note:* as mentioned above, the third argument to `sub' must be an
         lvalue.  Some versions of `awk' allow the third argument to be an
         expression which is not an lvalue.  In such a case, `sub' would
         still search for the pattern and return 0 or 1, but the result of
         the substitution (if any) would be thrown away because there is no
         place to put it.  Such versions of `awk' accept expressions like
         this:
    
              sub(/USA/, "United States", "the USA and Canada")
    
         But that is considered erroneous in `gawk'.
    
    `gsub(REGEXP, REPLACEMENT, TARGET)'
         This is similar to the `sub' function, except `gsub' replaces
         *all* of the longest, leftmost, *nonoverlapping* matching
         substrings it can find.  The `g' in `gsub' stands for "global,"
         which means replace everywhere.  For example:
    
              awk '{ gsub(/Britain/, "United Kingdom"); print }'
    
         replaces all occurrences of the string `Britain' with `United
         Kingdom' for all input records.
    
         The `gsub' function returns the number of substitutions made.  If
         the variable to be searched and altered, TARGET, is omitted, then
         the entire input record, `$0', is used.
    
         As in `sub', the characters `&' and `\' are special, and the third
         argument must be an lvalue.
    
    `substr(STRING, START, LENGTH)'
         This returns a LENGTH-character-long substring of STRING, starting
         at character number START.  The first character of a string is
         character number one.  For example, `substr("washington", 5, 3)'
         returns `"ing"'.
    
         If LENGTH is not present, this function returns the whole suffix of
         STRING that begins at character number START.  For example,
         `substr("washington", 5)' returns `"ington"'.  This is also the
         case if LENGTH is greater than the number of characters remaining
         in the string, counting from character number START.
    
    `tolower(STRING)'
         This returns a copy of STRING, with each upper-case character in
         the string replaced with its corresponding lower-case character.
         Nonalphabetic characters are left unchanged.  For example,
         `tolower("MiXeD cAsE 123")' returns `"mixed case 123"'.
    
    `toupper(STRING)'
         This returns a copy of STRING, with each lower-case character in
         the string replaced with its corresponding upper-case character.
         Nonalphabetic characters are left unchanged.  For example,
         `toupper("MiXeD cAsE 123")' returns `"MIXED CASE 123"'.
    
    http://docs.freebsd.org/info/gawk/gawk.info.String_Functions.html

