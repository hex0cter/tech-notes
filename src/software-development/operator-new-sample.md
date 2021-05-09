# Operator new sample

```C
#include "malloc.h"
#include "iostream.h"

class A
{
public:
    void * operator new (unsigned int size)
    {
        cout << "size is " << size << endl;
        return malloc(size);
    }
    A()
    {
        val=9;
        cout << "constructing "<< endl;
    }
    void set(int x) { val = x; }
    int val;
};

main()
{
    A * a = new A();
    a->set (10);
    cout << "a.val = " << a->val << endl;
}
```
**Output:**
```bash
/home/exiahan/code # ./a.out
size is 4
constructing
a.val = 10
```
