t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    if b == 1:
        print("NO")
    else:
        print("YES")
        sum = (a * b * 2)
        y = sum - a 
        print(a,y,sum)