t = int(input())
for i in range(t):
    a,b,c = list(map(int,input().split()))
    diff = abs(a-b)
    values = diff*2
    if(a>values or b>values or c>values):
        print(-1)
    else:
        d = c+diff
        if d>values:
            d = c - diff
        print(d)