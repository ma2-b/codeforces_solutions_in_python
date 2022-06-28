t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    check = False
    if n == 1:
        print(-1,-1)
    else:
        for i in range(n-1):
            if s[i] != s[i+1]:
                print(i+1,i+2)
                check = True
                break 
        if not check:
            print(-1,-1)