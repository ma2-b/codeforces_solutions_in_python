n = int(input()) 
a = list(map(int,input().split()))
mx,mn = 0 ,1000000007
c1,c2 = 0,0
for i in a:
    mx = max(mx,i)
    mn = min(mn,i) 
for i in range(n):
    if a[i] == mx:
        c1+=1 
    if a[i] == mn:
        c2+=1
if mx == mn:
    print(0)
else:
    print(n-c1-c2)