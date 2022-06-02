t = int(input())
l = []
for i in range(t):
    n,k = list(map(int,input().split()))
    div = k // (n-1) 
    ex = k % (n-1) 
    ans = n * div + ex 
    if(ex == 0):
        ans -=1 
    print(ans)