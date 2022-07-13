t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    s = 0
    if sum(a) == m:
        print("YES")
    else:
        print("NO")