t = int(input())
for _ in range(t):
    n,k1,k2 = list(map(int,input().split()))
    w,b = list(map(int,input().split()))
    if k1 + k2 >= 2 * w and (n - k1) + (n - k2) >= 2 * b:
        print("YES")
    else:
        print("NO")