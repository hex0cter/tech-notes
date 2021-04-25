
date: None  
author(s): None  

# [Python passes by reference - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/python/python-passes-by-reference)

<http://stackoverflow.com/questions/534375/passing-values-in-python>

Python passes references-to-objects by value (like Java), and everything in Python is an object. This sounds simple, but then you will notice that some data types seem to exhibit pass-by-value characteristics, while others seem to act like pass-by-reference... what's the deal?

It is important to understand mutable and immutable objects. Some objects, like strings, tuples, and numbers, are immutable. Altering them inside a function/method will create a new instance and the original instance outside the function/method is not changed. Other objects, like lists and dictionaries are mutable, which means you can change the object in-place. Therefore, altering an object inside a function/method will also change the original object outside.  
  
---

