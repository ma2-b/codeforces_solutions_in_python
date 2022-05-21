t = int(input())
while t > 0:
    a,b = map(int,input().split())
    print((abs(a - b) + 9) // 10)       
    t -= 1 