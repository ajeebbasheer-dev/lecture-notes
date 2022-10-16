===================
Control Statements
===================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

.. important:: 
    
    - No switch statement in C python.
    - No do-while loop in Python


Decision making statements
===========================

if, if-else and else if
------------------------

.. tabs::

   .. tab:: if

        ::
        
            >>> total = 149
            >>> if total > 150:
            ...     print('Discount applied')
            ... 


   .. tab:: if else

        ::
            
            >>> if total > 150:
            ...     print('Discount applied')
            ... else:
            ...     print('No Discount')
            ... 
            No Discount


   .. tab:: if-elif-else

        ::

            >>> if total > 150:
            ...     print('Discount applied')
            ... elif total > 100:
            ...     print('Cash back applied')
            ... else:
            ...     print('No Discount')
            ... 
            Cash back applied

    .. tab:: nested if-else

        ::

            >>> if total > 150:
            ...     print('Discount applied')
            ... else:
            ...     if total > 100:
            ...             print("Cash back applied")
            ...     else:
            ...             print("No Discount")
            ... 
            Cash back applied


Ternary operator
-----------------

Syntax: `[on_true] if [expression] else [on_false] `

::

    >>> total = 149
    >>> print('Discount applied') if total > 150 else print('No Discount')
    No Discount

Ternary operator can be written as nested if-else::

    >>> print("Discount applied" if total > 150 else "Cash back applied" if total > 100 else "No Discount")
    Cash back applied

Loop statements
================

iterables
----------

- Sequences we can iterate through each elements.
- All iterator will have `__iter__` dunder in dir(<object>)
- Examples: list, dictionaries, tuples, sets etc.

While loop
-----------

::

    while expression:
        statement(s)

While loop executes the block until a condition is satisfie::

    >>> while (index < len(fruits)):
    ...     print(fruits[index])
    ...     index +=1
    ... 
    apple
    orange
    grapes
    plums

The else clause is only executed when your while condition becomes false::

    >>> while (index < len(fruits)):
    ...     print(fruits[index])
    ...     index +=1
    ... else:
    ...     print("While executed without any issue")
    ... 
    apple
    orange
    grapes
    plums
    While executed without any issue

if an exception occurs, else will not be executed::

    >>> while (index < len(fruits)):
    ...     print(fruits[index])
    ...     index +=1
    ...     if index == 2:
    ...             raise Exception
    ... else:
    ...     print("While executed without any issue")
    ... 
    apple
    orange
    Traceback (most recent call last):
      File "<stdin>", line 5, in <module>
    Exception


For loop
---------

Syntax::

    for var in iterable:
        statements(s)

iterable can be a list::

    >>> for fruit in ['apple', 'orange', 'grapes', 'plums']:
    ...     print(fruit)
    ... 
    apple
    orange
    grapes
    plums

iterable can be a tuple::

    >>> for fruit in ('apple', 'orange', 'grapes', 'plums'):
    ...     print(fruit)
    ... 
    apple
    orange
    grapes
    plums


We know that string is a sequence of characters::

    >>> for character in "Hello":
    ...     print(character)
    ... 
    H
    e
    l
    l
    o

We can iterate through dictionary keys.

    ::

        >>> for keys in prices.keys():
        ...     print(keys)
        ... 
        tea
        coffee
        lime
        shake

We can iterate through dictionary value.

    ::

        >>> for value in prices.values():
        ...     print(value)
        ... 
        10
        12
        20
        60


How to iterate through keys and values together??

Use **tuple unpacking** in for-loops::

    >>> prices = {'tea': 10, 'coffee': 12, 'lime': 20, 'shake': 60}
    >>> 
    >>> prices.items()
    dict_items([('tea', 10), ('coffee', 12), ('lime', 20), ('shake', 60)])
    >>> 
    >>> for item in prices.items():
    ...     print(item)
    ... 
    ('tea', 10)
    ('coffee', 12)
    ('lime', 20)
    ('shake', 60)

now use **tuple unpacking**::

    >>> for key, value in prices.items():
    ...     print(key, value)
    ... 
    tea 10
    coffee 12
    lime 20
    shake 60

Finally, sets are also sequences::

    >>> for item in {10, 30, 2, 4}:
    ...     print(item)
    ... 
    10
    2
    4
    30


Commonly used iterable built-in functions
------------------------------------------

range() generator
------------------

- Syntax: `range(start, stop, step)`
- start, stop and step works similar to slice().
- range() is a generator. i.e. the entire list will not be stored in memory. It will be generated on demand.

    ::

        >>> range(2, 10)
        range(2, 10)
        >>> list(range(2, 10))
        [2, 3, 4, 5, 6, 7, 8, 9]

    
enumerate()
------------

- Syntax: `enumerate(iterable, start=0)`

::

    >>> fruits
    ['apple', 'orange', 'grapes', 'plums']
    >>> enumerate(fruits)
    <enumerate object at 0x1055dc300>
    >>> 
    >>> list(enumerate(fruits))
    [(0, 'apple'), (1, 'orange'), (2, 'grapes'), (3, 'plums')]

- Use tuple unpacking in for loops.

    ::

        >>> for index, value in enumerate(fruits):
        ...     print(index, value)
        ... 
        0 apple
        1 orange
        2 grapes
        3 plums
        >>> 

zip()
------

- zips multiple lists.

::

    >>> list1 = [1, 2, 3]
    >>> list2 = [5, 6, 7]
    >>> list3 = ['a', 'b' , 'c']

    >>> zip(list1, list2, list3)
    <zip object at 0x1055dc480>
    >>> 
    >>> list(zip(list1, list2, list3))
    [(1, 5, 'a'), (2, 6, 'b'), (3, 7, 'c')]

Use tuple unpacking in for loop::

    >>> for v1, v2, v3 in zip(list1, list2, list3):
    ...     print(v1, v2, v3)
    ... 
    1 5 a
    2 6 b
    3 7 c

What if the sizes are uneven?::

    >>> list2 = [5, 6, 7, 8, 9]
    >>> for v1, v2, v3 in zip(list1, list2, list3):
    ...     print(v1, v2, v3)
    ... 
    1 5 a
    2 6 b
    3 7 c

in operator
------------

Apart from using in for loop, we can also use in operator to check an entry in an iterator.

::

    >>> 2 in [1, 2, 3, 4]
    True
    >>> 20 in [1, 2, 3, 4]
    False
    >>> 'h' in "Hello World"
    False
    >>> 'H' in "Hello World"
    True


min() and max()
----------------

::

    >>> my_list = [2, 3, 1, 98, 4, 9]
    >>> min(my_list)
    1
    >>> max(my_list)
    98

Avoid using min and max as your variable name as they are built-ins.

random()
---------

randint
^^^^^^^^

::

    >>> from random import randint
    >>> randint(0,100)
    6
    >>> randint(0,100)
    94
    >>> randint(0,100)
    34
    >>> randint(0,100)
    59


shuffle()
^^^^^^^^^^

shuffle is an in-place operator. It returns None.

::

    >>> from random import shuffle
    >>> my_list = [2, 3, 1, 98, 4, 9]
    >>> shuffle(my_list)
    >>> my_list
    [3, 9, 4, 98, 1, 2]
    >>> shuffle(my_list)
    >>> my_list
    [1, 4, 98, 9, 2, 3]


Jump control Statements
========================

break statement
----------------

::

    >>> for i in range(10):
    ...     print(i)
    ...     if i == 5:
    ...             break
    ... 
    0
    1
    2
    3
    4
    5

continue statement
----------------

::

    >>> for i in range(10):
    ...     if i%2 == 0:
    ...             continue
    ...     print(i)
    ... 
    1
    3
    5
    7
    9


Do nothing statement 
=====================

pass statement
----------------

use it as a placeholder.

::

    >>> for i in range(10):
    ...     pass
    ... 
    