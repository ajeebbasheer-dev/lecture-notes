==================
File input/output
==================

- Memory is volatile and its contents would be lost once the program is terminated.
- To store the data in a manner that can be later retrieved either in full or part , we have a medium called **`file` on a disk**.
- All data stored on the disk is in binary form. How this binary data is stored on the disk varies from one OS to another. 
- It is the compiler vendor's responsibility to correctly implement the library functions for I/O by taking the help of OS.

.. important:: Our Program --> Library Functions --> Operating System --> DISK


File I/O Library functions in C
================================

**FILE**: A structure defined in **stdio.h** that maintains information like mode of opening, size, next address to read etc.

::
    
    FILE *fp; // first we need to have a file pointer.

**fopen()**: Opens a file in read mode.

::
    
    fp = fopen ( "details.txt", "r" );

- Firstly it searches on the disk the file to be opened.
- Then it loads the file from the disk into a place in memory called buffer.
- It sets up a **character pointer** that points to the first character of the buffer.
- If opening fails, it returns a NULL (defined as **#define NULL 0** in stdio.h)

**fgetc()**: Reads the character from the current pointer position.

::

    ch = fgetc(fp) ;

We can keep on getting characters in a while loop. But till what point? How dow we know end of file?

.. important:: The **ASCII value 26** which indicates this. **#define EOF 26** is defined in stdio.h.

**fclose()**:

::

    fclose(fp);