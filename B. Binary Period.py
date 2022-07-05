t = int(input())
for _ in range(t):
    s = input()
    f = True 
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            f = False 
            break 
    if f:
        print(s)
        continue 
    n = len(s)
    ans = ""
    ans+=s[0]
    i = 1 
    for i in range(1,n):
        if s[i] != s[i-1]:
            ans+=s[i]
            
        else:
            if s[i] == "0":
                ans+="1"
            else:
                ans+="0"
            ans+=s[i] 
    print(ans)