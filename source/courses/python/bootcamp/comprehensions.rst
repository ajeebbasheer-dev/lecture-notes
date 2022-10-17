===================
Comprehensions
===================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

Comprehensions are unique way of quickly creating a python iterable.

List Comprehensions
====================

We can replace a for-loop with .append() function with an elegant list comprehension.

To create a list of single digits::

    >>> my_list = []
    >>> for i in range(10):
    ...     my_list.append(i)
    ... 
    >>> my_list
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

We can do this using list comprehension (with same computation time)::

    >>> [i for i in range(10)]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


To create a list of all characters in a string::

    >>> [c for c in "Hello"]
    ['H', 'e', 'l', 'l', 'o']

To create a list with square of first 5 numbers::

    >>> [i**2 for i in range(1,6)]
    [1, 4, 9, 16, 25]

To create a list with only even numbers from a list of numbers::

    >>> some_list = [11, 23, 44, 55, 76, 9, 0, 33]
    >>> [i for i in some_list if i%2 == 0]
    [44, 76, 0]

We can have any formulas like this::

    >>> radius_list = [4, 5.2, 1.3, 8.9, 4.0]
    >>> areas = [(3.14 * r**2) for r in radius_list]
    >>> areas
    [50.24, 84.9056, 5.3066, 248.71940000000004, 50.24]

We can use if-else but if it looks ugly, better avoid::

    >>> some_list = [11, 23, 44, 55, 76, 9, 0, 33]
    >>> ["E" if x%2==0 else "O" for x in some_list  ]
    ['O', 'O', 'E', 'O', 'E', 'O', 'E', 'O']

See the order for if-else is different from if::

    >>> ["E" if x%2==0 for x in some_list  ]
      File "<stdin>", line 1
        ["E" if x%2==0 for x in some_list  ]
                       ^
    SyntaxError: invalid syntax

Nested loops::

    >>> for i in [1, 2, 3]:
    ...     for j in [10, 20]:
    ...             print(i*j)
    ... 
    10
    20
    20
    40
    30
    60

    >>> [i*j for i in [1, 2, 3] for j in [10, 20]]
    [10, 20, 20, 40, 30, 60]

Dictionary Comprehensions
==========================

similar to lists::

    >>> {x:x**2 for x in range(4)}
    {0: 0, 1: 1, 2: 4, 3: 9}


If we want keys and values from separate lists, then, use zip.

We know that::
    
    >>> keys = ['a','b','c','d','e']
    >>> values = [1,2,3,4,5] 
    >>> list(zip(keys, values))
    [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

Comprehension::

    >>> { k:v for (k,v) in zip(keys, values)} 
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

We can iterate through dictionary::

    >>> old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
    >>> old_price.items()
    dict_items([('milk', 1.02), ('coffee', 2.5), ('bread', 2.5)])

Comprehension::

    >>> dollar_to_pound = 0.76
    >>> new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
    >>> new_price
    {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}

If we need items of price less than 2, use conditions::

    >>> prices = {'milk': 1.02, 'coffee': 2.5, 'bread': 1.5}
    >>> {item: price for (item, price) in prices.items() if price < 2}
    {'milk': 1.02, 'bread': 1.5}

We can use multiple conditions::

    >>> {item: price for (item, price) in prices.items() if price < 2 if price>1.3}
    {'bread': 1.5}

if else::

    >>> {item: ('costly' if price>2 else 'ok') for (item, price) in prices.items()}
    {'milk': 'ok', 'coffee': 'costly', 'bread': 'ok'}

Set Comprehension
==================

::

    >>> {x**3 for x in range(4)}
    {0, 1, 27, 8}

Tuple comprehension
=====================

We can use generator expression passed to a tuple constructor::

    >>> (x for x in range(11, 17))
    <generator object <genexpr> at 0x104c7b7b0>

However we can do this::

    >>> tuple(x for x in range(11, 17))
    (11, 12, 13, 14, 15, 16)

.. important:: Beware that using parenthesis is already reserved for generator expressions.

    - Comprehensions result in faster construction compared to using a generator passed to a constructor.
    - In generators, you are creating and executing functions and functions are expensive in Python.
    - [x for x in x_list] constructs a list much list(x for x in x_list)

    ::

        >>> list(x for x in range(11, 17))
        [11, 12, 13, 14, 15, 16]

