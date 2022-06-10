n = int(input())
l = []
k = []
a = input()
b = input()
for x in a:
    l.append(x)
for t in b:
    k.append(t)
count = 0
for i in range(n):
    count += min(10 - abs(int(l[i])-int(k[i])),abs(int(l[i]) - int(k[i])))
print(count)