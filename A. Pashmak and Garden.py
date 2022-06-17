x1,y1,x2,y2 = list(map(int,input().split()))
dx = abs(x1-x2)
dy = abs(y1-y2)
if dx==dy:
    print(x1,y2,x2,y1)
elif x1==x2:
    x3 = x4 = x1 + abs(y1-y2)
    y3 = y1 
    y4 = y2 
    print(x3,y3,x4,y4)
elif y1==y2:
    y3 = y4 = y1 + abs(x1-x2)
    x3 = x1 
    x4 = x2 
    print(x3,y3,x4,y4)
else:
    print(-1)