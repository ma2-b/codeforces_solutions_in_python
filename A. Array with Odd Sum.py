t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    summ = 0 
    odd = 0
    even = 0
    for j in range(n):
        if a[j]%2!=0 or a[j]==1:
            odd+=1
        else:
            even+=1
        summ+=a[j]
    if summ%2!=0 or summ==1:
        print("YES")
    else:
        if odd!=0 and even!=0:
            print('YES')
        else:
            print('NO')