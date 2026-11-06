a = 66528
b = 52920
remainderArr = []

# We are using euclidian algorithm to find the greatest common divisor between 2 real numbers.

def gcd(x, y):
    # Need to take previous divider, divide it by the remainder of the result.
    # The original remainder becomes the previous divider, and the new remainder becomes the remainder of the previous result
    # Need rec

    # Take past and divide it by present.
    # Discard past and make present the past and the future the present and so on.

    # Add checks to see if present = 0, in that case print past. Past should the be the gcd in that case.
    # Remainder of a // b = x
    # Need to pass x and b to the next function

    x = x % y
    remainderArr.append(x)
    # Need to pass this to next function, along with y
    return x, y

x, y = gcd(a, b)
while x != 0:
    x, y = gcd(y, x)
print(f"[*] The GCD is {remainderArr[-2]}")
