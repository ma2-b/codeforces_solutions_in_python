a2,a3,a5,a6 = list(map(int,input().split()))
b = min(a2,min(a5,a6))
a2 -= b 
a5 -= b
a6 -= b 
c = min(a2,a3)
print((b * 256) + (c * 32))