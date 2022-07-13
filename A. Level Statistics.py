t = int(input())
for _ in range(t):
    n = int(input())
    ok = True 
    a,b = 0,0 
    for _ in range(n):
        x,y = list(map(int,input().split()))
        if x < a or y < b or x < y or x-a < y-b:
            ok = False 
        a = x
        b = y 
    if ok:
        print("YES")
    else:
        print("NO")