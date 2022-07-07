t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    result = 0 
    if a == 0:
        print(1)
    elif b == 0:
        print(a+1)
    else:
        print(a+(b*2)+1)