t = int(input())
for _ in range(t):
    r,b,d = list(map(int,input().split()))
    differ = abs(r - b)
    mn = min(r,b)
    each = (differ+mn-1)//mn 
    if each <= d:
        print("YES")
    else:
        print("NO")