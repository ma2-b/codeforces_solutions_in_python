n,m = list(map(int,input().split()))
i = 0 
if n > m:
    i = m
else:
    i = n
if i % 2 == 0:
    print("Malvika")
else:
    print("Akshat")