====================
Control Statements 
====================

**True and False**

- `Zero (0) is false`
- `Non-Zero (1, 2, 3, .. -1, -2, -3..) is true`

Decision making statements
===========================

if, if-else and else if
------------------------

.. tabs::

   .. tab:: if

        ::
        
            if (expression)
                statement;

   .. tab:: multi statement if

        ::
            
            if (expression){
                statement #1;
                statement #2;
            }

   .. tab:: if-else

        ::

            if (expression)
                statement;
            else
                statement;

   .. tab:: nested if-else

        ::

            if (expression){
                if (expression){
                }
                else{
                }
            }
            else{
            }
    
   .. tab:: else if

        ::

            if (expression)
                statement;
            else if (expression)
                statement;
            else if (expression)
                statement;
            else
                statement;

Examples::

    if (4 + 2 % 3)
        printf("this works")

    if (i = 20)
        printf("this works")

    var = 45;
    if ((var >= 50) && (var < 60))
        print("this doesn't work")

.. toggle::

    ::
    
        4 + 2 % 3 = (4 + 2) = 6 = true
        20 gets assigned to i => if ( a ) or if ( 10 ) => true



What will be the output of the following program when input is 1999?

.. code-block:: c

    main( )
    {
        int i ;
        printf("Enter value of i: ");
        scanf("%d", &i ) ;
        if (i = 10)
            printf ("You entered 10");
        else
            printf ("You entered something other than 10");
    }

    Enter value of i: 10
    You entered 10

    Enter value of i: 1999
    ??

.. toggle::

    ::

        You entered 10

.. code-block:: c

    main( )
    {
        int i=10;
        if (i==8);
            printf("i is 8");
    }

.. toggle::

    ::

        Compiler interpret this as follows:
        if (i == 8) # if (expression)
        ;   # statement
        printf ("i is 8");


ternary operator
----------------


**expression 1 ? expression 2 : expression 3**::
    
    y = ( x > 10 ? 9 : x );

    is equivalent to

    if (x > 10)
        y = 9;
    else
        y = x;
    
Statements can be anything, not necessarily arithmetic statement::

    (i == 1 ? printf ("foo") : printf ("bar"))

The conditional operators can be nested::

    big = ( a> b ? ( a > c ? 4: 5 ) : ( b > c ? 7: 9 ) ) ;

What is the output of this ternary operator?::

    result = (a>b)?b=a:b=b;

.. toggle::

    ::
        
        Assignment has a lower precedence than the ternary operator so the line evaluates like,

        ((a>b)?b=a:b)=b;

        use,

        a>b?a:b; 
        or
        a>b? b = a : (b = b);





Selection statements
=====================

switch-case-default
--------------------

What will be the output of the following?::

    main( )
    {
        int i = 2 ;
        switch ( i ){
            case 1 :
            printf ( "I am in case 1 \n" ) ;
            case 2 :
            printf ( "I am in case 2 \n" ) ;
            case 3 :
            printf ( "I am in case 3 \n" ) ;
            default :
            printf ( "I am in default \n" ) ;
        }
    }

.. toggle::

    ::

        I am in case 2 
        I am in case 3 
        I am in default 

        use break statement to get out of switch.
        Note that there is no need for a break statement after the default, since the control comes out of the switch anyway

If you want to execute common set of statements for multiple cases::

    main( )
    {
        char ch ;
        printf ( "Enter any of the alphabet a, b, or c " ) ;
        scanf ( "%c", &ch ) ;
        switch ( ch ){
            case 'a' :
            case 'A' :
                printf ( "a for apple" ) ;
                break ;
            case 'b' :
            case 'B' :
                printf ( "b for ball" ) ;
                break ;
            break ;
            default :
                printf ( "no idea" ) ;
        }
        return 0;
    }

Unlike if, and else,  multiple statements need not be enclosed within braces

Every statement in a switch must belong to some case or the other. However, compiler won’t report an error. It just ignore. 

The `printf("Hello World")` will never get executed::

    switch (ch){
        printf("Hello World");
        case 'a' :
            printf ( "a for apple" ) ;
            break ;
        default :
            printf ( "no idea" ) ;
    }

- If no default statement is given, then program simply ignore if choice not matching::

    int main( )
    {
        char ch ;
        printf ( "Enter any of the alphabet " ) ;
        scanf ( "%c", &ch ) ;
        switch (ch){
            case 'a' :
                printf ( "a for apple" ) ;
                break ;
        }
        return 0;
    }

.. toggle::

    a for apple # if input is a 
    nothing will be printed if input is not a

.. important:: 
    - Only allowed values are **int constant** or a **char constant**  or **an expression that evaluates to one of these**.
    - Even a float is not allowed.
    - **break** takes the control outside of switch. However, **continue** will not take you to the beginning as in the case of loops.
    - Multiple cases can't use same expressions. 
    - **case a + b** is an illegal statement but **case 3+7** is legal.
    - Every statement in a switch must belong to some case or the other. However, compiler won’t report an error. It just ignore



following switch statements are legal::

    switch ( i + j * k )
    switch ( 23 + 45 % 4 * k )
    case 3 + 7

Following is not legal::

    switch (a)
    {
    case 3 :
    ...
    case 1 + 2 :
    ...
    }


Loop statements
================

.. important:: 
    - **initialization**: executed only once. optional.
    - **condition**: check if the expression evaluates to true. 
      - for loop: optional, default to true.
      - while/do-while loop: mandatory.
    - **update**: optional but if not updated, then loop may end up in a infinite loop.


The `while` loop
-----------------

General form::

    initialization;
    while(condition){
        //loop body
        update 
        //loop body
    }


- In place of the condition there can be any other valid expression.

::

    while ( i <= 11 )
    while ( i >= 11 && j <= 15 )
    while ( j > 11 && ( b < 15 || c < 25 ) )

- Parentheses is optional for single statement while loops.



The `for` loop 
---------------

General form::

    for (initialization; condition; update)
        // loop body

- Initialization statement: executed only once, when the loop is entered for the first time.

::

    for (int i=10; i ; i--)
        printf ( "%d", i ) ;

.. toggle::

    ::

        10987654321

Any valid expression is possible in a for loop::

    for (j<4; j=5 ; j=0 )
        printf ( "%d", j ) ;

.. toggle::

    ::

        Infinite loop. since condition (j=5 => 5 => true) is always true

Remember just a semi colon is also a valid expression::

        for ( int i = 1; i <=5 ; printf ( "%d ",i++ ))
            ;

.. toggle::

    ::

        1 2 3 4 5


Remember the initialization runs only once::

    int i;
    printf("\nEnter a value less than 10: ");
    for (scanf ( "%d", &i ) ; i <= 10 ; i++ )
        printf ( "%d ", i ) ;

.. toggle::

    ::

        Enter a value less than 10: 6
        6 7 8 9 10 

Works like a while loop::

    int i = 0;
    for (; i<3; ) {
        i++;
    }


Nested for loop::

    for(int row=1; row<=3; row++){
        for(int col=1; col<=2; col++){
            printf("ROW: %d, COLUMN: %d\n", row, col);
        }
        printf("\n");
    }

.. toggle::

    ::

        ROW: 1, COLUMN: 1
        ROW: 1, COLUMN: 2

        ROW: 2, COLUMN: 1
        ROW: 2, COLUMN: 2

        ROW: 3, COLUMN: 1
        ROW: 3, COLUMN: 2


Multiple initialization inside for loop::

    for ( int i = 1,  j = 2 ; j <= 5 ; j++ ){
        printf("%d-%d ", i, j);
    }

.. toggle::

    ::

        1-2 1-3 1-4 1-5

.. important:: 
    - for (;;) {} = for(;true;){} = while(true){} = do{}while(true);
    - for (;;) {} = for(;1;){} = while(1){} = do{}while(1);
    - to use true/false you need to include <stdbool.h>
    - all the loops above are infinite.


The `do-while` loop
---------------------

General format::

    initialization;
    do{
        // loop body
        update;
        // loop body
    }while (condition)


Example::

    char another ;
    int price;
    do
    {
        printf("Enter item price ") ;
        scanf("%d", &price );
        printf("You entered: ", price);
        printf( "\nWant to enter another item? [y/n]");
        scanf("%c", &another);
    } while ( another == 'y') 

Jump statements
================

The `break` statement
-----------------------

- A `break` inside any loop passes the control to the first statement after the loop.
- A break is usually associated with an `if` condition.

Find number given is less than 100::

    int num_to_find = 3, i;
    for(i=0; i<10; i++){
        printf("%d \n", i);
        if (i==num_to_find){
            break;
        }
    }
    if (i==10)
        printf("number not found");
    else
        printf("number found");

.. toggle::

    ::

        0 
        1 
        2 
        3 
        number found

Breaks the control only from the loop in which it is placed::

    int num_to_find = 2, i, try;
    for (try=0; try<2; try++){
        for(i=0; i<10; i++){
            printf("inner loop: %d \n", i);
            if (i==num_to_find){
                break;
            }
        }
        printf("outer loop: %d \n\n", try);
    }
    printf("outside of all loops");

.. toggle::

    ::

        inner loop: 0 
        inner loop: 1 
        inner loop: 2 
        outer loop: 0 

        inner loop: 0 
        inner loop: 1 
        inner loop: 2 
        outer loop: 1 

        outside of all loops

The `continue`` Statement
--------------------------

- A `continue` in a loop passes the control to the beginning of the loop, bypassing the remaining loop body.

I am an introvert and I prefer not be printed::

    int introvert = 2, i;
    for(i=0; i<5; i++){
        if (i==introvert)
            continue;
        printf("I'm %d \n", i);
    }

.. toggle::

    ::
        
        I'm 0 
        I'm 1 
        I'm 3 
        I'm 4 

    What will the output if it was a break? instead of continue?

goto
-----

- Avoid goto keyword! They make programs become unreliable, unreadable, and hard to debug.
  
Usage::

    int x = 10, i=10;
    if (x==10)
        goto SOS;
    
    for (i=0;i<4;i++)
        printf("Hello");
        
    SOS:
        printf("Help me!");

exit
------

- Terminates the process

- There are two types of exit status:

  - Exit Success is indicated by exit(0): means successful termination of the program, i.e. program has been executed without any error or interrupt.
  - Exit Failure is indicated by exit(1) which means the abnormal termination of the program, i.e. some error or interrupt has occurred. We can use different integer other than 1 to indicate different types of errors.

return
-------

The return statement serves two purposes:

- Immediately transfers the control back to the calling program.
- It returns the value present in the return statement to the calling program.