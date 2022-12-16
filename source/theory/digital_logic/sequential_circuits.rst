=======================
Sequential Circuits
=======================

https://www.youtube.com/watch?v=oL0gpFjpJno&list=PLAoF4o7zqskSKR4JG_MZ67EnqTS6khWmE&index=131

Flipflop:
 - A flip-flop can store one bit(0/1).
 - D - flip-flop stores the bit provided on the D0 input.

Registers: 
 - A number of flip-flops grouped together on a single device called register.
 - if 4 flip-flops, then it is a 4-bit register.
 - Operations performed on a register is called micro operations. i.e. simple elementary operation.
 - In SRAM, the RAM cells are basically D-type flip-flops, so to understand RAM cells, you need to understand D flip-flops.

RAM:
 - RAM can simply be thought (not exactly, especially DRAMs) of as an array of registers.

WORD:
 - We call the data stored by a single register a word. 

Indexing and Address Inputs
 - In general, we can use N bits to index 2N numbers.
 - We want to activate the index 3 register only if the four address bits A3, A2, A1, A0) form a 3, i.e. 0011 in binary. A3 = 0, A2 = 0, A1 = 1, and A0 = 1.
 - 

DRAM and SRAM

RAM is actually classifiable into two main categories: DRAM and SRAM. DRAM stands for Dynamic RAM, and SRAM stands for Static RAM.

SRAM: D flip-flops(D flip-flop, which requires 6 transistors) as the storage mechanism
- does not require continuous refreshing, which is why it’s referred to as “static”
- Of course, you still need to maintain power to the SRAM, otherwise the flip-flop will lose its data.
DRAM: 
- Do not use flip-flops. Does not use D flip-flops, but instead uses a transistor and a capacitor to store data, using the charge on the capacitor to indicate a 0 or 1.
- Using a capacitor means that the data is stored only for a short period of time. If we are using DRAM, the CPU needs to continuously cycle through and “refresh”. this is where the “dynamic” portion of the DRAM name comes from.
- DRAM cell is built with 1 transistor and 1 capacitor,

Cost and density: DRAM is cheaper and more compact than SRAM, so it is available in larger quantities for the same price and space requirements.
Speed: SRAM is faster than DRAM, since it doesn’t need to keep being refreshed.
Power: SRAM takes less power than DRAM, also due to not needing to be refreshed. The ambient power requirement of the D flip-flop is significantly less than the capacitor-transistor pair.

As such, SRAM is faster, but it’s less cost efficient and harder to obtain. In modern computers targeted towards consumers, SRAM is integrated into the CPU and is available in quantities of around 8 MB. DRAM is the sort of “RAM sticks” that people use when building PCs, and they’re typically present in quantities of 4 – 32 GB, around 1000x more than SRAM.

Scaling Up

a C++ short stores 2 bytes, stores a number from -128 to 127, or 0 to 255


Control Unit
=============

The component which generates control signals for different purposes.

- after selecting a certain memory location through the address bus, and the address decoder h/w, what should we do with the memory? a read or a write? control signal decides that.
- should I make one I/O port for the input or for the output?
- should I make this data path enabled?
