t = int(input())
for _ in range(t):
    n,B,x,y = list(map(int,input().split()))
    cur = 0
    ans = 0 
    for i in range(n):
        cur+= x if (cur + x <= B) else -y 
        ans+=cur
    print(ans)