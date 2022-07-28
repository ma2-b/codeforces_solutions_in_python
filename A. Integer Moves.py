t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    d =  x * x + y * y 
    r = 0 
    while r * r < d:
        r+=1 
    ans = 2 
    if r * r == d:
        ans = 1 
    if x == 0 and y == 0:
        ans = 0 
    print(ans)