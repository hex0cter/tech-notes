# [Differences between gcc and g++](http://stackoverflow.com/questions/172587/what-is-the-difference-between-g-and-gcc)


GCC: GNU Compiler Collection


  * Referrers to all the different languages that are supported by the GNU compiler.



gcc: GNU C Compilerg++: GNU C++ Compiler

The main differences:

  1. gcc will compile: *.c/*.cpp files as C and C++ respectively.
  2. g++ will compile: *.c/*.cpp files but they will all be treated as C++ files.
  3. Also if you use g++ to link the object files it automatically links in the std C++ libraries (gcc does not do this).
  4. gcc compiling C files has less predefined macros.
  5. gcc compiling *.cpp and g++ compiling *.c/*.cpp files has a few extra macros.



Extra Macros when compiling *.cpp files:


    #define __GXX_WEAK__ 1
    #define __cplusplus 1
    #define __DEPRECATED 1
    #define __GNUG__ 4
    #define __EXCEPTIONS 1
    #define __private_extern__ extern





Although the gcc and g++ commands do very similar things, g++ is designed to be the command you'd invoke to compile a C++ program; it's intended to automatically do the right thing.

Behind the scenes, they're really the same program. As I understand, both decide whether to compile a program as C or as C++ based on the filename extension. Both are capable of linking against the C++ standard library, but only g++ does this by default. So if you have a program written in C++ that doesn't happen to need to link against the standard library, gcc will happen to do the right thing; but then, so would g++. So there's really no reason not to use g++ for general C++ development.

---
