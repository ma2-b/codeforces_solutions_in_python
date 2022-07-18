from collections import Counter
def free_cash_reg():
    n = int(input().strip())
    c = Counter()
    for i in range(n):
        ip = input().strip()
        c[ip] += 1
    return c.most_common()[0][1]
print(free_cash_reg())