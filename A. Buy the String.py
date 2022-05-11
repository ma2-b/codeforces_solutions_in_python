t = int(input())
for _ in range(t):
    n,c0,c1,h= list(map(int,input().split()))
    s = input()
    ans = 0 
    for i in range(n):
        if s[i] == '0':
            ans+=min(c0,c1+h) 
        else:
            ans+=min(c1,c0+h)  
    print(ans)  