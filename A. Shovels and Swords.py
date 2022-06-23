t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    counter = 0
    if a > b:
        r = a 
        a = b 
        b = r 
    if a*2 <= b:
        print(a)
    else:
        print((a+b)//3)