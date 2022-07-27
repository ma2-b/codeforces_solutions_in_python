x,y = list(map(int,input().split()))
n = int(input())
MOD = 1000000007
s = [x,y,y-x,-x,-y,x-y]
print((s[(n - 1) % 6] % MOD + MOD) % MOD)