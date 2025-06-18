string = "label"#our string
key = 13  # our key
list5 = []
key_Binary = format(key, '08b')  #chaneg to binary without 0b (raw binary)
# Convert string to binary
for i in string:
    list5.append(format(ord(i), '08b'))

# XOR process
for i in range(len(list5)):
    xor_result = int(list5[i], 2) ^ int(key_Binary, 2)
    list5[i] = format(xor_result, '08b')

# Convert the binary list back to ASCII
def binary_to_ascii(binary_list):
    binary_string = ''.join(binary_list)
    ascii_chars = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]
    return ''.join(ascii_chars)

# Decode the XORed binary back to string
ascii_result = binary_to_ascii(list5)
print("Decoded ASCII string after XOR:", ascii_result)

