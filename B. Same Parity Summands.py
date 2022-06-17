t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    avg = n // k
    if n & 1:   
        if k & 1 == 0: 
            avg = -1
        else:      
            if avg & 1 == 0:
                if (avg + 1) * (k - 1) + 1 > n:
                    avg -= 1 
                else:
                    avg += 1   
    else:     
        if k & 1 and avg & 1:
            if (avg + 1) * (k - 1) + 2 > n:
                avg -= 1
            else:
                avg += 1
    if avg <= 0:
        print("NO")
    else:
        a = [avg for i in range(k - 1)]
        a += [n - avg * (k - 1)]
        print("YES")
        print(*a)