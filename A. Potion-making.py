from math import gcd
t = int(input())
for _ in range(t):
    k = int(input())
    print(100 // gcd(100,k))