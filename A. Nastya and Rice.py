t = int(input())
for _ in range(t):
    n,a,b,c,d = list(map(int,input().split()))
    absum = 0
    absub = 0
    cdsum = 0
    cdsub = 0 
    absum = a + b 
    absub = a - b 
    cdsum=c+d
    cdsub=c-d
    if (n*absum >= cdsub) and (n*absub <= cdsum):
         print("YES")
    else:
        print("NO")