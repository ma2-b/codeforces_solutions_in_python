n = int(input())
points = list(map(int,input().split()))
counter =0 
for i in range(1,n):
    subconuter_highest = 0
    subconuter_lowest = 0
    for a in range(0,i):
        if points[i]>points[a]:
            subconuter_highest+=1
        elif points[i]<points[a]:
            subconuter_lowest+=1 
    if subconuter_highest == i or subconuter_lowest == i:
        counter+=1
print(counter)