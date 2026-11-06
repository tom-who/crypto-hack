from Crypto.Util.number import *
import time

enc_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
enc_bytes = bytes.fromhex(enc_hex)
print(f"[*] Encrypted bytes: {enc_bytes}")

check = b'crypto{'
print("[*] Partial key: ", end="")

for i in range(len(check)):
    for j in range(256):
        if (enc_bytes[i] ^ j) == check[i]:
            print(chr(j), end="")
print("\n[!] Assuming full key is \"myXORkey\"")
key = b'myXORkey'

j = 0
i = 0

# Have to make a "fullKey" where the phrase myXORkey repeats to the same length of the enc bytes.

fullKey = []
while j != len(enc_bytes):
    fullKey.append(key[i])
    i += 1
    j += 1
    if i == len(key):
        i = 0
print(fullKey)

for i in range(len(enc_bytes)):
#    print(chr(fullKey[i]))
    print(chr(enc_bytes[i] ^ fullKey[i]), end="")
print()
