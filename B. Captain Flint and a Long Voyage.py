t = int(input())
for _ in range(t):
    n = int(input())
    x = (n+3)//4
    for i in range(n-x):
        print(9,end='')
    for j in range(0,x):
        print(8,end="")   
    print()