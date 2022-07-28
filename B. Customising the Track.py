t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = 0 
    for i in range(n):
        s+=a[i]
    k = s % n 
    ans = k*(n - k)
    print(ans)