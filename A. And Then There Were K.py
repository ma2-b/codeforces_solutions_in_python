f = int(input())
for t in range(f):
    n = int(input())
    ans = 0
    last = 0
    while n > ans:
        last = ans
        ans = 2*ans +1
    print(last)