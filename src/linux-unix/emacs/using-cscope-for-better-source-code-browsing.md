
date: None  
author(s): None  

# [Using cscope for better source-code browsing - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/using-cscope-for-better-source-code-browsing)

Posted by Vedang 

October 05,  
2007 

In my last two posts ([here](http://tech-rantings.blogspot.com/2007/09/source-code-browsing-using-emacs.html) and [here](http://tech-rantings.blogspot.com/2007/09/creating-tags-using-etags-and-find.html)), I explained how you can simplify the task of browsing through code. So why is it that I'm writing another post on the same topic?If you use the tags method I described, you'll notice one small drawback. I can jump across function definitions to follow the flow of code, but I cannot:a) See which functions are calling the function I'm browsing.b) See a list of all the functions called by the current function.

These are serious drawbacks when you're trying to hack through the jungle of kernel-code. This is where Cscope comes into the picture. __

> Cscope is designed to answer questions like:Where is this variable used?What is the value of this preprocessor symbol?Where is this function in the source files?What functions call this function?What functions are called by this function?Where does the message "out of space" come from?Where is this source file in the directory structure?What files include this header file?

You can [download the tarball here](http://sourceforge.net/project/showfiles.php?group_id=4664). Extract the contents into a convenient directory, and let's get ready to roll.To install Cscope, open a terminal and navigated to the extracted directory.

Now run the commands 

> _**./configuremake
> 
> sudo make install
> 
> **_

This should install cscope on your computer. I use cscope with emacs, so the next set of steps explain how to integrate it with emacs. If you wish to use csope with other browsers, please visit their website ([http://cscope.sourceforge.net](http://cscope.sourceforge.net/)) for instructions.

1) Make the 'cscope-indexer' script (in cscope/contrib/xcscope) executable. 

> _**sudo chmod a+x ./contrib/xcscope/cscope-indexer**_

2)Copy it into /usr/bin or /usr/sbin (it needs to be in $PATH) 

> _**sudo cp ./contrib/xcscope/cscope-indexer /usr/bin**_

3)Copy the file xcscope.el (in cscope/contrib/xcscope) to /etc/emacs (basically it has to be in the emacs load-path) 

> _**sudo cp ./contrib/xcscope/xcsope.el /etc/emacs**_

4)Edit your ~/.emacs file and add the line 

> _**(require 'xcscope)**_

Now you can use the cscope key bindings in emacs. Here is a list of the most common key-bindings:1) to create a cscope database for your code files, navigate to the topmost direcory (under which all your code directories of current project are) in emacs (using C-x,C-f) and type C-c s I. This should create the files cscope.out and cscope.files. These together represent your database

2)While browsing through any source code file, use the following bindings:

C-c s s Find symbol.C-c s d Find global definition.C-c s g Find global definition (alternate binding).C-c s G Find global definition without prompting.C-c s c Find functions calling a function.C-c s C Find called functions (list functions called from a function).C-c s t Find text string.C-c s e Find egrep pattern.C-c s f Find a file.C-c s i Find files #including a file.

3)To navigate the cscope search results use:

C-c s n Next symbol.C-c s N Next file.C-c s p Previous symbol.C-c s P Previous file.

4)Once you have satisfied your curiosity, you can return to the point from where you jumped using

C-c s u Pop Mark

And thus, you have complete control over code navigation! I have used the file xcscope.el as a reference, and it goes on to detail far more complex tasks using cscope. Look into it once you get the hang of cscope! 

Filed under [Emacs](http://tech-rantings.blogspot.com/search/label/Emacs), [Open Source](http://tech-rantings.blogspot.com/search/label/Open%20Source)  
  
---

