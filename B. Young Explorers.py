from sys import stdin
def inp():
    return stdin.readline().strip()
t = int(inp())
for _ in range(t):
    n = int(inp())
    e = [int(x) for x in inp().split()]
    e.sort()
    x = list(set(e))
    big = max(e)
    results = {}
    for i in e:
        if results.get(i,0):
            results[i] += 1
        else:
            results[i] = 1
    groups = 0
    counter = 1
    for i, j in results.items():
        groups += j//i
        if i != big:
            results[x[counter]] += j%i
        counter += 1
    print(groups)