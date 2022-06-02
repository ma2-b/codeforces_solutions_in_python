t = int(input())
counter = 1
for i in range(t):
    c = 2
    result = 1
    n,x = list(map(int,input().split()))
    while c < n:
        c+=x
        result+=1
    print(result)