t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    ans = n//2
    if n % 2 == 1:
        ans+=1
    print(ans)