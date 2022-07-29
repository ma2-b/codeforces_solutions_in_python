a,b,c,d = list(map(int,input().split()))
if a+b == c+d or a+c == b+d or a+d == b+c or a+b+c == d or a+c+d == b or a+b+d == c or b+c+d == a:
    print("YES")
else:
    print("NO")