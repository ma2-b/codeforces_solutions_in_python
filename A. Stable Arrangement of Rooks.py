t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    q = 0
    if (a+1)/2<b:
        print(-1)
    else:
        for i in range(1,a+1):
            for j in range(1,a+1):
                if j % 2 == 1 and i==j and q<b:
                    print("R",end="")
                    q+=1
                else:
                    print(".",end="")
            print()