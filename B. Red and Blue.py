t = int(input())
for _ in range(t):
	n = int(input())
	a = [int(x) for x in input().split()]
	m = int(input())
	b = [int(x) for x in input().split()]
	dp = [[-10**9 for j in range(m + 1)] for i in range(n + 1)]
	dp[0][0] = 0
	ans = 0
	for i in range(n + 1):
		for j in range(m + 1):
			if i < n:
				dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + a[i])
			if j < m:
				dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + b[j])
			ans = max(ans, dp[i][j])
	print(ans)