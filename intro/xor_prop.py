import time
from Crypto.Util.number import *

key1 = b'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2xorkey3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
xor_flag = b'04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key1 = bytes_to_long(bytes.fromhex(key1))
key2_3 = bytes_to_long(bytes.fromhex(key2xorkey3))
xor_flag = bytes_to_long(bytes.fromhex(xor_flag))

key1_2_3 = key2_3 ^ key1

print(f"[*] Key1 ^ Key2 ^ Key3 : {key1_2_3}")
print(f"[*] Flag: {xor_flag}")

final = key1_2_3 ^ xor_flag

print(f"[*] all keys xored with flag xor: {final}")
print(f"[*] Flag in decimal: {final}")
print(f"[*] Converting to proper format...")
time.sleep(1)
final = long_to_bytes(final)
print(f"[!] Flag: {final.decode()}")
