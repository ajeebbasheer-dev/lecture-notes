===========
Functions
===========

- C program is a collection of one or more functions.
- Using a function is something like hiring a person to do a specific job for you.

**Advantages of using functions**


- Avoids rewriting the same code over and over.
- Dividing program into multiple smaller modules makes program easier to design and understand.
  
**Defining & calling a function**

::

    // function definition
    void print_alert(){
        printf("Battery Low");
    }

    main(){
        print_alert(); // function call
    }

**Formal arguments and actual arguments**

Here, x and y are actual arguments, a and b are formal arguments::

    int add(int a, int b){
        return (a+b);
    }

    main(){
        int x=2, y=3;
        int result = add(x ,y);
        printf("result: %d", result);
    }

Function Prototype
=====================

This will not work::

    main(){
    print_alert();
    }

    void print_alert(){
        printf("Battery Low");
    }

But this will work::

    void print_alert();
    main(){
        print_alert();
    }

    void print_alert(){
        printf("Battery Low");
    }

This will also work::

    main(){
        float add(float a, float b);
        add(1.2, 4.3);
    }

    float add(float a, float b){
        return (a+b);
    }

This statements `void print_alert();` and `float add(float a, float b);` are called  prototype declarations.


Return statement
=================

- Data type of value returned by the function should match function definition.

    ::

        int add(int a, int b){
            return (a+b);
        }

        main(){
            int result = add(2, 3);
            printf("result: %d", result);
        }

- No separate return statement was necessary to send back the control.
- Any C function by default returns an int value
- There is no restriction on the number of return statements that may be present in a function. 
- Also, the return statement need not always be present at the end of the called function.

See the use case::

    void atm(int amount){
        int num_of_100_notes = 0, num_of_500_notes=0;
    
        if (amount >= 100 && amount%100==0){
            int x = amount/100;
            if (x > 5){
                num_of_500_notes = x/5;
                num_of_100_notes = x%5;
            }
            else
                num_of_100_notes = x;

            printf("\n500s: %d, 100s: %d\n", num_of_500_notes, num_of_100_notes);
        }
        else
            printf("Invalid amount entered!\n");
        }
    }

Instead::

    if (amount < 100 || amount%100!=0){
        printf("Invalid amount entered!\n");
        return 0;
    }
    

A function can return only one value at a time. Thus, the following statements are invalid::

    return (a, b);
    return (x, 12);




Types of functions
====================

2 types of functions are there:

1. Library functions
   
   - Commonly required functions grouped together and stored in a library.
   - Example: printf(), scanf() etc.

2. User defined functions.

Recursion
==========

.. important:: 
    A function can call itself. Such a process is called **recursion**

The `main()` function
======================

.. important:: 
    - Every C program must contain a main() function. 
    - Program execution always begins with main().
    - When main() runs out of function calls, the program ends.
 
Every function including main() can be called from any other functions::

    void print_alert(){
        printf("Battery Low");
        main();
    }

    int main(){
        print_alert();
        return 0;
    }


Pass by value 
==============

Value of a formal argument is changed in the called function, the corresponding change does not take place in the calling function


::

    void fun(int x){ // x here is formal argument

        x = 20;
        printf("x = %d\n", x);
    }

    main(){
        int x = 10;
        fun(x); // x is actual argument
        printf("x = %d\n", x);
    }

- Library Function
- Local and global variables
- Types of storage class
- Scope and life
- 