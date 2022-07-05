t = int(input())
for _ in range(t):
    a,b,c,d = list(map(int,input().split()))
    ans = 0
    if b >= a:
        ans = b 
    elif c <= d:
        ans = -1
    else:
        a-=b 
        ans =  b + ((a + c - d - 1) // (c - d) * c)
    print(ans)