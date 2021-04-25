
date: None  
author(s): None  

# [如何只在堆上创建对象，如何只在栈上创建对象 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/heap-or-stack)

<http://topic.csdn.net/t/20050718/09/4150911.html>

========================================================================

class HeapOnly { public: HeapOnly() { cout << "constructor." << endl; } void destroy () const { delete this; } private: ~HeapOnly() {} }; 

========================================================================

class OnlyStack { public: OnlyStack(){} private: void* operator new( size_t ); };   
  
---

