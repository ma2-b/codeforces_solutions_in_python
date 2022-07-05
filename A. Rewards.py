from math import ceil
a1,a2,a3 = list(map(int,input().split()))
b1,b2,b3 = list(map(int,input().split()))
n = int(input())
a = a1 + a2 + a3 
b = b1 + b2 + b3 
a = ceil(a * 1.0 / 5)
b = ceil(b * 1.0 / 10)
if a + b <= n:
    print("YES")
else:
    print("NO")