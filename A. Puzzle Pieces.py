t = int(input()) 
for _ in range(t):
    n,m = list(map(int,input().split()))    
    edges = (n) * (m - 1) + m * (n - 1)
    if edges <= (n * m):
        print("YES")
    else:
        print("NO")