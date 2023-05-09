# Python Custom Assembly Simulator

This is a simple simulator that runs code in a custom assembly-like language. The simulator reads a file containing code, parses it, and executes the instructions. To use it, you should have Python 3 installed on your machine.

## Usage

To use the simulator, call `Simulator.run()`, the code will then :
- Ask for the name of the file containing the code to be executed (eg. `v1` for `snippets/v1.pasm`)
- Ask if you want to run the code step by step or all at once

```py
from simulator import Simulator

if __name__ == "__main__":
    Simulator.run()
```

## Language

The language used in the code files is a custom assembly-like language. It has the following instructions:

- `LDA`: loads a value into a register
- `STR`: stores a value into a memory location
- `PUSH`: pushes a value onto the stack
- `POP`: pops a value from the stack into a register
- `AND`: performs a bitwise AND operation between two values and stores the result in a register
- `OR`: performs a bitwise OR operation between two values and stores the result in a register
- `NOT`: performs a bitwise NOT operation on a value and stores the result in a register
- `ADD`: adds a value to a register
- `SUB`: subtracts a value from a register
- `DIV`: divides a register by a value
- `MUL`: multiplies a register by a value
- `MOD`: computes the remainder of a division between a value and a register and stores the result in the register
- `INC`: increments a register
- `DEC`: decrements a register
- `BEQ`: jumps to a label if two values are equal
- `BNE`: jumps to a label if two values are not equal
- `BBG`: jumps to a label if a value is greater than another value
- `BSM`: jumps to a label if a value is smaller than another value
- `JMP`: jumps to a label

The code is split into two sections:
- The data section (`#DATA`), which contains the variables and their initial values
- The code section (`#CODE`), which contains the instructions to be executed
