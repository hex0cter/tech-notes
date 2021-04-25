
date: None  
author(s): None  

# [How to input Chinese under Linux SuSe 10 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/ime)

I have an English version of SuSe Linux and OpenOffice 2.0. However, I need to input and read simplified and traditional Chinese occasionally. Although this page describes how to setup Chinese input it should also work for other asian languages.

A) Several packages (some asian fonts and an input method) are required that can be installed as administrator/root using Yast. In Yast go to Software>Software Management. 

1\. Search for “ttf”. 

In amongst a list of software packages should be the following:

“ttf-arphic” and “ttf-arphic-[package name]”. Check the boxes and install all these ttf components by clicking on the “accept” icon (bottom right). 

2\. Search for “scim” .

In amongst a list of software packages check the following components

“scim”, “mlterm-scim”, “scim-input-pad”, “scim-pinyin”, “scim-qtimm”, “scim-tables”, “scim- tables-ja”, “scim-tables-ko”, “scim-tables-scim”, “scim-tables-zh”, “scim-uim” and “scim (KDE integration for SCIM)”.

B) Open a terminal and write write small file in your home directory that should be called “.chinese”. In it put the following lines:

export XMODIFIERS="@im=SCIM"

export GTK_IM_MODULE=scim

export QT_IM_SWITCHER=imsw-multi

export QT_IM_MODULE=scim

scim -d

These are commands for starting SCIM and making sure linux uses SCIM as the input method. 

C) Configure OpenOffice Writer so that it can handle Chinese fonts. Open up OpenOffice-writer by typing “Ooo-writer”. Open 'Tools>Options>Language Setttings>Language. Choose the asian language you would like to use eg. Simplified Chinese. 

D) Each time you want to write Chinese you may have to repeat this step. The commands you wrote in section B in the file “.chinese” will only work if your shell is 'bash'. To check what shell you are using open a terminal and type “echo $SHELL”, which will return your shell. If you are not in bash, it is easy to change shell. Just type “bash”. 

Next, type “source .chinese”. This will intialize SCIM (the chinese input method). You will see a grey icon appear in the right-hand corner of the panel.

Now launch the application in which you want to write Chinese. eg “OOo-writer”.

Turn on (and off) the Chinese input method by pressing the 'Ctrl' and 'Space' key simultaneously. This will cause a small menu bar to appear in which you can select which input method you want eg 'Simplified Chinese>Smart Pinyin'. Now when typing pinyin within the OpenOffice-writer will produce Chinese characters. 

  


[http://www-cryst.bioc.cam.ac.uk/~rene/resource/chinese_input_on_linux.html](http://www-cryst.bioc.cam.ac.uk/%7Erene/resource/chinese_input_on_linux.html)  


