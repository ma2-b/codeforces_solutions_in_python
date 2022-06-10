t = int(input())
for _ in range(t):
    n,m,x = list(map(int,input().split()))
    x-=1
    col = x//n  
    row = x % n
    print(row*m+col+1)