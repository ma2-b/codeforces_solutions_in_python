t = int(input())
for _ in range(t):
    n,x,y = list(map(int,input().split()))
    diff = y - x 
    for delta in range(1,diff+1):
        if diff % delta:
            continue 
        if diff / delta + 1 > n:
            continue
        k = min((y - 1) // delta, n - 1)  
        a0 = y - k * delta 
        for i in range(n):
            print((a0 + i * delta),end=" ")
        break