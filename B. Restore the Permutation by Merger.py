t = int(input())
l = []
for i in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    for j in p:
        if j not in l:
            l.append(j)
    print(*l) 
    l = []