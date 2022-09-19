========================
Previous Year Questions
========================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

Assistant Professor
====================

ECE[2016], EEE[2016]
---------------------

.. mcq::
   :question: Q1. Central Processing Unit (CPU) is a combination of:

   - Control and storage
   - Arithmetic logic and input unit
   - Control and output unit
   - Arithmetic logic and control unit

.. toggle::

   **[D]** Arithmetic logic and control unit


.. mcq::
   :question: Q2. Which of the following memories needs refreshing? 

   - SRAM, DRAM, ROM, All of the above

.. toggle::

   **[B]** DRAM


.. mcq::
   :question: Q3. Recursion is a process in which a function calls:

   - itself, another function, main() function, none of the above

.. toggle::

   **[A]** itself


.. mcq::
   :question: Q4. What will be the final values of x and y?


.. container::

   .. code-block:: c 

      void main()
      {
          int x=1, y=1;
          do while(x<=7){
              x++, y++;
          }
          while (y<=5);
          printf("\nx=%d y=%d", x, y);
      }

.. mcq::

   - x=6 y=6, x=8 y=6, x=8 y=8, none of the above 

.. toggle::

   **[C]** x=8 y=8

.. mcq::
   :question: Q5. What will be the output of the following program?

.. container::

   .. code-block::

      void main()
      {
          char x = 'd';
          switch(x){
              case 'b':
              puts('0 1 001');
              break;
              default:
              puts('3 2 1');
              break;
              case 'R':
              puts('1 11 111');
          }
      }

.. mcq::

   - 0 1 001, 3 2 1, 1 11 111, none of the above

.. toggle::

   **[D]** none of the above

ME[2016], CS[2016]
-------------------

.. mcq::
   :question: Q1. What will be the output of the following program?

.. container::

   .. code-block::

      void main()
      {
          int i = 1;
          printf("%d", i=++i==1);
      }

.. mcq::

   - 0, 1, 2, error

.. toggle::

   **[A]** 0


.. mcq::
   :question: Q2. What will be the value of 'f' after execution of the following program?

.. container::

   .. code-block::

         void main()
         {
             char a;
             float f=10;
             for(a=1; a<=5;a++)
             {f -= .2;}
             printf("\nf=%g", f);
         }

.. mcq::

   - 5.0, 9, 9.0, error

.. toggle::

   **[B]** 9

.. mcq::
   :question: Q3. What will the output of the following program?

.. container::

   .. code-block::

      #define abc(x,y) x*y
      void main()
      {
          int a=1, b=2;
          printf("%d", abc(a+1, b-2));
      }
   
.. mcq::

   - 0, 1, 2, 3

.. toggle::

   **[B]** 1

.. mcq::
   :question: Q4. Which statement is added to the following program such that address of "r1" gets stored in "r2"?

.. container::

   .. code-block::

      void main()
      {
          int *r2;
          void abc(int **);
          abc(&r2);
          printf("%d", *r2);
      }

      void abc(int **r3){
          int r1 = 5;
          /**add statement here**/
      }

.. mcq::

   - \*r2 = &r1, \*r1 = &r3, \*r3 = &r1, none of the above

.. toggle::

   **[C]** \*r3 = &r1

.. mcq::
   :question: Q5. CPU can also be called as:

   - Processor hub, ISP, Node, All the above

.. toggle::

   **[X]**

CIVIL[2016]
------------

.. mcq::
   :question: Q1. The CPU Gets the address of next instruction to be executed from the:

   - Instruction register, Program counter, Memory address register, Accumulator

.. toggle::

   **[C]** Program counter

.. mcq::
   :question: Q2. What is the value of 'b' at the end of the following C program?

.. container::

   .. code-block::

      int add(int a){
       static int count = 0;
       count = count + a;
       return (count);
      }

      main()
      {
          int a, b;
          for(a=0; a<=4;a++)
          b = add(a);
      }

.. mcq::

   - 10, 12, 4, 6

.. toggle::

   **[A]** 10

.. mcq::
   :question: Q3. What will be the output of the C program segment?

.. container::

   .. code-block::

      int n = 1;
      switch(n){
          case 1: printf("One");
          case 2: printf("Two");
          case 3:
          case 4:
          case 5:
          default: printf("Wrong Choice");
      }

.. mcq::

   - One, Two, One Two Wrong Choice, One Two

.. toggle::

   **[B]** One Two Wrong Choice

.. mcq::
   :question: Q4. The default parameter passing mechanism of function is:

   - Call by value, Call by reference, Call by result, None of the above

.. mcq::
   :question: Q5. What is the output of this C code?

.. container::

   .. code-block::

      #include <stdio.h>

      int main()
      {
          do
              printf("Inside while loop");
          while(0);
          printf(" After while loop");
      }

.. mcq::

   - Infinite loop, After while loop, Compilation error, Inside while loop After while loop

.. toggle::

   **[D]** Inside while loop After while loop