t = int(input())
for _ in range(t):
    a,b,c,x,y = list(map(int,input().split())) 
    ax = min(a,x)
    by = min(b,y)
    a-=ax 
    x-=ax 
    b-=by 
    y-=by 
    if c >= x+y:
        print('YES')
    else:
        print('NO')