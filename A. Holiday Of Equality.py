n = int(input())
people = list(map(int,input().split()))
counter = 0
max = max(people)
for i in people:
    if i < max:
        counter+=max-i
print(counter)