n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(n):
    nodup = True 
    for j in range(i+1,n):
        if a[i] == a[j]:
            nodup = False 
            break 
    if nodup:
        ans.append(a[i])
print(len(ans))
print(*ans)