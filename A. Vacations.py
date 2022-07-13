n = int(input())
a = list(map(int,input().split()))
rest = 0 
p = 0 
for i in range(n):
    if a[i] == 0:
        rest+=1 
        p = 0
    elif not p:
        p=a[i]
    elif p == 3:
        p=a[i]
    elif p == 2 and a[i]!=2:
        p=1 
    elif p == 2 and a[i]==2:
        p = 0
        rest+=1 
    elif p == 1 and a[i] != 1:
        p = 2
    elif p == 1 and a[i]==1:
        p = 0
        rest+=1 
print(rest)