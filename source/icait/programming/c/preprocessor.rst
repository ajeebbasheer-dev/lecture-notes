===================
The C Preprocessor
===================

- Preprocessor is a program that processes the source program before it is passed to the compiler.
- Preprocessor commands are often called **preprocessor directives**.
- Every preprocessor directive begin with a **# symbol**.
- It can be placed anywhere in a program but placing it in the beginning is most common.
- In C, it is customary to use capital letters for macro


Directive #1: Macro Expansion (#define)
=========================================

During preprocessing, every occurrence of LIMIT will be replaced with 4. PI will be replaced with 3.14.

::

    #define LIMIT 4 // Called macro definition
    #define PI 3.14 // Called macro definition

    int main(){
        int radius = 3;
        for (int i=0; i<LIMIT; i++)
            printf("%d", i);
        int area = radius*radius*PI;
        printf("\nArea: %d", area);
    }

    Output: 
    0123
    Area: 28.260000


A #define directive could be used to replace even an entire C statement::

    #define SUCCESS printf ("Program execution was success!!") ;

Macros can have arguments, just as functions can::

    #define AREA(R) ( 3.14 * R * R )

So, are macros functions?
--------------------------

Though macro calls are ‘like’ function calls, they are not really the same things.

- Macro expansion increases code size if it is used in multiple places, functions reduces code size.
- Preprocessor replaces the macro template with its macro expansion, in a stupid, unthinking, literal way. In functions, it uses activation records, arguments gets passed, do some intelligent logic and return it's result.


Directive #2: File inclusion (#include)
=========================================

Two use cases:

1. Better divide a large program into several files and include all in the main program.
2. Add all commonly used macros in a file and include it in the main program.

- Usually we call such files header files and uses an extension **.h**.
- strings.h, math.h, stdlib.h etc.

There exist two ways to write #include statement::

    #include "filename" // look for file in the current directory or in specified list of directories
    #include <filename> // look for file only in specified list of directories

- specified list of directories differ from compilers to compilers. In Turbo C, we can setup in Options->Directories.

Directive #3: Conditional Compilation 
======================================

#ifdef
----------

Example::

    #define WINDOWS // #else block will be executed.
    int main(){
        char *hv;
        #ifdef MACBOOK
            hv = "UTM";
        #else
            hv = "VirtualBox";
        #endif
        printf("\n%s", hv);
    }

    Output: VirtualBox

To execute, mac related statements, just change the #define to MACBOOK.


#if and #elif 
---------------

Used to check if an expression evaluates to a nonzero value or not.

.. code-block:: c
    
    #define PLATFORM 'TEST'

    #if PLATFORM=='PROD'
        #define WORKERS  10
    #elif PLATFORM=='TEST'
        #define WORKERS  5
    #else
        #define WORKERS  1
    #endif

    int main(){
        printf("\n%d", WORKERS); // 5
    }


#undef and #pragma directives
==============================

#undef 
-------

To undefine an already defined macro::

    #define PLATFORM 2
    int main(){
        #undef PLATFORM
        printf("\n%d", PLATFORM); //Error
    }

#pragma
--------

- Special-purpose directive that you can use to turn on or off certain features.
- Pragmas vary from one compiler to another.

For example, the below program will not throw any warning by default in GCC.

::

    void fun(int x){
        int a = 10;
    }

    int main(){
        fun(10);
    }

But this throws::

    #pragma GCC diagnostic warning "-Wunused-parameter"
    void fun(int x){
        int a = 10;
    }

    int main(){
        fun(10);
    }

::

    test.c:8:14: warning: unused parameter 'x' [-Wunused-parameter]
    void fun(int x){
                 ^
    1 warning generated.
