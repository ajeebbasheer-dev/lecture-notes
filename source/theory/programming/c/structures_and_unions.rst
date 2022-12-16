==========================
User-defined datatypes
==========================

Structures
===========

In real life most often we deal with collection of data types. Not a single int, float or char.

When we need a program to list all students, we need to define a student first.

- Name: strings or char * or char[]
- Department: char []
- Roll number: (int)
- Marks: (float)

A structure is usually used when we wish to store dissimilar data together.


.. code-block:: c

    struct student{
        char name[20];
        int rollno;
        float marks;
    };

    void display_student_details(struct student s){
        printf("\nRollNo: %d: %s, Marks: %f", s.rollno, s.name, s.marks);
    }

    int main(){
        struct student s1, s2;
        strcpy(s1.name, "Tom");
        s1.rollno = 1;
        s1.marks = 99;
        strcpy(s2.name, "Jerry");
        s2.rollno = 2;
        s2.marks = 87.4;
        struct student s3 = { "Adam", 1, 33.3 } ;

        display_student_details(s1);
        display_student_details(s2);
        display_student_details(s3);
    }

.. toggle::

    ::
        
        RollNo: 1: Tom, Marks: 99.000000
        RollNo: 2: Jerry, Marks: 87.40000
        RollNo: 1: Adam, Marks: 33.29999


.. important:: 
    - Structure elements can be accessed through a structure variable using a **dot (.) operator.**.
    - Structure elements can be accessed through a pointer to a structure using the **arrow (->) operator**.
    - All elements of one structure variable can be assigned to another structure variable using the **assignment (=) operator**.
    - It is possible to pass a structure variable to a function either by value or by address.


How structure elements are stored
----------------------------------

.. code-block:: c

    int main(){
        struct student s = { "Adam", 1, 33.3 };
        printf("\nAddress of name: %p\n", s.name);
        printf("Address of rollno: %p\n", &s.rollno);
        printf("Address of marks: %p\n", &s.marks);
    }

::

    Address of name: 0x7ffee48b9a58
    Address of rollno: 0x7ffee48b9a6c // 58 + 20 = 6c
    Address of marks: 0x7ffee48b9a70 // 6c + 4 = 70

Array of structures
--------------------

.. code-block::

    int main(){
        struct student students[50];// array of 50 students.
        for (int i=0; i<50; i++){
            printf("\nStudent #%d:",i+1);
            printf("\nEnter name: ");
            scanf("%s", students[i].name);
            printf("Enter roll no: ");
            scanf("%d", &students[i].rollno);
            printf("Enter marks: ");
            scanf("%f", &students[i].marks);
        }

        printf("\nStudent Details\n");
        for (int i=0; i<50; i++){
            printf("\n%d: %s, Marks: %f", students[i].rollno, students[i].name, students[i].marks);
        }
    }



