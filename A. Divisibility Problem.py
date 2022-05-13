n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    if a%b == 0:
        print("0")
    elif a < b:
        print(b-a)
    else:
        print(b-(a%b))