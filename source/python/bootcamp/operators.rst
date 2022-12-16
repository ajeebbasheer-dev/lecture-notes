================
Operators
================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

Comparison Operators
=====================

Expressions using these operators will return a boolean.

::

    >>> 1 == 1
    True
    >>> 1.0 == 1
    True
    >>> 1 == '1'
    False
    >>> 'Hello' == 'Hello'
    True
    >>> 'Hello' == 'Hi'
    False
    >>> 2 != 2
    False
    >>> 10 > 20
    False
    >>> 10 >= 10
    True
    >>> 10 <= 10
    True
    >>> 10 < 20
    True

We can chain these operators::

    >>> 1 > 2 > 3
    False
    >>> 1 < 2 < 3
    True


Logical Operators
==================

We can use logical operators (**and, or and not**) to combine comparison operators or any Truthy or Falsy expression.

::

    >>> 10 > 20 or 30 > 20
    True
    >>> 10 > 20 and 30 > 20
    False
    >>> 10 == 10
    True
    >>> not (10 == 10)
    False
    >>> bool([])
    False
    >>> bool(not [])
    True







