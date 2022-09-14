==========
RST Guide
==========

.. sectnum::

.. contents::

Headings-Order
==============

::

    ============
    Main Title
    ============

    ============
        ------------
            ^^^^^^^^^^^^
                ~~~~~~~~~~~~
                    ''''''''''''


Add Image 
==========

::

    .. image:: _images/readme-sphinx/readme_sphinx.png
      :width: 600
      :align: center


Tables
==========

csv table
-----------

::

    .. csv-table:: 
       :header: "Category", "Command", "Use"
       :widths: 10, 20, 15

       a, b, c
       e, f, g


Directives
===========

section numbers
-----------------

Provide this directive at the top::

    .. sectnum::

.. image:: _images/rst_guide/section_num.png
  :width: 200
  :align: center

important
-----------

::

    .. important::
        - **point#1**: lorem ipsum. 
        - **point#1**: lorem ipsum. 


.. image:: _images/rst_guide/important.png
  :width: 500
  :align: center

Notes::

    .. note::

Warnings::

    .. warning::

Tips
------

- Superscript: E = mc\ :sup:`2`.
- Subscript: H\ :sub:`2`\ 0.