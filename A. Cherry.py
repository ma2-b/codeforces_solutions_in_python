t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  ans = 0
  for i in range(n - 1):
    ans = max(ans, a[i] * a[i + 1])
  print(ans)