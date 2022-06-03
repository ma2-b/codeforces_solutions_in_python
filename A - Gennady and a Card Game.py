a = input()
b = input().split()
n = len(b)
res = 'NO'
for i in range(n):
    if a[0] == b[i][0] or a[1] == b[i][1]:
        res = 'YES'
print (res)