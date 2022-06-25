s = input()
t = input()
slen = len(s)
tlen = len(t)
sk = 0
tk = 0
ans = 0
while sk < slen and tk < tlen:
    if s[sk] == t[tk]:
        ans+=1 
        sk+=1 
        tk+=1
    else:
        tk+=1 
print(ans+1)