t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2,30):
        val = (1 << i ) - 1
        if n % val == 0:
            print(n//val)
            break
