n,k = list(map(int,input().split()))
for i in range(k):
    r = n%10
    if r==0:
        n=n//10
    else:
        n-=1
print(n)