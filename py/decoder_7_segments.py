from rom import ROM

#      a, b, c, d, e, f, g
INT_TO_7_SEGMENTS = {
    0:[1, 1, 1, 1, 1, 1, 0],
    1:[0, 1, 1, 0, 0, 0, 0],
    2:[1, 1, 0, 1, 1, 0, 1],
    3:[1, 1, 1, 1, 0, 0, 1],
    4:[0, 1, 1, 0, 0, 1, 1],
    5:[1, 0, 1, 1, 0, 1, 1],
    6:[1, 0, 1, 1, 1, 1, 1],
    7:[1, 1, 1, 0, 0, 0, 0],
    8:[1, 1, 1, 1, 1, 1, 1],
    9:[1, 1, 1, 1, 0, 1, 1]
}

def decimal_to_binary(decimal):
    return bin(decimal)[2:].zfill(8)

def hexFormat(number):
    return hex(int(number, 2)).replace("0x", "").zfill(6)

def generate_addr_segments_codes():
    addr_segments = {}
    for addr in range(0, 255+1):
        binary_addr = hexFormat(decimal_to_binary(addr))
        string_addr = str(addr).zfill(6)
        # For each digit of 000 to 255, we take the parts (0 0 0, 2 5 5) 
        # and converts that into the 7_SEGMENTS code
        digit_1 = "".join([str(segment_decode) for segment_decode in INT_TO_7_SEGMENTS[int(string_addr[3])]])[::-1]
        digit_2 = "".join([str(segment_decode) for segment_decode in INT_TO_7_SEGMENTS[int(string_addr[4])]])[::-1]
        digit_3 = "".join([str(segment_decode) for segment_decode in INT_TO_7_SEGMENTS[int(string_addr[5])]])[::-1]
        segment_hexcodes = hexFormat(f"{digit_3}{digit_2}{digit_1}")
        addr_segments[binary_addr] = segment_hexcodes
    return addr_segments

addr_7_segments_hexcode = generate_addr_segments_codes()
myROM = ROM(size=0xf8, data_sizes=6)

for addr_hexcode in addr_7_segments_hexcode:
    myROM.in_ROM_addr_write(int(addr_hexcode, 16), addr_7_segments_hexcode[addr_hexcode])

print(myROM)
myROM.save_into_file("decoder_8bits_to_7_segments_ROM")