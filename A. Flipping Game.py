n = int(input())
nums = list(map(int,input().split()))
one = 0 
ssum = 0
ans=0
for i in range(n):
    if nums[i] == 1:
        one+=1
for i in range(n):
    if nums[i] == 0:
        ssum+=1
    else:
        ssum-=1
    ans=max(ans,ssum)
    if ssum<0:
        ssum = 0
if one == n:
    print(n-1)
else:
    print(one+ans)