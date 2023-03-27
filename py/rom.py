class ROM:
    def __init__(self, header="v3.0 hex words addressed\n", size=0x1f8, step=8, data_sizes=5):
        self.tittle = header
        self.size = size
        self.step = step
        self.data_sizes = data_sizes
        self.columns = step
        self.zfillForAddr = len(hex(self.size).replace("0x", ""))
        self.ROM = {}

    def init_empty_ROM(self):
        for addr in range(0, self.size+1, self.step):
            addr = hex(addr).replace("0x", "")
            formatedAddr = addr.zfill(self.zfillForAddr)
            self.ROM[formatedAddr] = ["0"*self.data_sizes for _ in range(self.columns)]
        return self.ROM

    def in_ROM_addr_write(self, tarjet_addr, data: str) -> bool:
        if len(self.ROM) == 0:
            self.init_empty_ROM()
        addr_counter = 0
        for rom_addr in self.ROM:
            for index, line in enumerate(self.ROM[rom_addr]):
                if tarjet_addr == addr_counter:
                    self.ROM[rom_addr][index] = data
                    return True
                addr_counter += 1
        return False

    def rom_to_text(self) -> str:
        return_text = ""
        return_text += self.tittle
        for addr_data_line in self.ROM:
            data_line = " ".join(self.ROM[addr_data_line])
            return_text += f"{addr_data_line}: {data_line}\n"
        return_text = return_text[:-1]
        return return_text

    def save_into_file(self, name="mi_rom"):
        with open(name, "wb") as f:
            f.write(self.rom_to_text().encode("utf-8"))

    def __str__(self) -> str:
        return self.rom_to_text()
    

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
        for rom_addr in self.ROM:
            for index, line in enumerate(self.ROM[rom_addr]):
                if tarjet_addr == addr_counter:
                    self.ROM[rom_addr][index] = data
                    return True
                addr_counter += 1
        return False

    def rom_to_text(self) -> str:
        return_text = ""
        return_text += self.tittle
        for addr_data_line in self.ROM:
            data_line = " ".join(self.ROM[addr_data_line])
            return_text += f"{addr_data_line}: {data_line}\n"
        return_text = return_text[:-1]
        return return_text

    def save_into_file(self, name="mi_rom"):
        with open(name, "wb") as f:
            f.write(self.rom_to_text().encode("utf-8"))

    def __str__(self) -> str:
        return self.rom_to_text()
"""