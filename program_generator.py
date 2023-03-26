from rom_class import InstruccionsRom

myROM = InstruccionsRom()
myROM.generate_empty_ROM(0xff0, 4, 2, 16)
myROM.write_ROM_in_addr(0, "00")
myROM.write_ROM_in_addr(1, "01")
myROM.write_ROM_in_addr(2, "11")
myROM.write_ROM_in_addr(3, "10")
print(myROM)
myROM.save_into_file("sum")