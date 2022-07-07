t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    lef, rig, sw = 1, 1, 0
    for i in range(n-1):
        if(s[i] > s[i+1]):
            sw = 1
            break
    if(sw == 0):
        print(s)
        continue
    for i in range(n):
        if (s[i] == '1'):
            lef = i
            break
    for i in range(n-1, 0, -1):
        if (s[i] == '0'):
            rig = i
            break
    st = s[:lef] + '0' + s[rig+1:]
    print(st)