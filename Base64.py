
import base64

string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytess = bytes.fromhex(string)
key = base64.b64encode(bytess)
print(key.decode())  # <-- decode from bytes to string

