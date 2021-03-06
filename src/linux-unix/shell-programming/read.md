# [Unix command：read](http://docs.sun.com/app/docs/doc/819-2239/read-1?a=view)

    Name

    read– read a line from standard input

    Synopsis

    /usr/bin/read [-r] var...
    sh
    read name...
    csh
    set variable= $<
    ksh
    read [-prsu [n]] [name ? prompt] [name]...
    ksh93
    read [-Aprs] [-d delim] [-n nsize] [-N nsize] [-t timeout][-u unit] [vname?prompt] [vname... ]

    Description

    /usr/bin/read

    The read utility reads a single line from standard input.

    By default, unless the -r option is specified, backslash (\) acts as an escape character. If standard input is a terminal device and the invoking shell is interactive, read prompts for a continuation line when:

    The shell reads an input line ending with a backslash, unless the -r option is specified.

    A here-document is not terminated after a NEWLINE character is entered.

    The line is split into fields as in the shell. The first field is assigned to the first variable var, the second field to the second variable var, and so forth. If there are fewer var operands specified than there are fields, the leftover fields and their intervening separators is assigned to the last var. If there are fewer fields than vars, the remaining vars is set to empty strings.

    The setting of variables specified by the var operands affects the current shell execution environment. If it is called in a sub-shell or separate utility execution environment, such as one of the following:


    (read foo)
    nohup read ...
    find . -exec read ... \;
    it does not affect the shell variables in the caller's environment.

    The standard input must be a text file.

    sh
    One line is read from the standard input and, using the internal field separator, IFS (normally space or tab), to delimit word boundaries, the first word is assigned to the first name, the second word to the second name, and so on, with leftover words assigned to the last name. Lines can be continued using \newline. Characters other than NEWLINE can be quoted by preceding them with a backslash. These backslashes are removed before words are assigned to names, and no interpretation is done on the character that follows the backslash. The return code is 0, unless an end-of-file is encountered.

    csh
    The notation:


    set variable = $<
    loads one line of standard input as the value for variable. (See csh(1)).

    ksh
    The shell input mechanism. One line is read and is broken up into fields using the characters in IFS as separators. The escape character, (\), is used to remove any special meaning for the next character and for line continuation. In raw mode, the -r, the , and the \ character are not treated specially. The first field is assigned to the first name, the second field to the second name, and so on, with leftover fields assigned to the last name. The -p option causes the input line to be taken from the input pipe of a process spawned by the shell using |&. If the -s flag is present, the input is saved as a command in the history file. The flag -u can be used to specify a one digit file descriptor unit n to read from. The file descriptor can be opened with the exec special command. The default value of n is 0. If name is omitted, REPLY is used as the default name. The exit status is 0 unless the input file is not open for reading or an end-of-file is encountered. An end-of-file with the -p option causes cleanup for this process so that another can be spawned. If the first argument contains a ?, the remainder of this word is used as a prompt on standard error when the shell is interactive. The exit status is 0 unless an end-of-file is encountered.

    ksh93
    read reads a line from standard input and breaks it into fields using the characters in the value of the IFS variable as separators. The escape character, \, is used to remove any special meaning for the next character and for line continuation unless the -r option is specified.

    If there are more variables than fields, the remaining variables are set to empty strings. If there are fewer variables than fields, the leftover fields and their intervening separators are assigned to the last variable. If no var is specified, the variable REPLY is used.

    When var has the binary attribute and -n or -N is specified, the bytes that are read are stored directly into var.

    If you specify ?prompt after the first var, read displays a prompt on standard error when standard input is a terminal or pipe.

    Options
    /usr/bin/read, ksh
    The following option is supported by /usr/bin/read and ksh:

    -r
    Do not treat a backslash character in any special way. Considers each backslash to be part of the input line.

    ksh93
    The following options are supported by ksh93:

    -A
    Unset var, and create an indexed array containing each field in the line starting at index 0.

    -d delim
    Read until delimiter delim instead of to the end of line.

    -n nsize
    Read at most nsize bytes. Binary field size is in bytes.

    -N nsize
    Read exactly nsize bytes. Binary field size is in bytes.

    -p
    Read from the current co-process instead of standard input. An end of file causes read to disconnect the co-process so that another can be created.

    -r
    Do not treat \ specially when processing the input line.

    -s
    Save a copy of the input as an entry in the shell history file.

    -t timeout
    Specify a timeout in seconds when reading from a terminal or pipe.

    -u fd
    Read from file descriptor number fd instead of standard input. The default value is 0.

    -v
    When reading from a terminal, display the value of the first variable and use it as a default value.

    Operands
    The following operand is supported:

    var
    The name of an existing or non-existing shell variable.

    Examples
    Example 1 Using the read Command

    The following example for /usr/bin/read prints a file with the first field of each line moved to the end of the line:


    example% while read -r xx yy
    do
            printf "%s %s\n" "$yy" "$xx"
    done < input_file
    Environment Variables
    See environ(5) for descriptions of the following environment variables that affect the execution of read: LANG, LC_ALL, LC_CTYPE, LC_MESSAGES, and NLSPATH.

    IFS
    Determines the internal field separators used to delimit fields.

    PS2
    Provides the prompt string that an interactive shell writes to standard error when a line ending with a backslash is read and the -r option was not specified, or if a here-document is not terminated after a NEWLINE character is entered.

    Exit Status
    The following exit values are returned:

    0
    Successful completion.

    >0
    End-of-file was detected or an error occurred.

    Attributes
    See attributes(5) for descriptions of the following attributes:

    /usr/bin/read, csh, ksh, sh
    ATTRIBUTE TYPE

    ATTRIBUTE VALUE

    Availability

    SUNWcsu

    Interface Stability

    Committed

    Standard

    See standards(5).

    ksh93
    ATTRIBUTE TYPE

    ATTRIBUTE VALUE

    Availability

    SUNWcsu

    Interface Stability

    Uncommitted

    See Also
    csh(1), ksh(1), ksh93(1), line(1), set(1), sh(1), attributes(5), environ(5), standards(5)
