t = int(input())
for i in range(t):
    a,b,c= [int(x) for x in input().split()]
    if (a+b+c)%3 == 0:
        print(0)
    else:
        print(1)
