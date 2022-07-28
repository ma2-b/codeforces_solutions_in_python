t = int(input())
for _ in range(t):
    a,b,c = list(map(int,input().split()))
    if (a + b + c) % 9 != 0:
        print("NO")
    else:
        print("YES" if min(a, b, c) >= (a + b + c)// 9 else "NO")