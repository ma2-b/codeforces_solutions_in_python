t = int(input())
for i in range(t):
    n = int(input())
    l=[]
    sm=0
    for i in range(1,n+1):
        l.append(2**i)
    ns = (n//2-2)
    for i in range(n-2,ns,-1):
        sm=sm+l[i]
        l.remove(l[i])
    n = sum(l)
    mode = abs(sm-n)
    print(mode)