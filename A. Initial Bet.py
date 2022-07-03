a, b, c, d, e = list(map(int,input().split()))
s = a + b + c + d + e 
if s > 0 and s % 5 == 0:
    print(s//5)
else:
    print(-1)