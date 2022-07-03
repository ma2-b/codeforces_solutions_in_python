def matip(n,m):
    lst=[]
    for _ in range(n):
        arr = list(map(int,input().split()))
        lst.append(arr)
    return lst
t = int(input())
while t:
    t-=1
    n,m = map(int,input().split())
    arr = matip(n,m)
    row = col = 0
    for i in range(n):
        if arr[i].count(0)==m:
            row+=1
    for i in range(m):
        p = 0
        for j in range(n):
            if arr[j][i]==0:
                p+=1
        if p==n:
            col+=1
    if min(row,col)%2==0:
        print('Vivek')
    else:
        print('Ashish')