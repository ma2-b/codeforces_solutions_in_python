t = int(input())
for _ in range(t):
    n = int(input())
    count = 0 
    while n:
        if n < 10:
            count+=n 
            n = 0 
        else:
            s = n//10 
            count+=s*10 
            n %= 10 
            n+=s 
    print(count)