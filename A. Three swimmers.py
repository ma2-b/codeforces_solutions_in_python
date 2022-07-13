t = int(input())
for _ in range(t):
    p,a,b,c = list(map(int,input().split()))
    x = a-p%a
    y = b-p%b
    z = c-p%c      
    if p%a == 0 or p%b==0 or p%c==0:
        print(0)
    else:
        print(min(x,min(y,z)))