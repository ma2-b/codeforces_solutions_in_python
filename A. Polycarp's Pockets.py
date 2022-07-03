n = int(input())
s = map(int, input().strip().split(' '))
t = [0 for i in range(101)]
for i in s:
    t[i] += 1
print(max(t))