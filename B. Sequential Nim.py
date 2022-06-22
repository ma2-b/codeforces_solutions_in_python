t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = 0
    while k < n and a[k] == 1:
        k+=1
    if (k == n) ^ (k%2):
        print('Second')
    else:
        print("First")