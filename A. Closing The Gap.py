t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if s % n == 0:
        print(0)
    else:
        print(1)