Code Reverse Engineering Project
================================

This is a project involving reverse engineering of a self-playing chessboard's atmega2560 firmware from a lost source. The firmware .hex file was dumped using `avrdude` and the raw .hex files were then converted into a disassembled format.

Steps Involved
--------------

Here is the sequence of actions we undertook for this project:

1.  Dumping the flash memory using `avrdude`.
2.  Converting and reading the raw .hex to a preliminary disassembled .dump format.
3.  Carrying out a full disassembly into assembly code.

Detailed Procedure
------------------

### 1\. AVR Memory Dump with `avrdude`

Following the loss of the source code, we had to retrieve the firmware burnt onto the atmega2560's flash memory using `avrdude`.


### 2\. Preliminary Disassembly of .hex file

The raw .hex file was processed by `avr-objdump` to interpret it as binary data for the AVR6 architecture.

Here is the command we used:

```bash
avr-objdump -s -m avr6 ~/readfile.hex > readfile.dump
```

They `-s` flag with `avr-objdump` helps to display the full contents of the specified sections. The output consists of memory addresses along with their corresponding values.

We observed a specific char array string literal from the resultant `readfile.dump`. However, it is still unclear if this literal means that the code has been properly disassembled.

### 3\. Full Disassembly into Assembly Language

Following the initial disassembly, we then carried out a full disassembly and translated the .hex file into Assembly language.

The command we used was:

```bash
avr-objdump -j .sec1 -d -m avr6 ~/readfile.hex > dissasembled.dump
```

In the command, `-d` invokes the disassemble mode, `-j .sec1` specifies the section we wished to disassemble, `-m avr6` while defines the architecture. The output consists of disassembled Assembly language code that gets written to `dissasembled.dump`.

Current Progress
----------------

While `dissasembled.dump` contains the disassembled code, parsing and understanding it has been challenging. To recreate the original C/C++ Arduino code equivalent to the assembly instructions, our next steps will involve mapping the instructions back to their higher-level constructs.

We'd appreciate any contribution that aids in understanding the disassembled instructions, translating them back into high-level language, or advancing the interpretation techniques. Any suggestions or questions are also most welcome.

