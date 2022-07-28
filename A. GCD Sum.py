from math import gcd
def valid(x):
    return gcd(x, sum([ord(c) - ord('0') for c in str(x)])) != 1
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    while not valid(n):
        n += 1
    print(n)