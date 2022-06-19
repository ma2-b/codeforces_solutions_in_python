t = int(input()) 
for _ in range(t):
    n = int(input())
    if n == 1:
        print("-1")
    else:
        for i in range(1,n):
            print("9",end="")
        print("4")