t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in a:
        ans|=i 
    print(ans)