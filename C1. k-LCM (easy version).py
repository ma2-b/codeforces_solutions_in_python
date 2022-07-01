t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    if n % 2:
        print(1, n//2, n//2)
    elif n % 2 == 0 and n % 4:
        print(2, n//2 - 1, n//2-1 )
    else:
        print(n//2, n//4, n//4)