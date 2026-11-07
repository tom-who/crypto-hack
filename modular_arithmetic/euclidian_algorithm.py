import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def gcd(a, b):
   while b > 0:
       a, b = b, a % b
   return a

print(f"[*] The GCD of {a} and {b} is: {gcd(a, b)}")
