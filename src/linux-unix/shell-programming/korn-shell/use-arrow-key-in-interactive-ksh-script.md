# [Use arrow key in interactive ksh script](http://www.unix.com/shell-programming-scripting/110380-using-arrow-keys-shell-scripts.html)

**Using arrow keys in shell scripts**

I recently needed to collect arrow keys (and function keys etc.) in a shell script so that I could run a text graphics-style data entry system (with text entry fields, drop-down list boxes, progress bars and the like). Yes you can do all this in shell, and portably too if you're careful.I've seen others asking how to capture keypresses in shell scripts in the past, with a variety of responses from other people, so thought you might all like to see a little mock-up program that catches keypresses and reports the key that was pressed. This has been tested in Solaris, Linux (SuSE) and AIX. It's written in ksh just because I like it, but would equally work in bash if you changed the 'print' commands to 'echo'. The script reports 10 keypresses in octal and then exits. Note the use of 'tput' to determine the correct terminal codes.

Enjoy.


    #!/bin/ksh
    AWK=gawk
    [ -x /bin/nawk ] && AWK=nawk
    ECHO="print"
    ECHO_N="print -n"

    tty_save=$(stty -g)

    function Get_odx
    {
        od -t o1 | $AWK '{ for (i=2; i<=NF; i++)
                            printf("%s%s", i==2 ? "" : " ", $i)
                            exit }'
    }

    # Grab terminal capabilities
    tty_cuu1=$(tput cuu1 2>&1 | Get_odx)            # up arrow
    tty_kcuu1=$(tput kcuu1 2>&1 | Get_odx)
    tty_cud1=$(tput cud1 2>&1 | Get_odx)            # down arrow
    tty_kcud1=$(tput kcud1 2>&1 | Get_odx)
    tty_cub1=$(tput cub1 2>&1 | Get_odx)            # left arrow
    tty_kcub1=$(tput kcud1 2>&1 | Get_odx)
    tty_cuf1=$(tput cuf1 2>&1 | Get_odx)            # right arrow
    tty_kcuf1=$(tput kcud1 2>&1 | Get_odx)
    tty_ent=$($ECHO | Get_odx)                      # Enter key
    tty_kent=$(tput kent 2>&1 | Get_odx)
    tty_bs=$($ECHO_N "\b" | Get_odx)                # Backspace key
    tty_kbs=$(tput kbs 2>&1 | Get_odx)

    # Some terminals (e.g. PuTTY) send the wrong code for certain arrow keys
    if [ "$tty_cuu1" = "033 133 101" -o "$tty_kcuu1" = "033 133 101" ]; then
        tty_cudx="033 133 102"
        tty_cufx="033 133 103"
        tty_cubx="033 133 104"
    fi

    stty cs8 -icanon -echo min 10 time 1
    stty intr '' susp ''

    trap "stty $tty_save; exit"  INT HUP TERM

    count=0
    while :; do
        [ $count -eq 10 ] && break
        count=$((count+1))

        keypress=$(dd bs=10 count=1 2> /dev/null | Get_odx)

        $ECHO_N "keypress=\"$keypress\""

        case "$keypress" in
            "$tty_ent"|"$tty_kent") $ECHO " -- ENTER";;
            "$tty_bs"|"$tty_kbs") $ECHO " -- BACKSPACE";;
            "$tty_cuu1"|"$tty_kcuu1") $ECHO " -- KEY_UP";;
            "$tty_cud1"|"$tty_kcud1"|"$tty_cudx") $ECHO " -- KEY_DOWN";;
            "$tty_cub1"|"$tty_kcub1"|"$tty_cubx") $ECHO " -- KEY_LEFT";;
            "$tty_cuf1"|"$tty_kcuf1"|"$tty_cufx") $ECHO " -- KEY_RIGHT";;
            *) $ECHO;;
        esac
    done

    stty $tty_save
