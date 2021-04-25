
date: None  
author(s): None  

# [Importing Python Modules - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/python/importing-python-modules)

The _import_ and _from-import_ statements are a constant cause of serious confusion for newcomers to Python. Luckily, once you’ve figured out what they really do, you’ll never have problems with them again.

This note tries to sort out some of the more common issues related to _import_ and _from-import_ and everything.

## There are Many Ways to Import a Module [#](http://effbot.org/zone/import-confusion.htm#many-ways)

Python provides at least three different ways to import modules. You can use the _import_ statement, the _from_ statement, or the builtin ___import___ function. (There are more contrived ways to do this too, but that’s outside the scope for this small note.)

Anyway, here’s how these statements and functions work:

  *  **import X** imports the module X, and creates a reference to that module in the current namespace. Or in other words, after you’ve run this statement, you can use _X.name_ to refer to things defined in module X.

  *  **from X import *** imports the module X, and creates references in the current namespace to all _public_ objects defined by that module (that is, everything that doesn’t have a name starting with “_”). Or in other words, after you’ve run this statement, you can simply use a plain _name_ to refer to things defined in module X. But X itself is not defined, so _X.name_ doesn’t work. And if _name_ was already defined, it is replaced by the new version. And if _name_ in X is changed to point to some other object, your module won’t notice.

  *  **from X import a, b, c** imports the module X, and creates references in the current namespace to the given objects. Or in other words, you can now use _a_ and _b_ and _c_ in your program.

  * Finally, **X = __import__(‘X’)** works like **import X** , with the difference that you 1) pass the module name as a string, and 2) explicitly assign it to a variable in your current namespace.




## Which Way Should I Use? [#](http://effbot.org/zone/import-confusion.htm#which-way-should-i-use)

Short answer: always use **import**.

As usual, there are a number of exceptions to this rule:

  *  **The Module Documentation Tells You To Use from-import**. The most common example in this category is _Tkinter_ , which is carefully designed to add only the widget classes and related constants to your current namespace. Using **import Tkinter** only makes your program harder to read; something that is generally a bad idea.

  *  **You’re Importing a Package Component**. When you need a certain submodule from a package, it’s often much more convenient to write **from io.drivers import zip** than **import io.drivers.zip** , since the former lets you refer to the module simply as **zip** instead of its full name. In this case, the _from-import_ statement acts pretty much like a plain _import_ , and there’s not much risk for confusion.

  *  **You Don’t Know the Module Name Before Execution**. In this case, use ___import__(module)_ where _module_ is a Python string. Also see the next item.

  *  **You Know Exactly What You’re Doing**. If you think you do, just go ahead and use _from-import_. But think twice before you ask for help ;-)




## What Does Python Do to Import a Module? [#](http://effbot.org/zone/import-confusion.htm#what-does-python-do)

When Python imports a module, it first checks the module registry ( _sys.modules_ ) to see if the module is already imported. If that’s the case, Python uses the existing module object as is.

Otherwise, Python does something like this:

  1. Create a new, empty module object (this is essentially a dictionary)
  2. Insert that module object in the _sys.modules_ dictionary
  3. Load the module code object (if necessary, compile the module first)
  4. Execute the module code object in the new module’s namespace. All variables assigned by the code will be available via the module object.



This means that it’s fairly cheap to import an already imported module; Python just has to look the module name up in a dictionary.

## Import Gotchas [#](http://effbot.org/zone/import-confusion.htm#import-gothas)

### Using Modules as Scripts [#](http://effbot.org/zone/import-confusion.htm#using-modules-as-scripts)

If you run a module as a script (i.e. give its name to the interpreter, rather than importing it), it’s loaded under the module name ___main___.

If you then import the same module from your program, it’s reloaded and reexecuted under its real name. If you’re not careful, you may end up doing things twice.

### Circular Imports [#](http://effbot.org/zone/import-confusion.htm#circular-imports)

In Python, things like _def_ , _class_ , and _import_ are statements too.

Modules are executed during import, and new functions and classes won’t appear in the module’s namespace until the _def_ (or _class_ ) statement has been executed.

This has some interesting implications if you’re doing recursive imports.

Consider a module _X_ which imports module _Y_ and then defines a function called _spam_ :
    
    
     # module X import Y def spam(): print "function in module x"

If you import _X_ from your main program, Python will load the code for _X_ and execute it. When Python reaches the **import Y** statement, it loads the code for _Y_ , and starts executing it instead.

At this time, Python has installed module objects for both _X_ and _Y_ in _sys.modules_. But _X_ doesn’t contain anything yet; the **def spam** statement hasn’t been executed.

Now, if _Y_ imports _X_ (a recursive import), it’ll get back a reference to an empty _X_ module object. Any attempt to access the _X.spam_ function on the module level will fail.
    
    
      # module Y from X import spam # doesn't work: spam isn't defined yet!

Note that you don’t have to use from-import to get into trouble:
    
    
     # module Y import X X.spam() # doesn't work either: spam isn't defined yet!

To fix this, either refactor your program to avoid circular imports (moving stuff to a separate module often helps), or move the imports to the end of the module (in this case, if you move **import Y** to the end of module X, everything will work just fine).

