t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ok = 1 
    for p1 in range(n):
        for p2 in range(p1):
            ok &= abs(a[p1] - a[p2]) != 1
    print(2 - ok)