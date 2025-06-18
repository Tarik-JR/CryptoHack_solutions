cipher = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
plaintext = "crypto{"
bytes_plaintext= plaintext.encode('utf-8')
bytes_cipher=bytes.fromhex(cipher)
key ="0"
def xor_bytes(a,b):
    results=[]
    for i,j in zip(a,b):
        xored=i^j
        results.append(xored)
    return bytes(results)
key=xor_bytes(bytes_cipher,bytes_plaintext)
key=b'\x10'

print(f"key is th following:{key}")
print(f"cipher text is the following: {bytes_cipher}")
flag=bytes([key[0]^b for b in bytes_cipher])
print(flag)
