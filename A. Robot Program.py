t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    res = max(x, y) * 2 - 1
    if x == y:
        res+=1 
    print(res)