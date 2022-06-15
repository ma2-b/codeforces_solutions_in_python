t = int(input())
n = []
sides = []
for _ in range(t):
    n.append(int(input()))
    sides.append(list(map(int,input().split())))
for te in range(t):
    found = 0
    if sides[te][0] + sides[te][1] <= sides[te][n[te]-1]:
        print(1, 2, n[te])
        found = 1
    if not found:
        print(-1)