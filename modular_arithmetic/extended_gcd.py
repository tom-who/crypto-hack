p = 26513
q = 32321
remainderArr = []

def gcd(x, y):
    print(f"[*] {x} = ({y})({x // y}) + {x % y}")
    x = x % y
    remainderArr.append(x)
    return x, y

x, y = gcd(q, p)

while x != 0:
    x, y = gcd(y, x)

print(f"[*] The gcd of P and Q is: {remainderArr[-2]}")

# gcd of p and q is 1
# We then have to re-arrange the equation to try write the gcd of p and q as a combination of p and q with certain weights
# We have to continuously factor backwords starting from the last equation until we get to the original 2 prime numbers.
# I think we can achieve this by 
