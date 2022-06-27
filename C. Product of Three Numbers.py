from math import floor, sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    flag,a,b = 0,0,0 
    for i in range(2,floor(sqrt(n))+1):
        if n%i == 0:
            if a == 0:
                a = i 
                n//=i 
            else:
                b = i 
                n //= i 
                if a < b and b < n:
                    flag = 1 
                    break 
    if flag:
        print("YES")
        print(a,b,n)
    else:
        print("NO")