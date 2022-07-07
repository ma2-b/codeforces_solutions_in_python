q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    if s == s[::-1] or k == 0:
        print(1)
    else:
        print(2)