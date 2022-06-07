n,m,k = list(map(int,input().split()))
army = []
for i in range(m+1):
    army.append(int(input()))
friends = 0
for j in range(m):
    t = 0
    for x in range(n):
        if ((army[j] >> x) & 1) != ((army[m] >> x) & 1):
            t+=1
    if t <= k:
        friends+=1
print(friends)