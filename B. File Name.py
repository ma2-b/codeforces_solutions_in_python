n = int(input())
a = input()
count = 0
l = []
for i in a:
    l.append(i)
for j in range(2,len(l)):
    if l[j] == "x" and l[j-1] == "x" and l[j-2] == "x":
        count+=1
print(count)