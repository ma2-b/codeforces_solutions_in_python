from math import sqrt
t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    factor = 2 
    maxFactor = sqrt(n)
    while factor <= maxFactor:
        if n % factor == 0:
            break 
        factor+=1
    if n % factor != 0:
        factor = n 
    res = n + factor + (k - 1)*2
    print(res)