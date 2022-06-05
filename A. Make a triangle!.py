n = list(map(int,input().split()))
a = sorted(n)
if a[0]+a[1]>a[2]:
    print(0)
else:
    print(a[2]+1-a[0]-a[1])
