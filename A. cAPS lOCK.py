s = input()
ans = s
if len(s) == 1 or s[1:].isupper():
    ans = ''
    for c in s:
        ans += (c.upper() if c.islower() else c.lower())
print(ans)