t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in reversed(range(n)):
        print(a[i],end=" ")