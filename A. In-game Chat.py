t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    b = 0 
    for i in range(n):
        if s[i] == ")":
            b+=1 
        else:
            b = 0 
    letters = len(s) - b 
    if b > letters:
        print("YES")
    else:
        print("NO")