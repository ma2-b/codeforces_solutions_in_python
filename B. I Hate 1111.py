t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if (n >= 111*(n%11)) else "NO")