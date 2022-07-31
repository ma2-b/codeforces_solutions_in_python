n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    if a[i] % 2 == 0:
        a[i] = a[i] - 1
for j in a:
    print(j,end=" ")