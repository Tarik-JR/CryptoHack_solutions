cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
plaintext = "crypto{"

# Step 1: Convert to bytes
bytes_plaintext = plaintext.encode()
bytes_cipher = bytes.fromhex(cipher)

# Step 2: XOR first 7 bytes of cipher with plaintext to get key
key = bytes([c ^ p for c, p in zip(bytes_cipher[:len(bytes_plaintext)], bytes_plaintext)])

print("Recovered key:", key)

# Step 3: Decrypt the full cipher using the key (repeating as needed)
flag = bytes([c ^ key[i % len(key)] for i, c in enumerate(bytes_cipher)])

print("Decrypted flag:", flag.decode())

