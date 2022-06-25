import string
alphabet = string.ascii_lowercase[1:]
t = int(input())
for i in range(t):
    s = input()
    if len(set(list(s))) < len(s):
        print("NO")
        continue
    if "a" not in s:
        print("NO")
        continue
    check = True
    rn = [s.index("a")] * 2
    for j in range(len(s) - 1):
        char = alphabet[j]
        if rn[0] > 0 and s[rn[0] - 1] == char:
            rn[0] -= 1
        elif rn[1] < len(s) - 1 and s[rn[1] + 1] == char:
            rn[1] += 1
        else:
            check = False
            break
    if check == True:
        print("YES")
    else:
        print("NO")