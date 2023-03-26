class ROM:
    def __init__(self):
        self.tittle = "v3.0 hex words addressed\n"
        self.ROM = {}

    def generate_empty_ROM(self, size=0x1f8, step=8, data_sizes=5, columns=8):
        for addr in range(0, size+1, step):
            addr = hex(addr).replace("0x", "")
            formatedAddr = "0"*(3-len(addr))+addr
            self.ROM[formatedAddr] = ["0"*data_sizes for _ in range(columns)]
        return self.ROM

    def write_ROM_in_addr(self, tarjet_addr, data: str):
        addr_counter = 0
        for rom_addr in self.ROM:
            for index, line in enumerate(self.ROM[rom_addr]):
                if tarjet_addr == addr_counter:
                    self.ROM[rom_addr][index] = data
                addr_counter += 1

    def rom_to_text(self):
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