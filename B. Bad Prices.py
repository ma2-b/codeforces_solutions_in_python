t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0 
    v = a[n-1]
    for i in reversed(range(n-1)):
        if v < a[i]:
            ans+=1 
        else:
            v = a[i]
    print(ans)