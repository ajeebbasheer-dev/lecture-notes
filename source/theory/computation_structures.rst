.. https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/

========================
Computation Structures
========================


Basics of Information
========================

In order to build circuit to manipulate, transmit or store information, we need some engineering tools to see if we are choosing good representation of information.
- What are the different ways of encoding information as bits.
- What if our encoding is corrupted by errors.

Information
-------------

`Data communicated or received that resolves uncertainty about a particular fact or circumstance.`

To know which card is chosen, we have the following information.

- The card is heart - uncertainty reduced to 13 from 52
- The card is not the Ace of Spades - not much info. just one case is eliminated.
- The card is a face card (JQK) - little more information
- The card is a suicide king. - resolves maximum uncertainty or no uncertainty at all.

Information content can be quantified as,

Given a probability p, of an event occurring, the amount of information that you get from being told that particular event occurred is log\ :sub:`2` (1/p)

.. image:: _images/computation_structures/001_info_content.png
  :width: 400
  :align: center

Question: Someone picks a name out of a hat known to contain the names of 3 men and 5 woman and tells you man has been selected. How much information have they given you about the selection?
  - p\ :sub:`men` = 3/8 ==> Amount of information = log\ :sub:`2` (1/(3/8)). 
  - In General, N = Original number of choices M = Reduced number of choices. amount of information = log\ :sub:`2` (N/M). 

More examples:

- To encode information in one coin flip: log2(2/1) = 1 bit of information
- card drawn from a fresh deck is heart - Uncertainty reduced from 52 to 13: log2(52/13) = 2 bits of information.

.. image:: _images/computation_structures/002_info_content.png
  :width: 400
  :align: center




Entropy
--------

.. important:: **Entropy H(X)= Average amount of information contained in each piece of data received about the value X.**

Encoding
---------

Unambiguous mapping between bit strings and the set of possible data.

1. Fixed length encoding.
2. Variable length encoding.
3. Ambigous encoding.


.. image:: _images/computation_structures/003_encoding.png
  :width: 250
  :align: center


We can draw a binary tree if the encoding is Unambiguous.

.. image:: _images/computation_structures/004_encoding.png
  :width: 250
  :align: center

Fixed-length encoding
^^^^^^^^^^^^^^^^^^^^^^^

If the symbols we are trying to encode occur in equal probability, then we use Fixed-length encoding. 

- **All leaves from the encoding's binary tree are same distance from root**.
- Fixed-length encoding **supports random access**. We can figure out Nth symbol of the message by skipping the required number of bits.
- Fixed-length encoding is often inefficient because we may use more than minimum number required to encode.

.. image:: _images/computation_structures/005_fixed_encoding.png
  :width: 250
  :align: center

Examples:

- 4-bit BCD (binary coded decimal) digits. Entropy = log\ :sub:`2` \(10) = 3.322 [only 3.322 bits is required but we use 4 bits in BCD as it is decimal]. Suppose we are encoding a message of 1000 symbols and we use 4000 bits to encode that. It actually requires around 3400 bits.
- 7-bit ASCII for printing characters. ASCII as 94 characters. Associated entropy = log\ :sub:`2` \(94) = 6.55bits. But we use 7 bits in our fixed length encoding.
- Encoding positive numbers using binary.

.. image:: _images/computation_structures/006_fixed_encoding.png
  :width: 250
  :align: center

- Long strings of binary are error prone and tedious to transcribe. So we use higher-radix hexadecimal notation where each group of 4 adjacent bits are represented as a single hexadecimal digit. To prevent confusion we prepend `0x` with a hexadecimal number.

.. image:: _images/computation_structures/007_hexadecimal.png
  :width: 250
  :align: center

Signed integers: 2's compliment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We leaned how to represent 2000 in binary and hexadecimal. What should be the representation for -2000?

Signed magnitude representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

just like we add `+` or `-` before decimals, we can also use a dedicated bit to indicate sign as follows.

.. image:: _images/computation_structures/008_signed_magnitude.png
  :width: 250
  :align: left

Drawbacks: 

- There are 2 possible binary representation for 0 (+0 and -0).
- Circuitry for addition is different from circuitry for subtraction. We need 2 circuitry if we use this representation.

To make things simple, most modern digital systems use 2's compliment binary representation for signed numbers.

2's compliment
~~~~~~~~~~~~~~~

- A way to represent both positive and negative numbers in binary.

.. important:: **Higher order bit of N-bit representation has a negative weight.**

.. image:: _images/computation_structures/009_2scompliment.png
  :width: 250
  :align: left

- There is a unique representation for 0 here.
- To negate a 2's compliment value, just do bitwise compliment and add 1. i.e. one's compliment is not that significant except when doing a A-B(A+ (-B)) which require negating B, a 2's compliment number.

.. image:: _images/computation_structures/010_2scompliment.png
  :width: 300
  :align: center

- How to find the value of 2's compliment number 001000
- **001000**: 0* -2^5 + 0* 2^4 + 1 * 2^3 + 0*2^2+ 0*2^1+ 0*2^0 = 8

- Negative numbers in 2's complement will always have a 1 in most significant bit. Let's take 101100
- Just add 1's in the MSB to represent the same number with larger bits. i.e. **101100** = **11101100**.
- **101100** = -2^5 + 2^3 + 2^2 = -32+8+4 = -20
- **11101100** = -2^7 + 2^6 + 2^5 + 2^3 + 2^2 = -128 + 64 + 32 + 8 + 4 = -20

Range of numbers that can be represented by N bit 2's complement
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Let's begin with example of 6 bits:

- Largest positive number = 011111 = 31 = 2^5-1
- Most negative number = 100000 = -2^5 = -32

.. important:: **Range of numbers that can be represented by N bit 2's complement**: -2\ :sup:`N-1` to  2\ :sup:`N-1` -1

Finding negative number of a 2's complement number
''''''''''''''''''''''''''''''''''''''''''''''''''''

.. important:: Negation of 2's compliment = Flip all and add 1.

- 101100 = -20 
- Flip all => 010011
- +1 => 010100 = 0*-2^5+ 2^4+ 0*2^3 + 2^2+ 0 + 0 = 20
- Flip all => 101011 
- +1 => 101100 = -20


2's compliment addition
''''''''''''''''''''''''

- subtraction A-B is adding A+(-B). We know how to negate 2's complement values.
- 15-18 = 001111 - 010010 = 001111 + 101110 = 111101 = -3
- 27-6 = 27 + (-6) = 011011 - 000110 = 011011 + (111001+1)  = 011011 - 111010 = 1010101 = MSB is dropped. => 010101 = 21

**Overflow**

- Occurs only if we add 2 numbers of same sign. 
  - If we add 2 positive numbers (MSB=0) and result ends up negative (MSB=1), then overflow occurred.
  - If we add 2 negative numbers (MSB=1) and result ends up positive (MSB=0), then overflow occurred.
- Overflow cannot occur when you add a negative and positive number within range.
- 31 + 12 = 011111 + 001100 = 101011 = 43. i.e not within the range. i.e. -32 to +31 (-2^5 to 2^5-1)

Variable-length Encoding
^^^^^^^^^^^^^^^^^^^^^^^^^

Fixed-length encoding works well when all the possible choices have same information content or same probability of occurring. If this is not the case, then we can do better. Means we can have **a shorter length encoding to match the entropy**.

More likely choices --> Shorter encodings
Less likely choices --> longer encodings

.. image:: _images/computation_structures/011_variable_length_encoding.png
  :width: 300
  :align: center

Huffman's Algorithm
^^^^^^^^^^^^^^^^^^^^^

- **Optimal Variable-length encoding**.
- Algorithm builds binary tree from bottom up.
  
Algorithm:

- starts with 2 symbols with smallest probability (means highest information content which should have the longest encoding).
- Example: A=1/3, B=1/2, C=1/12, D=1/12

  .. image:: _images/computation_structures/012_huffman.png
    :width: 100
    :align: left

  .. image:: _images/computation_structures/013_huffman.png
    :width: 100
    :align: left

  .. image:: _images/computation_structures/014_huffman.png
    :width: 100
    :align: left

- Example:

    .. image:: _images/computation_structures/017_huffman_example.png
      :width: 250
      :align: left
  
- We can draw Huffman encoding tree in different ways. Identical in structure and result in same encoding.

    .. image:: _images/computation_structures/019_same_encoding_diff_tre.png
      :width: 250
      :align: left

- Huffman tree can have more than one valid encoding. Only constraint is each node should have a 0 & 1 branch. side does not matter.

    .. image:: _images/computation_structures/018_different_encoding.png
      :width: 250
      :align: left
  

Huffman Code
^^^^^^^^^^^^^
**Most file compression algorithms uses this approach.**

.. image:: _images/computation_structures/015_huffman.png
  :width: 300
  :align: center

Error detection and correction
--------------------------------

- **Hamming Distance**: The number of positions in which the corresponding digits differ in 2 encoding of same length.
- Hamming distance is a handy tool to measure how encoding is different.
- Single bit error: Hamming distance b/w a valid code word and the same codeword with single bit error = 1
- Suppose if 0 sent is received as 1, then we don't know if that is an error or valid code word.
- So we need a way in which a single bit error does not produce another valid code word. We need the minimum Hamming Distance as 2 to detect errors. 
- **Even Parity**: Add 0/1 to make total number of 1s in the code word even.
- **Odd Parity**: Add 0/1 to make total number of 1s in the code word odd.
- Example: 0 ==add even parity==> 00 can be corrupted as 01 or 10 which has odd number of 1's. Hence confirmed that there is a single bit error.
  
.. image:: _images/computation_structures/016_single_bit_error.png
  :width: 300
  :align: center

- To detect "E" errors, we meed minimum hamming distance of "E+1" between code words.

Error correction
^^^^^^^^^^^^^^^^^
- By increasing hamming distance by 3, we guarantee that sets of code words produced by single bit errors don't overlap.
  - i.e. 0 ==> 000 ==> 100, 010, 001 has not over lap with 1 ==> 111 ==> 101, 110, 011 
- In general, to correct "E" errors, we need a minimum hamming distance of **2E + 1** between code words.
- To correct single bit errors, we need valid codewords with minimum hamming distance of 3.
- let's see how selected encoding of a message can help in detecting and correcting errors.

The Digital Abstraction
========================

We learned about bits. **where do bits come from???** 

What makes a good bit?
- small inexpensive (we need a lot of them) - the chemical encoding in DNA serves as the blue print for living organism. Molecular scale meets our size requirements but to manipulate information is difficult.
- stable and reliable (once 0 should stay as 0) - Rosetta stone
- ease and speed of manipulation (access, transform, transmit, and store,.)

We don't want to carry around buckets of DNAs and stone chisels, who should we represent bits.

Consider using **phenomenon associated with charged particles**. Presence of charged particles creates differences in electrical potential energy we can measure as **voltages**. and flow of charged particles as **currents**. we can also encode information using **phase** and **frequency** of electromagnetic fields associated with charged particles. phase and frequency form the basis of wireless communication. i.e. we have couple of choices:
- voltages
- current
- phase
- frequency

In this course we use **voltages** to represent bits. 0V to represent 0bit,1V to represent 1bit. To represent *sequence of bits* we can use multiple voltage measurements, either from many different wires or as a sequence of voltages over time on a single wire.

advantages of voltage:
- easy generation, inexpensive, reliable
- for mobile applications, we can use batteries to supply what we need.

disadvantages:
- easily affected by changing electromagnetic fields.
- to transfer, we need to be connected by a wire.
- Resistance and Capacitance of wire slowdown.

Analog Signalling
------------------

To represent a image:
- 0V: Black.
- 1V: White
- 0.37V: Grey

We can convert an image into a time-varying sequence of voltages. This is how the original televisions worked. The picture encoded as a voltage waveform.

Using Voltages Digitally
-------------------------

- There are lot of problems with analog signalling.
- Keep in mind that the world is not inherently digital. We need to engineer to behave that way.
- The key idea in using voltages digitally is to have a signalling convention that encodes only one bit of information at a time. i.e. 0 or 1.
- When a voltage V is less than a threshold value, we will take it to represent it as 0. if greater, then 1. So all possible voltages are covered by diving in to 2 ranges.

Combinational Devices
-----------------------

A combinational device is a circuit element that has

- one or more digital inputs. - accepts voltages above or below the threshold
- one or more digital outputs - generates voltages above or below the threshold
- a functional spec that specifies values of each input for every possible combination of inputs.
- a timing spec consisting of an upper bound on the required time for the device to compute the specified output values.

A compbinational digital system is a set of interconnected elements in a combinational device if:

- each circuit is combinational
- every input is connected to exactly one output.
- no directed cycles.


MOSFET
=======

MOSFET: Metal-Oxide-Semiconductor-Field-Effect-Transistor

Physical view
--------------

Combinational device should address the following wish lists:

- design the system to tolerate some amount of error.
- We need **Billions** of devices in our digital system, so each device will have to be quite small and inexpensive.
- We need system to run on battery for long period. So, the devices should dissipate little power. Changing voltages will dissipate power, but if no voltages are changing, we would like to have zero dissipation.
- should be able to design use full functionalities. 

There is a circuit technology that will make our wishes comes true. That technology is **Metal-Oxide-Semiconductor-Field-Effect-Transistor**.

Cross section of MOSFET looks like:
 - The substrate upon which IC is built is of a thin wafer of silicon crystal with added impurities to make it conductive. The impurity in this case is an acceptor atom like Boron and we characterize the doped silicon as a **p-type semiconductor**.
 - IC will include an electrical contact to the p-type substrate, called the **bulk** so we can control it's voltage.
 - To provide electrical insulation between conducting materials, we use a layer of SiO2
 - The gate terminal of the transistor is a conductor.
 - The gate, the thin oxide insulation layer and the p-type substrate forms a **capacitor**.
 - In the early stage, gate was of metal and that's why it's called Metal-Oxide-Semiconductor.
 - Donor atoms such as Phosphorous are implanted into 2 sides of gate and this forms a **n-type semiconductor**.

To summarize:
- The MOSFET has 4 electrical terminals. Bulk, Gate, Source and Drain.
- 2 of the device dimensions are under the control of the designer (W and L). the channel length(smallest as possible) and channel width.
- It's a solid state switch. no moving parts. The switch operation is controlled by electrical fields determined by relative voltages of 4 terminals. 

.. image:: _images/computation_structures/020_mosfet_crosssection.png
  :width: 300
  :align: center

- The above shown picture is 1/1000 th thickness of thin human hair. i.e. nano meters.
- MOSFET Can't be viewed using ordinary optical microscope.
- For many years, engineers have been able to shrink this by a factor of 2 on every 24 months. This observation is known as **Moores Law**. (by one of the founder of intel, Gorden Moore, who first remarked this trend in 1965)
- Each 50% shrink enables IC (integrated circuit) manufactures to build 4 times as many devices in the same area as before. This makes the devices **faster** and **smaller**.
- **In 1975, ICs might have had 2500 devices. Today we build ICs with 2 to 3 billions devices.**
- MOSFET - is a complicated samples of electrical materials.


Electrical view
-----------------

https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c3/c3s2/c3s2v2/

- Drain: Highest voltage potential terminal, Source: Lower potential terminal. So, Current flow in MOSFET is from Drain to Source. 
- MOSFET is manufactured with a particular threshold voltage (VTH).

.. image:: _images/computation_structures/021_mosfet_electrical.png
  :width: 300
  :align: center

**FET comes in 2 flavors (N type and P type transistors)**: That's why the family called **CMOS** (Complementary Metal Oxide Semiconductor.)


CMOS 
-----

MOSFETS can behave as a **Voltage controlled switch**

Combinational Logic
====================

Functional specification options:

1. Natural language

.. image:: _images/computation_structures/022_comb_logic.png
  :width: 300
  :align: center

2. Truth tables: For a 32bit number addition circuit, there would be 64 inputs and truth table would need 2^64 rows. If compute output of 1 row takes a second, it would take 584 billion years to fill in the table.
3. Boolean expressions whose operations are AND, OR and INVERSION. Example: A.B+ B.C.D where + is OR and . is AND

Sum of products
----------------
Truth tables and boolean equations are interchangeable. Any boolean combinational function can be specified as a **sum of products** as follows.

.. image:: _images/computation_structures/023_sumofprod.png
  :width: 300
  :align: center

i.e. we can build a combinational circuit only with AND, OR and an INVERTER.

.. image:: _images/computation_structures/024_circuit_to_sumofprod.png
  :width: 300
  :align: center

How to have AND and OR gates with more than 2 inputs?
------------------------------------------------------

Chain or Tree way?

.. image:: _images/computation_structures/025_chain_or_tree.png
  :width: 300
  :align: center

Both has same number of gates. So cost wise both are same.
Now propagation delay. **Chain grows linear, Tree grows logarithmic with number of gates**.. However it is hard to know which takes less delay.


Universal Gates
---------------

- In designing CMOS circuits, we use NAND and NOR gates.
- NAND and NOR gates are not associative. i.e. NAND(ABC) != NAND(C)NAND(AB). So, we can't use a chain or tree strategy.

.. image:: _images/computation_structures/026_nandnorxor.png
  :width: 300
  :align: center


.. important:: Any logic function can be implemented using only NAND gate or only NOR gates. So **NAND and NOR are called universal gates**.

CMOS Inverting Logic
---------------------

- Tpd = time propagation delay.
- AND4 means AND gates with 4 inputs (chain or tree)

.. image:: _images/computation_structures/027_cmos_gates.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/028_widenandsnors.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/029_cmos_sumofproducts.png
  :width: 300
  :align: center

Logic Simplification
---------------------

.. image:: _images/computation_structures/030_logic_simplify.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/031_simplify.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/032_dontcare.png
  :width: 300
  :align: center

Karnaugh Maps
--------------

.. image:: _images/computation_structures/033_kmap.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/034_kmap.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/035_implicant.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/036_prime_implicant.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/037_prime_imlicant.png
  :width: 300
  :align: center

Multiplexers (MUX)
-------------------

A MUX selects one of it's 2 input values as the output values. If value of S is 0, then D0 is selected as output Y. If S is 1, then D1 is selected as output Y.
MUX can be generalized to 2^k data inputs and k select inputs.

.. image:: _images/computation_structures/038_mux.png
  :width: 300
  :align: center

Why MUX is important?

- MUX provide a very elegant way to implement a logic function. 
  - A, B and Cin are 3 select signals of the MUX.

.. image:: _images/computation_structures/039_mux.png
  :width: 300
  :align: center

- We can build any 1-output combinational logic block with Multiplexers. For N input function, we need 2^N input MUX.


ROM (Read Only Memories)
--------------------------

.. important:: MUXs are good for implementing truth tables with **one output column**, Read-Only memories are good for implementing truth tables with **many output columns**.

- key component in read only memory is a **Decoder** which has k select inputs and 2^k data outputs.
  - Only one of the data output will be 1 or High at a given time.
  - The jth output is one  (high) when the select lines are set to the binary representation of j.

The below 2-output device is a Full adder (a building block in addition circuits)

.. image:: _images/computation_structures/040_rom.png
  :width: 300
  :align: center

- 3 inputs A, B and C are connected select lines of a 3-to-8 Decoder.
- When the inputs are 000, the top Decoder output will be high and all others low.
- The Decoder outputs control a matrix of NFET pull down switches.
- The column circuitry is designed so that if no pulldown switches force it's value to 0, it's output value will be 1.

.. image:: _images/computation_structures/041_rom.png
  :width: 300
  :align: center

.. image:: _images/computation_structures/042_summary.png
  :width: 300
  :align: center


Sequential Logic
=================

In the last section we learned about building combinational circuits given a functional spec. But here is a simple device we can't build with a combinational device. When we push the button when light is off, then it turns on the light. When we push the button again, it turns on.

The device has a light which serves as the output and push button which serves as the input. The difference here with previous examples is **the device's output is NOT a function of device's input value**.

- odd number of push makes the light turn on. Even number of pushes makes the light turn off.
- The device is **remembering** whether the last push was a odd push or even push. I.e. the **state**. i.e. **the device has memory!**.
- The output was changed by an input **event** (pushing the button) rather than an input level.


.. image:: _images/computation_structures/043_pushlight.png
  :width: 300
  :align: center

- The Memory component use one or more bit's to store the current state of the system.

.. image:: _images/computation_structures/044_seq_logic.png
  :width: 300
  :align: center

.. important:: circuits that implement **memory logic** and **combinational logic** are called **sequential logic**.

How to implement memory?
-------------------------

Using capacitors
^^^^^^^^^^^^^^^^^

We have chosen voltage to encode information. We know that we can **store** voltage as charge on a capacitor.

- capacitor is a passive 2 terminal device. The terminals are connected to 2 parallel conducting plates separated by insulator. 
- Adding charge Q to one plate of the capacitor generates a voltage difference V between 2 plate terminal. 
- **Q=CV** where C is the capacitance of capacitor. When we add charge to a capacitor by hooking a plate terminal to higher voltage and this is called **charging the capacitor**.
- When we take away charge by connecting the plate terminal to a lower voltage. This is called **discharging the capacitor**.
- **Capacitor-based memory device**: One terminal will be hooked to some stable reference voltage. We will use an **NFET** switch to connect the other plate of capacitor to a  wire called the **bit-line**. Gate of the NFET switch is connected to a wire called **word-line**.
  - To write a bit into memory: drive the bit line to the desired voltage (digital 0 or 1). Then set the word-line HIGH, turning on the NFET switch. The capacitor will then charge or discharge until it has the same voltage as bit-line. At this point set the word-line LOW, turning the NFET switch and isolating the capacitor's charge on the internal plate.
  - In a perfect world the capacitors charge would remain on the capacitor's plate indefinitely.
  - Later, to access the stored info, we first charge the bit-line to some intermediate voltage. Then set the word-line HIGH, turning on the NFET switch, which connects the charge on the bit-line to charge on the capacitor.
  - The charge sharing between the bit-line and capacitor will have some small effect on the charge on the bit line and hence it's voltage.
  - If the capacitor was storing a digital 1 and hence was at a higher voltage, charge will flow from the capacitor into the bit-line, raising the voltage of the bit-line.
  - If the capacitor was storing a digital 0 and was at a lower voltage, charge will flow from the bit line into the capacitor, lowering voltage of the bit line.
  - The change in the bit-line's voltage depends on the ratio of the bit-line capacitance to see the storage capacitor's capacitance, but usually quite small.
  - Very sensitive amplifier **sense amp** is used to detect that small change and produce some legal digital voltage as the value read from memory cell.
  - Reading a writing require a lot of resource along with carefully designed analog electronics.
- Pros: Compact, low cost/bit (on big memories)
- Cons: Access times are slow, not stable due to external electrical noise, NFET switch is not perfect and there is a tiny amount of leakage current across the switch even when it's officially off. So we need to periodically refresh the memory and rewrite everything stored.  In current technologies, this has to be done every 10mins.
- In modern ICs we can fit billions of bits of storage on relatively inexpensive chips called **dynamic random access memories (DRAMS)**.
- DRAMS are very low cost per-bit storage.

.. image:: _images/computation_structures/045_capacitor_memory.png
  :width: 300
  :align: center


Using feedback
^^^^^^^^^^^^^^^^

If we set one of the invertors to digital 0, it will produce a digital 1 on it's output. The 2nd invertor will produce a digital 0 on it's output. which is connected back around the original input. this is a stable system and these digital values will be maintained, even in the presence of noise, as long as this circuitry is connected to power and ground.

If we flip the values on the 2 wires, the result is a system that has 2 stable configurations, called a **bi-stable** storage.

.. image:: _images/computation_structures/046_feedback.png
  :width: 300
  :align: center

Settable storage element (D Latch)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can use a 2-to-1 MUX to build a storage element. Output of MUX serves as the state output of the memory component.

.. image:: _images/computation_structures/047_dlatch.png
  :width: 300
  :align: center


- Output will connect to the input D0 as well.
- D1 data input is the data input of memory component.
- Select line of MUX will be the memory component's load signal, here called the gate.
- When the gate input is LOW, the MUX's output is looped back through MUX through the D0 forming the bi-stable positive feedback loop.
- Note our circuit has a cycle, so it no longer qualifies as a combinational circuit.
- When the gate's input is high, the MUX's output is determined by the value of D1 input. 
- **To load new data**: we set the gate input HIGH for long enough for the Q output to become valid and stable.
  - When G is 1, Q output follows the D input.
  - While G is high, any changes in the D input will be reflected as changes in the Q output.
  - the timing being determined by the tpd of the MUX.
  - then **we can set the gate input low to switch the memory component to memory mode**. The stable Q value is maintained indefinitely by the positive feedback loop as shown in the first 2 rows of truth table.
- This memory component is called **D-Latch (or simply latch)** 

.. image:: _images/computation_structures/048_dlatch.png
  :width: 300
  :align: center

.. important::
  - **To Load new data**: Set Gate input HIGH, Provide input on D.
  - **To Store loaded data indefinitely**: Set Gate input LOW. This will form a positive feedback loop.


(Edge-Triggered)D-Register
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In D-Latch, the time period when G is set HIGH is important. If we set it high for long, then the new state information has a chance to propagate around the loop.

**Similar to a lane of cars waiting on a tool gate**: Gate should be opened only till the first car is through and should be closed before the the car behind it comes forward.

- This is exactly the issue with D-Latch. **How do we ensure only one car makes it through the gate**?
- Solution: **Use 2 gates**.

.. image:: _images/computation_structures/049_dregister.png
  :width: 300
  :align: center

Apply the same solution on memory component.

- Use 2 back to back latches.

.. image:: _images/computation_structures/050_dregister.png
  :width: 300
  :align: center

- Sometimes this is called **FlipFlop**.

Finite State Machines
======================

.. important:: 
  - sequential logic = Combinational logic + Memory components
  - Combinational Logic: Acyclic, Can be enumerated by a 2\ :sup:`k+m` rows and k+n output columns.


In the last chapter, we developed sequential logic (co)