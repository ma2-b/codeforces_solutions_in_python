t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if a[i]%2:
            cnt+=1
    if cnt == n or cnt == 0:
        print("YES")
    else:
        print("NO")