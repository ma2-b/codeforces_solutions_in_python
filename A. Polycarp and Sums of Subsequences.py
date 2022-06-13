n = int(input())
for _ in range(n):
    x = list(map(int,input().split()))
    print(x[0],x[1],x[6] - x[0] - x[1])