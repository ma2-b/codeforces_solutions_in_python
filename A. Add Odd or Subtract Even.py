t = int(input())
for i in range(t):
    a,b = list(map(int,input().split()))
    diff = b-a
    if diff > 0:
        if diff&1:
            print(1)
        else:
            print(2)
    elif b == a:
        print(0)
    else:
        if diff&1:
            print(2)
        else:
            print(1)