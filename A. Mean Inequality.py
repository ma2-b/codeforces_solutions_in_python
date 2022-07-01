t = int(input())
for _ in range(t):
    a = int(input())
    b = list(map(int, input().split()))
    b.sort()
    ptr1 = 0
    ptr2 = len(b)//2
    ans = []
    while ptr2 < len(b):
        ans.append(b[ptr1])
        ans.append(b[ptr2])
        ptr1+=1
        ptr2+=1
    print(*ans)