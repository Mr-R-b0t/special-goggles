Simulator
This is a simple simulator that runs code in a custom assembly-like language. The simulator reads a file containing code, parses it, and executes the instructions. The code is executed by calling functions that represent each instruction.

Installation
To use this simulator, you should have Python 3 installed on your machine.

Usage
To use the simulator, create an instance of the Simulator class, passing the path to the file containing the code to be executed as a parameter:


from simulator import Simulator

simulator = Simulator("path/to/code/file")
Then, call the run method to execute the code:

simulator.run()
Language
The language used in the code files is a custom assembly-like language. It has the following instructions:

LDA: loads a value into a register
STR: stores a value into a memory location
PUSH: pushes a value onto the stack
POP: pops a value from the stack into a register
AND: performs a bitwise AND operation between two values and stores the result in a register
OR: performs a bitwise OR operation between two values and stores the result in a register
NOT: performs a bitwise NOT operation on a value and stores the result in a register
ADD: adds a value to a register
SUB: subtracts a value from a register
DIV: divides a register by a value
MUL: multiplies a register by a value
MOD: computes the remainder of a division between a value and a register and stores the result in the register
INC: increments a register
DEC: decrements a register
BEQ: jumps to a label if two values are equal
BNE: jumps to a label if two values are not equal
BBG: jumps to a label if a value is greater than another value
BSM: jumps to a label if a value is smaller than another value
JMP: jumps to a label
The language also supports labels, which are defined by placing a colon at the end of a line. Labels can be used as operands for jump instructions.

The language also supports two data sections: #DATA and #CODE. The #DATA section is used to define variables and their initial values. The #CODE section contains the code to be executed.
