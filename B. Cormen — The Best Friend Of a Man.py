n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
tot = 0 
for i in range(1,n):
    if a[i-1]+a[i] < m:
        tot+=m-a[i]-a[i-1]
        a[i] = m - a[i-1]
print(tot)
for j in range(n-1):
    print(a[j],end=" ")
print(a[n-1])