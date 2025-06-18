cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
plaintext = "crypto{"  # Known part of the plaintext

# Convert known plaintext and ciphertext to bytes
bytes_plaintext = plaintext.encode('utf-8')
bytes_cipher = bytes.fromhex(cipher)

# XOR helper function
def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

# Recover part of the key using known plaintext
partial_key = xor_bytes(bytes_cipher[:len(bytes_plaintext)], bytes_plaintext)

print(f"Recovered key (partial or full): {partial_key}")

# Decrypt full ciphertext using repeating key
flag = bytes([c ^ partial_key[i % len(partial_key)] for i, c in enumerate(bytes_cipher)])

print("Decrypted flag:", flag.decode())
