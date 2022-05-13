n = input()
l = []
result = []
for i in n:
    if i.islower():
        l.append(i)
for j in l:
    if j not in result:
        result.append(j)
print(len(result))