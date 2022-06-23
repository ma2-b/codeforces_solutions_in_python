t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    if n <= k:
        print(k-n)
    else:
        print(((n%2)^(k%2)))