global addr_counter
addr_counter = 0

def generate_empty_ROM():
    def write_empty_ROM():
        global addr_counter
        return_ROM = ""
        line_templade = "00000 00000 00000 00000 00000 00000 00000 00000"
        return_ROM += line_templade
        return_ROM += "\n"
        return return_ROM
    ROM = ""
    ROM += "v3.0 hex words addressed\n"
    for addr in range(0, 0x1f8+1, 8):
        addr = hex(addr).replace("0x", "")
        formatedAddr = "0"*(3-len(addr))+addr
        ROM += f"{formatedAddr}: "
        ROM += write_empty_ROM()
    ROM = ROM[:-1]    
    return ROM

def write_ROM_in_addr(ROM, tarjet_addr, data):

    def make_ROM_with_templade(list_data_lines):
        ROM = ""
        ROM += "v3.0 hex words addressed\n"
        for addr in range(0, 0x1f8+1, 8):
            bytes_line = "".join(list_data_lines[round(addr/8)])
            addr = hex(addr).replace("0x", "")
            formatedAddr = "0"*(3-len(addr))+addr
            ROM += f"{formatedAddr}: {bytes_line}\n"
        ROM = ROM[:-1]
        return ROM

    global addr_counter
    addr_counter = 0
    addr_data_lines = ROM.split("\n")[1:]
    data_lines = ["".join(line[5:]) for line in addr_data_lines]
    list_data_lines = [byte_of_line.split(" ") for byte_of_line in data_lines]
    for line_index, line in enumerate(list_data_lines):
        for byte_index, write_byte in enumerate(line):
            if addr_counter == int(tarjet_addr, 16):
                list_data_lines[line_index][byte_index] = f"{data} "
            else:
                list_data_lines[line_index][byte_index] = f"{write_byte} "
            addr_counter += 1
    return make_ROM_with_templade(list_data_lines)

"""
class ROM:
    def __init__(self, head="v3.0 hex words addressed\n"):
        self.tittle = head
        self.ROM = {}

    def init_empty_ROM(self, size=0x1f8, step=8, data_sizes=5, columns=8):
        for addr in range(0, size+1, step):
            addr = hex(addr).replace("0x", "")
            formatedAddr = "0"*(3-len(addr))+addr
            self.ROM[formatedAddr] = ["0"*data_sizes for _ in range(columns)]
        return self.ROM

    def in_ROM_addr_write(self, tarjet_addr, data: str) -> bool:
        addr_counter = 0
        firs_item_of_row_counter = 0
        for rom_addr in self.ROM:    
            addr_counter += 8
            if tarjet_addr < addr_counter:
                if tarjet_addr == 0:
                    self.ROM[rom_addr][tarjet_addr] = data
                else:
                    self.ROM[rom_addr][tarjet_addr-firs_item_of_row_counter-1] = data
                return True
            elif tarjet_addr == addr_counter:
                self.ROM[rom_addr][-1] = data
                return True
            firs_item_of_row_counter += 8
        return False

    def rom_to_text(self) -> str:
        return_text = ""
        return_text += self.tittle
        for addr_data_line in self.ROM:
            data_line = " ".join(self.ROM[addr_data_line])
            return_text += f"{addr_data_line}: {data_line}\n"
        return_text = return_text[:-1]
        return return_text

    def save_into_file(self, name="mi_rom") -> None:
        with open(name, "wb") as f:
            f.write(self.rom_to_text().encode("utf-8"))

    def __str__(self) -> str:
        return self.rom_to_text()
"""
"""
ROM = generate_empty_ROM()
ROM = write_ROM_in_addr(ROM, 511, "11111")
ROM = write_ROM_in_addr(ROM, 1, "11111")
ROM = write_ROM_in_addr(ROM, 13, "11111")
print(ROM)
"""
"""
global addr_counter
addr_counter = 0

def write_empty_ROM():
    global addr_counter
    return_ROM = ""
    line_templade = "00000 00000 00000 00000 00000 00000 00000 00000"
    return_ROM += line_templade
    return_ROM += "\n"
    return return_ROM

def generate_empty_ROM():
    ROM = ""
    ROM += "v3.0 hex words addressed\n"
    for addr in range(0, 0x1f8+1, 8):
        addr = hex(addr).replace("0x", "")
        formatedAddr = "0"*(3-len(addr))+addr
        ROM += f"{formatedAddr}: "
        ROM += write_empty_ROM()
    ROM = ROM[:-1]    
    return ROM

def write_ROM_in_addr(ROM, tarjet_addr, data):

    def make_ROM_with_templade(list_data_lines):
        ROM = ""
        ROM += "v3.0 hex words addressed\n"
        for addr in range(0, 0x1f8+1, 8):
            bytes_line = "".join(list_data_lines[round(addr/8)])
            addr = hex(addr).replace("0x", "")
            formatedAddr = "0"*(3-len(addr))+addr
            ROM += f"{formatedAddr}: {bytes_line}\n"
        ROM = ROM[:-1]
        return ROM

    global addr_counter
    addr_counter = 0
    addr_data_lines = ROM.split("\n")[1:]
    data_lines = ["".join(line[5:]) for line in addr_data_lines]
    list_data_lines = [byte_of_line.split(" ") for byte_of_line in data_lines]
    for line_index, line in enumerate(list_data_lines):
        for byte_index, write_byte in enumerate(line):
            if addr_counter == tarjet_addr:
                list_data_lines[line_index][byte_index] = f"{data} "
            else:
                list_data_lines[line_index][byte_index] = f"{write_byte} "
            addr_counter += 1
    return make_ROM_with_templade(list_data_lines)

ROM = generate_empty_ROM()
print(ROM)
ROM = write_ROM_in_addr(ROM, 511, "11111")
ROM = write_ROM_in_addr(ROM, 0, "11111")
print(ROM)
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
print("v3.0 hex words addressed")
for addr in range(0, 0x1f8+1, 8):
    addr = hex(addr).replace("0x", "")
    formatedAddr = "0"*(3-len(addr))+addr
    print(f"{formatedAddr}: 00000 00000 00000 00000 00000 00000 00000 00000")
"""