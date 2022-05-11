n = list(input().split())
l = []
for i in n:
    if i not in l:
        l.append(i)
result = len(n)-len(l)
print(result)