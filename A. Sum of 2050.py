t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2050 == 0:
        x = n//2050
        sum = 0 
        while x != 0:
            sum+=x%10 
            x//=10
        print(sum)
    else:
        print(-1)