
date: None  
author(s): None  

# [Create and use static and shared C++ libraries - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/create-and-use-static-and-shared-c-libraries)

## Content

The goal of this document is to explain how to compile, link and use static and shared C++ libraries using g++ (GNU GCC) and ar (GNU ar) commands. If you are not familiar to g++ read first the [create a simple C++ program](http://www.iram.fr/~roche/code/c++/c++_HelloWorld.html) tutorial.

Click on following links to download the AddNumbers examples: [AddNumbers.tar.bz2](http://www.iram.fr/~roche/code/c++/files/AddNumbers.tar.bz2) and [AddNumbersClient.tar.bz2](http://www.iram.fr/~roche/code/c++/files/AddNumbersClient.tar.bz2).

program | version  
---|---  
g++ | 3.4.3  
ar | 2.15.92.0.2  
nm | 2.15.92.0.2  
c++filt | 3.4  
ldd | 2.3.4  
  
## Write a library

Let us write a simple code for the AddNumbers library that allow to store and add two integers. It is composed of both interface and source files.
    
    
    ~/workspace/C++/AddNumbers/inc/AddNumbers.h
    
    
    #ifndef _ADDNUMBERS_H
    #define _ADDNUMBERS_H
    
    class AddNumbers
    {
            private:
            int _a;
            int _b;
    
            public:
            AddNumbers ();
            ~AddNumbers ();
    
            void setA (int a);
            void setB (int b);
    
            int getA () const;
            int getB () const;
    
            int getSum () const;
    
    }; // AddNumbers
    
    #endif // _ADDNUMBERS_H
    
    
    ~/workspace/C++/AddNumbers/src/AddNumbers.cpp
    
    
    #include "AddNumbers.h"
    
    AddNumbers::AddNumbers ()
    : _a(0), _b(0)
    {
    }
    
    AddNumbers::~AddNumbers ()
    {
    }
    
    void AddNumbers::setA (int a)
    {
            _a = a;
    }
    
    void AddNumbers::setB (int b)
    {
            _b = b;
    }
    
    int AddNumbers::getA () const
    {
            return _a;
    }
    
    int AddNumbers::getB () const
    {
            return _b;
    }
    
    int AddNumbers::getSum () const
    {
            return _a + _b;
    }

## Create a static library

First the source file src/AddNumbers.cpp is turned into an object file.
    
    
    [~/workspace/C++/AddNumbers] > g++ -I ./inc -c src/AddNumbers.cpp -o obj/AddNumbers.o

A **static library** is basically a set of object files that were copied into a single file. It is created invoking the **archiver** ar. The library name must start with the three letters **lib** and have the suffix **.a**.
    
    
    [~/workspace/C++/AddNumbers] > ar rcs lib/libAddNumbers.a obj/AddNumbers.o

You can also write similar rules in a makefile. See the file Makefile.static given in the [AddNumbers.tar.bz2](http://www.iram.fr/~roche/code/c++/files/AddNumbers.tar.bz2) archive.

Refer to [useful options of g++](http://www.iram.fr/~roche/code/c++/c++_HelloWorld.html#g++) for details.

## Create a shared library

The -fpic option tells g++ to create position independant code which is needed for shared libraries.
    
    
    [~/workspace/C++/AddNumbers] > g++ -I ./inc -fpic -c src/AddNumbers.cpp -o obj/AddNumbers.o

Finally the **shared library** is created. Note the library name must start with the three letters **lib** and have the suffix **.so**.
    
    
    [~/workspace/C++/AddNumbers] > g++ -shared -o lib/libAddNumbers.so obj/AddNumbers.o

As a makefile example see the file Makefile.shared given in the [AddNumbers.tar.bz2](http://www.iram.fr/~roche/code/c++/files/AddNumbers.tar.bz2) archive.

Refer to [useful options of g++](http://www.iram.fr/~roche/code/c++/c++_HelloWorld.html#g++) for details.

## C++ symbols

Commands nm and c++filt allow to list and demangle C++ symbols from object files. Let us try those commands with the static library libAddNumbers.a.
    
    
    [~/workspace/C++/AddNumbers] > nm lib/libAddNumbers.a
    
    AddNumbers.o:
    0000003c T _ZN10AddNumbers4setAEi
    0000004a T _ZN10AddNumbers4setBEi
    00000018 T _ZN10AddNumbersC1Ev
    00000000 T _ZN10AddNumbersC2Ev
    00000036 T _ZN10AddNumbersD1Ev
    00000030 T _ZN10AddNumbersD2Ev
    00000058 T _ZNK10AddNumbers4getAEv
    00000062 T _ZNK10AddNumbers4getBEv
    0000006e T _ZNK10AddNumbers6getSumEv

It means the library libAddNumbers.a has been built with the AddNumbers.o object file that contains some symbols. First column is the **symbol value** (it represent the position of the symbol in the library). The second column is the **symbol type**. And the third column is the **symbol name**.

See the following table that describe some usual symbol types.

symbol type | description  
---|---  
A | The symbol's value is **absolute** , and will not be changed by further linking.  
N | The symbol is a **debugging** symbol.  
T | The symbol is in the **text (code) section**.  
U | The symbol is **undefined**.  
W | The symbol is a **weak** symbol that has not been specifically tagged as a weak object symbol. When a weak defined symbol is linked with a normal defined symbol, the normal defined symbol is used with no error. When a weak undefined symbol is linked and the symbol is not defined, the value of the symbol is determined in a system-specific manner without error. Uppercase indicates that a default value has been specified.  
? |  The symbol type is **unknown** , or object file format specific.  
  
See the [nm manual](http://www.gnu.org/software/binutils/manual/html_chapter/binutils_2.html) for more details. Symbols are not human comprehensible. It is with the fact C++ language provides function overloading, which means that you can write many functions with the same name (providing each takes parameters of different types). All C++ function names are encoded into a low-level assembly label (this process is known as **mangling** ). The c++filt program does the inverse mapping: it decodes ( **demangling** process) low-level names into user-level names.
    
    
    [~/workspace/C++/AddNumbers] > c++filt _ZNK10AddNumbers6getSumEv
    AddNumbers::getSum() const

The program nm allow to directly demangle symbols using the -C option.
    
    
    [~/workspace/C++/AddNumbers] > nm -C lib/libAddNumbers.a
    
    AddNumbers.o:
    0000003c T AddNumbers::setA(int)
    0000004a T AddNumbers::setB(int)
    00000018 T AddNumbers::AddNumbers()
    00000000 T AddNumbers::AddNumbers()
    00000036 T AddNumbers::~AddNumbers()
    00000030 T AddNumbers::~AddNumbers()
    00000058 T AddNumbers::getA() const
    00000062 T AddNumbers::getB() const
    0000006e T AddNumbers::getSum() const

See [useful options of nm](http://www.iram.fr/~roche/code/c++/c++_AddNumbers.html#nm) for more options.

## Using libraries

This section describes how to use static or shared libraries in programs. First we need to create a main program.
    
    
    ~/workspace/C++/AddNumbersClient/src/main.cpp
    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include "AddNumbers.h"
    
    int main(int argc, const char* argv[])
    {
    	if(argc == 3)
    	{
    		int a, b;
    		a = atoi(argv[1]);
    		b = atoi(argv[2]);
    		AddNumbers ab;
    		ab.setA(a);
    		ab.setB(b);
    		printf("%d + %d = %d\n", ab.getA(), ab.getB(), ab.getSum());
    	}
    	else
    	{
    		printf("*** Error: Bad number of arguments (%d)\n", argc-1);
    	}
    	
    	return 0;
    }

To link this program against the **static** library, write the following command that compile and link the main executable.
    
    
    [~/workspace/C++/AddNumbersClient] > g++ -I ../AddNumbers/inc -L ../AddNumbers/lib -static src/main.cpp -lAddNumbers -o bin/AddNumbersClient_static

Note that the first three letters **lib** as well as the suffix **.a** are not specified for the name of the library. Now the program  AddNumbersClient_static can be executed.
    
    
    [~/workspace/C++/AddNumbersClient] > bin/AddNumbersClient_static 5 2
    5 + 2 = 7

To link against the **shared** library, enter the following command.
    
    
    [~/workspace/C++/AddNumbersClient] > g++ -I ../AddNumbers/inc -L ../AddNumbers/lib src/main.cpp -lAddNumbers -o bin/AddNumbersClient_shared

The first three letters **lib** as well as the suffix **.so** are not specified for the name of the library. To run the program  AddNumbersClient_shared you need to tell to the LD_LIBRARY_PATH environment variable where found the shared library.
    
    
    [~/workspace/C++/AddNumbersClient] > LD_LIBRARY_PATH=../AddNumbers/lib
    [~/workspace/C++/AddNumbersClient] > bin/AddNumbersClient_shared 8 3
    8 + 3 = 11

In the real world it is better to use an **absolute path** for  LD_LIBRARY_PATH.

As makefile examples see Makefile.static and Makefile.shared files given in the [AddNumbersClient.tar.bz2](http://www.iram.fr/~roche/code/c++/files/AddNumbersClient.tar.bz2) archive.

## List of shared libraries

The command ldd prints the shared libraries required by each program or shared library specified on the command line.
    
    
    [~/workspace/C++/AddNumbersClient] > ldd bin/AddNumbersClient_shared
            libAddNumbers.so => ../AddNumbers/lib/libAddNumbers.so (0x00c36000)
            libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x009bf000)
            libm.so.6 => /lib/tls/libm.so.6 (0x00639000)
            libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x008b1000)
            libc.so.6 => /lib/tls/libc.so.6 (0x0050e000)
            /lib/ld-linux.so.2 (0x004f5000)

## Useful options of ar
    
    
    ar [option] ... <archive> <member> ...

The GNU ar program creates, modifies, and extracts from archives. An archive is a single file holding a collection of other files in a structure that makes it possible to retrieve the original individual files (called members of the archive). The original files'contents, mode (permissions), timestamp, owner, and group are preserved in the archive, and can be restored on extraction.

option | description  
---|---  
r | Insert the files member ... into archive (with replacement).  
c | Create the archive. The specified archive is always created if it did not exist, when you request an update.  
s | Write an object-file index into the archive, or update an existing one, even if no other change is made to the archive. You may use this modifier flag either with any operation, or alone.  
u | Normally, ar r ... inserts all files listed into the archive. If you would like to insert only those of the files you list that are newer than existing members of the same names, use this modifier. The u modifier is allowed only for the operation r (replace).  
v | This modifier requests the verbose version of an operation. Many operations display additional information, such as filenames processed, when the modifier v is appended.  
  
## Useful options of nm
    
    
    nm [option] ... <objfile> ...

The GNU nm program lists the symbols from object files objfile.

option | description  
---|---  
-A-o

\--print-file-name

| Precede each symbol by the **name of the input file** (or archive member) in which it was found, rather than identifying the input file once only, before all of its symbols.  
-a  
\--debug-syms | Display **all symbols** , even debugger-only symbols; normally these are not listed.  
-C  
\--demangle | Decode ( **demangle** ) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C++ function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.  
-D  
\--dynamic | Display the **dynamic** symbols rather than the normal symbols. This is only meaningful for dynamic objects, such as certain types of shared libraries.  
-g  
\--extern-only | Display only **external symbols**.  
-u  
\--undefined-only | Display only **undefined symbols** (those external to each object file).  
\--defined-only | Display only **defined symbols** for each object file.  
  
## Useful links

