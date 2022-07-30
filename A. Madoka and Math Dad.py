t = int(input())
for _ in range(t):
    n = int(input())
    type = 0 
    if n % 3 == 1:
        type = 1 
    else:
        type = 2 
    ans = 0  
    while ans != n:
        print(type,end="")
        ans+=type 
        type = 3 - type       
    print()