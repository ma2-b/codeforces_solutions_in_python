t = int(input()) 
for _ in range(t):
    n = int(input()) 
    a = list(map(int,input().split()))
    even1,even2,odd1,odd2 = 0,0,0,0 
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 == 1:
                odd1 = 1 
            else:
                even1 = 1 
        else:
            if a[i] % 2 == 1:
                odd2 = 1 
            else:
                even2 = 1 
    if even1 and odd1:
        print("NO")
    elif even2 and odd2:
        print('NO')
    else:
        print("YES")