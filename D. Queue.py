n = int(input())
a = list(map(int,input().split()))
l = []
counter = 0
a.sort()
for i in a:
    if sum(l) <= i:
        counter+=1 
        l.append(i)
print(counter)