
date: None  
author(s): None  

# [Operator new sample - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/operator-new-sample)

#include "malloc.h"  
#include "iostream.h"

class A{public: void * operator new (unsigned int size) { cout << "size is " << size << endl; return malloc(size); } A() { val=9; cout << "constructing "<< endl; } void set(int x) { val = x; } int val;

};

main(){ A * a = new A(); a->set (10); cout << "a.val = " << a->val << endl;

}

**Output:**

_/home/exiahan/code # **./a.out**_ size is 4constructinga.val = 10  
  
---

