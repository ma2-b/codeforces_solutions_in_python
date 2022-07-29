R = lambda:map(int,input().split())
n,=R()
a=sorted(x-y for x,y in zip(R(),R()))
r=i=0
j=n-1
while i<j:
 if a[i]+a[j]>0:
    r+=j-i;j-=1
 else:
    i+=1
print(r)