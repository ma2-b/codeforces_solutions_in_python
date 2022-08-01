n = int(input())
f = list(map(int,input().split()))
triangle = False 
for i in range(n):
    if i == f[f[f[i] - 1] - 1] - 1:
        triangle = True 
if triangle:
    print("YES")
else:
    print("NO")