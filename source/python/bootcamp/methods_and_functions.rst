======================
Methods and Functions
======================

.. toctree::
   :maxdepth: 3
   :caption: Contents:


Built-in methods
====================

Use `dir` method to get the list of method available to an object.

For example, for a list object::

    >>> my_list = ['a', 'b', 'c']
    >>> dir(my_list)
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>> my_list.reverse()
    >>> my_list
    ['c', 'b', 'a']
    >>> my_list.sort()
    >>> my_list
    ['a', 'b', 'c']
    >>> my_list.pop()
    'c'
    >>> my_list.append('x')
    >>> my_list
    ['a', 'b', 'x']

Learning thousands of built-in in functions is not practical. Use **help()** function instead.

To know how to use a function::

    >>> help(my_list.insert)
    Help on built-in function insert:
    
    insert(index, object, /) method of builtins.list instance
        Insert object before index.

or use Python official documentation **docs.python.org**.

Functions
===========

- To avoid code redundancy or rewriting same code again and again.
- To Modularize logic.

def keyword
============

The `def` tells python compiler that this is a function.

To define a function::

    def <function_name>(<zero or more args>):
        """
        Docstring 
        """
        // function logic

- It is recommended to have name with lower case words separated by underscores. 

Example::

    >>> def display_name(name):
    ...     """
    ...     This function says hello to the name passed in
    ...     """
    ...     print(f"Hello {name}!")
    ...

Call the function::

    >>> display_name("Mike")
    Hello Mike!
    >>> display_name("Donna")
    Hello Donna!

Let's see where doc string comes in picture::

    >>> help(display_name)
    Help on function display_name in module __main__:

    display_name(name)
        This function says hello to the name passed in

See the use of __doc__ dunder::

    >>> dir(display_name)
    ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    >>> display_name.__doc__
    '\n\tThis function says hello to the name passed in\n\t'

Note that paranthesis is important when calling a function::

    >>> display_name
    <function display_name at 0x000001FF23EBF880>

Number of arguments should also match::

    >>> display_name()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: display_name() missing 1 required positional argument: 'name'

We can avoid this error by adding default values to argument::

    >>> def display_name(name="No one"):
    ...     """
    ...     This just displays the name passed in
    ...     """
    ...     print(f"Hello {name}")
    ...
    >>> display_name()
    Hello No one

return result
==============

::

    >>> def print_result(x, y):
    ...     print(x+y)
    ...
    >>> def return_result(x, y):
    ...     return x+y
    ...
    >>> print_result(10, 20)
    30
    >>> return_result(10, 20)
    30

result1 is None and result2 is the value returned by return_result::

    >>> result1 = return_result(10, 20)
    >>> result1 = print_result(10, 20)
    30
    >>> result2 = return_result(10, 20)
    >>>
    >>> result1
    >>> result2
    30

Example 2::

    >>> def vegetable_price(tomato_in_kg, onion_in_kg):
    ...     tomato_price = 11
    ...     onion_price = 13
    ...     return tomato_in_kg * tomato_price + onion_in_kg * onion_price
    ...
    >>> def grocery_price(rice_in_kg, sugar_in_kg, salt):
    ...     rice_price = 22
    ...     sugar_price = 35
    ...     salt_price = 8
    ...     return rice_in_kg * rice_price + sugar_in_kg * sugar_price + salt * salt_price
    ...
    >>> total_bill = vegetable_price(4, 9) + grocery_price(10, 6, 2)
    >>> total_bill
    607

Remember `return` will take control back to the caller, so never put in an else condition like this::

    >>> def get_odd_numbers(n = 10):
    ...     result = []
    ...     for i in range(n):
    ...             if i % 2 == 1:
    ...                     result.append(i)
    ...             else:
    ...                     return result
    ...
    >>> get_odd_numbers(20)
    []


Tuple unpacking
================

We know that for loop unpacks tuples::

    >>> prices = [('tea', 10), ('coffee', 12), ('lime', 15)]
    >>> for price in prices:
    ...     print(price)
    ...
    ('tea', 10)
    ('coffee', 12)
    ('lime', 15)

    >>> for drinks, price in prices:
    ...     print(f'{drinks} - {price}')
    ...
    tea - 10
    coffee - 12
    lime - 15


similar to that, function will also unpacks tuple::

    >>> from datetime import datetime
    >>> def get_day_month_and_year():
    ...     d = datetime.now()
    ...     return (d.day, d.month, d.year)
    ...
    >>> get_day_month_and_year()
    (4, 11, 2022)
    >>> day, month, year = get_day_month_and_year()
    >>> day
    4
    >>> month
    11
    >>> year
    2022

What happen if we provide more variables?::

    >>> day, month, year, minute = get_day_month_and_year()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: not enough values to unpack (expected 4, got 3)

How functions interact?
========================

Activation records...

`*args` and `**kwargs`
========================

- `*args` (tuple): arbitrary number of arguments. name `args` is not enforced.
- `**kwargs` (dict): arbitrary number of keyword arguments. name `kwargs` is not enforced.

**positional arguments**:

Here, arg1 and arg2 are positional arguments and their position is important::

    >>> def add(arg1, arg2):
    ...     return arg1 + arg2
    ...
    >>> add(100, 200)
    300

See how variable number of args works::

    >>> def total(carry_bag_price, *veg_prices):
    ...     return carry_bag_price + sum(veg_prices)
    ...
    >>> total(12, 3, 4, 2, 14, 30)
    65

`*args` is nothing but a tuple::

    >>> def total(carry_bag_price, *veg_prices):
    ...     print(veg_prices)
    ...
    >>> total(12, 3, 4,2,14, 30)
    (3, 4, 2, 14, 30)

as it is an iterable::

    >>> def fun(*args):
    ...     for x in args:
    ...             print(x)
    ...
    >>> fun(34, 2, 1, 0, 102, 23)
    34
    2
    1
    0
    102
    23

Let's see how kwargs works::

    >>> def total(carry_bag_price, *veg_prices, **tax):
    ...     print(carry_bag_price, veg_prices, tax)
    ...     return carry_bag_price + sum(veg_prices) + tax.get('gst', 0) + tax.get('cess', 0)
    ...
    >>> total(12, 23, 34, 57, 90, gst=18, cess=2)
    12 (23, 34, 57, 90) {'gst': 18, 'cess': 2}
    236

Lambda expressions, map and filter
====================================

- **map** applies a function to each element in an iterable
- Syntax: `map(function, iterable)`

::

    >>> def shout(slogan):
    ...     return f"{slogan}!!!"
    ...
    >>> slogans = ["jai hind", "Hi", "Hello"]
    >>> map(shout, slogans)
    <map object at 0x000001FF23F17DF0>
    >>> for i in map(shout, slogans):
    ...     print(i)
    ...
    jai hind!!!
    Hi!!!
    Hello!!!

We can also use list to see the function applied::

    >>> list(map(shout, slogans))
    ['jai hind!!!', 'Hi!!!', 'Hello!!!']

See another example of checking all numbers in a list odd or not::

    >>> def check_odd(num):
    ...     return num%2 == 1:

    >>> list(map(check_odd, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    [False, True, True, False, False, False, False, False, True]
    >>>

See the result if we use **filter** instead of map::

    >>> list(filter(check_odd, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    [31, 33, 67]

To make this map and filter more simpler, we can use **Lambda** expressions::

    >>> list(filter(lambda num: num%2==1, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    [31, 33, 67]

To get square of all numbers in a list::

    >>> list(map(lambda num: num*num, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    [100, 961, 1089, 484, 16, 0, 10000, 9604, 4489]

See what happens if we give filter in the square function::

    >>> list(filter(lambda num: num*num, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    [10, 31, 33, 22, 4, 100, 98, 67]

It just returned the same list. Why?? because for all numbers in the list, the result is square of the number which is a non zero value means TRUE. i.e::

    >>> list(filter(lambda num: True, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    [10, 31, 33, 22, 4, 0, 100, 98, 67]
    >>> list(filter(lambda num: 0, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    []
    >>> list(filter(lambda num: False, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    []
    >>> list(filter(lambda num: 11, [10, 31, 33, 22, 4, 0, 100, 98, 67]))
    [10, 31, 33, 22, 4, 0, 100, 98, 67]

Scope [LEGB Rule]
=====================
The order python looks at variable names is as per LEGB rule.

- L (local): assigned within a function (def or lambda).
- E (enclosing function locals): 
- G (global): declared outside of function or declared as `global` inside function.
- B (Built-in): python built-in (open, range, etc.)

first check local, if not exists, check enclosing, and then global::

    >>> msg = "Hi" # Global
    >>> def shout():
    ...     msg = "Hello" # Enclosing
    ...     def greet():
    ...             msg = "Good morning" # Local
    ...             print(msg)
    ...     greet()
    ...
    >>> shout()
    Good morning