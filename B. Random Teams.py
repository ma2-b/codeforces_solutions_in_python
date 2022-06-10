n,m = list(map(int,input().split()))
def nC2(n):
	if(n < 2):
		return 0
	return (n * (n - 1) // 2)
minofpairs = (m - n % m) * (nC2(n//m)) + (n % m) * (nC2(n//m + 1))
maxofpairs = nC2(n - m + 1)
print(minofpairs,maxofpairs)