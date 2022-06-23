t = int(input())
for _ in range(t):
    n = int(input())
    l = input()
    s = []
    for i in l:
        s.append(i)

    if ((s[0] == '2' and s[1] == '0') and (s[n-2] == '2' and s[n-1] == '0')):
        print("YES")
    elif ((s[0] == '2' and s[n-3] == '0') and (s[n-2] == '2'and s[n-1] == '0')):
        print("YES")
    elif ((s[n-4] == '2' and s[n-3] == '0') and (s[n-2] == '2' and s[n-1] == '0')):     
        print("YES")
    elif ((s[0] == '2' and s[1] == '0') and (s[2] == '2' and s[3] == '0')):
        print("YES")
    elif ((s[0] == '2' and s[1] == '0') and (s[2] == '2' and s[n-1] == '0')):
        print("YES")
    else:
        print("NO")