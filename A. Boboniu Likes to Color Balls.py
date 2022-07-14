t = int(input())
for _ in range(t):
    r,g,b,w = list(map(int,input().split()))
    cnt = 0 
    if r % 2:
        cnt+=1 
    if g % 2:
        cnt+=1 
    if b % 2:
        cnt+=1 
    if w % 2:
        cnt+=1 
    if cnt <= 1:
        print("YES")
        continue 
    if (r > 0 and g > 0 and b > 0):
        r-=1
        g-=1
        b-=1
        w+=3
    cnt = 0 
    if r % 2:
        cnt+=1 
    if g % 2:
        cnt+=1 
    if b % 2:
        cnt+=1 
    if w % 2:
        cnt+=1 
    if cnt <= 1:
        print("YES")
        continue
    print("NO")