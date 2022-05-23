n,k = list(map(int,input().split()))
nums = list(map(int,input().split()))
empty_chairs = 0
for i in nums:
    if 5 - i >= k:
        empty_chairs+=5-i
nums_of_times = 0
for i in range(n):
    if empty_chairs >= k*3:
        nums_of_times+=1
        empty_chairs-= k*3
print(nums_of_times)