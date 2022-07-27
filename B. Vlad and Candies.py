t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if n == 1:
        if a[0] > 1:
            print("NO")
        else:
            print("YES")
        continue
    if a[-2] + 1 < a[-1]:
        print("NO")
    else:
        print("YES")