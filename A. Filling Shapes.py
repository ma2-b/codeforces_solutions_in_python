n = int(input())
res = 1 
if n%2 == 1:
    print(0)
else:
    for i in range(n//2):
        res*=2
    print(res)