import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

# We are using euclidian algorithm to find the greatest common divisor between 2 real numbers.
def gcd(x, y):
    # Need to take previous divider, divide it by the remainder of the result.
    # The original remainder becomes the previous divider, and the new remainder becomes the remainder of the previous result

    # Remainder of x // y = z
    # Need to pass y and z to the next function
    while y > 0:
        x, y = y, x % y
    return x

print(f"[*] The GCD of {a} and {b} is: {gcd(a, b)}")
