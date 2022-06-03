t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    od_sum = 0
    ev_sum = 0
    for j in range(n*2):
        if nums[j] & 1:
            od_sum+=1
        else:
            ev_sum+=1
    if od_sum == ev_sum:
        print("YES")
        continue
    else:
        print("NO")