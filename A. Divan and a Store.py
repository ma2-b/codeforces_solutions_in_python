t = int(input())
for _ in range(t):
    n, down, up, money = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    count = 0
    arr.sort()
    for i in range(len(arr)):
        if arr[i] >= down:
            if arr[i] <= up:
                if arr[i] <= money:
                    money-=arr[i]
                    count+=1
    print(count)