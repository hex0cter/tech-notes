
date: None  
author(s): None  

# [Python Objects - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/python/python-objects)

Reset your brain.

## Objects [#](http://effbot.org/zone/python-objects.htm#objects)

All Python objects have this:

  * a unique identity (an integer, returned by _id(x)_ )
  * a type (returned by _type(x)_ )
  * some content



You cannot change the identity.

You cannot change the type.

Some objects allow you to change their _content_ (without changing the identity or the type, that is).

Some objects don’t allow you to change their content (more below).

The type is represented by a type object, which knows more about objects of this type (how many bytes of memory they usually occupy, what methods they have, etc).

( _Update: In CPython 2.2 and later, you can change the type under[some rather limited circumstances](http://article.gmane.org/gmane.comp.python.general/427452)_.)

## More about objects [#](http://effbot.org/zone/python-objects.htm#more-about-objects)

Objects may also have this:

  * zero or more methods (provided by the type object)
  * zero or more names



Some objects have methods that allow you to change the contents of the object (modify it in place, that is).

Some objects only have methods that allow you to access the contents, not change it.

Some objects don’t have any methods at all.

Even if they have methods, you can never change the type, nor the identity.

Things like attribute assignment and item references are just syntactic sugar (more below).

## Names [#](http://effbot.org/zone/python-objects.htm#names)

The names are a bit different — they’re not really properties of the object, and the object itself doesn’t know what it’s called.

An object can have any number of names, or no name at all.

Names live in namespaces (such as a module namespace, an instance namespace, a function’s local namespace).

Namespaces are collections of (name, object reference) pairs (implemented using dictionaries).

When you call a function or a method, its namespace is initialized with the arguments you call it with (the names are taken from the function’s argument list, the objects are those you pass in).

## Assignment [#](http://effbot.org/zone/python-objects.htm#assignments)

Assignment statements modify namespaces, not objects.

In other words,

>  **name = 10**

means that you’re adding the name “name” to your local namespace, and making it refer to an integer object containing the value 10.

If the name is already present, the assignment replaces the original name:

>  **name = 10  
>  name = 20**

means that you’re first adding the name “name” to the local namespace, and making it refer to an integer object containing the value 10. You’re then replacing the name, making it point to an integer object containing the value 20. The original “10” object isn’t affected by this operation, and it doesn’t care.

In contrast, if you do:

>  **name = []  
>  name.append(1)**

you’re first adding the name “name” to the local namespace, making it refer to an empty list object. This modifies the namespace. You’re then calling a method on that object, telling it to append an integer object to itself. This modifies the content of the list object, but it doesn’t touch the namespace, and it doesn’t touch the integer object.

Things like _name.attr_ and _name[index]_ are just syntactic sugar for method calls. The first corresponds to ___setattr___ / ___getattr___ , the second to ___setitem___ / ___getitem___ (depending on which side of the assignment they appear).

That’s all.

[Copyright](http://effbot.org/zone/copyright.htm) © 2000 by Fredrik Lund

