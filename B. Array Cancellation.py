t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    cur = 0 
    for i in a:
        cur = max(0,cur + i)
    print(cur)