r=int(input())
for i in range(r):
    x,y,n=[int(x) for x in input().split()]
    m=n%x
    if m>y:
            print(n-m+y)
    elif m==y:
        print(n)
    elif m<y:
        print(n-m-x+y)