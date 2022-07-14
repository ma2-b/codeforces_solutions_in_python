n, m = map(int, input().split())
for i in range(0, n):
    s = input()
    ans = ""
    for j in range(0, m):
        if s[j] == '.':
            if (i + j) & 1 == 1:
                ans = ans + "B"
            else:
                ans = ans + "W"
        else:
            ans = ans + s[j]
    print(ans)