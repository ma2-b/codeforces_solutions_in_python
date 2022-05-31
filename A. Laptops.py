n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    if a!=b:
        print("Happy Alex")
        break
else:
    print("Poor Alex")