from collections import deque
t = int(input())
for _ in range(t):
    n, x = list(map(int,input().split()))
    w = list(map(int,input().split()))
    w.sort(reverse=True)
    dq = deque(w)
    ans = []
    acc = 0
    while dq:
        if acc + dq[0] != x:
            acc += dq[0]
            ans.append(dq.popleft())
        elif acc + dq[-1] != x:
            acc += dq[-1]
            ans.append(dq.pop())
        else:
            print('NO')
            break
    if len(ans) == n:
        print('YES')
        print(' '.join(map(str, ans)))