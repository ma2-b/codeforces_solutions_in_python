from math import ceil
t = int(input())
for i in range(t):
    n = int(input())
    result = "989" + ("0123456789" * ceil(n / 10))
    print(result[:n])