t = int(input())
for _ in range(t):
    n = int(input())
    k = 0
    while n > 1:
        if n % 2 == 0:
            n//=2 
        elif n % 3 == 0:
            n//=3 
            n*=2 
        elif n % 5 == 0:
            n//=5 
            n*=4 
        else:
            k = -1 
            break 
        k+=1 
    print(k)