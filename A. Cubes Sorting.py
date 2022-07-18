t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    can = False 
    for i in range(1,n):
        if a[i] >= a[i-1]:
            can = True 
            break 
    if can:
        print("YES")
    else:
        print('NO')