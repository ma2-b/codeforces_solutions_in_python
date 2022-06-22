t = int(input())
for _ in range(t):
    n = int(input())
    tmp = 1 
    sum = 1 
    ans = 1 
    while sum < n:
        tmp+=2 
        sum+=tmp 
        ans+=1 
    print(ans)