t = int(input())
for _ in range(t):
    a,b,x,y,n = list(map(int,input().split()))
    ans = 0 
    p = max(x,a-n)
    q = b 
    if a - p <= n:
        q = max(y,b-(n-(a-p)))
    ans = p*q 
    p = max(y,b-n)
    q = a
    if b-p<=n:
        q = max(x,a-(n-(b-p)))
    ans=min(ans,p*q) 
    print(ans)