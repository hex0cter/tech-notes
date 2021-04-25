
date: None  
author(s): None  

# [Easy way to concatenate PDF files in Ubuntu Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/easy-way-to-concatenate-pdf-files-in-ubuntu-linux)

http://doeidoei.wordpress.com/2009/04/12/easy-way-to-concatenate-pdf-files-in-ubuntu-linux/

gs -q -sPAPERSIZE=a4 -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=output.pdf file1.pdf file2.pdf file3.pdf [...] lastfile.pdf  
  
---

