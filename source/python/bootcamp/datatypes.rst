================
Getting Started
================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

Data Types
===========

.. list-table:: Python Data Types
   :widths: 15 10 50 60
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Example
   * - Integers
     - int
     - whole numbers
     - 1, 2, 50, 100, 100000, etc.
   * - Floating point
     - float
     - numbers with decimal points
     - 1.2, 5.6, 9.3, 234.54, etc.
   * - String
     - str
     - **ordered** sequence of characters
     - "Hello", "", "foo", etc.
   * - Lists
     - list
     - **ordered** sequence of objects
     - ["Hello", 24.1, 2], [], [1, 3]
   * - Dictionaries
     - dict
     - **un-ordered** key-value pairs
     - {'name': 'john', 'age': 10}, {}, {1:2, 2:3}
   * - Tuples
     - tuple
     - **ordered immmutable** sequence of objects
     - ("Hello", 112, 12.3)
   * - Sets
     - set
     - **un-ordered** collection of **unique objects**
     - {"a", "b", "d", "c"}
   * - Boolean
     - bool
     - Logical values
     - True or False


Numbers in python
==================

Mainly 2 number types in python:

- Integers: Whole numbers
- Floating point numbers: Numbers with decimal value

::

	>>> 10 + 34 + 4
	48
	>>> 3-4
	-1
	>>> 3*9
	27
	>>> 36/8
	4.5
	>>> 36%8
	4
	>>> 2**5
	32
	>>> (2+10)* 3 - 36
	0
	>>> 3.12 * 4.08
	12.729600000000001

Variable assignments
=====================

In real life, the above numbers represent something. It must be something like 2 boys, 7.5 percentage, 11 balls etc.
Suppose if you want to use a number many times later in a program, what can we do?

We use `variable name` to represent a particular object in python.

Variables should adhere to the following rules.

- Can't start with a number.
- No spaces allowed. use underscore instead.
- No special characters other than underscore is allowed.

.. important:: Follow PEP8 convensions as a best practice.

	- Use lower case variable names
	- Avoid using words that have a special meaning in python. Example: str, float etc. (all syntax highlighiting tools highlight your variable in that case)
	- Doesn't mean we can't use python keywords as variable name::

		>>> float = 101
		>>> str = 9
		>>> float + str
		110

- Python uses **Dynamic Typing**. 

  - **Statically typed**:
  
    - A language is statically typed if the type of a variable is known at compile time.
    - Therefore, a lot of trivial bugs are caught at a very early stage.
    - Examples: C, C++, Java, Rust, Go

	::

		int main(){
	    	int pin = 676204;
	    	pin = 6767.04;
	    	pin = "676104";
		}

		$ gcc test.c
		test.c:3:11: warning: implicit conversion from 'double' to 'int' changes value from 6767.04 to 6767 [-Wliteral-conversion]
		    pin = 6767.04;
		        ~ ^~~~~~~
		test.c:4:9: warning: incompatible pointer to integer conversion assigning to 'int' from 'char [7]' [-Wint-conversion]
		    pin = "676104";
		        ^ ~~~~~~~~
		2 warnings generated.


  - **Dynamically typed**:
  
    - Type is associated with run-time values.
    - Most scripting languages have this feature as there is no compiler to do static type-checking anyway.
    - Most dynamically typed languages do allow you to provide type information, but do not require it. 
	- Very easy to work with. Faster development time.
	- My lead to unexpected bugs. Be aware of type() to check the type of a variable.
    - Perl, Ruby, Python, PHP, JavaScript, Erlang

	In Python, This is totally okay!::

		>>> address= "Calicut"
		>>> address= {"place" : "Calicut", "pin": 676294}


- We can reuse a variable any number of times

	::

		>>> number = 5
		>>> number = number + number
		>>> number
		10
		>>> number = number + number
		>>> number
		20
		>>> number = number + number
		>>> number
		40

- We can check the type of a variable using type()

	::

		>>> type(number)
		<class 'int'>
		>>> type(3.4)
		<class 'float'>
		>>> type('Calicut')
		<class 'str'>

- We can use variable names to make the logic more readable

	::

		>>> price = 100
		>>> discount = 30
		>>> final_price = price - discount
		>>> final_price
		70


Strings
=========

Sequence of characters inside either a pair of single quotes or double quotes.

::

	>>> 'Hello'
	'Hello'
	>>> "Hello"
	'Hello'
	>>> "What's up"
	"What's up"
	>>> 'What"s up'
	'What"s up'

However, this is not allowed::

	>>> 'Let's enjoy'
      File "<stdin>", line 1
        'Let's enjoy'
             ^
    SyntaxError: invalid syntax

To see length of a string::

	>>> len("Hello")
    5
    >>> s = "Hello"
    >>> len(s)
    5

Note that spaces is also a character::

	>>> len(" Hi ")
    4


Since srings are sequence of characters, we can grab any character or substring using indexing, reverse indexing or slicing.

::

	>>> place = "Calicut"

**Indexing** (Syntax: <name_of_string>[<index>])::

	>>> place[0]
	'C'
	>>> place[1]
	'a'
	>>> place[0] + place[1] + place[2] + place[3] + place[4] + place[5] + place[6]
	'Calicut'

So, what will be place[7]::

	>>> place[7]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: string index out of range


**Revesre Index**::

	>>> place[-1]
	't'
	>>> place[-2]
	'u'
	>>> place[-3]
	'c'
	>>> place[-4]
	'i'
	>>> place[-5]
	'l'
	>>> place[-6]
	'a'
	>>> place[-7]
	'C'
	>>> place[-8]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: string index out of range


::

	String: 		 C  a  l  i  c  u  t
	Index:  		 0  1  2  3  4  5  6
	Reverse Index:  -1 -2 -3 -4 -5 -6 -7


**Slicing** (<name_of_string>[start:end:step]).

- start: starting index you want to slice from.
- end: end slice before this index. (**excluding character at this index**)
- step: steps you want to take.

::

	>>> s = "Let's Start at 10AM"
	>>> len(s)
    19
    >>> s[0:19]
    "Let's Start at 10AM"
    >>> s[0:len(s)]
    "Let's Start at 10AM"

Note that, Unlike indexing, even if you give an end index bigger than string size, it works::

	>>> s[0:25]
    "Let's Start at 10AM"

	>>> s[25]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range


::

    >>> s[0:10]
    "Let's Star"
    >>> s[0:2]
    'Le'
    >>> s[0:0]
    ''

Start index will work similar to end index. Even if you give an start index which is greater than end, it will not throw error::

	>>> s[2:0]
    ''

::

	>>> s[6:11]
    'Start'
    >>> "Let's Start at 10AM"[6:11]
    'Start'

Slicing with negative ::

    >>> s[-19:-16]
    'Let'
	>>> s[-19:0]
    ''
    >>> s[-19:-1]
    "Let's Start at 10A"

To see all characters **upto (not including)** an index::

    >>> s[:5]
    "Let's"

To see all characters **all the way till end** from an index::

    >>> s[12:]
    'at 10AM'

Different ways to see entire string::

    >>> s
    "Let's Start at 10AM"
    >>> s[:]
    "Let's Start at 10AM"
    >>> s[-19:]
    "Let's Start at 10AM"
    >>> s[0:]
    "Let's Start at 10AM"
    >>> s[0:19]
    "Let's Start at 10AM"

Step::

   >>> s[0:19:2]
   'LtsSata 0M'

To reverse a string (**Return entire string but take reverse STEP**)::

	>>> s[::-1]
	"MA01 ta tratS s'teL"


Immmutability
--------------

Suppose we want to change Bat to Cat::

	>>> my_string = "Bat"
    >>> my_string[0] = "C"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

You can't change a string. You need to create a new string and bind the variable to it if you want.

	>>> my_string = "Cat"
	>>> my_string 
	'Cat'

or you can use **String concatenation**

String concatenation
---------------------

::
	
	>>> my_string = "Bat"
	>>> my_string = "C" + my_string[1:]
	>>> my_string
	'Cat'

You can add any number of strings::

	>>> "Hello" + " Good morning" + " How are you?"
	'Hello Good morning How are you?'

However don't try to concatenate different types::

	>>> 2 + "Animals"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'


upper(), lower() and more..
---------------------------

::

	>>> my_str = "Hello World"
	>>> my_str.upper()
	'HELLO WORLD'
	>>> my_str.upper # you have'nt executed the function, you just asked what it is...
	<built-in method upper of str object at 0x10a7eadf0>
	>>> my_str.lower()
	'hello world'
	>>> my_str.lower
	<built-in method lower of str object at 0x10a7eadf0>

To see what all such functions are available to your object, use **dir()**::

	>>> dir(my_str)
	['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
	>>> 

	>>> my_str.split()
	['Hello', 'World']
	>>> my_str.split('o')
	['Hell', ' W', 'rld']


Formatting strings 
------------------

Most of the time you will have to add a variable in a string as follows::

	>>> place = "Calicut"
	>>> "Hey, I am from " + place
	'Hey, I am from Calicut'

There are multiple ways to format string in a better way. Two important ways are,

- format()
- f-strings: formatted string literals

format() method
^^^^^^^^^^^^^^^^

::

	>>> my_str = "Hey, I am from {}"
	>>> my_str.format(place)
	'Hey, I am from Calicut'
	>>> my_str = "Hey, I am from {}. I am a {}"
	>>> my_str.format(place, job)
	'Hey, I am from Calicut. I am a Teacher'

Sometimes you will have to specify the order::

    >>> first_prize = "Kevin"
    >>> second_prize = "Bob"
    >>> third_prize = "Julie"

	>>> prize_announcement = "Third_prize goes to {2}, 2nd prize goes to {1}, and here is the winner {0}"

    >>> prize_announcement.format(first_prize, second_prize, third_prize)
    'Third_prize goes to Julie, 2nd prize goes to Bob, and here is the winner Kevin'

We can also specify variables for replacemnet::

	>>> prize_announcement = "Third_prize goes to {third}, 2nd prize goes to {sec}, and here is the winner {first}"
    >>> prize_announcement.format(first = first_prize, sec=second_prize, third=third_prize)
    'Third_prize goes to Julie, 2nd prize goes to Bob, and here is the winner Kevin'
    >>> 

**format with precision**

Syntax: **{value:width.precision f}**

::

	>>> result = 100/3
    >>> result 
    33.333333333333336

	>>> "result is {r}".format(r=result)
    'result is 33.333333333333336'

    >>> "result is {r:1.2f}".format(r=result)
    'result is 33.33'

To have more spaces before the value, use more width::

	>>> "result is {r:20.2f}".format(r=result)
    'result is                33.33'



f-strings
^^^^^^^^^^

::

	>>> f"Hey, I am from {place}. I am a {job}"
    'Hey, I am from Calicut. I am a Teacher'


Lists 
======

Lists are **ordered** sequences that can hold **different types** of objects.

- use [] and commas to separate objects inside the list.

::

	>>> [1, 2, 3, 4, 5]
	[1, 2, 3, 4, 5]
	>>> ['k', 'z', 'a', 'c', 'b']
	['k', 'z', 'a', 'c', 'b']
	>>> [1, 2, 'a', 400, 'bc', '43']
	[1, 2, 'a', 400, 'bc', '43']

- List supports indexing and slicing exactly like strings.

::

    >>> my_list = [1, 2, 3, 4, 5]
    >>> my_list[2]
    3
    >>> my_list[2:]
    [3, 4, 5]

	>>> my_list[2:4]
	[3, 4]
	>>> my_list[:4]
	[1, 2, 3, 4]
	>>> my_list[:-4]
	[1]

- List can hold any type of objects, including nested list

::

	>>> [1, 1.2, [11,22,33], 'a']
    [1, 1.2, [11, 22, 33], 'a']

- We can concatenate lists similar to strings

::

	>>> [1, 2, 3] + [11, 22, 33]
	[1, 2, 3, 11, 22, 33]

	>>> boys = ['bob', 'joe', 'aslam', 'kevin', 'ajay']
	>>> girls = ['merin', 'jing', 'monika']
	>>> students = boys + girls
	>>> students
	['bob', 'joe', 'aslam', 'kevin', 'ajay', 'merin', 'jing', 'monika']
	>>> boys
	['bob', 'joe', 'aslam', 'kevin', 'ajay']
	>>> girls
	['merin', 'jing', 'monika']


List are **Mutable** Strings are **Immutable**::

	>>> num_list= [1, 2, 3, 4, 5]
    >>> num_list
    [1, 2, 3, 4, 5]
    >>> num_list[3] = 111
    >>> num_list
    [1, 2, 3, 111, 5]

append() and pop() 
------------------

**append()**: insert a new item at the end of list::

	>>> num_list= [1, 2, 3, 4, 5]
    >>> num_list.append(111)
    >>> num_list
    [1, 2, 3, 4, 5, 111]

Note that **append()** permanently changes the list!

**pop()**: pops & return last item by default::

	>>> popped = num_list.pop()
    >>> num_list
    [1, 2, 3, 4, 5]
    >>> popped
    111

We can pop a specific index as well::

	>>> popped = num_list.pop(2)
    >>> popped
    3
    >>> num_list
    [1, 2, 4, 5]

sort()
-------

sort() permanently changes the list::

    >>> num_list = [111, 1, 33, 444, 32]
    >>> num_list.sort()
    >>> num_list
    [1, 32, 33, 111, 444]

    >>> my_list = ['p', 'q', 'a', 'c', 'b']
    >>> my_list.sort()
    >>> my_list
    ['a', 'b', 'c', 'p', 'q']

sort() returns nothing (None)! So, never do this:;

    >>> sorted_list = my_list.sort()
    >>> my_list
    ['a', 'b', 'c', 'p', 'q']
    >>> sorted_list 
    >>> 

    >>> type(sorted_list)
    <class 'NoneType'>

.. important:: None is a special object in python to indicate no value!

reverse()
----------

::

	>>> num_list= [1, 2, 3, 4, 5]
    >>> num_list.reverse()
    >>> num_list
    [5, 4, 3, 2, 1]
    >>> 

insert(<index>, <value>)
--------------------------

::

	>>> num_list= [1, 2, 3, 4, 5]
    >>> num_list.insert(2, 11111)
    >>> num_list
    [1, 2, 11111, 3, 4, 5]

    >>> num_list.insert(2, [1, 2, 3])
    >>> num_list
    [1, 2, [1, 2, 3], 11111, 3, 4, 5]

extend(<list>) 
----------------

::

	>>> num_list= [1, 2, 3, 4, 5]
    >>> num_list.extend(['a', 'b', 'c'])
    >>> num_list
    [1, 2, 3, 4, 5, 'a', 'b', 'c']

See what will happen we use append instead of extend??::

	>>> num_list= [1, 2, 3, 4, 5]
	>>> num_list.append(['a', 'b', 'c'])
	>>> num_list
	[1, 2, 3, 4, 5, ['a', 'b', 'c']]

.. important:: 
	- Only pop() returns a value.
	- The methods append(), insert(), reverse(), extend(), sort() methods returns None
	- All the above are **inplace** methods.


dir() for more 
---------------

::

	>>> dir(num_list)
	['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


Dictionaries
=============

Unordered mapping for storing objects.

- Uses `Key:Value` pairs.
- Use curly braces and colons to signify the keys and their associated values.

.. important:: When to use a List? When to choose a dictionary?

	- **Dictionaries**: Objects retrieved by **key name**. Unorderd.
	- **List**: Objects retrieved by **location**. Ordered sequence can be indexed or sliced.

::

	>>> my_address = {'name': 'john', 'city': 'Calicut', 'street': 'link road'}
	>>> my_address
	{'name': 'john', 'city': 'Calicut', 'street': 'link road'}
	
To retrieve a key value::

	>>> my_address['city']
	'Calicut'

What happens if we try to get a non-existing key?::

	>>> my_address['foobar']
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'foobar'

To avoid this error, we can use get() method::

	>>> my_address.get('foobar')
	>>> 
	>>> my_address.get('foobar', 'Unknown')
	'Unknown'
	>>> my_address.get('street', 'Unknown')
	'link road'

	>>> tea_prices = {'lemon': 12, 'ginger': 15, 'masala': 13}
	>>> tea_prices.get('lemon', 10)
	12
	>>> tea_prices.get('blacktea', 10)
	10

Dictionary can be nested::

	>>> prices = {'coffee': 15, 'tea': {'lemon': 12, 'ginger': 13}}
    >>> prices['tea']['lemon']
    12


The keys() and values() methods 
---------------------------------

::

	>>> prices.keys()
	dict_keys(['coffee', 'tea'])
	>>> prices.values()
	dict_values([15, {'lemon': 12, 'ginger': 13}])
	>>> 

To get the pairings: items()
-----------------------------

::

	>>> prices.items()
	dict_items([('coffee', 15), ('tea', {'lemon': 12, 'ginger': 13})])


Tuples
========

Very similar to lists but **Immutable**.

- The element inside a tuple can't be reassigned.
- Uses parenthesis and commas. (1, 3, 5)
- len(), indexing and reverse indexing works similar to lists.
- When to use?: if you want all features of a list but need to ensure data integrity. i.e. you want to ensure that elements will not get reassigned later in code.

::

	>>> items = (1,2,3)
	>>> items1 = (1,2,3)
	>>> items2 = [1,2,3]
	>>> 
	>>> type(items1)
	<class 'tuple'>
	>>> type(items2)
	<class 'list'>
	>>> len(items1)
	3
	>>> items1[-1]
	3


count() and index() methods
-----------------------------

t.count(x): returns count of x in the tuple t.
t.index(x): index of x in tuple x. if multiple entries, then returns the index of first occurrence.

::

	>>> my_tuple = (1, 2, 3, 4, 3, 4, 5, 3, 1)
    >>> my_tuple.count(3)
    3
    >>> my_tuple.count(1)
    2
    >>> my_tuple.index(3)
    2

Immmutability
--------------

::

	>>> my_list = ['x', 'y', 'z']
	>>> my_list[0] = "NEW VALUE"
	>>> my_list
	['NEW VALUE', 'y', 'z']

This will not work in tuples::

	>>> my_tuple = ('x', 'y', 'z')
	>>> my_tuple[0] = "NEW VALUE"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment


Sets 
=====

Unorderd collection of **Unique** elements. There cannot be duplicate elements in a set.

Beware that we are not creating empty dict for a set::

	>>> my_set = {}
	>>> type(my_set)
	<class 'dict'> # OOPS!!!

	>>> my_set = set()
	>>> type(my_set)
	<class 'set'>

::

	>>> my_set.add(10)
	>>> my_set
	{10}
	>>> my_set.add(20)
	>>> my_set
	{10, 20}

You can't add same element again::

	>>> my_set.add(20)
	>>> my_set
	{10, 20}

.. important:: We can convert list/tuples to set() to removed duplicate elements

	::

		>>> my_list = [5,5,5,5, 6, 7, 6, 5, 5, 5, 7]
		>>> my_tuple = (5,5,5,5, 6, 7, 6, 5, 5, 5, 7)
		>>> 
		>>> my_list
		[5, 5, 5, 5, 6, 7, 6, 5, 5, 5, 7]
		>>> my_tuple
		(5, 5, 5, 5, 6, 7, 6, 5, 5, 5, 7)
		>>> 
		>>> unique_list = set(my_list)
		>>> unique_list
		{5, 6, 7}
		>>> unique_tuple = set(my_tuple)
		>>> unique_tuple
		{5, 6, 7}
		>>> 


- We can do any set operation with set datatype.

::

	>>> my_set
    {10, 20}
    >>> new_set 
    {40, 20, 30}
    >>> my_set.union(new_set)
    {20, 40, 10, 30}
    >>> my_set.intersection(new_set)
    {20}
    >>> 


Booleans
=========

Booelan values in python to indicate True and False.

::

	>>> type(True)
	<class 'bool'>
	>>> type(False)
	<class 'bool'>

	>>> 1 > 20
	False
	>>> 1 < 20
	True


Make sure the T and F are caps::

	>>> True
    True
    >>> False
    False
    >>> true
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'true' is not defined
    >>> false
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'false' is not defined
    >>> 


Truthy and Falsy 
----------------

- Values that evaluate to False are considered Falsy.
	- Empty lists []
	- Empty tuples ()
	- Empty dictionaries {}
	- Empty sets set()
	- Empty strings ""
	- Zero of any numeric type including complex types(0, 0.0, 0j)
	- Empty ranges range(0)
	- Constants like None, False
- Values that evaluate to True are considered Truthy
	- By default, an object is considered true.
	- Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
	- All numeric non-zero values.
	- Constants like True
- They can use in conditional statatements like if, while etc.


Bool()
-------

To evaluate a expression to boolean::

	>>> bool([])
	False
	>>> bool(0)
	False
	>>> bool(0.0)
	False
	>>> bool(0j)
	False
	>>> bool(1.2)
	True
	>>> bool(111)
	True
	>>> bool(None)
	False
	>>> bool("")
	False
	>>> bool("Hi")
	True
