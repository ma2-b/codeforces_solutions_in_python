t = int(input())
for _ in range(t):
    n,x,a,b = list(map(int,input().split()))
    print(min(n-1,abs(a - b) + x))