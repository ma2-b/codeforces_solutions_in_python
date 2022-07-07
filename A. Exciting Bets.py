t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    diff = abs(a-b)
    if a > b:
        print(diff,min(diff - (a % diff), b % diff))   
    elif b > a:
        print(diff,min(diff - (b % diff), a % diff)) 
    else:
        print(0,0)