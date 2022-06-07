t = int(input())
for i in range(t):
    c = 0
    v = 0
    a,n,m = list(map(int,input().split()))
    while n>0:
        c = a
        v = a//2+10
        a = min(v,c)
        n-=1
    if (a-(m*10)<=0):
        print("YES")
    else:
        print("NO")