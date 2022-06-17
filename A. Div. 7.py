t = int(input())
for _ in range(t):
    n = int(input())
    if n%7 == 0:
        print(n)
    else:
        ans = -1
        for i in range(10):
            if (n - n % 10 + i) % 7 == 0:
                ans = n - n % 10 + i
        print(ans)