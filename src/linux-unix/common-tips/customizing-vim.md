
date: Apr 01, 2000
author(s): [Dan Puckett](http://www.linuxjournal.com/user/800675)

# Customizing Vim


Some great customizations to Vim's default behavior—make Vim work for you.

Vim is an editor designed to work like that most venerable of UNIX editors, vi. Vim doesn't just clone vi; it extends vi with features like multi-level undo, a graphical interface (if you want it), windows, block operations, on-line help and syntax coloring.

Along with the new features, Vim 5.5 (the current version as I write) has 196 options you can set. Practically any behavior you might have found obnoxious in plain vi can be configured to your liking in Vim. To download or get more information on Vim, see the Vim home page at <http://www.vim.org/>. Within Vim, you can view the on-line help at any time by pressing **ESC** , typing **:help** and pressing **ENTER**.

I'll admit that the thought of trudging through 196 options on the off chance that one or two will do what I want might seem a bit daunting, so here are several of my favorite Vim customizations just to get you started. These customizations have saved me much frustration and helped make a regular Vim user out of me.

Saving Your Customizations

Before I talk about specific Vim customizations, however, let me explain how to save your customizations so they are loaded each time you start Vim. When you first start using Vim, it will be 100% compatible with vi. You won't notice any of Vim's fancy features until you activate them.

This behavior is nice: it allows system administrators to replace /bin/vi with a link to Vim without their users rising up against them screaming, “vi is broken. Fix it!” In fact, some people have used Vim for years this way without realizing they were using anything fancier than vi. But strict vi emulation can confuse people who expect to see all of Vim's bells and whistles right from the start.

Luckily, it's easy to convince Vim that we know we're actually in Vim and not in vi. Vim customizations are stored in a file called .vimrc in your home directory. If Vim sees that you have a .vimrc file—even if that file is empty—Vim will turn off vi-compatibility mode, which will configure Vim as Vim, rather than vi.

If you don't have a .vimrc file, but you do have an .exrc file that you have used to customize your vi sessions in the past, execute the command


    mv ~/.exrc ~/.vimrc


to rename your .exrc file to .vimrc.

If you have neither a .exrc file nor a .vimrc file, execute the command


    touch ~/.vimrc


to create an empty .vimrc file.

You're now ready to begin configuring Vim in earnest. You can add commands to your .vimrc file in the same way you would add them to your .exrc file. That is, if you tried Vim's incremental searching feature (which I'll describe shortly) by pressing the **ESC** key and entering the command


    :set incsearch


and decided you wanted to make incremental searching the default behavior for future Vim sessions, you could do it by putting the line


    set incsearch


into your .vimrc file on a line by itself. Note the lack of a leading colon.

Finding it Fast: incsearch

Suppose you have the following text file to edit:


    In Xanadu did Kubla Khan
    A stately pleasure-dome decree:
    Where Alph, the sacred river, ran
    Through caverns measureless to man
    Down to a sunless sea.


Your cursor is on the **I** in the first line. You need to get to the first occurrence of the word “measureless”. How do you do it?

One way is to press **/** to put Vim into search mode, type in “measureless”, and press **ENTER**. Vim will find the first “measureless” after the current cursor position and leave your cursor on the **m**. Easy, in principle, that is. I'm not such a great typist. When I try to search forward for the word “measureless”, I'm just as likely to misspell it as not. And if I misspell it as “measurless”, I won't realize my mistake until I press **ENTER** and Vim returns “Pattern not found: measurless”.

I could increase my chances of typing the search pattern correctly by searching for a substring of “measureless”. For example, if I search for “measu”, I have fewer characters to type, which means fewer ways I can mistype my search pattern. However, that means I have to guess how many characters will specify a unique substring of the word I want to find. If I don't type in enough for my search pattern, I'll end up in the wrong location. For example, if _search_ for “me”, I'll end up in “pleasure-dome” on line two rather than where I want to be, which is on line four. I'd then have to search again by pressing **n**.

Vim's incremental search feature can help with both of these problems. To try it out, press the **ESC** key to enter command mode, then type


    :set incsearch


and press **ENTER**.

Incremental searching means that as you enter your search pattern, Vim will show you the next match as you type each letter. So when you start your search for “measureless” by pressing **m** , Vim will immediately search forward for the first **m** in the file following the current cursor position. In this case, it's the **m** in “pleasure-dome” on line two. Vim will then highlight in the text the pattern it has matched so far for you. Since “pleasure-dome” isn't where you wanted to go, you need to type more letters in your search pattern. When you press **e** , “pleasure-dome” still matches the substring **me** , so Vim will highlight the “me” in “pleasure-dome” and wait for more input. When you press **a** , “pleasure-dome” no longer matches the substring **mea** , so Vim will highlight the next match for **mea** , which is “measureless” on line four. Jackpot! Since that's the word you are looking for, press **ENTER** , and Vim will leave your cursor on the **m** in “measureless”.

With incremental searching, you always know what the results of your search will be, because the results are highlighted on your screen at all times. If you misspell your search pattern, Vim will no longer show you a highlighted match for your search pattern. When your highlighted match string disappears from the screen, you know immediately that you should back up by using the **BACKSPACE** key, and fix your search pattern. If you change your mind about what you wish to search for, you can press the **ESCAPE** key, and Vim will return the cursor to its previous location.

Even Better Searching: ignorecase and smartcase

Programmers often don't capitalize code consistently. I'm no exception here. From one program to another—and sometimes even, to my shame, within the same program—my capitalization scheme changes.

“Let's see, was that subroutine named “CrashAndBurn”, “CRASHANDBURN”, “crashandburn” or “Crashandburn”?” If your editor is too picky about distinguishing upper-case from lower-case letters in its search patterns, you'll have a hard time matching the string. On the other hand, sometimes case is significant, and you do want to find “CrashAndBurn” and not “crashandburn”. What to do?

By default, both vi and Vim won't match anywhere in the text where the capitalization isn't exactly the same as the search pattern you entered; however, we can change this default behavior. Vim has a couple of options that, when used together, can take the pain out of upper/lower-case confusion. You can try these options by pressing the **ESCAPE** key, then typing the following two commands, pressing **ENTER** after each one:


    :set ignorecase
    :set smartcase


The ignorecase option is supported in vi as well as in Vim. It entirely disregards upper- and lower-case distinctions in search patterns. With ignorecase set, a search for the pattern “crashandburn” will match “CrAsHaNdBuRn” and “crashANDburn” as well as “crashandburn” in the text.

This is an improvement over the default behavior in some cases, but what if I really do want to search based on case distinctions? Will I have to set and unset ignorecase each time I want to search a different way?

In vi, the answer, unfortunately, is yes. Vim is a little more subtle, though, in that it offers the smartcase option as well. If both ignorecase and smartcase are set, Vim will ignore the case of the search only if the search pattern is all in lower-case. But if there are any upper-case characters in the search pattern, Vim will assume you really want to do a case-sensitive search and will do its matching accordingly.

For example, with both ignorecase and smartcase turned on, Vim will match “crashandburn” with both “CrashAndBurn” and “crashandburn”. If you enter “CrashAndBurn” as your search pattern, however, Vim will only match the string “CrashAndBurn” in the text. It won't match “crashaNDBUrn”.

In practice, this combination of options works out to be a good compromise, letting you balance case-sensitive and case-insensitive searches nicely without having to set or unset an option to do them.

Keep Some Context: scrolloff

When I'm editing a program or document, I like to have a little context around my work by keeping the line of text I'm working on a couple of lines away from the edge of the window at all times.

In vi, I would maintain this bit of context by scrolling a few lines either above or below the line I wished to edit, then moving back to my destination and doing my editing. It wasn't great, but it was better than typing blind, which is how I felt whenever I worked on the first or last line of the screen.

Luckily, Vim can maintain some context for you automatically through the use of the scrolloff option. You can try setting this option by pressing the **ESC** key and entering


    :set scrolloff=2


The **2** means I want at least two lines of context visible around the cursor at all times. You can set this to any number you like. Vim will scroll your file so that your cursor will never be closer to the top and bottom edge of the screen than the number of lines you specify.

Vim won't always be able to honor your scrolloff specification. If you're near the bottom or top of the file, there may not be enough lines left between your cursor and the file's beginning or end to give you the context you asked for. It will do the best it can, though.

I recommend the scrolloff feature highly. It's been a great help to me.

File Name Completion: wildmode

I hate typing file names. Why should I have to type out a file name like “thelongestfilenameintheworld.html” if the starting characters “thelong” will uniquely identify it from all other files in the current subdirectory? I also have the habit of wanting to edit a file deep within an unfamiliar directory structure.

Luckily, Vim has file name completion. File name completion lets you enter a partial file name into Vim, then press the **TAB** key to have Vim search for a file or directory name that could complete it. If Vim finds exactly one file or directory that matches, it fills in the rest of the name. If Vim can't find any match, it beeps.

What if Vim finds more than one file or directory name that matches? You can specify what Vim does next in this case by setting the wildmode option. The default setting for wildmode is “full”. When wildmode is set like this, the first time you press **TAB** , Vim will fill in one of the files or directory names that match what you have typed so far. If you hit **TAB** again, Vim will show you another file that completes your match. As you keep pressing **TAB** , Vim will go through all the possible completions. When it runs out, the next time you press **TAB** , Vim will show you the original incomplete string you entered. Now you're back where you started. If you press **TAB** again, Vim will show you the first match again.

While this is good, I prefer my file name completion to work a little differently. Here's how I like to have wildmode set:


    :set wildmode=longest,list


Setting wildmode this way makes Vim act as follows. When I enter part of a file name and press **TAB** , Vim completes my file name to the longest common string among the alternatives. It then waits for me to do one of the following: press **ENTER** to accept that as the file name, keep typing the file name from that place, press **ESC** to cancel the command, or press **TAB** again. The second time I press **TAB** , Vim will list all possible files that could complete my partial file or directory name.

Don't like either of the file completion methods I listed above? Not to worry: wildmode has many different options. For details, enter


    :help wildmode


and Vim will show you every possible option.

Enjoy customizing Vim. If you take one step at a time, you'll find that using Vim becomes more and more pleasant as time goes by. I think the more you make Vim work your way rather than its default way, the more you'll come to like it.

[More Information](http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/038/3805/3805s1.html)
