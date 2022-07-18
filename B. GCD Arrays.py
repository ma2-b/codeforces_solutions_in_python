t = int(input())
while(t):
    t-= 1
    l,r,k= list(map(int,input().split()))
    if(l==r):
        if(l ==1):
            print('NO')
        else:
            print('YES')
    else:
        if(l%2==1):
            if(k>= ((r-l+2)//2) ):
                print('YES')
            else:
                print('NO')
        else:
            if(k>=((r-l+1)//2)):
                print('YES')
            else:
                print('NO')