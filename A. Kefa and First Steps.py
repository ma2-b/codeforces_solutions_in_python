n = int(input())
arr = [int(x) for x in input().split()]
best = 0
counter = 0
last = 0
for x in arr:
    if x < last:
        best = max(best, counter)
        counter = 0
    counter += 1
    last = x
print(max(best, counter))