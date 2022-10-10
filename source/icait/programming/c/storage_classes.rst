=================
Storage Classes
=================

Data types
===========

Primary data types could be of 3 varieties:

1. char
   
   - signed and unsigned: A signed char is same as an ordinary char and has a range from -128 to +127. Unsigned char has a range from 0 to 255.
2. int 
   
   - variants of int are **short** and **long**. Size depends on compiler but follows the rules

       - shorts are at least 2 bytes big, longs are at least 4 bytes big
       - shorts are never bigger than ints.ints are never bigger than longs
   - signed and unsigned: In this case the range will shift from -32768 to +32767  to 0 to 65535

3. float: C offers **double** if float is not sufficient.

- As mentioned, Range of an different data types depends on compiler. For **16bit Turbo C** compiler, range of int is -32768 to 32767 (2^15). 16th bit stores the sign.
  - 16bit compiler means, it generates machine code targeted to run on 16 microprocessor like intel 8086. 


Storage Classes in C
=====================

So far, we know that a variable declaration, for example `int a;`, compiler identifies some physical location to store the value represented by the variable.

But, 

- In which type of location does it reserve space? 
- How long should we keep the variable?
- Who all can access the variable?

Storage class tells us the following things:

- Where would the variable be stored. **Memory or Registers**?
- What will the **default initial value**?
- **Scope** and **Life** of variable?


+-----------+----------------------------+------------------------+---------------------+-------------------------------------------------------------------+
|           | Storage                    | Default initial value  | Scope               | Life                                                              |
+===========+============================+========================+=====================+===================================================================+
| Auto      | Memory                     | Garbage                | Local to the block  | Till control remains within the block                             |
+-----------+----------------------------+------------------------+---------------------+-------------------------------------------------------------------+
| Register  | Register (not guaranteed)  | Garbage                | Local to the block  | Till the control remains within the block                         |
+-----------+----------------------------+------------------------+---------------------+-------------------------------------------------------------------+
| Static    | Memory                     | Zero                   | Local to the block  | Value of the variable persists between different function calls.  |
+-----------+----------------------------+------------------------+---------------------+-------------------------------------------------------------------+
| Extern    | Memory                     | Zero                   | Global              | Throughout program execution                                      |
+-----------+----------------------------+------------------------+---------------------+-------------------------------------------------------------------+

Auto Example::

    int main()
    {
        auto int x;
        {
            auto int x = 20;
            {
                auto int x = 30;
                auto int y = 50; // scope is limited to this block. Can't access from outside.
                printf("\nx = %d", x, y); // works
            }
            printf("\nx = %d", x); // value 30 is lost as soon as exit this block.
            printf("\ny = %d", y); // Compile error!! undeclared identifier 'y'
        }
        printf("\nx = %d", x); // Garbage! value 20 is lost as soon as exiting the block.
    }

.. important:: 
    - Scope and Life of a register variable is exactly same as that of Auto variable.
    - Storage is in register is not guaranteed as number of registers are limited.
    - Not every type of variable can be stored in a CPU register. A microprocessor with 16 bit registers can't store a double.


Static::

    void add_to_cart(items){
    static int count;
    count += items;
    printf("Number of items in cart = %d\n", count);
    }

    int main()
    {
        add_to_cart(2);
        add_to_cart(5);
        add_to_cart(1);
    }

::

    Number of items in cart = 2
    Number of items in cart = 7
    Number of items in cart = 8


What will be the output if the declaration was just `int count= 0`?


Extern::

    int i = 53;
    int main(){
        extern int j;
        printf("i=%d, j=%d\n", i, j);
    }
    int j = 34;

::

    i=53, j=34

Note that a variable can be declared several times but can be defined only once.

.. important:: 
    - A static variable can also be declared outside all the functions. However, the scope of this variable is limited to the same file in which it is declared.


Use cases of storage classes
------------------------------

Main purpose of storage classes.

- Improve memory space economy.
- Imporve speed and performance.

- **static**: Use only if you want the value of a variable to persist between different function calls.
- **register**: for varables that are used very often in the program. Example: loop counters.
- **extern**: use if the variable is used by almost all the functions in the program.
- **auto**: if you don't have any above mentioned use cases.

