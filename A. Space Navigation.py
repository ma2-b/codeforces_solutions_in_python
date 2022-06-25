t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    u = 0
    d = 0 
    l = 0
    r = 0 
    s = input()
    for i in range(len(s)):
        if s[i] == "U":
            u+=1
        elif s[i] == "R":
            r+=1
        elif s[i] == "D":
            d+=1 
        else:
            l+=1 
    if x > 0 and r >= x :
        x = 0
    if x < 0 and l >= -x:
        x = 0 
    if y > 0 and u >= y:
        y = 0
    if y < 0 and d >= -y :
        y = 0 
    if not x and not y:
        print("YES")
    else:
        print("NO")