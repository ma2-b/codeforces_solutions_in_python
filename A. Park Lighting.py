from math import ceil
t = int(input())
counter = 0
for i in range(t):
    n,m = list(map(int,input().split()))
    counter = ceil((n*m) / 2)
    print(counter)