class MIPSProcessor:
    def __init__(self, memory):
        self.memory = memory
        self.registers = [0 for _ in range(32)]
        self.pc = 0  # Program Counter

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def decode(self, instruction):
        opcode = (instruction >> 26) & 0x3F
        rs = (instruction >> 21) & 0x1F
        rt = (instruction >> 16) & 0x1F
        rd = (instruction >> 11) & 0x1F
        imm = instruction & 0xFFFF
        return opcode, rs, rt, rd, imm

    def execute(self, opcode, rs, rt, rd, imm):
        if opcode == 0x00:  # R-Type instructions
            if rt == 0:
                if rd == 0:
                    self.registers[rd] = 0  # add
                else:
                    self.registers[rd] = self.registers[rs]  # move
            else:
                if rd == 0:
                    self.registers[rd] = self.registers[rs] + \
                        self.registers[rt]  # add
                else:
                    self.registers[rd] = self.registers[rs] - \
                        self.registers[rt]  # sub
        elif opcode == 0x04:  # I-Type instructions
            if rt == 0:
                self.registers[rd] = imm  # addi
            else:
                self.registers[rd] = self.registers[rs] + imm  # addiu
        elif opcode == 0x08:  # J-Type instructions
            self.pc = (self.pc & 0xF0000000) | (imm << 2)

    def run(self):
        while True:
            instruction = self.fetch()
            opcode, rs, rt, rd, imm = self.decode(instruction)
            self.execute(opcode, rs, rt, rd, imm)

            # Add a break condition here to stop the execution (e.g., when a certain instruction is encountered)


# Sample Memory and Instructions
memory = [
    0x00000000,  # nop
    0x20010003,  # addi $1, $0, 3  (Set $1 to 3)
    0x00000000,  # nop
    0x01001002,  # add $2, $0, $1  (Add $1 to $0 and store in $2)
    0x20020005,  # addi $2, $0, 5  (Add 5 to $0 and store in $2)
    0x00000000,  # nop
    0x02002001,  # sub $1, $0, $2  (Subtract $2 from $0 and store in $1)
    0x08000014,  # j 0x14  (Jump to address 0x14)
    0x20020001,  # addi $2, $0, 1  (Set $2 to 1)
    0x01002002,  # add $2, $0, $2  (Add $2 to $0 and store in $2)
]

# Create the processor and run it
processor = MIPSProcessor(memory)
processor.run()

# Print the final register values
for i in range(32):
    print(f"$s{i} = {processor.registers[i]}")
