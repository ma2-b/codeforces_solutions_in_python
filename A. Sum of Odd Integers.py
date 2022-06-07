t = int(input())
for i in range(t):
    n,k = list(map(int,input().split()))
    if k*k<= n:
        if (n+k)%2==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")