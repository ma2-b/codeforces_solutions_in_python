t = int(input())
for _ in range(t):
    l = ""
    n = int(input())
    a = input()
    for i in a:
        if i == "U":
            l+="D"
        elif i == "D":
            l+="U"
        else:
            l+=i
    print(l)