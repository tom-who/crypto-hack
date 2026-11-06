from Crypto.Util.number import *

hidden = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
text = [byte for byte in bytes.fromhex(hidden)]
# maximum number of completely random bytes is 256.

def findByte(text):
    for i in range(255):
        if long_to_bytes(text[0] ^ i) == b'c':
            print(f"{long_to_bytes(text[0] ^ i)} {i}")
            return i

byte = findByte(text)
final = []
print(f"[*] Found byte: {byte} | {long_to_bytes(byte)}")
for i in range(len(text)):
    print(long_to_bytes(text[i] ^ byte))
    final.append(long_to_bytes(text[i] ^ byte).decode())
print("".join(final))
