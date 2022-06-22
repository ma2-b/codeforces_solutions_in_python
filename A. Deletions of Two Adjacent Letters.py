t = int(input())
for _ in range(t):
    s = input()
    t = input()
    yes = False 
    for i in range(len(s)):
        if s[i] == t[0] and i % 2 == 0:
            yes = True 
    if yes:
        print("YES")
    else:
        print("NO")