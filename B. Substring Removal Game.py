N = int(input())
s = []
for _ in range(N):
    s.append(input())
for n in range(N):
    ones = []
    count = 0
    for c in s[n]:
        if c == '1':
            count += 1
        else:
            if count:
                ones.append(count)
                count = 0
    if count:
        ones.append(count)
    onessorted = sorted(ones, reverse=True)
    print(sum(onessorted[0::2]))