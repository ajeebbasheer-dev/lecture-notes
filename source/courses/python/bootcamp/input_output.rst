=====
I/O
=====

.. toctree::
   :maxdepth: 3
   :caption: Contents:

Getting user input
==================

- Use special built-in function `input()`.
- `input()` always accept user inputs as strings.

    ::

        >>> user_input = input("Enter a number: ")
        Enter a number: 123
        >>> user_input
        '123'
        >>> type(user_input)
        <class 'str'>

- So need to use type casting if you need anything other than string.

    ::

        >>> int(user_input)
        123
        >>> float(user_input)
        123.0


- In a more elegant way, use `int(input("Enter a number: "))`

    ::

        >>> int(input("Enter a number: "))
        Enter a number: 123
        123
        >>> type(123)
        <class 'int'>

File I/O
=========

Let's have a file to work on::

	$ cat myfile.txt 
	First Line
	Second Line
	Third Line

open the file::

	>>> f = open('myfile.txt') # need to provide full path if file not in the same location.

By default the file is opened in `read mode`::

	>>> f
	<_io.TextIOWrapper name='myfile.txt' mode='r' encoding='UTF-8'>


If the file is not there, it will throw `FileNotFoundError`::

	>>> f = open('oops.txt')
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	FileNotFoundError: [Errno 2] No such file or directory: 'oops.txt'


Once opened, don't forget to close it::

	>>> f.close()

Use `with` to open a file as best practice::

	with open('oops.txt') as f:
		pass

read()
-------

This function will return the entire file contents as a string::

	>>> f.read()
	'First Line\nSecond Line\nThird Line\n'

Note that the new line is shown as \n.

If we do this again, it's no longer there::

	>>> f.read()
	''

In the beginning the cursor is at the beginning of the file. When we did the first read(), the cursor went to the end of the file.

To reset the cursor back to the beginning::

	>>> f.seek(0)
	0
	>>> f.read()
	'First Line\nSecond Line\nThird Line\n'

We can seek to any point::

	>>> f.seek(10)
	10
	>>> f.read()
	'\nSecond Line\nThird Line\n'

readlines()
------------

So get each line as a list::

	>>> f.seek(0)
	0
	>>> f.readlines()
	['First Line\n', 'Second Line\n', 'Third Line\n']


Open modes
-----------

- mode = 'r' : read only.
- mode = 'w' : write only.
- mode = 'a' : append to file 
- mode = 'r+' : read and write
- mode = 'w+' : read and write (overwrite existing file or create a new file)

If we open in write mode and try to read it::

    >>> with open('myfile.txt', mode='w') as f:
    ...     f.read()
    ... 
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    io.UnsupportedOperation: not readable
    >>> 

To append to the file::

	>>> with open('myfile.txt', mode='a') as f:
    ...     f.write('\nFourth Line')
    ... 
    12
    >>> with open('myfile.txt', mode='r') as f:
    ...     f.read()
    ... 
    'First Line\nSecond Line\nThird Line\n\nFourth Line'

But when we open as write mode, it will overwrite everything::

	>>> with open('myfile.txt', mode='w') as f:
    ...     f.write('\nFourth Line')
    ... 
    12
    >>> with open('myfile.txt', mode='r') as f:
    ...     f.read()
    ... 
    '\nFourth Line'

