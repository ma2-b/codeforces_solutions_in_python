t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    for i in range(n-1):
        if a[i]<k:
            k-=a[i]
            a[n-1]+=a[i]
            a[i] = 0
        else:
            a[i]-=k 
            a[n-1]+=k 
            k = 0
    for i in range(n):
        print(a[i],end=" ")