t = int(input())
for _ in range(t):
    n = int(input())
    ans=n*(n+1)//2
    r = 1 
    while (r <= n):
        ans -= 2 * r
        r = r*2
    print(ans)