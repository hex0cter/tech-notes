
date: None  
author(s): None  

# [Add a Binary Payload to your Shell Scripts - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/add-a-binary-payload-to-your-shell-scripts)

Feb 19, 2009 By [Mitch Frazier](http://www.linuxjournal.com/users/mitch-frazier)

Generally when we think of shell scripts we think of editable text, but it's possible to add binary data to your shell script as well. In this case we're going to talk about adding a binary payload to the end of your shell script.

Adding a binary payload to a shell script could, for instance, be used to create a single file shell script that installs your entire software package which could be composed of hundreds of files. You merely append the tar or gzip file of your package as a binary payload to the script file, when the script runs it extracts the payload and does its task with the extracted files.

For this example I assume the appended file is a `tar.gz` file. The payload is appended to the end of an installation script preceded by a marker line (PAYLOAD:). The appended data is either uuencoded or just binary data. The script that follows takes a single argument which should be the `tar.gz` to append to the installation script. The`installation` script template `install.sh.in` is copied to `install.sh` with the payload appended. This script is named `addpayload.sh` follows:
    
    
    #!/bin/bash # Check for payload format option (default is uuencode).
    uuencode=1
    if [[ "$1" == '--binary' ]]; then
    	binary=1 uuencode=0 shift
    fi
    if [[ "$1" == '--uuencode' ]]; then
    	binary=0 uuencode=1 shift
    fi if [[ ! "$1" ]]; then
    	echo "Usage: $0 [--binary | --uuencode] PAYLOAD_FILE" exit 1
    fi if [[ $binary -ne 0 ]]; then # Append binary data. sed \ -e 's/uuencode=./uuencode=0/' \ -e 's/binary=./binary=1/' \ install.sh.in >install.sh echo "PAYLOAD:" >> install.sh cat $1 >>install.sh
    fi
    if [[ $uuencode -ne 0 ]]; then # Append uuencoded data. sed \ -e 's/uuencode=./uuencode=1/' \ -e 's/binary=./binary=0/' \ install.sh.in >install.sh echo "PAYLOAD:" >> install.sh cat $1 | uuencode - >>install.sh
    fi
    

In addition to appending the payload it also modifies the installer script to tell it whether the payload is binary or uuencoded.

The template script `install.sh.in` is out installation script which at this point just untars the payload and nothing else. Actually, it doesn't even untar the payload it just tests it with `tar`'s `-t` option:
    
    
    #!/bin/bash uuencode=1
    binary=0 function untar_payload()
    { match=$(grep --text --line-number '^PAYLOAD:$' $0 | cut -d ':' -f 1) payload_start=$((match + 1)) if [[ $binary -ne 0 ]]; then
     tail -n +$payload_start $0 | tar -tzvf - fi
    	if [[ $uuencode -ne 0 ]]; then
     tail -n +$payload_start $0 | uudecode | tar -tzvf - fi
    } read -p "Install files? " ans
    if [[ "${ans:0:1}" || "${ans:0:1}" ]]; then
    	untar_payload # Do remainder of install steps.
    fi exit 0
    

In the function `untar_payload` the script uses `grep` to search throught itself (`$0`) for the marker and then it extracts the line number from the `grep` output and adds one to it. This line number is then passed to `tail` preceded by a plus sign which causes `tail` to output everything starting at that line number. The data is then fed directly into `tar`for extraction if the payload is binary. If it's uuencoded then it's first fed into `uudecode`before being fed into `tar`.

To create our installer let's use a simple payload file that contains three files name a, b, and c. We'll add the payload as an uuencoded block:
    
    
    $ sh addpayload.sh --uuencode abc.tar.gz
    $ cat install.sh
    #!/bin/bash
    
    ... # Installer script lines (see above)
    read -p "Install files? " ans
    ... # More installer script lines (see above)
    exit 0
    
    PAYLOAD:
    begin 644 -
    M'XL(`))%G$D``^W12PJ$0`Q%T2REEI!HK%J/BM`]Z(F?_?O#J8+0&=TS"8'`
    M"[Q6_D\WV7V?5AH]=COWBYB9%_4J:Q$UK6J7I`&_R3+-[9B2_+YS_[F]&\8I
    JXJ%874#&J_X;^H_0!V2\ZC_3/P```````````````/!D!0OB?_,`*```
    `
    end
    

At the end of the file you see the `PAYLOAD:` marker and the uuencoded block. If we now run the script we get:
    
    
    $ sh install.sh
    Install files? y
    -rw-r--r-- mitch/users       0 2009-02-18 11:29 a
    -rw-r--r-- mitch/users       0 2009-02-18 11:29 b
    -rw-r--r-- mitch/users       0 2009-02-18 11:29 c
    

I won't show you the `--binary` usage but it produces the same result, albeit with a slightly smaller foot print since the payload does not have to be uuencoded.

______________________

Mitch Frazier is an Associate Editor for _Linux Journal_.

