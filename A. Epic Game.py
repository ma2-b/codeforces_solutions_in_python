from math import gcd
a,b,n = list(map(int,input().split()))
p1 = 0 
p2 = 0 
for i in range(n): 
    if n<= 0:
        break
    elif i%2 == 0:
        g = gcd(a,n)
        p1+=1 
        n-=g 
    else:
        g = gcd(b,n)
        p2+=1 
        n-=g 
if p1 > p2:
    print(0)
else:
    print(1)