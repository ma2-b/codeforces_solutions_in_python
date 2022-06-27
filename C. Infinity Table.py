t = int(input())
for _ in range(t):
    k = int(input())
    left = 0
    right = 0 
    step = -2 
    while right < k:
        step+=2 
        left = right + 1 
        right = left + step 
    x = 0 
    y = 0
    half = left + step // 2
    if k <= half:
        x = k - left + 1
        y = step // 2 + 1
    else:
        x = step // 2 + 1
        y = step // 2 - (k - half) + 1
    print(x,y)