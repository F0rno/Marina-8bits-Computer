from itertools import product
from el_limbo.romtools import *
from rom_class import InstruccionsRom

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
    [CO|MI, CE|RO|II,     0,     0, 0, 0, 0, 0], # 0000 NOP
    [CO|MI, CE|RO|II,    HL,     0, 0, 0, 0, 0], # 0001 HALT
    [CO|MI, CE|RO|II, IO|MI, RO|AI, 0, 0, 0, 0], # 0010 LDA [ADDR]
    [CO|MI, CE|RO|II, IO|MI, RO|BI, EO|AI, 0, 0, 0], # 0011 ADD [ADDR]
    [CO|MI, CE|RO|II, AO|OI,     0,     0, 0, 0, 0], # 0100 OUTA
    [CO|MI, CE|RO|II, 0, 0, 0, 0, 0, 0], # STA [ADDR]
    [CO|MI, CE|RO|II, 0, 0, 0, 0, 0, 0], # SUB [ADDR]
    [CO|MI, CE|RO|II, 0, 0, 0, 0, 0, 0], # JMP [ADDR]
    [CO|MI, CE|RO|II, 0, 0, 0, 0, 0, 0], # JPZ [ADDR]
    [CO|MI, CE|RO|II, 0, 0, 0, 0, 0, 0], # JPZ [ADDR]
    [CO|MI, CE|RO|II, 0, 0, 0, 0, 0, 0], # JPZ [ADDR]
    [CO|MI, CE|RO|II, 0, 0, 0, 0, 0, 0], # JPC [ADDR]
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
    0b1011:8
}

CODES_FOR_ROM = {}

def decimal_to_binary(decimal):
    return bin(decimal)[2:].zfill(3)

def generate_addr_instruccions_codes():
    # steps zf cf instruc_addr
    return_dic = {}
    for addr in INSTRUCTIONS_NUMBER:
        for flags_combination in product(["0", "1"], repeat=2):
            for step in range(0, INSTRUCTIONS_NUMBER[addr]):
                binary_step = str(decimal_to_binary(step))
                binary_addr = bin(addr).replace("0b", "").zfill(4)
                rom_addr = hex(int(f"{binary_addr}{''.join(flags_combination)}{binary_step}", 2)).replace("0x", "")
                #rom_addr = f"{binary_addr} {''.join(flags_combination)} {binary_step}"
                #if binary_addr == bin(0b0001).replace("0b", "").zfill(4):
                #print(rom_addr, hex(INSTRUCTIONS_MICRO_CODES[int(binary_addr,2)][int(binary_step,2)]).replace("0x", "").zfill(5))
                return_dic[rom_addr] = hex(INSTRUCTIONS_MICRO_CODES[int(binary_addr,2)][int(binary_step,2)]).replace("0x", "").zfill(5)
    return return_dic

def generate_my_ROM(instructions):
    myROM = InstruccionsRom()
    myROM.generate_empty_ROM()
    for addr_instruc in instructions:
        #print(int(addr_instruc, 16), instructions[addr_instruc])
        myROM.write_ROM_in_addr(int(addr_instruc, 16), instructions[addr_instruc])
    myROM.save_into_file()
    return myROM.rom_to_text()

INSTRUCTIONS_ADDR = generate_addr_instruccions_codes()

ROM = generate_my_ROM(INSTRUCTIONS_ADDR)

"""
for i in instructions:
    if instructions[i] != "0":
        print(f"{i} {instructions[i]}")
·"""
#ROM = generate_my_ROM(instructions)
#print(ROM)

"""
with open("mi_rom", "wb") as f:
    f.write("v3.0 hex words addressed\n".encode("utf-8"))
    for addr in range(0, 0x1f8+1, 8):
        addr = hex(addr).replace("0x", "")
        formatedAddr = "0"*(3-len(addr))+addr
        f.write(f"{formatedAddr}: 00000 00000 00000 00000 00000 00000 00000 00000\n".encode("utf-8"))
"""

"""
def read_ROM():
    with open("mi_rom", "r") as f:
        lines = f.readlines()[1:]
    return lines

def write_ROM_in_addr(tarjet_addr, data):
    addr_counter = 0
    rom_content = read_ROM()
    for line in rom_content:
        for index, addres in enumerate(line.split(" ")[1:]):
            #print(addr_counter)
            if addr_counter == tarjet_addr:
                line[index] = data
            addr_counter += 1
    print()
"""
"""
write_ROM_in_addr(0x3, 11111)

# Write 11111, in address 3
#000: 00000 00000 11111 00000 00000 00000 00000 00000
#008: 00000 00000 00000 00000 00000 00000 00000 00000
"""
"""
for addr in range(0, 0x1f8+1, 8):
    addr = hex(addr)
    formatedAddr = "0"*(3-len(addr.replace("0x", "")))+addr.replace("0x", "")

"""
"""

"""
"""
print("v3.0 hex words addressed")
for addr in range(0, 0x1f8+1, 8):
    addr = hex(addr).replace("0x", "")
    formatedAddr = "0"*(3-len(addr))+addr
    print(f"{formatedAddr}: 00000 00000 00000 00000 00000 00000 00000 00000")
"""