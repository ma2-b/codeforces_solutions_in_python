t = int(input())
maps = [
    lambda x: 0,
    lambda x: x,
    lambda x: -1,
    lambda x: -x - 1
]
for _ in range(t):
    x0, n = map(int, input().split())
    d = maps[n % 4](n)
    print(x0 - d if x0 % 2 == 0 else x0 + d)