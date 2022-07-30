n = int(input())
a = list(map(int,input().split()))
counter = 0 
l = []
for j in range(n):
    if a[j] == 1:
        counter+=1 
for i in range(1,n):
    if a[i] <= a[i-1]:
        l.append(a[i-1])
print(counter)
print(*l,a[-1])