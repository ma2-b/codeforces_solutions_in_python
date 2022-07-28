t = int(input())
for _ in range(t):
    n = int(input())
    for j in range(n):
        print("()" * j + "(" * (n - j) + ")" * (n - j))