import re
import argparse

def hex_to_ascii(hex_values):
    ascii_str = ""
    for hex_value in hex_values:
        if hex_value == 0x00:
            ascii_str += "\\0"  # Represent null character as \0
        else:
            ascii_str += chr(hex_value)
    return ascii_str

def read_asm_flash_dump(file_path, start_address, end_address):
    hex_values = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        capture = False
        for line in lines:
            addr_match = re.search(r'([0-9a-fA-F]+):', line)
            if addr_match:
                addr = int(addr_match.group(1), 16)
                if addr == start_address:
                    capture = True
                if addr == end_address:
                    break
            if capture:
                hex_match = re.findall(r'([0-9a-fA-F]{2})\s', line)
                hex_values.extend([int(x, 16) for x in hex_match])
    return hex_values

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a section of an ASM flash dump to ASCII.')
    parser.add_argument('file_path', type=str, help='Path to the ASM flash dump file')
    parser.add_argument('start_address', type=lambda x: int(x, 0), help='Starting address (hex) of the section to convert')
    parser.add_argument('end_address', type=lambda x: int(x, 0), help='Ending address (hex) of the section to convert')

    args = parser.parse_args()

    hex_values = read_asm_flash_dump(args.file_path, args.start_address, args.end_address)
    ascii_str = hex_to_ascii(hex_values)
    print(f"ASCII string: {ascii_str}")
