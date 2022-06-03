n = int(input())
for i in range(n):
    x= 0
    y = 0
    l,r = list(map(int,input().split()))
    x=l
    y = l*2
    if y > r:
        print(-1,-1)
    else:
        print(x,y)