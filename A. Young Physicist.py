num = int(input())
a = [0] * 3
for i in range(num):
    b = [int(x) for x in input().split()]
    for j in range(3):
        a[j] += b[j]
m = [x for x in a if x == 0]
print('YES' if len(m) == 3 else 'NO')