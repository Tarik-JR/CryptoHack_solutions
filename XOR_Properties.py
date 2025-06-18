KEY1 ="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2XORk3="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGxorKEY1xorKEY3xorKEY2="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY1_Bytes=bytes.fromhex(KEY1)
k2XORk3_Bytes=bytes.fromhex(k2XORk3)
FLAGxorKEY1xorKEY3xorKEY2_Bytes=bytes.fromhex(FLAGxorKEY1xorKEY3xorKEY2)

def XOR_bytes(a,b):
    results= []
    for x,y in zip(a,b):
        results.append(x^y)
    return bytes(results)

d=XOR_bytes(KEY1,k2XORk3)
rr=XOR_bytes(d^FLAGxorKEY1xorKEY3xorKEY2)
print(rr)
