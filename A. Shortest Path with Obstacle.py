t = int(input())
for i in range(t):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = list(map(int, input().split()))
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    if a[0] == b[0] and b[0] == f[0]:
        if f[1] > min(a[1], b[1]) and f[1] < max(a[1], b[1]):
            distance += 2
    elif a[1] == b[1] and b[1] == f[1]:
        if f[0] > min(a[0], b[0]) and f[0] < max(a[0], b[0]):
            distance += 2
    print(distance)