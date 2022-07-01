t = int(input())
for _ in range(t):
    x,y,a,b = list(map(int,input().split()))
    dist = y - x
    speed = a + b 
    if dist % speed == 0:
        print(dist//speed)
    else:
        print(-1)