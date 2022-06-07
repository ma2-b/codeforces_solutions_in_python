t = int(input())
for i in range(t):
    a,b,n = list(map(int,input().split()))
    summ = 0
    c = 0
    while summ <= n:
        if a > b:
            b+=a
            summ = b 
            c+=1
        else:
            a+=b 
            summ = a 
            c+=1
        if summ > n:
            break
    print(c)