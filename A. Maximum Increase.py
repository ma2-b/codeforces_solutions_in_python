n = int(input())
nums = list(map(int,input().split()))
counter = 1
max = 1
for i in range(1,n):
    if nums[i] > nums[i-1]:
        counter+=1
    else:
        if counter > max:
            max=counter
        counter=1
if counter > max:
    max=counter 
print(max)