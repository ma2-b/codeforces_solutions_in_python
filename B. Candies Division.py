t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    full = n - n % k 
    full+=min(n % k,k//2)
    print(full)