from rom import ROM


myROM = ROM()
myROM.generate_empty_ROM(0xfff0, 4, 2, 16)

#myROM.save_into_file("sum")