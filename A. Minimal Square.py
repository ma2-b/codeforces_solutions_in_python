t=int(input())
for i in range(t):
    l,b=[int(x) for x in input().split()]
    c = min(l,b)
    c = 2*c
    c = max(l,b,c)
    print(c*c)