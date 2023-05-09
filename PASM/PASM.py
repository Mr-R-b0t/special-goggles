class Simulator:
    def __init__(self):
        self.pc = 0
        self.stack = []
        self.memory = {"LABELS": {}, "CODE": []}
        self.registers = {"T0": 0, "T1": 0, "T2": 0, "T3": 0}

        in_data_block = True

        for line in open(f"snippets/{input('Enter file name: ')}.pasm"):
            line = line.upper().strip()

            if line == "#CODE":
                in_data_block = False
                continue

            if len(line) == 0 or line[0] == '!' or line[0] == '#':
                continue

            if in_data_block:
                name, value = line.split()
                self.memory[name] = int(value)
                continue

            if ':' in line:
                label = line[:-1]
                self.memory["LABELS"][label] = len(self.memory["CODE"])
            else:
                self.memory["CODE"].append(line)


    def get(self, value):
        return self.registers.get(value) or self.memory.get(value) or int(value)

    def step(self):
        instruction = self.memory["CODE"][self.pc]
        print(f"Current step: {instruction} ({self.pc})")

        print("Registers:", end=" ")
        print(self.registers)

        print("Stack:", end=" ")
        print(self.stack)

        print("Memory:", end=" ")
        print({k: v for k,v in self.memory.items() if k not in ["LABELS", "CODE"]})

        if instruction == "HLT":
            exit(0)

        opcode, operands = instruction.split(" ", 1)
        getattr(self, opcode, Simulator.NOT_FOUND)(operands)

        self.pc += 1


    def LDA(self, operands):
        reg, value = operands.split()
        self.registers[reg] = self.get(value)

    def STR(self, operands):
        var, value = operands.split()
        self.memory[var] = self.get(value)
    
    def PUSH(self, operands):
        if len(self.stack) > 4096:
            raise IndexError("Stack size is limited to 4096 bytes")

        self.stack.append(
            self.get(operands.strip())
        )

    def POP(self, operands):
        reg = operands.strip()
        self.registers[reg] = self.stack.pop()

    def AND(self, operands):
        reg, value = operands.split()
        self.registers[reg] &= self.get(value)

    def OR(self, operands):
        reg, value = operands.split()
        self.registers[reg] |= self.get(value)

    def NOT(self, operands):
        reg = operands.strip()
        self.registers[reg] = ~self.registers[reg]
    
    def ADD(self, operands):
        reg, value = operands.split()
        self.registers[reg] += self.get(value)
    
    def SUB(self, operands):
        reg, value = operands.split()
        self.registers[reg] = self.get(value) - self.registers[reg]
            
    def DIV(self, operands):
        reg, value = operands.split()
        self.registers[reg] //= self.get(value)
    
    def MUL(self, operands):
        reg, value = operands.split()
        self.registers[reg] *= self.get(value) 

    def MOD(self, operands):
        reg, value = operands.split()
        self.registers[reg] = self.get(value) % self.registers[reg]

    def INC(self, operands):
        reg = operands.strip()
        self.registers[reg] += 1
    
    def DEC(self, operands):
        reg = operands.strip()
        self.registers[reg] -= 1

    def BNE(self, operands):
        value1, value2, label = operands.split()
        
        if self.get(value1) != self.get(value2):
            self.pc = self.memory["LABELS"][label] - 1
        
    def BEQ(self, operands):
        value1, value2, label = operands.split()

        if self.get(value1) == self.get(value2):
            self.pc = self.memory["LABELS"][label] - 1
    
    def BBG(self, operands):
        value1, value2, label = operands.split()

        if self.get(value1) > self.get(value2):
            self.pc = self.memory["LABELS"][label] - 1

    def BSM(self, operands):
        value1, value2, label = operands.split()
                
        if self.get(value1) < self.get(value2):
            self.pc = self.memory["LABELS"][label] - 1

    def JMP(self, operands):
        label = operands.strip()
        self.pc = self.memory["LABELS"][label] - 1

    @staticmethod
    def NOT_FOUND(_):
        raise NotImplementedError("Instruction not found")

    @staticmethod
    def run():
        sim = Simulator()
        step_by_step = input("Step by step? (y/n): ") == "y"

        while True:
            sim.step()

            if step_by_step:
                input("Press enter for next step...")

            print()


if __name__ == "__main__":
    Simulator.run()
