n = int(input())
a = list(map(int,input().split()))
s = 0
l = []
ar = sorted(a)
for i in range(n-1):
    l.append(ar[i+1]-ar[i])
for j in range(len(l)):
    if j%2==0:
        s+=l[j]
print(s)