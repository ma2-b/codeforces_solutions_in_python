t = int(input())
for _ in range(t):
    n = input()
    print(*sorted(map(int, input().split()))[::-1])