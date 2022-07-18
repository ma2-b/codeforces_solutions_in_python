q = int(input())
for _ in range(q):
    n = int(input())
    print(2 if n == 2 else (n & 1))