t = int(input())
for i in range(t):
    n = int(input())
    p = n%2020
    k = n//2021
    if p<=k:
        print("YES")
    else:
        print("NO")