t = int(input())
for _ in range(t):
    k, s = input(), input()
    res = 0
    for i in range(1, len(s)):
        res += abs(k.index(s[i]) - k.index(s[i - 1]))
    print(res)