n,d = list(map(int,input().split()))
t = list(map(int,input().split()))
sum = 0
for i in t:
    sum+=i
if d < (sum + (n - 1) * 10):
    print(-1)
else:
    print((d-sum)//5)