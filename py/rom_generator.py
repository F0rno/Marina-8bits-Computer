from itertools import product
from rom import ROM

HL = 0b10000000000000000
CE = 0b01000000000000000
CO = 0b00100000000000000
JP = 0b00010000000000000
AI = 0b00001000000000000
AO = 0b00000100000000000
EO = 0b00000010000000000
SU = 0b00000001000000000
BI = 0b00000000100000000
BO = 0b00000000010000000
FI = 0b00000000001000000
MI = 0b00000000000100000
RI = 0b00000000000010000
RO = 0b00000000000001000
II = 0b00000000000000100
IO = 0b00000000000000010
OI = 0b00000000000000001

#HL	CE	CO	JP	AI	AO	EO	SU	BI	BO	FI	MI	RI	RO	II	IO	OI

INSTRUCTIONS_MICRO_CODES = [
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0], # 0000 NOP
    [CO|MI, CE|RO|II,    HL,     0,           0, 0, 0, 0], # 0001 HALT
    [CO|MI, CE|RO|II, IO|MI, RO|AI,           0, 0, 0, 0], # 0010 LDA 
    [CO|MI, CE|RO|II, IO|MI, RO|BI,    EO|AI|FI, 0, 0, 0], # 0011 ADD 
    [CO|MI, CE|RO|II, MI|IO, BI|RO, AI|EO|SU|FI, 0, 0, 0], # 0100 SUB
    [CO|MI, CE|RO|II, MI|IO, AO|RI,           0, 0, 0, 0], # 0101 STA
    [CO|MI, CE|RO|II, AI|IO,     0,           0, 0, 0, 0], # 0110 LDI
    [CO|MI, CE|RO|II, JP|IO,     0,           0, 0, 0, 0], # 0111 JMP
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0], # 1000 JC
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0], # 1001 JZ
    [CO|MI, CE|RO|II, AO|OI,     0,           0, 0, 0, 0], # 1010 OUT
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0], # 1011
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0], # 1100
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0], # 1101
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0], # 1110
    [CO|MI, CE|RO|II,     0,     0,           0, 0, 0, 0]  # 1111
]

INSTRUCTIONS_NUMBER = {
    0b0000:8,
    0b0001:8,
    0b0010:8,
    0b0011:8,
    0b0100:8,
    0b0101:8,
    0b0110:8,
    0b0111:8,
    0b1000:8,
    0b1001:8,
    0b1010:8,
    0b1011:8,
    0b1100:8,
    0b1101:8,
    0b1110:8,
    0b1111:8
}

FLAG_JC = bin(0b1000).replace("0b", "").zfill(4)
FLAG_JZ = bin(0b1001).replace("0b", "").zfill(4)

CODES_FOR_ROM = {}

def decimal_to_binary(decimal):
    return bin(decimal)[2:].zfill(3)

def hexFormat(number):
    return hex(number).replace("0x", "").zfill(5)

def generate_addr_instruccions_codes():
    addr_instructions = {}
    for addr in INSTRUCTIONS_NUMBER:
        for flags_combination in product(["0", "1"], repeat=2):
            for step in range(0, INSTRUCTIONS_NUMBER[addr]):
                binary_step = str(decimal_to_binary(step))
                binary_addr = bin(addr).replace("0b", "").zfill(4)
                rom_addr = hexFormat(int(f"{binary_addr}{''.join(flags_combination)}{binary_step}", 2))
                # Depending on the value of the flags we change the microcodes of the instruction to make the jump
                if FLAG_JC == binary_addr and step == 2 and flags_combination[0] == "1":
                    instruction_hex_code = hexFormat(JP|IO)
                    addr_instructions[rom_addr] = instruction_hex_code
                elif FLAG_JZ == binary_addr and step == 2 and flags_combination[1] == "1":
                    instruction_hex_code = hexFormat(JP|IO)
                    addr_instructions[rom_addr] = instruction_hex_code
                else:
                    instruction_hex_code = hexFormat(INSTRUCTIONS_MICRO_CODES[int(binary_addr,2)][int(binary_step,2)])
                    addr_instructions[rom_addr] = instruction_hex_code
    return addr_instructions

def generate_my_ROM(instructions):
    myROM = ROM()
    myROM.init_empty_ROM()
    for addr_instruc in instructions:
        myROM.in_ROM_addr_write(int(addr_instruc, 16), instructions[addr_instruc])
    myROM.save_into_file()
    return myROM.rom_to_text()

if __name__ == "__main__":
    ADDRS_INSTRUCTIONS = generate_addr_instruccions_codes()
    ROM = generate_my_ROM(ADDRS_INSTRUCTIONS)
    print(ROM)