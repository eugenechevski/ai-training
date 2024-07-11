
# MIPS Processor Simulator in Python

class MIPSProcessor:
    def __init__(self):
        # Initialize register file with 32 32-bit registers (0-31)
        self.registers = [0] * 32

        # We'll use a dictionary to implement the ALU operations
        self.alu_ops = {
            'add': self.add,
            'sub': self.sub,
            'and': self.and_,
            'or': self.or_,
        }

    def add(self, rs, rt):
        return rs + rt

    def sub(self, rs, rt):
        return rs - rt

    def and_(self, rs, rt):
        return rs & rt

    def or_(self, rs, rt):
        return rs | rt

    def run_instruction(self, instruction):
        # MIPS instruction format: 32 bits (0x00000000)
        # Opcode: High 6 bits (bits 26-31)
        # Rs:     Bits 21-25
        # Rt:     Bits 16-20
        # Rd:     Bits 11-15
        # Shamt:  Bits 6-10 (Shift amount)
        # Funct:  Low 6 bits (bits 0-5)

        opcode = (instruction >> 26) & 0x3F
        rs = (instruction >> 21) & 0x1F
        rt = (instruction >> 16) & 0x1F
        rd = (instruction >> 11) & 0x1F
        shamt = (instruction >> 6) & 0x1F
        funct = instruction & 0x3F

        # We'll decode and simulate the relevant instructions only for simplicity.
        if opcode == 0x00 and funct == 0x20:  # ADD
            res = self.alu_ops['add'](self.registers[rs], self.registers[rt])
            self.registers[rd] = res & 0xFFFFFFFF  # 32-bit mask
        elif opcode == 0x00 and funct == 0x22:  # SUB
            res = self.alu_ops['sub'](self.registers[rs], self.registers[rt])
            self.registers[rd] = res & 0xFFFFFFFF
        elif opcode == 0x00 and funct == 0x24:  # AND
            res = self.alu_ops['and'](self.registers[rs], self.registers[rt])
            self.registers[rd] = res
        elif opcode == 0x00 and funct == 0x25:  # OR
            res = self.alu_ops['or'](self.registers[rs], self.registers[rt])
            self.registers[rd] = res
        else:
            print(f"Unsupported instruction: {hex(instruction)}")

    def load_program(self, program):
        self.program = program
        # We'll assume the program starts at address 0x00000000
        self.pc = 0

    def step(self):
        # Fetch the instruction from memory
        instruction = self.program[self.pc]
        # Print the instruction (in hexadecimal) and PC
        print(f"PC: 0x{self.pc:08x}, Instruction: 0x{instruction:08x}")
        # Execute the instruction
        self.run_instruction(instruction)
        # Increment the program counter (simulate single-step execution)
        self.pc += 1


if __name__ == "__main__":
    # Sample MIPS program: Adds two integers stored in registers $1 and $2, result in $3
    program = [
        0x2008021,  # add $1, $0, $8  (Set $1 to 33)
        0x2009042,  # add $2, $0, $9  (Set $2 to 66)
        0x00C32021,  # add $3, $1, $2  (Add $1 and $2, store in $3)
    ]

    processor = MIPSProcessor()
    # Load the program into memory
    processor.load_program(program)

    # Simulate the processor executing the program
    num_steps = len(program)
    for _ in range(num_steps):
        processor.step()
