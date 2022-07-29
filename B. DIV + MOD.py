from math import floor
t = int(input())
for _ in range(t):
    l,r,x = list(map(int,input().split()))
    ans = floor(r/x) + r % x
    m = floor(r/x) * x - 1 
    if m >= l:
        ans = max(ans,floor(m / x) + m % x)
    print(ans)