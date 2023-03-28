from py.rom import ROM

INSTRUCTIONS_NUMBER = {
    "NOP":0b0000,
    "HALT":0b0001,
    "LDA":0b0010,
    "ADD":0b0011,
    "SUB":0b0100,
    "STA":0b0101,
    "LDI":0b0110,
    "JMP":0b0111,
    "JC":0b1000,
    "JZ":0b1001,
    "OUT":0b1010
}

PROGRAM = [
    "OUT",
    "ADD",
    "JC",
    "JMP",
    "SUB",
    "OUT",
    "JZ",
    "JMP",
    "NOP",
    "NOP",
    "NOP",
    "NOP",
    "NOP",
    "NOP",
    "NOP",
    "NOP"
]

ADDRS = [
    0,
    15,
    4,
    0,
    15,
    0,
    4,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

def decimal_to_binary(decimal):
    return bin(decimal)[2:].zfill(4)

def hexFormat(number):
    return hex(number).replace("0x", "").zfill(2)



def generate_code_in_hex():
    code_in_hex = []
    for index, instruc in enumerate(PROGRAM):
        binary_instruc = decimal_to_binary(int(INSTRUCTIONS_NUMBER[instruc]))
        binary_addr = decimal_to_binary(ADDRS[index])
        data = hexFormat(int(f"{binary_instruc}{binary_addr}", 2))
        code_in_hex.append(data)
    return code_in_hex

code_in_hex = generate_code_in_hex()

def generate_addr_in_hex():
    addr_cod_in_hex = {}
    for _ in range(0, 16):
        addr_mask = ["0" for _ in range(0,16)]
        addr_mask[_] = "1"
        binary_addr = "".join(addr_mask)[::-1]
        addr_cod_in_hex[binary_addr] = code_in_hex[_]
    return addr_cod_in_hex

def generate_ROM_program(ADDR_COD_IN_HEX):
    for addr in ADDR_COD_IN_HEX:
        #print(f"{addr} {ADDR_COD_IN_HEX[addr]}")
        myROM.in_ROM_addr_write(int(addr, 2), ADDR_COD_IN_HEX[addr])

ADDR_COD_IN_HEX = generate_addr_in_hex()
myROM = ROM(size=0xfff0, step=16, data_sizes=2)
myROM.init_empty_ROM()

generate_ROM_program(ADDR_COD_IN_HEX)
myROM.save_into_file("test_ram")
#print(myROM)
