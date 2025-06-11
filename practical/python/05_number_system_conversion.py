"""
Number System Conversion in Python:

Convert numbers between:
- Decimal (base 10)
- Binary (base 2)
- Octal (base 8)
- Hexadecimal (base 16)
"""

# Decimal number
decimal_num = 42
print("Decimal:", decimal_num)

# Convert decimal to binary (string)
binary_num = bin(decimal_num)
print("Binary (bin):", binary_num)  # Output: '0b101010'

# Convert decimal to octal (string)
octal_num = oct(decimal_num)
print("Octal (oct):", octal_num)    # Output: '0o52'

# Convert decimal to hexadecimal (string)
hex_num = hex(decimal_num)
print("Hexadecimal (hex):", hex_num)  # Output: '0x2a'

# Convert binary string back to decimal
binary_str = "0b101010"
decimal_from_binary = int(binary_str, 2)
print("Decimal from binary:", decimal_from_binary)

# Convert octal string back to decimal
octal_str = "0o52"
decimal_from_octal = int(octal_str, 8)
print("Decimal from octal:", decimal_from_octal)

# Convert hex string back to decimal
hex_str = "0x2a"
decimal_from_hex = int(hex_str, 16)
print("Decimal from hex:", decimal_from_hex)
