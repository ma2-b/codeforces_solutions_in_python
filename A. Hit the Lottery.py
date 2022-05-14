n = int(input())
denom = [1, 5, 10, 20, 100]
denom.reverse()
c = 0
for x in denom:
    if n >= x:
        num = n // x
        n = n - (num * x)
        c += num
print(c)