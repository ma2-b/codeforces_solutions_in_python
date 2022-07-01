t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 3:
        print(n-1)
    else:
        print(2 + (n&1))